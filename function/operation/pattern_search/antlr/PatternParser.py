# Generated from Pattern.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\20")
        buf.write("\63\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\2\3\2\3")
        buf.write("\3\3\3\3\3\3\3\3\3\5\3\24\n\3\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\5\4 \n\4\3\5\3\5\3\5\3\5\3\5\7\5\'\n")
        buf.write("\5\f\5\16\5*\13\5\3\5\5\5-\n\5\3\5\3\5\5\5\61\n\5\3\5")
        buf.write("\2\2\6\2\4\6\b\2\3\3\2\f\16\2\64\2\n\3\2\2\2\4\16\3\2")
        buf.write("\2\2\6\37\3\2\2\2\b\60\3\2\2\2\n\13\5\4\3\2\13\f\7\13")
        buf.write("\2\2\f\r\5\b\5\2\r\3\3\2\2\2\16\17\7\7\2\2\17\20\7\3\2")
        buf.write("\2\20\21\5\6\4\2\21\23\7\4\2\2\22\24\5\4\3\2\23\22\3\2")
        buf.write("\2\2\23\24\3\2\2\2\24\5\3\2\2\2\25\26\7\t\2\2\26\27\7")
        buf.write("\5\2\2\27\30\t\2\2\2\30 \7\n\2\2\31\32\7\t\2\2\32\33\7")
        buf.write("\5\2\2\33\34\7\n\2\2\34\35\7\17\2\2\35 \7\n\2\2\36 \7")
        buf.write("\t\2\2\37\25\3\2\2\2\37\31\3\2\2\2\37\36\3\2\2\2 \7\3")
        buf.write("\2\2\2!\"\7\b\2\2\"#\7\6\2\2#(\7\7\2\2$%\7\13\2\2%\'\7")
        buf.write("\7\2\2&$\3\2\2\2\'*\3\2\2\2(&\3\2\2\2()\3\2\2\2),\3\2")
        buf.write("\2\2*(\3\2\2\2+-\7\13\2\2,+\3\2\2\2,-\3\2\2\2-.\3\2\2")
        buf.write("\2.\61\5\b\5\2/\61\7\2\2\3\60!\3\2\2\2\60/\3\2\2\2\61")
        buf.write("\t\3\2\2\2\7\23\37(,\60")
        return buf.getvalue()


class PatternParser ( Parser ):

    grammarFileName = "Pattern.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "','", "':'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'>'", "'<'", "'='", "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "WORD", "FIELD", "ID", "INT", "SPL", 
                      "MOR", "LES", "EQU", "SCO", "WS" ]

    RULE_prog = 0
    RULE_expr = 1
    RULE_req = 2
    RULE_field = 3

    ruleNames =  [ "prog", "expr", "req", "field" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    WORD=5
    FIELD=6
    ID=7
    INT=8
    SPL=9
    MOR=10
    LES=11
    EQU=12
    SCO=13
    WS=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(PatternParser.ExprContext,0)


        def SPL(self):
            return self.getToken(PatternParser.SPL, 0)

        def field(self):
            return self.getTypedRuleContext(PatternParser.FieldContext,0)


        def getRuleIndex(self):
            return PatternParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = PatternParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.expr()
            self.state = 9
            self.match(PatternParser.SPL)
            self.state = 10
            self.field()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self):
            return self.getToken(PatternParser.WORD, 0)

        def req(self):
            return self.getTypedRuleContext(PatternParser.ReqContext,0)


        def expr(self):
            return self.getTypedRuleContext(PatternParser.ExprContext,0)


        def getRuleIndex(self):
            return PatternParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = PatternParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.match(PatternParser.WORD)
            self.state = 13
            self.match(PatternParser.T__0)
            self.state = 14
            self.req()
            self.state = 15
            self.match(PatternParser.T__1)
            self.state = 17
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==PatternParser.WORD:
                self.state = 16
                self.expr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ReqContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PatternParser.RULE_req

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class OP2Context(ReqContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PatternParser.ReqContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(PatternParser.ID, 0)
        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(PatternParser.INT)
            else:
                return self.getToken(PatternParser.INT, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOP2" ):
                listener.enterOP2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOP2" ):
                listener.exitOP2(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOP2" ):
                return visitor.visitOP2(self)
            else:
                return visitor.visitChildren(self)


    class OP1Context(ReqContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PatternParser.ReqContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(PatternParser.ID, 0)
        def INT(self):
            return self.getToken(PatternParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOP1" ):
                listener.enterOP1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOP1" ):
                listener.exitOP1(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOP1" ):
                return visitor.visitOP1(self)
            else:
                return visitor.visitChildren(self)


    class IdContext(ReqContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PatternParser.ReqContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(PatternParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId" ):
                listener.enterId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId" ):
                listener.exitId(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId" ):
                return visitor.visitId(self)
            else:
                return visitor.visitChildren(self)



    def req(self):

        localctx = PatternParser.ReqContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_req)
        self._la = 0 # Token type
        try:
            self.state = 29
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                localctx = PatternParser.OP1Context(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 19
                self.match(PatternParser.ID)
                self.state = 20
                self.match(PatternParser.T__2)
                self.state = 21
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PatternParser.MOR) | (1 << PatternParser.LES) | (1 << PatternParser.EQU))) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 22
                self.match(PatternParser.INT)
                pass

            elif la_ == 2:
                localctx = PatternParser.OP2Context(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 23
                self.match(PatternParser.ID)
                self.state = 24
                self.match(PatternParser.T__2)
                self.state = 25
                self.match(PatternParser.INT)
                self.state = 26
                localctx.op = self.match(PatternParser.SCO)
                self.state = 27
                self.match(PatternParser.INT)
                pass

            elif la_ == 3:
                localctx = PatternParser.IdContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 28
                self.match(PatternParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FieldContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PatternParser.RULE_field

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class FIELD0Context(FieldContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PatternParser.FieldContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FIELD(self):
            return self.getToken(PatternParser.FIELD, 0)
        def WORD(self, i:int=None):
            if i is None:
                return self.getTokens(PatternParser.WORD)
            else:
                return self.getToken(PatternParser.WORD, i)
        def field(self):
            return self.getTypedRuleContext(PatternParser.FieldContext,0)

        def SPL(self, i:int=None):
            if i is None:
                return self.getTokens(PatternParser.SPL)
            else:
                return self.getToken(PatternParser.SPL, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFIELD0" ):
                listener.enterFIELD0(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFIELD0" ):
                listener.exitFIELD0(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFIELD0" ):
                return visitor.visitFIELD0(self)
            else:
                return visitor.visitChildren(self)


    class FIELD1Context(FieldContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PatternParser.FieldContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def EOF(self):
            return self.getToken(PatternParser.EOF, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFIELD1" ):
                listener.enterFIELD1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFIELD1" ):
                listener.exitFIELD1(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFIELD1" ):
                return visitor.visitFIELD1(self)
            else:
                return visitor.visitChildren(self)



    def field(self):

        localctx = PatternParser.FieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_field)
        self._la = 0 # Token type
        try:
            self.state = 46
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [PatternParser.FIELD]:
                localctx = PatternParser.FIELD0Context(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 31
                self.match(PatternParser.FIELD)
                self.state = 32
                self.match(PatternParser.T__3)
                self.state = 33
                self.match(PatternParser.WORD)
                self.state = 38
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 34
                        self.match(PatternParser.SPL)
                        self.state = 35
                        self.match(PatternParser.WORD) 
                    self.state = 40
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

                self.state = 42
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==PatternParser.SPL:
                    self.state = 41
                    self.match(PatternParser.SPL)


                self.state = 44
                self.field()
                pass
            elif token in [PatternParser.EOF]:
                localctx = PatternParser.FIELD1Context(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 45
                self.match(PatternParser.EOF)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





