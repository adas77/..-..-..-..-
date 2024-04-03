import sys
from antlr4 import FileStream, CommonTokenStream, InputStream
from g4.ExprLexer import ExprLexer
from g4.ExprParser import ExprParser
from ExprVisitorImpl import ExprVisitorImpl
# from g4.ExprListener import ExprListener
# from VisitorInterp import VisitorInterp


def main(argv):
    input_stream = FileStream(argv[1]) if len(
        sys.argv) > 1 else InputStream(sys.stdin.readline())

    lexer = ExprLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ExprParser(stream)
    tree = parser.r()

    visitor = ExprVisitorImpl()
    visitor.visit(tree)

    # tree_str = tree.toStringTree(recog=parser)
    # print(tree_str)


if __name__ == '__main__':
    main(sys.argv)
