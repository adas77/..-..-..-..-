from g4.ExprListener import ExprListener
from g4.ExprParser import ExprParser
from LLVMGenerator import LLVMGenerator
# from g4.ExprParser import ExprParser
# This class defines a complete listener for a parse tree produced by ExprParser.


class ExprListenerImpl(ExprListener):
    def __init__(self):
        self.memory = {}
        self.generator = LLVMGenerator()

    def add_variable(self, ID, TYPE, data = None):
        if self.variable_exists(ID):
            raise ValueError(f"{ID} already declared")
        variable_struct = {
            "TYPE": TYPE,
            "data": data
        }
        self.memory[ID] = variable_struct
    
    def remove_variable(self, ID):
        if not self.variable_exists(ID):
            raise ValueError(f"{ID} not declared")
        self.memory.pop(ID)
    
    def get_variable(self, ID):
        if not self.variable_exists(ID):
            raise ValueError(f"{ID} not declared")
        return self.memory.get(ID, None)

    def variable_exists(self, ID):
        return ID in self.memory

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
            self.generator.declare_double(ID)
            print(f"declared double {ID}")
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
        # print("exitass", dir(ctx))
        print("exitass__", dir(ctx.expr()))
        print(ID)

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
            self.generator.assign_double(ID, DOUBLE)
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
        else:
            raise Exception(f"variable type not known {ID}")
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

        # ops = {
        #     ExprParser.INT: ctx.INT(),
        #     ExprParser.DOUBLE: ctx.DOUBLE(),
        #     ExprParser.STR: ctx.STR(),
        #     ExprParser.ID: None if not hasattr(ctx.ID(), "getText") else
        #     self.memory.get(
        #         ctx.ID().getText(), None)
        # }
        # v = ops.get(ctx.op.type, None)
        # v = v if v is None or isinstance(v, (str, list)) else v.getText()

        # # print("ctx", dir(ctx))

        # print(ctx.getText())
        # self.generator.printf()
        # print(f"{v=}")
        pass

    # Exit a parse tree produced by ExprParser#print.
    def exitPrint(self, ctx: ExprParser.PrintContext):
        print(f"{ctx.op.type=}")
        # print(f"{ExprParser.DOUBLE=}")
        # print("printdir", dir(ctx))

        if ctx.INT() is not None:
            INT = ctx.INT().getText()
            self.generator.printf_int(INT)
        elif ctx.ID() is not None:
            ID = ctx.ID().getText()
            val = self.memory.get(ID, None)
            type_ = ctx.op.type
            print(F"{type_=}")
            print(F"{self.memory=}")
            if val is None:
                raise Exception(f"variable not declared {ID}")
            elif isinstance(val, int):
                self.generator.printf_int(ID)
            elif isinstance(val, float):
                self.generator.printf_double(ID)
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
        pass

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
        pass

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


del ExprParser
