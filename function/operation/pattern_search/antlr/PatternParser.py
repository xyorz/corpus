# Generated from Pattern.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\20")
        buf.write("\66\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\2\3\2\3")
        buf.write("\3\3\3\3\3\3\3\5\3\23\n\3\3\3\3\3\5\3\27\n\3\5\3\31\n")
        buf.write("\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4#\n\4\3\5\3\5\3")
        buf.write("\5\3\5\3\5\7\5*\n\5\f\5\16\5-\13\5\3\5\5\5\60\n\5\3\5")
        buf.write("\3\5\5\5\64\n\5\3\5\2\2\6\2\4\6\b\2\2\2:\2\n\3\2\2\2\4")
        buf.write("\30\3\2\2\2\6\32\3\2\2\2\b\63\3\2\2\2\n\13\5\4\3\2\13")
        buf.write("\f\7\n\2\2\f\r\5\b\5\2\r\3\3\2\2\2\16\17\7\3\2\2\17\20")
        buf.write("\5\6\4\2\20\22\7\4\2\2\21\23\5\4\3\2\22\21\3\2\2\2\22")
        buf.write("\23\3\2\2\2\23\31\3\2\2\2\24\26\7\6\2\2\25\27\5\4\3\2")
        buf.write("\26\25\3\2\2\2\26\27\3\2\2\2\27\31\3\2\2\2\30\16\3\2\2")
        buf.write("\2\30\24\3\2\2\2\31\5\3\2\2\2\32\"\7\b\2\2\33\34\7\f\2")
        buf.write("\2\34#\7\t\2\2\35\36\7\r\2\2\36#\7\t\2\2\37 \7\t\2\2 ")
        buf.write("!\7\16\2\2!#\7\t\2\2\"\33\3\2\2\2\"\35\3\2\2\2\"\37\3")
        buf.write("\2\2\2\"#\3\2\2\2#\7\3\2\2\2$%\7\7\2\2%&\7\5\2\2&+\7\6")
        buf.write("\2\2\'(\7\n\2\2(*\7\6\2\2)\'\3\2\2\2*-\3\2\2\2+)\3\2\2")
        buf.write("\2+,\3\2\2\2,/\3\2\2\2-+\3\2\2\2.\60\7\n\2\2/.\3\2\2\2")
        buf.write("/\60\3\2\2\2\60\61\3\2\2\2\61\64\5\b\5\2\62\64\7\2\2\3")
        buf.write("\63$\3\2\2\2\63\62\3\2\2\2\64\t\3\2\2\2\t\22\26\30\"+")
        buf.write("/\63")
        return buf.getvalue()


class PatternParser ( Parser ):

    grammarFileName = "Pattern.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "':'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'>'", "'<'", 
                     "'='", "'-'", "' '" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "WORD", "FIELD", "ID", "INT", "SPL", "MOR", "LES", 
                      "EQU", "SCO", "SPC", "WS" ]

    RULE_prog = 0
    RULE_expr = 1
    RULE_req = 2
    RULE_field = 3

    ruleNames =  [ "prog", "expr", "req", "field" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    WORD=4
    FIELD=5
    ID=6
    INT=7
    SPL=8
    MOR=9
    LES=10
    EQU=11
    SCO=12
    SPC=13
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

        def req(self):
            return self.getTypedRuleContext(PatternParser.ReqContext,0)


        def expr(self):
            return self.getTypedRuleContext(PatternParser.ExprContext,0)


        def WORD(self):
            return self.getToken(PatternParser.WORD, 0)

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
            self.state = 22
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [PatternParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 12
                self.match(PatternParser.T__0)
                self.state = 13
                self.req()
                self.state = 14
                self.match(PatternParser.T__1)
                self.state = 16
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==PatternParser.T__0 or _la==PatternParser.WORD:
                    self.state = 15
                    self.expr()


                pass
            elif token in [PatternParser.WORD]:
                self.enterOuterAlt(localctx, 2)
                self.state = 18
                self.match(PatternParser.WORD)
                self.state = 20
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==PatternParser.T__0 or _la==PatternParser.WORD:
                    self.state = 19
                    self.expr()


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

    class ReqContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PatternParser.RULE_req

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class OP0Context(ReqContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PatternParser.ReqContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(PatternParser.ID, 0)
        def LES(self):
            return self.getToken(PatternParser.LES, 0)
        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(PatternParser.INT)
            else:
                return self.getToken(PatternParser.INT, i)
        def EQU(self):
            return self.getToken(PatternParser.EQU, 0)
        def SCO(self):
            return self.getToken(PatternParser.SCO, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOP0" ):
                listener.enterOP0(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOP0" ):
                listener.exitOP0(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOP0" ):
                return visitor.visitOP0(self)
            else:
                return visitor.visitChildren(self)



    def req(self):

        localctx = PatternParser.ReqContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_req)
        try:
            localctx = PatternParser.OP0Context(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(PatternParser.ID)
            self.state = 32
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [PatternParser.LES]:
                self.state = 25
                self.match(PatternParser.LES)
                self.state = 26
                self.match(PatternParser.INT)
                pass
            elif token in [PatternParser.EQU]:
                self.state = 27
                self.match(PatternParser.EQU)
                self.state = 28
                self.match(PatternParser.INT)
                pass
            elif token in [PatternParser.INT]:
                self.state = 29
                self.match(PatternParser.INT)
                self.state = 30
                self.match(PatternParser.SCO)
                self.state = 31
                self.match(PatternParser.INT)
                pass
            elif token in [PatternParser.T__1]:
                pass
            else:
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
            self.state = 49
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [PatternParser.FIELD]:
                localctx = PatternParser.FIELD0Context(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 34
                self.match(PatternParser.FIELD)
                self.state = 35
                self.match(PatternParser.T__2)
                self.state = 36
                self.match(PatternParser.WORD)
                self.state = 41
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 37
                        self.match(PatternParser.SPL)
                        self.state = 38
                        self.match(PatternParser.WORD) 
                    self.state = 43
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

                self.state = 45
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==PatternParser.SPL:
                    self.state = 44
                    self.match(PatternParser.SPL)


                self.state = 47
                self.field()
                pass
            elif token in [PatternParser.EOF]:
                localctx = PatternParser.FIELD1Context(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 48
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





