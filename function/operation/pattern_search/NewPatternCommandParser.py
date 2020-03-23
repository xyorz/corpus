import sys, re, os
from antlr4 import *
from antlr4 import Recognizer
sys.path.append(os.path.dirname(os.path.abspath(__file__))+'/antlr')
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from PatternParser import PatternParser
from PatternLexer import PatternLexer
from NewPatternEvalVisitor import PatternEvalVisitor


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

        self._flagsList = v.getFlagsList()
        self._flagsInfo = v.getFlagsInfo()
        self._fields = v.getFields()
        self._haveSomeFlag = v.getHaveSomeFlag()

    def getFlagsList(self):
        return self._flagsList

    def getFlagsInfo(self):
        return self._flagsInfo

    def getFields(self):
        return self._fields

    def getHaveSomeFlag(self):
        return self._haveSomeFlag


if __name__ == '__main__':
    # print(pattern('爱(v,=5)不(t)'))
    print(CommandParser('(V2-5)故好評(T<5)我我我').getFlagsInfo())
    print(CommandParser('(V2-5)故好評(T<5)我我我').getFlagsList())
    # t('爱(v,=5??)不(v)')
    # print()
