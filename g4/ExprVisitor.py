# Generated from Expr.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete generic visitor for a parse tree produced by ExprParser.

class ExprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExprParser#r.
    def visitR(self, ctx:ExprParser.RContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#printExpr.
    def visitPrintExpr(self, ctx:ExprParser.PrintExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#declaration.
    def visitDeclaration(self, ctx:ExprParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#assign.
    def visitAssign(self, ctx:ExprParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#arrayDeclaration.
    def visitArrayDeclaration(self, ctx:ExprParser.ArrayDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#arrayAssign.
    def visitArrayAssign(self, ctx:ExprParser.ArrayAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#print.
    def visitPrint(self, ctx:ExprParser.PrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#read.
    def visitRead(self, ctx:ExprParser.ReadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#blank.
    def visitBlank(self, ctx:ExprParser.BlankContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#parens.
    def visitParens(self, ctx:ExprParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#MulDiv.
    def visitMulDiv(self, ctx:ExprParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#AddSub.
    def visitAddSub(self, ctx:ExprParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#id.
    def visitId(self, ctx:ExprParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#arrayAccess.
    def visitArrayAccess(self, ctx:ExprParser.ArrayAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#float.
    def visitFloat(self, ctx:ExprParser.FloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#int.
    def visitInt(self, ctx:ExprParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#val.
    def visitVal(self, ctx:ExprParser.ValContext):
        return self.visitChildren(ctx)



del ExprParser