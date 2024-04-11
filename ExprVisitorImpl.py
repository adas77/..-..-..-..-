from g4.ExprVisitor import ExprVisitor
from g4.ExprParser import ExprParser


class ExprVisitorImpl(ExprVisitor):
    def __init__(self):
        self.memory = {}

    def visitAssign(self, ctx):
        name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.memory[name] = value
        print(self.memory)
        return value

    def visitPrintExpr(self, ctx):
        value = self.visit(ctx.expr())
        print(value)
        return 0

    # def visitArray(self, ctx: ExprParser.ArrayContext):
    #     name = ctx.ID().getText()
    #     v = ctx.arr()
    #     arr_len = len(v.val())

    #     self.memory[name] = [float(v.val(i).getText()) if '.' in v.val(
    #         i).getText() else int(v.val(i).getText()) for i in range(arr_len)]
    #     return self.visitChildren(ctx)

    def visitPrint(self, ctx: ExprParser.PrintContext):
        ops = {
            ExprParser.INT: ctx.INT(),
            ExprParser.FLOAT: ctx.FLOAT(),
            ExprParser.STR: ctx.STR(),
            ExprParser.ID: (
                None
                if not hasattr(ctx.ID(), "getText")
                else self.memory.get(ctx.ID().getText(), None)
            ),
        }
        v = ops.get(ctx.op.type, None)
        v = v if v is None or isinstance(v, (str, list)) else v.getText()
        print(f"{v=}")
        return self.visitChildren(ctx)

    def visitInt(self, ctx):
        return ctx.INT().getText()

    def visitId(self, ctx):
        name = ctx.ID().getText()
        if name in self.memory:
            return self.memory[name]
        return 0

    def visitMulDiv(self, ctx):
        left = int(self.visit(ctx.expr(0)))
        right = int(self.visit(ctx.expr(1)))
        if right == 0:
            raise ValueError("Division by zero")
        return left * right if ctx.op.type == ExprParser.MUL else left / right

    def visitAddSub(self, ctx):
        left = int(self.visit(ctx.expr(0)))
        right = int(self.visit(ctx.expr(1)))
        return left + right if ctx.op.type == ExprParser.ADD else left - right

    def visitParens(self, ctx):
        return self.visit(ctx.expr())
