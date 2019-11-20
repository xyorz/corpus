# Generated from Corpus.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\r")
        buf.write(">\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3\2")
        buf.write("\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5")
        buf.write("\3\35\n\3\3\4\3\4\3\4\3\4\3\4\3\4\5\4%\n\4\3\5\3\5\3\5")
        buf.write("\3\5\5\5+\n\5\3\6\3\6\3\6\3\6\3\6\7\6\62\n\6\f\6\16\6")
        buf.write("\65\13\6\3\6\5\68\n\6\3\6\3\6\5\6<\n\6\3\6\2\2\7\2\4\6")
        buf.write("\b\n\2\2\2@\2\f\3\2\2\2\4\34\3\2\2\2\6$\3\2\2\2\b*\3\2")
        buf.write("\2\2\n;\3\2\2\2\f\r\5\4\3\2\r\16\7\6\2\2\16\17\5\n\6\2")
        buf.write("\17\3\3\2\2\2\20\21\5\b\5\2\21\22\7\7\2\2\22\23\7\f\2")
        buf.write("\2\23\24\5\b\5\2\24\35\3\2\2\2\25\35\5\6\4\2\26\27\5\b")
        buf.write("\5\2\27\30\7\t\2\2\30\31\7\f\2\2\31\32\5\b\5\2\32\35\3")
        buf.write("\2\2\2\33\35\5\b\5\2\34\20\3\2\2\2\34\25\3\2\2\2\34\26")
        buf.write("\3\2\2\2\34\33\3\2\2\2\35\5\3\2\2\2\36\37\5\b\5\2\37 ")
        buf.write("\7\b\2\2 !\7\f\2\2!\"\5\6\4\2\"%\3\2\2\2#%\5\b\5\2$\36")
        buf.write("\3\2\2\2$#\3\2\2\2%\7\3\2\2\2&\'\7\4\2\2\'(\7\6\2\2(+")
        buf.write("\5\b\5\2)+\7\4\2\2*&\3\2\2\2*)\3\2\2\2+\t\3\2\2\2,-\7")
        buf.write("\5\2\2-.\7\3\2\2.\63\7\4\2\2/\60\7\6\2\2\60\62\7\4\2\2")
        buf.write("\61/\3\2\2\2\62\65\3\2\2\2\63\61\3\2\2\2\63\64\3\2\2\2")
        buf.write("\64\67\3\2\2\2\65\63\3\2\2\2\668\7\6\2\2\67\66\3\2\2\2")
        buf.write("\678\3\2\2\289\3\2\2\29<\5\n\6\2:<\7\2\2\3;,\3\2\2\2;")
        buf.write(":\3\2\2\2<\13\3\2\2\2\b\34$*\63\67;")
        return buf.getvalue()


class CorpusParser ( Parser ):

    grammarFileName = "Corpus.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'#'", "<INVALID>", "<INVALID>", "'!'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "WORD", "FIELD", "SPL", 
                      "KEY1", "KEY2", "KEY3", "IMP", "ID", "INT", "WS" ]

    RULE_prog = 0
    RULE_expr = 1
    RULE_op2 = 2
    RULE_sim = 3
    RULE_field = 4

    ruleNames =  [ "prog", "expr", "op2", "sim", "field" ]

    EOF = Token.EOF
    T__0=1
    WORD=2
    FIELD=3
    SPL=4
    KEY1=5
    KEY2=6
    KEY3=7
    IMP=8
    ID=9
    INT=10
    WS=11

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
            return self.getTypedRuleContext(CorpusParser.ExprContext,0)


        def SPL(self):
            return self.getToken(CorpusParser.SPL, 0)

        def field(self):
            return self.getTypedRuleContext(CorpusParser.FieldContext,0)


        def getRuleIndex(self):
            return CorpusParser.RULE_prog

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

        localctx = CorpusParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.expr()
            self.state = 11
            self.match(CorpusParser.SPL)
            self.state = 12
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


        def getRuleIndex(self):
            return CorpusParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class OP2Context(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CorpusParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def op2(self):
            return self.getTypedRuleContext(CorpusParser.Op2Context,0)


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


    class OP1Context(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CorpusParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def sim(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CorpusParser.SimContext)
            else:
                return self.getTypedRuleContext(CorpusParser.SimContext,i)

        def KEY1(self):
            return self.getToken(CorpusParser.KEY1, 0)
        def INT(self):
            return self.getToken(CorpusParser.INT, 0)

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


    class OP3Context(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CorpusParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def sim(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CorpusParser.SimContext)
            else:
                return self.getTypedRuleContext(CorpusParser.SimContext,i)

        def KEY3(self):
            return self.getToken(CorpusParser.KEY3, 0)
        def INT(self):
            return self.getToken(CorpusParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOP3" ):
                listener.enterOP3(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOP3" ):
                listener.exitOP3(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOP3" ):
                return visitor.visitOP3(self)
            else:
                return visitor.visitChildren(self)


    class SOLOContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CorpusParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def sim(self):
            return self.getTypedRuleContext(CorpusParser.SimContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSOLO" ):
                listener.enterSOLO(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSOLO" ):
                listener.exitSOLO(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSOLO" ):
                return visitor.visitSOLO(self)
            else:
                return visitor.visitChildren(self)



    def expr(self):

        localctx = CorpusParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        try:
            self.state = 26
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                localctx = CorpusParser.OP1Context(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 14
                self.sim()
                self.state = 15
                self.match(CorpusParser.KEY1)
                self.state = 16
                self.match(CorpusParser.INT)
                self.state = 17
                self.sim()
                pass

            elif la_ == 2:
                localctx = CorpusParser.OP2Context(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 19
                self.op2()
                pass

            elif la_ == 3:
                localctx = CorpusParser.OP3Context(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 20
                self.sim()
                self.state = 21
                self.match(CorpusParser.KEY3)
                self.state = 22
                self.match(CorpusParser.INT)
                self.state = 23
                self.sim()
                pass

            elif la_ == 4:
                localctx = CorpusParser.SOLOContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 25
                self.sim()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Op2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sim(self):
            return self.getTypedRuleContext(CorpusParser.SimContext,0)


        def KEY2(self):
            return self.getToken(CorpusParser.KEY2, 0)

        def INT(self):
            return self.getToken(CorpusParser.INT, 0)

        def op2(self):
            return self.getTypedRuleContext(CorpusParser.Op2Context,0)


        def getRuleIndex(self):
            return CorpusParser.RULE_op2

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOp2" ):
                listener.enterOp2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOp2" ):
                listener.exitOp2(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp2" ):
                return visitor.visitOp2(self)
            else:
                return visitor.visitChildren(self)




    def op2(self):

        localctx = CorpusParser.Op2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_op2)
        try:
            self.state = 34
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 28
                self.sim()
                self.state = 29
                self.match(CorpusParser.KEY2)
                self.state = 30
                self.match(CorpusParser.INT)
                self.state = 31
                self.op2()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 33
                self.sim()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SimContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CorpusParser.RULE_sim

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SP0Context(SimContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CorpusParser.SimContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WORD(self):
            return self.getToken(CorpusParser.WORD, 0)
        def SPL(self):
            return self.getToken(CorpusParser.SPL, 0)
        def sim(self):
            return self.getTypedRuleContext(CorpusParser.SimContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSP0" ):
                listener.enterSP0(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSP0" ):
                listener.exitSP0(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSP0" ):
                return visitor.visitSP0(self)
            else:
                return visitor.visitChildren(self)


    class SP1Context(SimContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CorpusParser.SimContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WORD(self):
            return self.getToken(CorpusParser.WORD, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSP1" ):
                listener.enterSP1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSP1" ):
                listener.exitSP1(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSP1" ):
                return visitor.visitSP1(self)
            else:
                return visitor.visitChildren(self)



    def sim(self):

        localctx = CorpusParser.SimContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_sim)
        try:
            self.state = 40
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = CorpusParser.SP0Context(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 36
                self.match(CorpusParser.WORD)
                self.state = 37
                self.match(CorpusParser.SPL)
                self.state = 38
                self.sim()
                pass

            elif la_ == 2:
                localctx = CorpusParser.SP1Context(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 39
                self.match(CorpusParser.WORD)
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
            return CorpusParser.RULE_field

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class FIELD0Context(FieldContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CorpusParser.FieldContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FIELD(self):
            return self.getToken(CorpusParser.FIELD, 0)
        def WORD(self, i:int=None):
            if i is None:
                return self.getTokens(CorpusParser.WORD)
            else:
                return self.getToken(CorpusParser.WORD, i)
        def field(self):
            return self.getTypedRuleContext(CorpusParser.FieldContext,0)

        def SPL(self, i:int=None):
            if i is None:
                return self.getTokens(CorpusParser.SPL)
            else:
                return self.getToken(CorpusParser.SPL, i)

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

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CorpusParser.FieldContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def EOF(self):
            return self.getToken(CorpusParser.EOF, 0)

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

        localctx = CorpusParser.FieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_field)
        self._la = 0 # Token type
        try:
            self.state = 57
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CorpusParser.FIELD]:
                localctx = CorpusParser.FIELD0Context(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 42
                self.match(CorpusParser.FIELD)
                self.state = 43
                self.match(CorpusParser.T__0)
                self.state = 44
                self.match(CorpusParser.WORD)
                self.state = 49
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 45
                        self.match(CorpusParser.SPL)
                        self.state = 46
                        self.match(CorpusParser.WORD) 
                    self.state = 51
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

                self.state = 53
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CorpusParser.SPL:
                    self.state = 52
                    self.match(CorpusParser.SPL)


                self.state = 55
                self.field()
                pass
            elif token in [CorpusParser.EOF]:
                localctx = CorpusParser.FIELD1Context(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 56
                self.match(CorpusParser.EOF)
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





