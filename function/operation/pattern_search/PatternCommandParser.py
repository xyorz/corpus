import sys, re, os
from antlr4 import *
from antlr4 import Recognizer
sys.path.append(os.path.dirname(os.path.abspath(__file__))+'/antlr')
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from PatternParser import PatternParser
from PatternLexer import PatternLexer
from PatternEvalVisitor import PatternEvalVisitor


class CommandParser(object):
    def __init__(self, cmd: str):
        i = InputStream(cmd)
        lexer = PatternLexer(i)
        stream = CommonTokenStream(lexer)
        parser = PatternParser(stream)
        if cmd.find(':') >= 0:
            tree = parser.prog()
        else:
            tree = parser.expr()
        v = PatternEvalVisitor()
        res = v.visit(tree)

        self._re = res
        self._words = v.getWords()
        self._fields = v.getFields()

    def getRe(self):
        return self._re

    def getWords(self):
        return self._words

    def getFields(self):
        return self._fields

# if __name__ == '__main__':
    # print(pattern('爱(v,=5)不(t)'))
    # print(Token('是(v,<5)沒(t) author:我的').getRe())
    # t('爱(v,=5??)不(v)')
    # print()
