from g4.ExprListener import ExprListener
from g4.ExprParser import ExprParser
from LLVMGenerator import LLVMGenerator
from uuid import uuid4
# from g4.ExprParser import ExprParser
# This class defines a complete listener for a parse tree produced by ExprParser.


class ExprListenerImpl(ExprListener):
    def __init__(self):
        self.memory = {}
        self.generator = LLVMGenerator()

    # Enter a parse tree produced by ExprParser#r.

    def enterR(self, ctx: ExprParser.RContext):
        pass

    # Exit a parse tree produced by ExprParser#r.
    def exitR(self, ctx: ExprParser.RContext):
        self.generator.save()

    # Enter a parse tree produced by ExprParser#printExpr.
    def enterPrintExpr(self, ctx: ExprParser.PrintExprContext):
        pass

    # Exit a parse tree produced by ExprParser#printExpr.
    def exitPrintExpr(self, ctx: ExprParser.PrintExprContext):
        pass

    # Enter a parse tree produced by ExprParser#declaration.
    def enterDeclaration(self, ctx: ExprParser.DeclarationContext):
        pass

    # Exit a parse tree produced by ExprParser#declaration.
    def exitDeclaration(self, ctx: ExprParser.DeclarationContext):
        ID = ctx.ID().getText()
        if ID in self.memory:
            raise Exception(f"variable already declared {ID}")
        TYPE = ctx.TYPE().getText()
        if TYPE == "int":
            self.memory[ID] = int(0)  # just to be sure
            self.generator.declare_int(ID)
            print(f"declared int {ID}")
        elif TYPE == "double":
            self.memory[ID] = float(0)
            self.generator.declare_float(ID)
            print(f"declared float {ID}")
        elif TYPE == "string":
            self.memory[ID] = ""
            # self.generator.declare_str(ID)
            print(f"declared string {ID}")
        else:
            raise Exception(f"unknown type {TYPE}")

    # Enter a parse tree produced by ExprParser#assign.
    def enterAssign(self, ctx: ExprParser.AssignContext):
        pass

    # Exit a parse tree produced by ExprParser#assign.
    def exitAssign(self, ctx: ExprParser.AssignContext):
        ID = ctx.ID().getText()

        if ID not in self.memory:
            raise ValueError(f"{ID} not declared")

        if hasattr(ctx.expr(), "INT"):
            INT = ctx.expr().INT().getText()
            print(f"INT assign {ID} = {INT}")
            self.memory[ID] = int(INT)
            self.generator.assign_int(ID, INT)
        elif hasattr(ctx.expr(), "DOUBLE"):
            DOUBLE = ctx.expr().DOUBLE().getText()
            print(f"DOUBLE assign {ID} = {DOUBLE}")
            self.memory[ID] = float(DOUBLE)
            self.generator.assign_float(ID, DOUBLE)
        elif hasattr(ctx.expr(), "STR"):
            STR = ctx.expr().STR().getText()
            print(f"STR assign {ID} = {STR}")
            STR = STR[1:-1]
            self.memory[ID] = STR
            # self.generator.assign_str(ID, STR)
            self.generator.declare_static_string(ID, STR)
        elif hasattr(ctx.expr(), "ID"):
            ID_ID = ctx.expr().ID().getText()
            print(f"ID assign = {ID} = {ID_ID}")
            # generator mov by id to id in llvm IR
            self.memory[ID] = self.memory[STR]
        elif hasattr(ctx.expr(), "DIV") or hasattr(ctx.expr(), "MUL"):
            pass
        elif hasattr(ctx.expr(), "SUB") or hasattr(ctx.expr(), "ADD"):
            pass
        else:
            raise Exception(f"variable type not known {ID}")
    # Exit a parse tree produced by ExprParser#arrayDeclaration.

    def exitArrayDeclaration(self, ctx: ExprParser.ArrayDeclarationContext):
        ID = ctx.ID().getText()
        SIZE = int(ctx.INT().getText())
        TYPE = ctx.TYPE().getText()
        self.memory[ID] = (
            [.0 if TYPE == "double" else 0 for _ in range(SIZE)], TYPE)
        TYPE_GEN = "i32" if TYPE == "int" else TYPE
        self.generator.declare_arr(ID, TYPE_GEN, SIZE)

    # Enter a parse tree produced by ExprParser#arrayAssign.
    def enterArrayAssign(self, ctx: ExprParser.ArrayAssignContext):
        pass

    # Exit a parse tree produced by ExprParser#arrayAssign.
    def exitArrayAssign(self, ctx: ExprParser.ArrayAssignContext):
        ID = ctx.ID(0).getText()
        index = int(self.memory.get(
            ctx.ID(1).getText()) if ctx.op.type == ExprParser.ID else ctx.INT().getText())

        update, TYPE = self.memory.get(ID, None)
        if not update:
            raise ValueError(f"Array with ID: {ID} is not declared")
        # TODO handle more than: INT | DOUBLE
        if not hasattr(ctx.expr(), f"{TYPE}".upper()):
            raise ValueError(
                f"Array with ID: {ID} stores only {TYPE} type variables")
        val = int(ctx.expr().INT().getText()) if TYPE == "int" else float(
            ctx.expr().DOUBLE().getText())
        update[index] = val
        self.memory[ID] = (update, TYPE)
        TYPE_GEN = "i32" if TYPE == "int" else TYPE
        self.generator.assign_arr(ID, TYPE_GEN, len(update), index, val)

    # Enter a parse tree produced by ExprParser#print.

    def enterPrint(self, ctx: ExprParser.PrintContext):
        pass

    # Exit a parse tree produced by ExprParser#print.
    def exitPrint(self, ctx: ExprParser.PrintContext):
        if ctx.INT() is not None:
            INT = ctx.INT().getText()
            self.generator.printf_int(INT)
        elif ctx.ID() is not None:
            ID = ctx.ID().getText()
            val = self.memory.get(ID, None)
            if val is None:
                raise Exception(f"variable not declared {ID}")
            elif isinstance(val, int):
                self.generator.printf_int(ID)
            elif isinstance(val, float):
                self.generator.printf_float(ID)
            elif isinstance(val, str):
                self.generator.printf_str(ID, len(val)+1)
        else:
            raise Exception("unknown print type")

        print(self.memory)
    # Enter a parse tree produced by ExprParser#read.

    def enterRead(self, ctx: ExprParser.ReadContext):
        pass

    # Exit a parse tree produced by ExprParser#read.
    def exitRead(self, ctx: ExprParser.ReadContext):
        pass

    # Enter a parse tree produced by ExprParser#blank.
    def enterBlank(self, ctx: ExprParser.BlankContext):
        pass

    # Exit a parse tree produced by ExprParser#blank.
    def exitBlank(self, ctx: ExprParser.BlankContext):
        pass

    # Enter a parse tree produced by ExprParser#parens.
    def enterParens(self, ctx: ExprParser.ParensContext):
        pass

    # Exit a parse tree produced by ExprParser#parens.
    def exitParens(self, ctx: ExprParser.ParensContext):
        pass

    # Enter a parse tree produced by ExprParser#MulDiv.
    def enterMulDiv(self, ctx: ExprParser.MulDivContext):

        pass

    # Exit a parse tree produced by ExprParser#MulDiv.
    def exitMulDiv(self, ctx: ExprParser.MulDivContext):
        # FIXME
        def parse(x):
            return float(x) if hasattr(
                ctx.expr(0), "DOUBLE") or hasattr(ctx.expr(1), "DOUBLE") else int(x)
        left = ctx.expr(0).getText()
        right = ctx.expr(1).getText()

    # Enter a parse tree produced by ExprParser#AddSub.

    def enterAddSub(self, ctx: ExprParser.AddSubContext):
        pass

    # Exit a parse tree produced by ExprParser#AddSub.
    def exitAddSub(self, ctx: ExprParser.AddSubContext):
        pass

    # Enter a parse tree produced by ExprParser#id.
    def enterId(self, ctx: ExprParser.IdContext):
        pass

    # Exit a parse tree produced by ExprParser#id.
    def exitId(self, ctx: ExprParser.IdContext):
        pass

    # Enter a parse tree produced by ExprParser#arrayAccess.
    def enterArrayAccess(self, ctx: ExprParser.ArrayAccessContext):
        pass

    # Exit a parse tree produced by ExprParser#arrayAccess.
    def exitArrayAccess(self, ctx: ExprParser.ArrayAccessContext):
        id_ = ctx.ID(0).getText()
        index = int(self.memory.get(
            ctx.ID(1).getText(), None) if ctx.op.type == ExprParser.ID else ctx.INT().getText())
        if not index:
            raise ValueError(
                f"There is no variable with ID: {ctx.ID().getText(1)}")
        arr, type_ = self.memory.get(id_, None)
        size = len(arr)

        if index >= size:
            raise ValueError(f"index {index} out of bounds")

        if not arr:
            raise ValueError(
                f"There is no arr with ID: {id_}")
        # TODO:
        # FIXME: hardcoded
        id_new = ''.join([char for char in f"{uuid4()}" if char not in "-"])

        TYPE_GEN = "i32" if type_ == "int" else type_
        id_new_print = self.generator.access_arr(
            index, id_, id_new, size, TYPE_GEN)

        # FIXME: remove this - only for testing
        if TYPE_GEN == "i32":
            self.generator.printf_int(id_new_print)
        else:
            self.generator.printf_float(id_new_print)

    # Enter a parse tree produced by ExprParser#double.
    def enterDouble(self, ctx: ExprParser.DoubleContext):
        pass

    # Exit a parse tree produced by ExprParser#double.
    def exitDouble(self, ctx: ExprParser.DoubleContext):
        pass

    # Enter a parse tree produced by ExprParser#int.
    def enterInt(self, ctx: ExprParser.IntContext):
        pass

    # Exit a parse tree produced by ExprParser#int.
    def exitInt(self, ctx: ExprParser.IntContext):
        pass

    # Enter a parse tree produced by ExprParser#val.
    def enterVal(self, ctx: ExprParser.ValContext):
        pass

    # Exit a parse tree produced by ExprParser#val.
    def exitVal(self, ctx: ExprParser.ValContext):
        pass
