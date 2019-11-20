import sys, os
from antlr4 import *
sys.path.append(os.path.dirname(os.path.abspath(__file__))+'/antlr')
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from CorpusParser import CorpusParser
from CorpusLexer import CorpusLexer
from CorpusEvalVisitor import CorpusEvalVisitor


class CommandParser(object):
    def __init__(self, cmd: str):
        i = InputStream(cmd)
        lexer = CorpusLexer(i)
        stream = CommonTokenStream(lexer)
        parser = CorpusParser(stream)

        # print(cmd)
        if cmd.find("author:") == 0 or cmd.find("section:") == 0 or cmd.find("document:") == 0 or cmd.find("dynasty:") == 0:
            tree = parser.field()

        elif cmd.find(':') >= 0:
            tree = parser.prog()
        else:
            tree = parser.expr()
        v = CorpusEvalVisitor()
        v.visit(tree)

        self._wordList = v.getWordList()
        self._key = v.getKey()
        self._num = v.getNum()
        self._impWord = v.getImpWord()
        self._fields = v.getFields()

    def getWordList(self):
        return self._wordList

    def getKey(self):
        return self._key

    def getNum(self):
        return self._num

    def getImpWord(self):
        return self._impWord

    def getFields(self):
        return self._fields


# if __name__ == '__main__':
#     print(Token('真的 还行#5可以 不行 section:还行 好的 好的 section:不行 还好').getWordList())
    # main('好的-9无奈')
    # main('可以')