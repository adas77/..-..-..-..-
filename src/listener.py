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
            ctx.functionReturn().ID().getText()
            if ctx.functionReturn().ID() is not None
            else None
        )
        # TODO: validate return type match defined
        if id_ is not None:
            sign, id_, variable = self.memory.get_variable(
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
            for id_or_val, (param_name, type_, mut) in zip(
                ctx.functionArgsCall().value(), args_
            )
        ]  # TODO ARGS  variable["llvm_id"]

        # for id_or_val, type_, param_name, mut in args_:
        #     (val_name, val_type) = self.memory.stack.pop()

        # (i32 %12, double %13)

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
