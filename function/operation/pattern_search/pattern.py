import sys, re, os
from antlr4 import *
from antlr4 import Recognizer
sys.path.append(os.path.dirname(os.path.abspath(__file__))+'/antlr')
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from PatternParser import PatternParser
from PatternLexer import PatternLexer
from PatternEvalVisitor import PatternEvalVisitor


# def pattern(s):
#     i = InputStream(s)
#     lexer = PatternLexer(i)
#     stream = CommonTokenStream(lexer)
#     parser = PatternParser(stream)
#     if s.find(':') >= 0:
#         tree = parser.prog()
#     else:
#         tree = parser.expr()
#     v = PatternEvalVisitor()
#     return v.visit(tree)
#
#
# def get_pattern_fields(s):
#     i = InputStream(s)
#     lexer = PatternLexer(i)
#     stream = CommonTokenStream(lexer)
#     parser = PatternParser(stream)
#     if s.find(':') >= 0:
#         tree = parser.prog()
#     else:
#         tree = parser.expr()
#     v = PatternEvalVisitor()
#     v.visit(tree)
#     return v.getFields()

class Token(object):
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

if __name__ == '__main__':
    # print(pattern('爱(v,=5)不(t)'))
    print(Token('故(V,<5)評(T,=1)').getRe())
    # t('爱(v,=5??)不(v)')
    # print()
