# Generated from Reader.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\r")
        buf.write("H\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\3\2\3\2")
        buf.write("\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\n\6\n;\n\n\r\n\16\n<\3\13\6\13@\n\13\r\13\16")
        buf.write("\13A\3\f\6\fE\n\f\r\f\16\fF\2\2\r\3\3\5\4\7\5\t\6\13\7")
        buf.write("\r\b\17\t\21\n\23\13\25\f\27\r\3\2\5\24\2\"\"\u2016\u2016")
        buf.write("\u201a\u201b\u201e\u201f\u2028\u2028\u3003\u3004\u300a")
        buf.write("\u3013\u3016\u3017\u4e02\u9fa7\ufe45\ufe46\ufe51\ufe51")
        buf.write("\uff03\uff03\uff0a\uff0b\uff0e\uff0e\uff1c\uff1d\uff21")
        buf.write("\uff21\uff60\uff60\uffe7\uffe7\4\2C\\c|\3\2\62;\2J\2\3")
        buf.write("\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2")
        buf.write("\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2")
        buf.write("\2\2\25\3\2\2\2\2\27\3\2\2\2\3\31\3\2\2\2\5\35\3\2\2\2")
        buf.write("\7\37\3\2\2\2\t!\3\2\2\2\13%\3\2\2\2\r*\3\2\2\2\17/\3")
        buf.write("\2\2\2\21\64\3\2\2\2\23:\3\2\2\2\25?\3\2\2\2\27D\3\2\2")
        buf.write("\2\31\32\7/\2\2\32\33\7/\2\2\33\34\7u\2\2\34\4\3\2\2\2")
        buf.write("\35\36\7\f\2\2\36\6\3\2\2\2\37 \7\17\2\2 \b\3\2\2\2!\"")
        buf.write("\7/\2\2\"#\7/\2\2#$\7r\2\2$\n\3\2\2\2%&\7/\2\2&\'\7v\2")
        buf.write("\2\'(\3\2\2\2()\5\23\n\2)\f\3\2\2\2*+\7/\2\2+,\7c\2\2")
        buf.write(",-\3\2\2\2-.\5\23\n\2.\16\3\2\2\2/\60\7/\2\2\60\61\7f")
        buf.write("\2\2\61\62\3\2\2\2\62\63\5\23\n\2\63\20\3\2\2\2\64\65")
        buf.write("\7/\2\2\65\66\7e\2\2\66\67\3\2\2\2\678\5\23\n\28\22\3")
        buf.write("\2\2\29;\t\2\2\2:9\3\2\2\2;<\3\2\2\2<:\3\2\2\2<=\3\2\2")
        buf.write("\2=\24\3\2\2\2>@\t\3\2\2?>\3\2\2\2@A\3\2\2\2A?\3\2\2\2")
        buf.write("AB\3\2\2\2B\26\3\2\2\2CE\t\4\2\2DC\3\2\2\2EF\3\2\2\2F")
        buf.write("D\3\2\2\2FG\3\2\2\2G\30\3\2\2\2\6\2<AF\2")
        return buf.getvalue()


class ReaderLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    TITLE = 5
    AUTHOR = 6
    DYNASTY = 7
    CATEGORY = 8
    WORD = 9
    ID = 10
    INT = 11

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'--s'", "'\n'", "'\r'", "'--p'" ]

    symbolicNames = [ "<INVALID>",
            "TITLE", "AUTHOR", "DYNASTY", "CATEGORY", "WORD", "ID", "INT" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "TITLE", "AUTHOR", "DYNASTY", 
                  "CATEGORY", "WORD", "ID", "INT" ]

    grammarFileName = "Reader.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


