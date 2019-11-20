import sys, os
from antlr4 import *
sys.path.append(os.path.dirname(os.path.abspath(__file__))+'/antlr')
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from ReaderParser import ReaderParser
from ReaderLexer import ReaderLexer
from DocReaderVisitor import DocReaderVisitor


class Reader(object):
    def __init__(self, s: str):
        i = InputStream(s)
        lexer = ReaderLexer(i)
        stream = CommonTokenStream(lexer)
        parser = ReaderParser(stream)
        tree = parser.prog()
        v = DocReaderVisitor()
        v.visit(tree)

        self._infoDict = v.getInfoDict()

    def getInfoDict(self):
        return self._infoDict


if __name__ == '__main__':
    # s = '--s-t无敌\n\n--p-a第一行\n第三行\n第四行\n二次回车\n--p-d数据\n第二段\n\n--s-c你的-t好的-a校\n\n--p-c无敌\n数据\n'
    with open('测试文本0.txt', 'r', encoding='utf-8') as file:
        s = file.read()
    print(Reader(s).getInfoDict())
