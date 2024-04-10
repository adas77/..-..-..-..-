from g4.ExprListener import ExprListener
from g4.ExprParser import ExprParser
from LLVMGenerator import LLVMGenerator, Type

class ExprListenerImpl(ExprListener):
    def __init__(self):
        self.memory = {}
        self.generator = LLVMGenerator()

    # Enter a parse tree produced by ExprParser#r.
    def enterR(self, ctx:ExprParser.RContext):
        pass

    # Exit a parse tree produced by ExprParser#r.
    def exitR(self, ctx:ExprParser.RContext):
        pass


    # Enter a parse tree produced by ExprParser#declaration.
    def enterDeclaration(self, ctx:ExprParser.DeclarationContext):
        pass

    # Exit a parse tree produced by ExprParser#declaration.
    def exitDeclaration(self, ctx:ExprParser.DeclarationContext):
        pass


    # Enter a parse tree produced by ExprParser#assign.
    def enterAssign(self, ctx:ExprParser.AssignContext):
        pass

    # Exit a parse tree produced by ExprParser#assign.
    def exitAssign(self, ctx:ExprParser.AssignContext):
        pass


    # Enter a parse tree produced by ExprParser#arrayDeclaration.
    def enterArrayDeclaration(self, ctx:ExprParser.ArrayDeclarationContext):
        pass

    # Exit a parse tree produced by ExprParser#arrayDeclaration.
    def exitArrayDeclaration(self, ctx:ExprParser.ArrayDeclarationContext):
        pass


    # Enter a parse tree produced by ExprParser#arrayAssign.
    def enterArrayAssign(self, ctx:ExprParser.ArrayAssignContext):
        pass

    # Exit a parse tree produced by ExprParser#arrayAssign.
    def exitArrayAssign(self, ctx:ExprParser.ArrayAssignContext):
        pass


    # Enter a parse tree produced by ExprParser#print.
    def enterPrint(self, ctx:ExprParser.PrintContext):
        pass

    # Exit a parse tree produced by ExprParser#print.
    def exitPrint(self, ctx:ExprParser.PrintContext):
        pass


    # Enter a parse tree produced by ExprParser#read.
    def enterRead(self, ctx:ExprParser.ReadContext):
        pass

    # Exit a parse tree produced by ExprParser#read.
    def exitRead(self, ctx:ExprParser.ReadContext):
        pass


    # Enter a parse tree produced by ExprParser#structAssign.
    def enterStructAssign(self, ctx:ExprParser.StructAssignContext):
        pass

    # Exit a parse tree produced by ExprParser#structAssign.
    def exitStructAssign(self, ctx:ExprParser.StructAssignContext):
        pass


    # Enter a parse tree produced by ExprParser#structFieldAssign.
    def enterStructFieldAssign(self, ctx:ExprParser.StructFieldAssignContext):
        pass

    # Exit a parse tree produced by ExprParser#structFieldAssign.
    def exitStructFieldAssign(self, ctx:ExprParser.StructFieldAssignContext):
        pass


    # Enter a parse tree produced by ExprParser#comment.
    def enterComment(self, ctx:ExprParser.CommentContext):
        pass

    # Exit a parse tree produced by ExprParser#comment.
    def exitComment(self, ctx:ExprParser.CommentContext):
        pass


    # Enter a parse tree produced by ExprParser#addSub.
    def enterAddSub(self, ctx:ExprParser.AddSubContext):
        pass

    # Exit a parse tree produced by ExprParser#addSub.
    def exitAddSub(self, ctx:ExprParser.AddSubContext):
        pass


    # Enter a parse tree produced by ExprParser#single.
    def enterSingle(self, ctx:ExprParser.SingleContext):
        pass

    # Exit a parse tree produced by ExprParser#single.
    def exitSingle(self, ctx:ExprParser.SingleContext):
        pass


    # Enter a parse tree produced by ExprParser#arrayAccess.
    def enterArrayAccess(self, ctx:ExprParser.ArrayAccessContext):
        pass

    # Exit a parse tree produced by ExprParser#arrayAccess.
    def exitArrayAccess(self, ctx:ExprParser.ArrayAccessContext):
        pass


    # Enter a parse tree produced by ExprParser#structAccess.
    def enterStructAccess(self, ctx:ExprParser.StructAccessContext):
        pass

    # Exit a parse tree produced by ExprParser#structAccess.
    def exitStructAccess(self, ctx:ExprParser.StructAccessContext):
        pass


    # Enter a parse tree produced by ExprParser#structField.
    def enterStructField(self, ctx:ExprParser.StructFieldContext):
        pass

    # Exit a parse tree produced by ExprParser#structField.
    def exitStructField(self, ctx:ExprParser.StructFieldContext):
        pass


    # Enter a parse tree produced by ExprParser#arrayIndexExpr.
    def enterArrayIndexExpr(self, ctx:ExprParser.ArrayIndexExprContext):
        pass

    # Exit a parse tree produced by ExprParser#arrayIndexExpr.
    def exitArrayIndexExpr(self, ctx:ExprParser.ArrayIndexExprContext):
        pass


    # Enter a parse tree produced by ExprParser#term.
    def enterTerm(self, ctx:ExprParser.TermContext):
        pass

    # Exit a parse tree produced by ExprParser#term.
    def exitTerm(self, ctx:ExprParser.TermContext):
        pass


    # Enter a parse tree produced by ExprParser#factor.
    def enterFactor(self, ctx:ExprParser.FactorContext):
        pass

    # Exit a parse tree produced by ExprParser#factor.
    def exitFactor(self, ctx:ExprParser.FactorContext):
        pass


    # Enter a parse tree produced by ExprParser#function.
    def enterFunction(self, ctx:ExprParser.FunctionContext):
        pass

    # Exit a parse tree produced by ExprParser#function.
    def exitFunction(self, ctx:ExprParser.FunctionContext):
        pass


    # Enter a parse tree produced by ExprParser#functionParam.
    def enterFunctionParam(self, ctx:ExprParser.FunctionParamContext):
        pass

    # Exit a parse tree produced by ExprParser#functionParam.
    def exitFunctionParam(self, ctx:ExprParser.FunctionParamContext):
        pass


    # Enter a parse tree produced by ExprParser#functionBlock.
    def enterFunctionBlock(self, ctx:ExprParser.FunctionBlockContext):
        pass

    # Exit a parse tree produced by ExprParser#functionBlock.
    def exitFunctionBlock(self, ctx:ExprParser.FunctionBlockContext):
        pass


    # Enter a parse tree produced by ExprParser#struct.
    def enterStruct(self, ctx:ExprParser.StructContext):
        pass

    # Exit a parse tree produced by ExprParser#struct.
    def exitStruct(self, ctx:ExprParser.StructContext):
        pass


    # Enter a parse tree produced by ExprParser#structId.
    def enterStructId(self, ctx:ExprParser.StructIdContext):
        pass

    # Exit a parse tree produced by ExprParser#structId.
    def exitStructId(self, ctx:ExprParser.StructIdContext):
        pass


    # Enter a parse tree produced by ExprParser#structBlock.
    def enterStructBlock(self, ctx:ExprParser.StructBlockContext):
        pass

    # Exit a parse tree produced by ExprParser#structBlock.
    def exitStructBlock(self, ctx:ExprParser.StructBlockContext):
        pass


    # Enter a parse tree produced by ExprParser#while.
    def enterWhile(self, ctx:ExprParser.WhileContext):
        pass

    # Exit a parse tree produced by ExprParser#while.
    def exitWhile(self, ctx:ExprParser.WhileContext):
        pass


    # Enter a parse tree produced by ExprParser#whileBlock.
    def enterWhileBlock(self, ctx:ExprParser.WhileBlockContext):
        pass

    # Exit a parse tree produced by ExprParser#whileBlock.
    def exitWhileBlock(self, ctx:ExprParser.WhileBlockContext):
        pass


    # Enter a parse tree produced by ExprParser#value.
    def enterValue(self, ctx:ExprParser.ValueContext):
        pass

    # Exit a parse tree produced by ExprParser#value.
    def exitValue(self, ctx:ExprParser.ValueContext):
        pass