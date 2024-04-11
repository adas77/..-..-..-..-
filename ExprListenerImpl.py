from g4.ExprListener import ExprListener
from g4.ExprParser import ExprParser
from LLVMGenerator import LLVMGenerator, Type
from Memory import Memory, VarType


class ExprListenerImpl(ExprListener):
    def __init__(self):
        self.memory = Memory()
        self.generator = LLVMGenerator()

    # Enter a parse tree produced by ExprParser#r.
    def enterR(self, ctx: ExprParser.RContext):
        pass

    # Exit a parse tree produced by ExprParser#r.
    def exitR(self, ctx: ExprParser.RContext):
        self.generator.save()

    # Enter a parse tree produced by ExprParser#assign.
    def enterAssign(self, ctx: ExprParser.AssignContext):
        pass

    # Exit a parse tree produced by ExprParser#assign.
    def exitAssign(self, ctx: ExprParser.AssignContext):
        TYPE = ctx.TYPE()
        if TYPE is not None:
            TYPE = TYPE.getText()
            TYPE = Type.map_(TYPE)
        ID = ctx.ID().getText()
        (val_name, val_type) = self.memory.stack.pop()
        (global_char, id_, variable) = self.set_variable(ID, val_type, TYPE is not None)
        if val_type != variable["type_"]:
            if variable["locked_type"]:
                raise ValueError(
                    f"LockeType Types: {val_type} must match {variable['type_']}"
                )
            else:
                # del self.memory.local_variables[ID]
                # (global_char, id_, variable) = self.set_variable(ID, val_type, TYPE is not None)

                raise Exception("variable type change not implemented")
        self.generator.assign(global_char + id_, (val_name, val_type))

    # Enter a parse tree produced by ExprParser#arrayDeclaration.
    def enterArrayDeclaration(self, ctx: ExprParser.ArrayDeclarationContext):
        pass

    # Exit a parse tree produced by ExprParser#arrayDeclaration.
    def exitArrayDeclaration(self, ctx: ExprParser.ArrayDeclarationContext):
        pass

    # Enter a parse tree produced by ExprParser#arrayAssign.
    def enterArrayAssign(self, ctx: ExprParser.ArrayAssignContext):
        pass

    # Exit a parse tree produced by ExprParser#arrayAssign.
    def exitArrayAssign(self, ctx: ExprParser.ArrayAssignContext):
        pass

    # Enter a parse tree produced by ExprParser#print.
    def enterPrint(self, ctx: ExprParser.PrintContext):
        pass

    # Exit a parse tree produced by ExprParser#print.
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
        elif hasattr(ctx, "ID"):
            ID = ctx.ID().getText()
            (global_char, id_, variable) = self.get_variable(ID)
            type_ = variable["type_"]
            if type_ == Type.INT:
                (val_name, val_type) = self.memory.stack.pop()
                self.generator.printf(val_name, Type.INT)
                # self.generator.printf_int(global_char + id_)
            elif type_ == Type.DOUBLE:
                (val_name, val_type) = self.memory.stack.pop()
                self.generator.printf(val_name, Type.DOUBLE)
            elif type_ == Type.STR:
                self.generator.printf_str(ID, variable["data"]["length"])
            elif type_ == Type.FLOAT:
                (val_name, val_type) = self.memory.stack.pop()
                self.generator.printf(val_name, Type.FLOAT)
            else:
                raise Exception(f"Unknown variable print type: {ctx}")
        else:
            raise Exception(f"Unknown print type: {ctx}")

    # Enter a parse tree produced by ExprParser#read.
    def enterRead(self, ctx: ExprParser.ReadContext):
        pass

    # Exit a parse tree produced by ExprParser#read.
    def exitRead(self, ctx: ExprParser.ReadContext):
        ID = ctx.ID().getText()
        (global_char, id_, variable) = self.get_variable(ID)
        type_ = variable["type_"]
        self.generator.scanf(global_char + id_, type_)

    # Enter a parse tree produced by ExprParser#structAssign.
    def enterStructAssign(self, ctx: ExprParser.StructAssignContext):
        pass

    # Exit a parse tree produced by ExprParser#structAssign.
    def exitStructAssign(self, ctx: ExprParser.StructAssignContext):
        pass

    # Enter a parse tree produced by ExprParser#structFieldAssign.
    def enterStructFieldAssign(self, ctx: ExprParser.StructFieldAssignContext):
        pass

    # Exit a parse tree produced by ExprParser#structFieldAssign.
    def exitStructFieldAssign(self, ctx: ExprParser.StructFieldAssignContext):
        pass

    # Enter a parse tree produced by ExprParser#comment.
    def enterComment(self, ctx: ExprParser.CommentContext):
        pass

    # Exit a parse tree produced by ExprParser#comment.
    def exitComment(self, ctx: ExprParser.CommentContext):
        pass

    # Enter a parse tree produced by ExprParser#addSub.
    def enterAddSub(self, ctx: ExprParser.AddSubContext):
        pass

    # Exit a parse tree produced by ExprParser#addSub.
    def exitAddSub(self, ctx: ExprParser.AddSubContext):
        # print(2*"\n","exitAddSub")
        # print(f"{dir(ctx)}")
        # print(f"{dir(ctx.term)}")

        # TODO: Chceck muldiv

        # if ctx.term() is not None:

        #
        # ``

        r: tuple[str, Type] = self.memory.stack.pop()
        l: tuple[str, Type] = self.memory.stack.pop()
        l_id, l_type = l
        r_id, r_type = r
        if l_type != r_type:
            raise ValueError(f"Types: {l_type} must match {r_type}")

        type_ = l_type
        fn = self.generator.add if ctx.op.type == ExprParser.ADD else self.generator.sub

        anon_id = fn(l_id, r_id, type_)
        self.memory.stack.append((anon_id, type_))

    # Enter a parse tree produced by ExprParser#single.
    def enterSingle(self, ctx: ExprParser.SingleContext):
        pass

    # Exit a parse tree produced by ExprParser#single.
    def exitSingle(self, ctx: ExprParser.SingleContext):
        pass

    # Enter a parse tree produced by ExprParser#int.
    def enterInt(self, ctx: ExprParser.IntContext):
        pass

    # Exit a parse tree produced by ExprParser#int.
    def exitInt(self, ctx: ExprParser.IntContext):
        INT = ctx.INT().getText()
        anon_id = self.generator.assign_anonymous(int(INT), Type.INT)
        anon_id = self.generator.load(anon_id, Type.INT)
        self.memory.stack.append((anon_id, Type.INT))

    # Enter a parse tree produced by ExprParser#double.
    def enterDouble(self, ctx: ExprParser.DoubleContext):
        pass

    # Exit a parse tree produced by ExprParser#double.
    def exitDouble(self, ctx: ExprParser.DoubleContext):
        DOUBLE = ctx.DOUBLE().getText()
        anon_id = self.generator.assign_anonymous(float(DOUBLE), Type.DOUBLE)
        anon_id = self.generator.load(anon_id, Type.DOUBLE)
        self.memory.stack.append((anon_id, Type.DOUBLE))

    # Exit a parse tree produced by ExprParser#double.
    def exitFloat(self, ctx: ExprParser.DoubleContext):
        FLOAT = ctx.FLOAT().getText()
        FLOAT = FLOAT[:-1]
        anon_id = self.generator.assign_anonymous(float(FLOAT), Type.FLOAT)
        anon_id = self.generator.load(anon_id, Type.FLOAT)
        self.memory.stack.append((anon_id, Type.FLOAT))

    # Enter a parse tree produced by ExprParser#str.
    def enterStr(self, ctx: ExprParser.StrContext):
        pass

    # Exit a parse tree produced by ExprParser#str.
    def exitStr(self, ctx: ExprParser.StrContext):
        STR = ctx.STR().getText()
        self.memory.stack.append((None, Type.STR))

    # Enter a parse tree produced by ExprParser#id.
    def enterId(self, ctx: ExprParser.IdContext):
        pass

    # Exit a parse tree produced by ExprParser#id.
    def exitId(self, ctx: ExprParser.IdContext):
        ID = ctx.ID().getText()
        (global_char, id_, variable) = self.get_variable(ID)
        type_ = variable["type_"]
        anon_id = ""
        if type_ == Type.INT:
            anon_id = self.generator.load(global_char + id_, Type.INT)
        elif type_ == Type.DOUBLE:
            anon_id = self.generator.load(global_char + id_, Type.DOUBLE)
        elif type_ == Type.FLOAT:
            anon_id = self.generator.load(global_char + id_, Type.FLOAT)
        else:
            raise Exception(f"Unknown variable type: {type_}")
        self.memory.stack.append((anon_id, type_))

    # Enter a parse tree produced by ExprParser#arrayAccess.
    def enterArrayAccess(self, ctx: ExprParser.ArrayAccessContext):
        pass

    # Exit a parse tree produced by ExprParser#arrayAccess.
    def exitArrayAccess(self, ctx: ExprParser.ArrayAccessContext):
        pass

    # Enter a parse tree produced by ExprParser#structAccess.
    def enterStructAccess(self, ctx: ExprParser.StructAccessContext):
        pass

    # Exit a parse tree produced by ExprParser#structAccess.
    def exitStructAccess(self, ctx: ExprParser.StructAccessContext):
        pass

    # Enter a parse tree produced by ExprParser#structField.
    def enterStructField(self, ctx: ExprParser.StructFieldContext):
        pass

    # Exit a parse tree produced by ExprParser#structField.
    def exitStructField(self, ctx: ExprParser.StructFieldContext):
        pass

    # Enter a parse tree produced by ExprParser#arrayIndexExpr.
    def enterArrayIndexExpr(self, ctx: ExprParser.ArrayIndexExprContext):
        pass

    # Exit a parse tree produced by ExprParser#arrayIndexExpr.
    def exitArrayIndexExpr(self, ctx: ExprParser.ArrayIndexExprContext):
        pass

    # Enter a parse tree produced by ExprParser#term.
    def enterTerm(self, ctx: ExprParser.TermContext):
        pass

    # Exit a parse tree produced by ExprParser#term.
    def exitTerm(self, ctx: ExprParser.TermContext):
        pass

    # Enter a parse tree produced by ExprParser#factor.
    def enterFactor(self, ctx: ExprParser.FactorContext):
        pass

    # Exit a parse tree produced by ExprParser#factor.
    def exitFactor(self, ctx: ExprParser.FactorContext):
        pass

    # Enter a parse tree produced by ExprParser#function.
    def enterFunction(self, ctx: ExprParser.FunctionContext):
        pass

    # Exit a parse tree produced by ExprParser#function.
    def exitFunction(self, ctx: ExprParser.FunctionContext):
        pass

    # Enter a parse tree produced by ExprParser#functionParam.
    def enterFunctionParam(self, ctx: ExprParser.FunctionParamContext):
        pass

    # Exit a parse tree produced by ExprParser#functionParam.
    def exitFunctionParam(self, ctx: ExprParser.FunctionParamContext):
        pass

    # Enter a parse tree produced by ExprParser#functionBlock.
    def enterFunctionBlock(self, ctx: ExprParser.FunctionBlockContext):
        pass

    # Exit a parse tree produced by ExprParser#functionBlock.
    def exitFunctionBlock(self, ctx: ExprParser.FunctionBlockContext):
        pass

    # Enter a parse tree produced by ExprParser#struct.
    def enterStruct(self, ctx: ExprParser.StructContext):
        pass

    # Exit a parse tree produced by ExprParser#struct.
    def exitStruct(self, ctx: ExprParser.StructContext):
        pass

    # Enter a parse tree produced by ExprParser#structId.
    def enterStructId(self, ctx: ExprParser.StructIdContext):
        pass

    # Exit a parse tree produced by ExprParser#structId.
    def exitStructId(self, ctx: ExprParser.StructIdContext):
        pass

    # Enter a parse tree produced by ExprParser#structBlock.
    def enterStructBlock(self, ctx: ExprParser.StructBlockContext):
        pass

    # Exit a parse tree produced by ExprParser#structBlock.
    def exitStructBlock(self, ctx: ExprParser.StructBlockContext):
        pass

    # Enter a parse tree produced by ExprParser#while.
    def enterWhile(self, ctx: ExprParser.WhileContext):
        pass

    # Exit a parse tree produced by ExprParser#while.
    def exitWhile(self, ctx: ExprParser.WhileContext):
        pass

    # Enter a parse tree produced by ExprParser#whileBlock.
    def enterWhileBlock(self, ctx: ExprParser.WhileBlockContext):
        pass

    # Exit a parse tree produced by ExprParser#whileBlock.
    def exitWhileBlock(self, ctx: ExprParser.WhileBlockContext):
        pass

    # Enter a parse tree produced by ExprParser#value.
    def enterValue(self, ctx: ExprParser.ValueContext):
        pass

    # Exit a parse tree produced by ExprParser#value.
    def exitValue(self, ctx: ExprParser.ValueContext):
        pass

    def set_variable(self, id_: str, assign_type: Type, locked_type: bool = False):
        final_id: tuple[str, str, object] = ""
        if self.memory.global_context:
            variable = self.memory.global_variables.get(id_, None)
            if variable is None:
                self.memory.add_variable(
                    id_, assign_type, VarType.GLOBAL_VAR, locked_type
                )
                self.generator.declare_variable(id_, assign_type, is_global=True)
                variable = self.memory.global_variables.get(id_, None)
            else:
                if variable["locked_type"]:
                    if variable["type_"] != assign_type:
                        raise ValueError(
                            f"Types: {variable['type_']} must match {assign_type}"
                        )

            final_id = ("@", id_, variable)
        else:
            variable = self.memory.local_variables.get(id_, None)
            if variable is None:
                # self.memory.add_variable(id_,type_,var_type,locked_type,data)

                self.memory.add_variable(
                    id_, assign_type, VarType.LOCAL_VAR, locked_type
                )
                self.generator.declare_variable(id_, assign_type, is_global=False)
                variable = self.memory.local_variables.get(id_, None)
            else:
                if variable["locked_type"]:
                    if variable["type_"] != assign_type:
                        raise ValueError(
                            f"Types: {variable['type_']} must match {assign_type}"
                        )
            final_id = ("%", id_, variable)
        return final_id

    def get_variable(self, id_: str):
        final_id: tuple[str, str, object] = None
        if self.memory.local_variables.get(id_, None) is not None:
            final_id = ("%", id_, self.memory.local_variables.get(id_, None))
        elif self.memory.global_variables.get(id_, None) is not None:
            final_id = ("@", id_, self.memory.global_variables.get(id_, None))
        else:
            raise ValueError(f"{id_} not found")
        return final_id

    # Enter a parse tree produced by ExprParser#mulDiv.
    def enterMulDiv(self, ctx: ExprParser.MulDivContext):
        pass

    # Exit a parse tree produced by ExprParser#mulDiv.
    def exitMulDiv(self, ctx: ExprParser.MulDivContext):
        r: tuple[str, Type] = self.memory.stack.pop()
        l: tuple[str, Type] = self.memory.stack.pop()
        l_id, l_type = l
        r_id, r_type = r
        if l_type != r_type:
            raise ValueError(f"Types: {l_type} must match {r_type}")

        type_ = l_type
        fn = self.generator.mul if ctx.op.type == ExprParser.MUL else self.generator.div

        anon_id = fn(l_id, r_id, type_)
        self.memory.stack.append((anon_id, type_))
