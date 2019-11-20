# Generated from Corpus.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\r")
        buf.write("d\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\3\2\3\3")
        buf.write("\5\3\35\n\3\3\3\6\3 \n\3\r\3\16\3!\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\5\4H\n\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b")
        buf.write("\3\b\3\t\3\t\3\n\6\nU\n\n\r\n\16\nV\3\13\6\13Z\n\13\r")
        buf.write("\13\16\13[\3\f\6\f_\n\f\r\f\16\f`\3\f\3\f\2\2\r\3\3\5")
        buf.write("\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\3\2\t\t")
        buf.write("\2\u2e82\u2fe1\u3002\u3041\u31c2\u31f1\u3202\u9fc1\uf902")
        buf.write("\ufb01\ufe32\ufe51\uff02\ufff1\4\2\"\"~~\4\2&&--\4\2/")
        buf.write("/\u0080\u0080\4\2C\\c|\3\2\62;\4\2\13\f\17\17\2m\2\3\3")
        buf.write("\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2")
        buf.write("\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2")
        buf.write("\2\25\3\2\2\2\2\27\3\2\2\2\3\31\3\2\2\2\5\34\3\2\2\2\7")
        buf.write("G\3\2\2\2\tI\3\2\2\2\13K\3\2\2\2\rM\3\2\2\2\17O\3\2\2")
        buf.write("\2\21Q\3\2\2\2\23T\3\2\2\2\25Y\3\2\2\2\27^\3\2\2\2\31")
        buf.write("\32\7<\2\2\32\4\3\2\2\2\33\35\7#\2\2\34\33\3\2\2\2\34")
        buf.write("\35\3\2\2\2\35\37\3\2\2\2\36 \t\2\2\2\37\36\3\2\2\2 !")
        buf.write("\3\2\2\2!\37\3\2\2\2!\"\3\2\2\2\"\6\3\2\2\2#$\7f\2\2$")
        buf.write("%\7{\2\2%&\7p\2\2&\'\7c\2\2\'(\7u\2\2()\7v\2\2)H\7{\2")
        buf.write("\2*+\7v\2\2+,\7{\2\2,-\7r\2\2-H\7g\2\2./\7c\2\2/\60\7")
        buf.write("w\2\2\60\61\7v\2\2\61\62\7j\2\2\62\63\7q\2\2\63H\7t\2")
        buf.write("\2\64\65\7u\2\2\65\66\7g\2\2\66\67\7e\2\2\678\7v\2\28")
        buf.write("9\7k\2\29:\7q\2\2:H\7p\2\2;<\7f\2\2<=\7q\2\2=>\7e\2\2")
        buf.write(">?\7w\2\2?@\7o\2\2@A\7g\2\2AB\7p\2\2BH\7v\2\2CD\7c\2\2")
        buf.write("DE\7t\2\2EF\7g\2\2FH\7c\2\2G#\3\2\2\2G*\3\2\2\2G.\3\2")
        buf.write("\2\2G\64\3\2\2\2G;\3\2\2\2GC\3\2\2\2H\b\3\2\2\2IJ\t\3")
        buf.write("\2\2J\n\3\2\2\2KL\7%\2\2L\f\3\2\2\2MN\t\4\2\2N\16\3\2")
        buf.write("\2\2OP\t\5\2\2P\20\3\2\2\2QR\7#\2\2R\22\3\2\2\2SU\t\6")
        buf.write("\2\2TS\3\2\2\2UV\3\2\2\2VT\3\2\2\2VW\3\2\2\2W\24\3\2\2")
        buf.write("\2XZ\t\7\2\2YX\3\2\2\2Z[\3\2\2\2[Y\3\2\2\2[\\\3\2\2\2")
        buf.write("\\\26\3\2\2\2]_\t\b\2\2^]\3\2\2\2_`\3\2\2\2`^\3\2\2\2")
        buf.write("`a\3\2\2\2ab\3\2\2\2bc\b\f\2\2c\30\3\2\2\2\t\2\34!GV[")
        buf.write("`\3\b\2\2")
        return buf.getvalue()


class CorpusLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    WORD = 2
    FIELD = 3
    SPL = 4
    KEY1 = 5
    KEY2 = 6
    KEY3 = 7
    IMP = 8
    ID = 9
    INT = 10
    WS = 11

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "':'", "'#'", "'!'" ]

    symbolicNames = [ "<INVALID>",
            "WORD", "FIELD", "SPL", "KEY1", "KEY2", "KEY3", "IMP", "ID", 
            "INT", "WS" ]

    ruleNames = [ "T__0", "WORD", "FIELD", "SPL", "KEY1", "KEY2", "KEY3", 
                  "IMP", "ID", "INT", "WS" ]

    grammarFileName = "Corpus.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


