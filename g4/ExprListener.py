# Generated from Expr.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete listener for a parse tree produced by ExprParser.
class ExprListener(ParseTreeListener):

    # Enter a parse tree produced by ExprParser#r.
    def enterR(self, ctx:ExprParser.RContext):
        pass

    # Exit a parse tree produced by ExprParser#r.
    def exitR(self, ctx:ExprParser.RContext):
        pass


    # Enter a parse tree produced by ExprParser#printExpr.
    def enterPrintExpr(self, ctx:ExprParser.PrintExprContext):
        pass

    # Exit a parse tree produced by ExprParser#printExpr.
    def exitPrintExpr(self, ctx:ExprParser.PrintExprContext):
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


    # Enter a parse tree produced by ExprParser#blank.
    def enterBlank(self, ctx:ExprParser.BlankContext):
        pass

    # Exit a parse tree produced by ExprParser#blank.
    def exitBlank(self, ctx:ExprParser.BlankContext):
        pass


    # Enter a parse tree produced by ExprParser#str.
    def enterStr(self, ctx:ExprParser.StrContext):
        pass

    # Exit a parse tree produced by ExprParser#str.
    def exitStr(self, ctx:ExprParser.StrContext):
        pass


    # Enter a parse tree produced by ExprParser#parens.
    def enterParens(self, ctx:ExprParser.ParensContext):
        pass

    # Exit a parse tree produced by ExprParser#parens.
    def exitParens(self, ctx:ExprParser.ParensContext):
        pass


    # Enter a parse tree produced by ExprParser#MulDiv.
    def enterMulDiv(self, ctx:ExprParser.MulDivContext):
        pass

    # Exit a parse tree produced by ExprParser#MulDiv.
    def exitMulDiv(self, ctx:ExprParser.MulDivContext):
        pass


    # Enter a parse tree produced by ExprParser#AddSub.
    def enterAddSub(self, ctx:ExprParser.AddSubContext):
        pass

    # Exit a parse tree produced by ExprParser#AddSub.
    def exitAddSub(self, ctx:ExprParser.AddSubContext):
        pass


    # Enter a parse tree produced by ExprParser#double.
    def enterDouble(self, ctx:ExprParser.DoubleContext):
        pass

    # Exit a parse tree produced by ExprParser#double.
    def exitDouble(self, ctx:ExprParser.DoubleContext):
        pass


    # Enter a parse tree produced by ExprParser#id.
    def enterId(self, ctx:ExprParser.IdContext):
        pass

    # Exit a parse tree produced by ExprParser#id.
    def exitId(self, ctx:ExprParser.IdContext):
        pass


    # Enter a parse tree produced by ExprParser#arrayAccess.
    def enterArrayAccess(self, ctx:ExprParser.ArrayAccessContext):
        pass

    # Exit a parse tree produced by ExprParser#arrayAccess.
    def exitArrayAccess(self, ctx:ExprParser.ArrayAccessContext):
        pass


    # Enter a parse tree produced by ExprParser#int.
    def enterInt(self, ctx:ExprParser.IntContext):
        pass

    # Exit a parse tree produced by ExprParser#int.
    def exitInt(self, ctx:ExprParser.IntContext):
        pass


    # Enter a parse tree produced by ExprParser#val.
    def enterVal(self, ctx:ExprParser.ValContext):
        pass

    # Exit a parse tree produced by ExprParser#val.
    def exitVal(self, ctx:ExprParser.ValContext):
        pass



del ExprParser