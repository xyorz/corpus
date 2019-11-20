# Generated from Reader.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\r")
        buf.write("Z\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\3\2\3\2\3\3\3\3\3\3\3\3\5\3\27\n\3\3\3\3\3\5\3\33")
        buf.write("\n\3\3\3\3\3\3\3\5\3 \n\3\3\3\3\3\5\3$\n\3\3\3\5\3\'\n")
        buf.write("\3\3\3\3\3\5\3+\n\3\6\3-\n\3\r\3\16\3.\5\3\61\n\3\3\3")
        buf.write("\5\3\64\n\3\3\4\3\4\3\4\3\4\5\4:\n\4\3\5\3\5\3\5\3\5\5")
        buf.write("\5@\n\5\3\5\3\5\3\5\5\5E\n\5\3\5\5\5H\n\5\3\6\6\6K\n\6")
        buf.write("\r\6\16\6L\3\7\6\7P\n\7\r\7\16\7Q\3\b\7\bU\n\b\f\b\16")
        buf.write("\bX\13\b\3\b\2\2\t\2\4\6\b\n\f\16\2\4\3\2\7\n\3\2\b\n")
        buf.write("\2b\2\20\3\2\2\2\4\22\3\2\2\2\69\3\2\2\2\b;\3\2\2\2\n")
        buf.write("J\3\2\2\2\fO\3\2\2\2\16V\3\2\2\2\20\21\5\4\3\2\21\3\3")
        buf.write("\2\2\2\22\23\7\3\2\2\23\24\5\f\7\2\24\26\7\4\2\2\25\27")
        buf.write("\7\5\2\2\26\25\3\2\2\2\26\27\3\2\2\2\27\30\3\2\2\2\30")
        buf.write("\32\7\4\2\2\31\33\7\5\2\2\32\31\3\2\2\2\32\33\3\2\2\2")
        buf.write("\33\34\3\2\2\2\34&\5\b\5\2\35\37\7\4\2\2\36 \7\5\2\2\37")
        buf.write("\36\3\2\2\2\37 \3\2\2\2 !\3\2\2\2!#\7\4\2\2\"$\7\5\2\2")
        buf.write("#\"\3\2\2\2#$\3\2\2\2$%\3\2\2\2%\'\5\4\3\2&\35\3\2\2\2")
        buf.write("&\'\3\2\2\2\'\60\3\2\2\2(*\7\4\2\2)+\7\5\2\2*)\3\2\2\2")
        buf.write("*+\3\2\2\2+-\3\2\2\2,(\3\2\2\2-.\3\2\2\2.,\3\2\2\2./\3")
        buf.write("\2\2\2/\61\3\2\2\2\60,\3\2\2\2\60\61\3\2\2\2\61\63\3\2")
        buf.write("\2\2\62\64\7\2\2\3\63\62\3\2\2\2\63\64\3\2\2\2\64\5\3")
        buf.write("\2\2\2\65:\7\13\2\2\66\67\7\13\2\2\678\7\4\2\28:\5\6\4")
        buf.write("\29\65\3\2\2\29\66\3\2\2\2:\7\3\2\2\2;<\7\6\2\2<=\5\16")
        buf.write("\b\2=?\7\4\2\2>@\7\5\2\2?>\3\2\2\2?@\3\2\2\2@A\3\2\2\2")
        buf.write("AG\5\6\4\2BD\7\4\2\2CE\7\5\2\2DC\3\2\2\2DE\3\2\2\2EF\3")
        buf.write("\2\2\2FH\5\b\5\2GB\3\2\2\2GH\3\2\2\2H\t\3\2\2\2IK\t\2")
        buf.write("\2\2JI\3\2\2\2KL\3\2\2\2LJ\3\2\2\2LM\3\2\2\2M\13\3\2\2")
        buf.write("\2NP\t\2\2\2ON\3\2\2\2PQ\3\2\2\2QO\3\2\2\2QR\3\2\2\2R")
        buf.write("\r\3\2\2\2SU\t\3\2\2TS\3\2\2\2UX\3\2\2\2VT\3\2\2\2VW\3")
        buf.write("\2\2\2W\17\3\2\2\2XV\3\2\2\2\22\26\32\37#&*.\60\639?D")
        buf.write("GLQV")
        return buf.getvalue()


class ReaderParser ( Parser ):

    grammarFileName = "Reader.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'--s'", "'\n'", "'\r'", "'--p'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "TITLE", "AUTHOR", "DYNASTY", "CATEGORY", 
                      "WORD", "ID", "INT" ]

    RULE_prog = 0
    RULE_sec = 1
    RULE_data = 2
    RULE_para = 3
    RULE_d_info = 4
    RULE_s_info = 5
    RULE_p_info = 6

    ruleNames =  [ "prog", "sec", "data", "para", "d_info", "s_info", "p_info" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    TITLE=5
    AUTHOR=6
    DYNASTY=7
    CATEGORY=8
    WORD=9
    ID=10
    INT=11

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sec(self):
            return self.getTypedRuleContext(ReaderParser.SecContext,0)


        def getRuleIndex(self):
            return ReaderParser.RULE_prog

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

        localctx = ReaderParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.sec()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SecContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def s_info(self):
            return self.getTypedRuleContext(ReaderParser.S_infoContext,0)


        def para(self):
            return self.getTypedRuleContext(ReaderParser.ParaContext,0)


        def sec(self):
            return self.getTypedRuleContext(ReaderParser.SecContext,0)


        def EOF(self):
            return self.getToken(ReaderParser.EOF, 0)

        def getRuleIndex(self):
            return ReaderParser.RULE_sec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSec" ):
                listener.enterSec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSec" ):
                listener.exitSec(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSec" ):
                return visitor.visitSec(self)
            else:
                return visitor.visitChildren(self)




    def sec(self):

        localctx = ReaderParser.SecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.match(ReaderParser.T__0)
            self.state = 17
            self.s_info()
            self.state = 18
            self.match(ReaderParser.T__1)
            self.state = 20
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ReaderParser.T__2:
                self.state = 19
                self.match(ReaderParser.T__2)


            self.state = 22
            self.match(ReaderParser.T__1)
            self.state = 24
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ReaderParser.T__2:
                self.state = 23
                self.match(ReaderParser.T__2)


            self.state = 26
            self.para()
            self.state = 36
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 27
                self.match(ReaderParser.T__1)
                self.state = 29
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ReaderParser.T__2:
                    self.state = 28
                    self.match(ReaderParser.T__2)


                self.state = 31
                self.match(ReaderParser.T__1)
                self.state = 33
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ReaderParser.T__2:
                    self.state = 32
                    self.match(ReaderParser.T__2)


                self.state = 35
                self.sec()


            self.state = 46
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 42 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 38
                        self.match(ReaderParser.T__1)
                        self.state = 40
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==ReaderParser.T__2:
                            self.state = 39
                            self.match(ReaderParser.T__2)



                    else:
                        raise NoViableAltException(self)
                    self.state = 44 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,6,self._ctx)



            self.state = 49
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 48
                self.match(ReaderParser.EOF)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DataContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self):
            return self.getToken(ReaderParser.WORD, 0)

        def data(self):
            return self.getTypedRuleContext(ReaderParser.DataContext,0)


        def getRuleIndex(self):
            return ReaderParser.RULE_data

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterData" ):
                listener.enterData(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitData" ):
                listener.exitData(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitData" ):
                return visitor.visitData(self)
            else:
                return visitor.visitChildren(self)




    def data(self):

        localctx = ReaderParser.DataContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_data)
        try:
            self.state = 55
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 51
                self.match(ReaderParser.WORD)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 52
                self.match(ReaderParser.WORD)
                self.state = 53
                self.match(ReaderParser.T__1)
                self.state = 54
                self.data()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ParaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def p_info(self):
            return self.getTypedRuleContext(ReaderParser.P_infoContext,0)


        def data(self):
            return self.getTypedRuleContext(ReaderParser.DataContext,0)


        def para(self):
            return self.getTypedRuleContext(ReaderParser.ParaContext,0)


        def getRuleIndex(self):
            return ReaderParser.RULE_para

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPara" ):
                listener.enterPara(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPara" ):
                listener.exitPara(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPara" ):
                return visitor.visitPara(self)
            else:
                return visitor.visitChildren(self)




    def para(self):

        localctx = ReaderParser.ParaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_para)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(ReaderParser.T__3)
            self.state = 58
            self.p_info()
            self.state = 59
            self.match(ReaderParser.T__1)
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ReaderParser.T__2:
                self.state = 60
                self.match(ReaderParser.T__2)


            self.state = 63
            self.data()
            self.state = 69
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 64
                self.match(ReaderParser.T__1)
                self.state = 66
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ReaderParser.T__2:
                    self.state = 65
                    self.match(ReaderParser.T__2)


                self.state = 68
                self.para()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class D_infoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.info = None # Token

        def TITLE(self, i:int=None):
            if i is None:
                return self.getTokens(ReaderParser.TITLE)
            else:
                return self.getToken(ReaderParser.TITLE, i)

        def AUTHOR(self, i:int=None):
            if i is None:
                return self.getTokens(ReaderParser.AUTHOR)
            else:
                return self.getToken(ReaderParser.AUTHOR, i)

        def DYNASTY(self, i:int=None):
            if i is None:
                return self.getTokens(ReaderParser.DYNASTY)
            else:
                return self.getToken(ReaderParser.DYNASTY, i)

        def CATEGORY(self, i:int=None):
            if i is None:
                return self.getTokens(ReaderParser.CATEGORY)
            else:
                return self.getToken(ReaderParser.CATEGORY, i)

        def getRuleIndex(self):
            return ReaderParser.RULE_d_info

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterD_info" ):
                listener.enterD_info(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitD_info" ):
                listener.exitD_info(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitD_info" ):
                return visitor.visitD_info(self)
            else:
                return visitor.visitChildren(self)




    def d_info(self):

        localctx = ReaderParser.D_infoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_d_info)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 71
                localctx.info = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ReaderParser.TITLE) | (1 << ReaderParser.AUTHOR) | (1 << ReaderParser.DYNASTY) | (1 << ReaderParser.CATEGORY))) != 0)):
                    localctx.info = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 74 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ReaderParser.TITLE) | (1 << ReaderParser.AUTHOR) | (1 << ReaderParser.DYNASTY) | (1 << ReaderParser.CATEGORY))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class S_infoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.info = None # Token

        def TITLE(self, i:int=None):
            if i is None:
                return self.getTokens(ReaderParser.TITLE)
            else:
                return self.getToken(ReaderParser.TITLE, i)

        def AUTHOR(self, i:int=None):
            if i is None:
                return self.getTokens(ReaderParser.AUTHOR)
            else:
                return self.getToken(ReaderParser.AUTHOR, i)

        def DYNASTY(self, i:int=None):
            if i is None:
                return self.getTokens(ReaderParser.DYNASTY)
            else:
                return self.getToken(ReaderParser.DYNASTY, i)

        def CATEGORY(self, i:int=None):
            if i is None:
                return self.getTokens(ReaderParser.CATEGORY)
            else:
                return self.getToken(ReaderParser.CATEGORY, i)

        def getRuleIndex(self):
            return ReaderParser.RULE_s_info

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS_info" ):
                listener.enterS_info(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS_info" ):
                listener.exitS_info(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitS_info" ):
                return visitor.visitS_info(self)
            else:
                return visitor.visitChildren(self)




    def s_info(self):

        localctx = ReaderParser.S_infoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_s_info)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 76
                localctx.info = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ReaderParser.TITLE) | (1 << ReaderParser.AUTHOR) | (1 << ReaderParser.DYNASTY) | (1 << ReaderParser.CATEGORY))) != 0)):
                    localctx.info = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 79 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ReaderParser.TITLE) | (1 << ReaderParser.AUTHOR) | (1 << ReaderParser.DYNASTY) | (1 << ReaderParser.CATEGORY))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class P_infoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.info = None # Token

        def AUTHOR(self, i:int=None):
            if i is None:
                return self.getTokens(ReaderParser.AUTHOR)
            else:
                return self.getToken(ReaderParser.AUTHOR, i)

        def DYNASTY(self, i:int=None):
            if i is None:
                return self.getTokens(ReaderParser.DYNASTY)
            else:
                return self.getToken(ReaderParser.DYNASTY, i)

        def CATEGORY(self, i:int=None):
            if i is None:
                return self.getTokens(ReaderParser.CATEGORY)
            else:
                return self.getToken(ReaderParser.CATEGORY, i)

        def getRuleIndex(self):
            return ReaderParser.RULE_p_info

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterP_info" ):
                listener.enterP_info(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitP_info" ):
                listener.exitP_info(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitP_info" ):
                return visitor.visitP_info(self)
            else:
                return visitor.visitChildren(self)




    def p_info(self):

        localctx = ReaderParser.P_infoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_p_info)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ReaderParser.AUTHOR) | (1 << ReaderParser.DYNASTY) | (1 << ReaderParser.CATEGORY))) != 0):
                self.state = 81
                localctx.info = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ReaderParser.AUTHOR) | (1 << ReaderParser.DYNASTY) | (1 << ReaderParser.CATEGORY))) != 0)):
                    localctx.info = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 86
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





