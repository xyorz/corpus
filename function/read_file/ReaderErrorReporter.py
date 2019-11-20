import sys, os
from antlr4.error.ErrorListener import *
from antlr4 import *
sys.path.append(os.path.dirname(os.path.abspath(__file__))+'/antlr')
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from ReaderParser import ReaderParser
from ReaderLexer import ReaderLexer
from DocReaderVisitor import DocReaderVisitor

class ReaderErrorListener(ErrorListener):

    def __init__(self):
        self._message = ''

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        if self._message == '':
            self._message = "出现错误：" + str(line) + "行 " + str(column) + "列 " + "错误描述：" + msg

    def getMessage(self):
        return self._message