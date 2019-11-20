import sys, re, os
from antlr4.error.ErrorListener import *
from antlr4 import *
sys.path.append(os.path.dirname(os.path.abspath(__file__))+'/antlr')
sys.path.append('./pattern_search/antlr')
from PatternParser import PatternParser
from PatternLexer import PatternLexer
from PatternEvalVisitor import PatternEvalVisitor


class PatternErrorListener(ErrorListener):

    def __init__(self):
        self._message = ''

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        if self._message == '':
            self._message = "line " + str(line) + ":" + str(column) + " " + msg

    def getMessage(self):
        return self._message


class PatternErrorReporter(object):
    def __init__(self, cmd: str):
        input = InputStream(cmd)
        lexer = PatternLexer(input)
        lexer.removeErrorListeners()
        listener = PatternErrorListener()
        lexer.addErrorListener(listener)
        stream = CommonTokenStream(lexer)
        parser = PatternParser(stream)
        parser.removeErrorListeners()
        parser.addErrorListener(listener)
        if cmd.find(':') >= 0:
            parser.prog()
        else:
            parser.expr()
        self._message = listener.getMessage()

    def error(self):
        if self._message == '':
            return False
        return True

    def getMessage(self):
        return self._message


if __name__ == '__main__':
    # PatternErrorReporter('爱(v,<5!)不(t)').getMessage()
    print(PatternErrorReporter('爱(v,<5)不(t)').getMessage())