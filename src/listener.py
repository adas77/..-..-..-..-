import random
from g4.ExprListener import ExprListener
from g4.ExprParser import ExprParser
from .generator import LLVMGenerator, Type
from .memory import Memory
from .enums import Context


class ExprListenerImpl(ExprListener):
    def __init__(self):
        self.memory = Memory()
        self.generator = LLVMGenerator()

    def exitR(self, ctx: ExprParser.RContext):
        self.generator.save()

    def exitAssign(self, ctx: ExprParser.AssignContext):
        ID = ctx.ID().getText()
        TYPE = Type.map_(ctx.TYPE().getText()) if ctx.TYPE() is not None else None
        locked_type = TYPE is not None
        val_name, val_type = self.memory.stack.pop()
        global_char, id_, variable = self.memory.set_variable(
            self.generator,
            ID,
            self.generator.text_generator.get_current_context(),
            val_type,
            locked_type,
        )
        if val_type != variable["type_"]:
            if variable["locked_type"]:
                raise ValueError(
                    f"LockeType Types: {val_type} must match {variable['type_']}"
                )
            else:
                self.memory.remove_variable(
                    ID, self.generator.text_generator.get_current_context()
                )
                global_char, id_, variable = self.memory.set_variable(
                    self.generator,
                    ID,
                    self.generator.text_generator.get_current_context(),
                    val_type,
                    locked_type,
                )

        self.generator.assign(variable["llvm_id"], (val_name, val_type))

    def exitArrayDeclaration(self, ctx: ExprParser.ArrayDeclarationContext):
        ID = ctx.ID().getText()
        SIZE = int(ctx.INT().getText())
        TYPE = ctx.TYPE().getText()
        type_ = Type.map_(TYPE)

        self.memory.add(
            ID,
            TYPE,
            False,
            self.generator.text_generator.get_current_context(),
            data=(type_, SIZE),
        )
        self.generator.declare_arr(ID, type_, SIZE)

    def exitArrayAssign(self, ctx: ExprParser.ArrayAssignContext):
        ID = ctx.ID().getText()
        type_, size = self.memory.get_arr(
            ID, self.generator.text_generator.get_current_context()
        )
        INDEX = ctx.arrayIndexExpr().expr()
        VAL = ctx.expr()
        index = None
        if hasattr(INDEX, "getText"):
            index = int(INDEX.getText())
        else:
            raise NotImplementedError()
        val = None
        if hasattr(VAL, "getText"):
            val = VAL.getText()
        else:
            raise NotImplementedError()

        self.generator.assign_arr(ID, type_, size, index, val)

    def exitPrint(self, ctx: ExprParser.PrintContext):
        ctx = ctx.value()
        if hasattr(ctx, "INT"):
            (val_name, val_type) = self.memory.stack.pop()
            self.generator.printf(val_name, Type.INT)
        elif hasattr(ctx, "DOUBLE"):
            (val_name, val_type) = self.memory.stack.pop()
            self.generator.printf(val_name, Type.DOUBLE)
        elif hasattr(ctx, "FLOAT"):
            (val_name, val_type) = self.memory.stack.pop()
            self.generator.printf(val_name, Type.FLOAT)
        elif hasattr(ctx, "STR"):
            (val_name, val_type) = self.memory.stack.pop()
            self.generator.printf(val_name, Type.STR)
        elif hasattr(ctx, "ID"):
            ID = ctx.ID().getText()  # type: ignore
            _global_char, _id_, variable = self.memory.get_variable(
                ID, self.generator.text_generator.get_current_context()
            )
            type_ = variable.get("type_", None)
            if type_ not in [Type.INT, Type.DOUBLE, Type.FLOAT, Type.STR]:
                raise Exception(f"Unknown variable print type: {type_}")

            val_name, _val_type = self.memory.stack.pop()
            self.generator.printf(val_name, type_)

        else:
            raise Exception(f"Unknown print type: {ctx}")

    def exitRead(self, ctx: ExprParser.ReadContext):
        ID = ctx.ID().getText()
        global_char, id_, variable = self.memory.get_variable(
            ID, self.generator.text_generator.get_current_context()
        )
        type_ = variable["type_"]
        self.generator.scanf(variable["llvm_id"], type_)

    def exitAddSub(self, ctx: ExprParser.AddSubContext):
        r = self.memory.stack.pop()
        l = self.memory.stack.pop()
        l_id, l_type = l
        r_id, r_type = r
        if l_type != r_type:
            raise ValueError(f"Types: {l_type} must match {r_type}")

        type_ = l_type
        fn = self.generator.add if ctx.op.type == ExprParser.ADD else self.generator.sub  # type: ignore

        anon_id = fn(l_id, r_id, type_)
        self.memory.stack.append((anon_id, type_))

    def exitInt(self, ctx: ExprParser.IntContext):
        INT = ctx.INT().getText()
        anon_id, type_ = self.generator.assign_anonymous(INT, Type.INT)
        self.memory.stack.append((anon_id, type_))

    def exitDouble(self, ctx: ExprParser.DoubleContext):
        DOUBLE = ctx.DOUBLE().getText()
        anon_id, type_ = self.generator.assign_anonymous(DOUBLE, Type.DOUBLE)
        self.memory.stack.append((anon_id, type_))

    def exitFloat(self, ctx: ExprParser.FloatContext):
        FLOAT = ctx.FLOAT().getText()
        FLOAT = FLOAT[:-1]
        anon_id, type_ = self.generator.assign_anonymous(FLOAT, Type.FLOAT)
        self.memory.stack.append((anon_id, type_))

    def exitStr(self, ctx: ExprParser.StrContext):
        STR = ctx.STR().getText()
        STR = STR[1:-1]
        anon_id, type_ = self.generator.assign_anonymous(STR, Type.STR)
        self.memory.stack.append((anon_id, type_))

    def exitId(self, ctx: ExprParser.IdContext):
        ID = ctx.ID().getText()
        (global_char, id_, variable) = self.memory.get_variable(
            ID, self.generator.text_generator.get_current_context()
        )
        type_ = variable.get("type_", None)
        if type_ is None:
            raise ValueError("Variable does not have a type_ property")
        llvm_id = variable["llvm_id"]
        anon_id = self.generator.load(f"{llvm_id}", type_, str_length=12)
        # TODO: variable["data"]["length"]
        self.memory.stack.append((anon_id, type_))

    def exitArrayAccess(self, ctx: ExprParser.ArrayAccessContext):
        ID = ctx.ID().getText()
        arr_val = self.memory.get_arr(
            ID, self.generator.text_generator.get_current_context()
        )
        type_, size = arr_val
        EXPR = ctx.expr()

        index = None
        if hasattr(EXPR, "getText"):
            index = int(EXPR.getText())
        else:
            raise NotImplementedError()

        anon_id = self.generator.access_arr(ID, type_, size, index)
        self.memory.stack.append((anon_id, type_))

    def exitMulDiv(self, ctx: ExprParser.MulDivContext):
        r = self.memory.stack.pop()
        l = self.memory.stack.pop()
        l_id, l_type = l
        r_id, r_type = r
        if l_type != r_type:
            raise ValueError(f"Types: {l_type} must match {r_type}")

        type_ = l_type
        fn = self.generator.mul if ctx.op.type == ExprParser.MUL else self.generator.div  # type: ignore

        anon_id = fn(l_id, r_id, type_)
        self.memory.stack.append((anon_id, type_))

    def exitBitAndOrXor(self, ctx: ExprParser.BitAndOrXorContext):
        r = self.memory.stack.pop()
        l = self.memory.stack.pop()
        l_id, l_type = l
        r_id, r_type = r
        if l_type != r_type:
            raise ValueError(f"Types: {l_type} must match {r_type}")
        if l_type != Type.INT:
            raise ValueError(f"Types: {l_type} must be INT")
        if r_type != Type.INT:
            raise ValueError(f"Types: {r_type} must be INT")
        type_ = l_type
        fn = None
        if ctx.op.type == ExprParser.BIT_AND:  # type: ignore
            fn = self.generator.bit_and
        elif ctx.op.type == ExprParser.BIT_OR:  # type: ignore
            fn = self.generator.bit_or
        elif ctx.op.type == ExprParser.BIT_XOR:  # type: ignore
            fn = self.generator.bit_xor
        else:
            raise ValueError(f"Unknown binary operator: {ctx.op.type}")  # type: ignore

        anon_id = fn(l_id, r_id, type_)
        self.memory.stack.append((anon_id, type_))

    def exitBitNot(self, ctx: ExprParser.BitNotContext):
        r = self.memory.stack.pop()
        r_id, r_type = r
        if r_type != Type.INT:
            raise ValueError(f"Types: {r_type} must be INT")

        type_ = r_type
        anon_id = self.generator.bit_not(r_id, type_)
        self.memory.stack.append((anon_id, type_))

    def exitLogicalNot(self, ctx: ExprParser.LogicalNotContext):
        r = self.memory.stack.pop()
        r_id, r_type = r
        if r_type != Type.INT:
            raise ValueError(f"Types: {r_type} must be INT")

        type_ = r_type
        _anon_id = self.generator.logical_not(r_id, type_)

    def exitArray2dDeclaration(self, ctx: ExprParser.Array2dDeclarationContext):
        ID = ctx.ID().getText()
        try:
            rows, cols = ctx.INT()
            rows = int(rows.getText())
            cols = int(cols.getText())
        except:  # noqa: E722
            raise Exception("Invalid matrix declaration")
        TYPE = ctx.TYPE().getText()
        type_ = Type.map_(TYPE)

        self.memory.add(
            ID,
            TYPE,
            False,
            self.generator.text_generator.get_current_context(),
            data=(type_, rows, cols),
        )
        self.generator.declare_arr2d(ID, type_, rows, cols)

    def exitArray2dAssign(self, ctx: ExprParser.Array2dAssignContext):
        ID = ctx.ID().getText()
        arr_val = self.memory.get_arr(
            ID, self.generator.text_generator.get_current_context()
        )
        type_, rows, cols = arr_val
        r, c = ctx.arrayIndexExpr()
        r = r.expr()
        c = c.expr()
        VAL = ctx.expr()

        if hasattr(r, "getText") and hasattr(c, "getText"):
            r = int(r.getText())
            c = int(c.getText())
        else:
            raise NotImplementedError()

        val = None
        if hasattr(VAL, "getText"):
            val = VAL.getText()
        else:
            raise NotImplementedError()

        self.generator.assign_arr2d(ID, type_, rows, cols, r, c, val)

    def exitArray2dAccess(self, ctx: ExprParser.Array2dAccessContext):
        ID = ctx.ID().getText()
        type_, rows, cols = self.memory.get_arr(
            ID, self.generator.text_generator.get_current_context()
        )
        r, c = ctx.expr()

        if hasattr(r, "getText") and hasattr(c, "getText"):
            r = int(r.getText())
            c = int(c.getText())
        else:
            raise NotImplementedError()

        anon_id = self.generator.access_arr2d(ID, type_, rows, cols, r, c)
        self.memory.stack.append((anon_id, type_))

    def exitIcmpExpr(self, ctx: ExprParser.IcmpExprContext):
        r = self.memory.stack[-1]
        r_id, r_type = r
        self.generator.icmp(r_id, r_type)

    def enterIfBlock(self, ctx: ExprParser.IfBlockContext):
        self.generator.if_start()

    def exitIfBlock(self, ctx: ExprParser.IfBlockContext):
        self.generator.if_end()

    def enterWhile(self, ctx: ExprParser.WhileContext):
        self.generator.while_start()

    def enterWhileBlock(self, ctx: ExprParser.WhileBlockContext):
        self.generator.while_start_block()

    def exitWhileBlock(self, ctx: ExprParser.WhileBlockContext):
        self.generator.while_end_block()

    def enterFunction(self, ctx: ExprParser.FunctionContext):
        self.memory.clean_local_variables()
        function_id_ = ctx.functionParam().ID().getText()
        function_type_ = Type.map_(ctx.TYPE().getText())
        args = [
            (
                str(f.ID().getText()),
                Type.map_(f.TYPE().getText()),
                None if f.MUTABLE() is None else str(f.MUTABLE().getText()),
            )
            for f in ctx.functionArgs().functionArg()
        ]
        self.memory.add(
            function_id_,
            function_type_,
            True,
            self.generator.text_generator.get_current_context(),
            data=(function_type_, args),
        )

        self.generator.text_generator.set_current_context(Context.FUNCTION)
        self.generator.text_generator.reset_function_counter()

        context = self.generator.text_generator.get_current_context()

        for i, arg in enumerate(args):
            id_, type_, mut_ = arg

            _, _, variable = self.memory.set_variable(
                generator=self.generator,
                id_=id_,
                context=context,
                assign_type=type_,
                locked_type=True,
                function_args=True,
            )
            args[i] = (variable["llvm_id"], type_, mut_)

        self.generator.fn_start(function_id_, function_type_, args)

    def exitFunction(self, ctx: ExprParser.FunctionContext):
        type_ = Type.map_(ctx.TYPE().getText())
        id_ = (
            None
            if ctx.functionReturn().ID() is None
            or ctx.functionReturn().ID().getText() == "<missing ID>"
            else ctx.functionReturn().ID().getText()
        )

        # TODO: validate return type match defined

        if id_ is not None:
            _sign, id_, variable = self.memory.get_variable(
                id_, self.generator.text_generator.get_current_context()
            )
            id_ = variable["llvm_id"]
        self.generator.fn_end(id_, type_)

    def exitFunctionCall(self, ctx: ExprParser.FunctionCallContext):
        id_ = ctx.ID().getText()
        value = self.memory.get(id_, Context.HEADER)
        if value is None:
            raise ValueError(f"Function with ID: {id_} does not exist")
        data = value.get("data", None)
        if data is None:
            raise ValueError("Function with ID does not have data")
        type_returned, args_ = data
        args: list[tuple[tuple[str, Type], str, str | None]] = [
            (
                self.memory.stack.pop(),
                str(param_name),
                mut,
            )
            for _id_or_val, (param_name, _type_, mut) in zip(
                ctx.functionArgsCall().value(), args_
            )
        ]  # TODO ARGS  variable["llvm_id"]

        args = args[::-1]
        self.generator.fn_call(id_, type_returned, args)
        self.memory.stack.append(
            (f"%{self.generator.text_generator.get_incremented()-1}", type_returned)
        )

    def exitGlobalDeclaration(self, ctx: ExprParser.GlobalDeclarationContext):
        ID = ctx.ID().getText()
        self.memory.copy_global_to_local(ID)

    def exitDeleteVariable(
        self, ctx: ExprParser.DeleteVariableContext
    ):  # TODO WARN will not work!!!
        ID = ctx.ID().getText()
        self.memory.remove_variable(
            ID, self.generator.text_generator.get_current_context()
        )

    def exitStruct(self, ctx: ExprParser.StructContext):
        struct_id_ = ctx.structId().ID().getText()
        block: list[tuple[str, Type]] = [
            (str(block_id.getText()), Type.map_(block_type.getText()))
            for block_id, block_type in zip(
                ctx.structBlock().ID(), ctx.structBlock().TYPE()
            )
        ]
        block = block[::-1]
        # print(f"{block=}\n\n")
        self.memory.structs[struct_id_] = {
            "block": block,
        }
        self.generator.struct_start(struct_id_, block)
        print(f"defining struct {struct_id_} with block {block}")

    def exitStructAssign(self, ctx: ExprParser.StructAssignContext):
        id_ = ctx.ID().getText()
        struct_id = ctx.structId().ID().getText()
        print(f"creating struct {struct_id} with id {id_}")

        self.memory.add(
            id_,
            Type.STRUCT,
            False,
            self.generator.text_generator.get_current_context(),
            data=struct_id,
        )

        print(self.memory)
        print(f"structs {self.memory.structs}")
        struct = self.memory.structs[struct_id]
        block = struct["block"]
        args: list[tuple[str, Type]] = [
            self.memory.stack.pop() for _ in range(len(block))
        ]

        llvm_id = self.memory.get(
            id_, self.generator.text_generator.get_current_context()
        )["llvm_id"]

        self.generator.struct_assign(llvm_id, struct_id, args)  # FIXME TODO

    def exitStructFieldAssign(self, ctx: ExprParser.StructFieldAssignContext):
        # | ID '.' structField '=' expr								# structFieldAssign
        id_ = ctx.ID().getText()
        field = ctx.structField().ID().getText()
        struct = self.memory.get(
            id_, self.generator.text_generator.get_current_context()
        )
        struct_id = struct["data"]
        block = self.memory.structs[struct_id]["block"]

        field_index, type_ = next(
            (i, t) for i, (f, t) in enumerate(block) if f == field
        )

        print(f'assigning field "{field}" to struct "{id_}"')
        arg = self.memory.stack.pop()
        llvm_id = self.memory.get(
            id_, self.generator.text_generator.get_current_context()
        )["llvm_id"]
        self.generator.struct_field_assign(llvm_id, struct_id, field_index, arg)

    def exitStructAccess(self, ctx: ExprParser.StructAccessContext):
        # ID '.' structField				# structAccess
        id_ = ctx.ID().getText()
        field = ctx.structField().ID().getText()
        print(f'accessing field "{field}" from struct "{id_}"')
        struct = self.memory.get(
            id_, self.generator.text_generator.get_current_context()
        )
        struct_id = struct["data"]
        block = self.memory.structs[struct_id]["block"]
        # %2 = load i32, i32* getelementptr inbounds (%struct.s, %struct.s* @aaa, i32 0, i32 0)

        field_index, type_ = next(
            (i, t) for i, (f, t) in enumerate(block) if f == field
        )

        llvm_id = struct["llvm_id"]
        anon_id = self.generator.struct_load_field(
            llvm_id, struct_id, field_index, type_
        )
        # TODO: variable["data"]["length"]
        self.memory.stack.append((anon_id, type_))

        # Exit a parse tree produced by ExprParser#generator.

    def exitGenerator(self, ctx: ExprParser.GeneratorContext):
        generator_id = ctx.generatorId().ID().getText()
        array_id = ctx.arrayId().ID().getText()
        arr = self.memory.get_arr(
            array_id, self.generator.text_generator.get_current_context()
        )
        type_, size = arr

        self.memory.generators[generator_id] = {
            "array_id": array_id,
            "type_": type_,
            "size": size,
            "global_iterator_id": f"@genrator_it_{random.randint(0, 1000)}",
            "index": 0,
        }
        gen_llvm_id = self.memory.generators[generator_id]["global_iterator_id"]
        self.generator.generator_start(gen_llvm_id, array_id, type_, size)

        print(
            f"creating generator {generator_id} with array {array_id} of type {type_} and size {size}"
        )

    # Exit a parse tree produced by ExprParser#generatorCall.
    def exitGeneratorCall(self, ctx: ExprParser.GeneratorCallContext):
        generator_id = ctx.generatorId().ID().getText()

        generator = self.memory.generators[generator_id]
        array_id = generator["array_id"]
        type_ = generator["type_"]
        size = generator["size"]
        gen_llvm_id = generator["global_iterator_id"]

        array_llvm = self.memory.get_arr(
            array_id, self.generator.text_generator.get_current_context()
        )

        print(
            f"calling generator {generator_id} with array {array_id} of type {type_} and size {size}"
        )

        arr_val = self.memory.get_arr(
            array_id, self.generator.text_generator.get_current_context()
        )
        type_, size = arr_val

        index = generator["index"]
        if index >= size:
            raise ValueError("Index out of bounds")

        anon_id = self.generator.access_arr(array_id, type_, size, index)
        self.memory.stack.append((anon_id, type_))
        generator["index"] = index + 1

        # self.generator.generator_call(gen_llvm_id, array_id, type_, size)
