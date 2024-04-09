# Generated from Expr.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,18,81,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,4,0,10,8,0,11,0,12,
        0,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,3,1,51,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,3,2,66,8,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,74,
        8,2,10,2,12,2,77,9,2,1,3,1,3,1,3,0,1,4,4,0,2,4,6,0,5,1,0,14,15,1,
        0,13,16,1,0,9,10,1,0,11,12,1,0,15,16,91,0,9,1,0,0,0,2,50,1,0,0,0,
        4,65,1,0,0,0,6,78,1,0,0,0,8,10,3,2,1,0,9,8,1,0,0,0,10,11,1,0,0,0,
        11,9,1,0,0,0,11,12,1,0,0,0,12,1,1,0,0,0,13,14,3,4,2,0,14,15,5,17,
        0,0,15,51,1,0,0,0,16,17,5,8,0,0,17,18,5,14,0,0,18,51,5,17,0,0,19,
        20,5,14,0,0,20,21,5,1,0,0,21,22,3,4,2,0,22,23,5,17,0,0,23,51,1,0,
        0,0,24,25,5,8,0,0,25,26,5,14,0,0,26,27,5,2,0,0,27,28,5,15,0,0,28,
        29,5,3,0,0,29,51,5,17,0,0,30,31,5,14,0,0,31,32,5,2,0,0,32,33,7,0,
        0,0,33,34,5,3,0,0,34,35,5,1,0,0,35,36,3,4,2,0,36,37,5,17,0,0,37,
        51,1,0,0,0,38,39,5,4,0,0,39,40,5,5,0,0,40,41,7,1,0,0,41,42,5,6,0,
        0,42,51,5,17,0,0,43,44,5,14,0,0,44,45,5,1,0,0,45,46,5,7,0,0,46,47,
        5,5,0,0,47,48,5,6,0,0,48,51,5,17,0,0,49,51,5,17,0,0,50,13,1,0,0,
        0,50,16,1,0,0,0,50,19,1,0,0,0,50,24,1,0,0,0,50,30,1,0,0,0,50,38,
        1,0,0,0,50,43,1,0,0,0,50,49,1,0,0,0,51,3,1,0,0,0,52,53,6,2,-1,0,
        53,66,5,15,0,0,54,66,5,16,0,0,55,66,5,13,0,0,56,66,5,14,0,0,57,58,
        5,5,0,0,58,59,3,4,2,0,59,60,5,6,0,0,60,66,1,0,0,0,61,62,5,14,0,0,
        62,63,5,2,0,0,63,64,7,0,0,0,64,66,5,3,0,0,65,52,1,0,0,0,65,54,1,
        0,0,0,65,55,1,0,0,0,65,56,1,0,0,0,65,57,1,0,0,0,65,61,1,0,0,0,66,
        75,1,0,0,0,67,68,10,8,0,0,68,69,7,2,0,0,69,74,3,4,2,9,70,71,10,7,
        0,0,71,72,7,3,0,0,72,74,3,4,2,8,73,67,1,0,0,0,73,70,1,0,0,0,74,77,
        1,0,0,0,75,73,1,0,0,0,75,76,1,0,0,0,76,5,1,0,0,0,77,75,1,0,0,0,78,
        79,7,4,0,0,79,7,1,0,0,0,5,11,50,65,73,75
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'['", "']'", "'print'", "'('", 
                     "')'", "'read'", "<INVALID>", "'*'", "'/'", "'+'", 
                     "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "TYPE", "MUL", "DIV", "ADD", "SUB", "STR", "ID", "INT", 
                      "DOUBLE", "NEWLINE", "WS" ]

    RULE_r = 0
    RULE_stat = 1
    RULE_expr = 2
    RULE_val = 3

    ruleNames =  [ "r", "stat", "expr", "val" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    TYPE=8
    MUL=9
    DIV=10
    ADD=11
    SUB=12
    STR=13
    ID=14
    INT=15
    DOUBLE=16
    NEWLINE=17
    WS=18

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.StatContext)
            else:
                return self.getTypedRuleContext(ExprParser.StatContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_r

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterR" ):
                listener.enterR(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitR" ):
                listener.exitR(self)




    def r(self):

        localctx = ExprParser.RContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_r)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 8
                self.stat()
                self.state = 11 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 254256) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_stat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PrintContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StatContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def NEWLINE(self):
            return self.getToken(ExprParser.NEWLINE, 0)
        def ID(self):
            return self.getToken(ExprParser.ID, 0)
        def INT(self):
            return self.getToken(ExprParser.INT, 0)
        def DOUBLE(self):
            return self.getToken(ExprParser.DOUBLE, 0)
        def STR(self):
            return self.getToken(ExprParser.STR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint" ):
                listener.enterPrint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint" ):
                listener.exitPrint(self)


    class ReadContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(ExprParser.ID, 0)
        def NEWLINE(self):
            return self.getToken(ExprParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRead" ):
                listener.enterRead(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRead" ):
                listener.exitRead(self)


    class BlankContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NEWLINE(self):
            return self.getToken(ExprParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlank" ):
                listener.enterBlank(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlank" ):
                listener.exitBlank(self)


    class ArrayAssignContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StatContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.ID)
            else:
                return self.getToken(ExprParser.ID, i)
        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)

        def NEWLINE(self):
            return self.getToken(ExprParser.NEWLINE, 0)
        def INT(self):
            return self.getToken(ExprParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayAssign" ):
                listener.enterArrayAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayAssign" ):
                listener.exitArrayAssign(self)


    class ArrayDeclarationContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TYPE(self):
            return self.getToken(ExprParser.TYPE, 0)
        def ID(self):
            return self.getToken(ExprParser.ID, 0)
        def INT(self):
            return self.getToken(ExprParser.INT, 0)
        def NEWLINE(self):
            return self.getToken(ExprParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayDeclaration" ):
                listener.enterArrayDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayDeclaration" ):
                listener.exitArrayDeclaration(self)


    class DeclarationContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TYPE(self):
            return self.getToken(ExprParser.TYPE, 0)
        def ID(self):
            return self.getToken(ExprParser.ID, 0)
        def NEWLINE(self):
            return self.getToken(ExprParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)


    class PrintExprContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)

        def NEWLINE(self):
            return self.getToken(ExprParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintExpr" ):
                listener.enterPrintExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintExpr" ):
                listener.exitPrintExpr(self)


    class AssignContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(ExprParser.ID, 0)
        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)

        def NEWLINE(self):
            return self.getToken(ExprParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)



    def stat(self):

        localctx = ExprParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        self._la = 0 # Token type
        try:
            self.state = 50
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                localctx = ExprParser.PrintExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 13
                self.expr(0)
                self.state = 14
                self.match(ExprParser.NEWLINE)
                pass

            elif la_ == 2:
                localctx = ExprParser.DeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 16
                self.match(ExprParser.TYPE)
                self.state = 17
                self.match(ExprParser.ID)
                self.state = 18
                self.match(ExprParser.NEWLINE)
                pass

            elif la_ == 3:
                localctx = ExprParser.AssignContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 19
                self.match(ExprParser.ID)
                self.state = 20
                self.match(ExprParser.T__0)
                self.state = 21
                self.expr(0)
                self.state = 22
                self.match(ExprParser.NEWLINE)
                pass

            elif la_ == 4:
                localctx = ExprParser.ArrayDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 24
                self.match(ExprParser.TYPE)
                self.state = 25
                self.match(ExprParser.ID)
                self.state = 26
                self.match(ExprParser.T__1)
                self.state = 27
                self.match(ExprParser.INT)
                self.state = 28
                self.match(ExprParser.T__2)
                self.state = 29
                self.match(ExprParser.NEWLINE)
                pass

            elif la_ == 5:
                localctx = ExprParser.ArrayAssignContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 30
                self.match(ExprParser.ID)
                self.state = 31
                self.match(ExprParser.T__1)
                self.state = 32
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==14 or _la==15):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 33
                self.match(ExprParser.T__2)
                self.state = 34
                self.match(ExprParser.T__0)
                self.state = 35
                self.expr(0)
                self.state = 36
                self.match(ExprParser.NEWLINE)
                pass

            elif la_ == 6:
                localctx = ExprParser.PrintContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 38
                self.match(ExprParser.T__3)
                self.state = 39
                self.match(ExprParser.T__4)
                self.state = 40
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 122880) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 41
                self.match(ExprParser.T__5)
                self.state = 42
                self.match(ExprParser.NEWLINE)
                pass

            elif la_ == 7:
                localctx = ExprParser.ReadContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 43
                self.match(ExprParser.ID)
                self.state = 44
                self.match(ExprParser.T__0)
                self.state = 45
                self.match(ExprParser.T__6)
                self.state = 46
                self.match(ExprParser.T__4)
                self.state = 47
                self.match(ExprParser.T__5)
                self.state = 48
                self.match(ExprParser.NEWLINE)
                pass

            elif la_ == 8:
                localctx = ExprParser.BlankContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 49
                self.match(ExprParser.NEWLINE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class StrContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STR(self):
            return self.getToken(ExprParser.STR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStr" ):
                listener.enterStr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStr" ):
                listener.exitStr(self)


    class ParensContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParens" ):
                listener.enterParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParens" ):
                listener.exitParens(self)


    class MulDivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def MUL(self):
            return self.getToken(ExprParser.MUL, 0)
        def DIV(self):
            return self.getToken(ExprParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDiv" ):
                listener.enterMulDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDiv" ):
                listener.exitMulDiv(self)


    class AddSubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def ADD(self):
            return self.getToken(ExprParser.ADD, 0)
        def SUB(self):
            return self.getToken(ExprParser.SUB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSub" ):
                listener.enterAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSub" ):
                listener.exitAddSub(self)


    class DoubleContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def DOUBLE(self):
            return self.getToken(ExprParser.DOUBLE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDouble" ):
                listener.enterDouble(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDouble" ):
                listener.exitDouble(self)


    class IdContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId" ):
                listener.enterId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId" ):
                listener.exitId(self)


    class ArrayAccessContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.ID)
            else:
                return self.getToken(ExprParser.ID, i)
        def INT(self):
            return self.getToken(ExprParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayAccess" ):
                listener.enterArrayAccess(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayAccess" ):
                listener.exitArrayAccess(self)


    class IntContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(ExprParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = ExprParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 53
                self.match(ExprParser.INT)
                pass

            elif la_ == 2:
                localctx = ExprParser.DoubleContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 54
                self.match(ExprParser.DOUBLE)
                pass

            elif la_ == 3:
                localctx = ExprParser.StrContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 55
                self.match(ExprParser.STR)
                pass

            elif la_ == 4:
                localctx = ExprParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 56
                self.match(ExprParser.ID)
                pass

            elif la_ == 5:
                localctx = ExprParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 57
                self.match(ExprParser.T__4)
                self.state = 58
                self.expr(0)
                self.state = 59
                self.match(ExprParser.T__5)
                pass

            elif la_ == 6:
                localctx = ExprParser.ArrayAccessContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 61
                self.match(ExprParser.ID)
                self.state = 62
                self.match(ExprParser.T__1)
                self.state = 63
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==14 or _la==15):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 64
                self.match(ExprParser.T__2)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 75
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 73
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = ExprParser.MulDivContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 67
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 68
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==9 or _la==10):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 69
                        self.expr(9)
                        pass

                    elif la_ == 2:
                        localctx = ExprParser.AddSubContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 70
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 71
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==11 or _la==12):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 72
                        self.expr(8)
                        pass

             
                self.state = 77
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ValContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(ExprParser.INT, 0)

        def DOUBLE(self):
            return self.getToken(ExprParser.DOUBLE, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_val

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVal" ):
                listener.enterVal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVal" ):
                listener.exitVal(self)




    def val(self):

        localctx = ExprParser.ValContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_val)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            _la = self._input.LA(1)
            if not(_la==15 or _la==16):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 7)
         




