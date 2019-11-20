import sys
import os
from antlr4 import *
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from CorpusVisitor import CorpusVisitor
from CorpusParser import CorpusParser

class CorpusEvalVisitor(CorpusVisitor):
    def __init__(self):
        self._wordList = []
        self._key = []
        self._num = []
        self._impWord = ''
        self._mark = -1
        self._words = []
        self._fields = {}

    def visitSOLO(self, ctx: CorpusParser.SOLOContext):
        return super().visitSOLO(ctx)

    def visitOP1(self, ctx: CorpusParser.OP1Context):
        self._key.append(ctx.KEY1().getText())
        self._num.append(ctx.INT().getText())
        return super().visitOP1(ctx)

    def visitOP2(self, ctx: CorpusParser.OP2Context):
        return super().visitOP2(ctx)

    def visitOP3(self, ctx: CorpusParser.OP3Context):
        self._key.append(ctx.KEY3().getText())
        self._num.append(ctx.INT().getText())
        return super().visitOP3(ctx)

    def visitOp2(self, ctx: CorpusParser.Op2Context):
        if ctx.INT():
            self._key.append(ctx.KEY2().getText())
            self._num.append(ctx.INT().getText())
        return super().visitOp2(ctx)

    def visitSP0(self, ctx: CorpusParser.SP0Context):
        if ctx.WORD().getText()[0] == '!':
            word = ctx.WORD().getText()[1:]
            self._impWord = word
        else:
            word = ctx.WORD().getText()
        if self._mark == -1:
            self._wordList.append([[word]])
        elif self._mark == 0:
            self._wordList[-1].append([word])
        elif self._mark == 1:
            self._wordList[-1][-1].append(word)
        if ctx.SPL().getText() == ' ':
            self._mark = 0
        elif ctx.SPL().getText() == '|':
            self._mark = 1
        return self.visitChildren(ctx)

    def visitSP1(self, ctx: CorpusParser.SP1Context):
        if ctx.WORD().getText()[0] == '!':
            word = ctx.WORD().getText()[1:]
            self._impWord = word
        else:
            word = ctx.WORD().getText()
        if self._mark == 0:
            self._wordList[-1].append([word])
        elif self._mark == -1:
            self._wordList.append([[word]])
        elif self._mark == 1:
            self._words.append(word)
            self._wordList[-1][-1].append(word)
        self._words = []
        self._mark = -1
        return self.visitChildren(ctx)

    def visitFIELD0(self, ctx:CorpusParser.FIELD0Context):
        if ctx.FIELD().getText() in self._fields.keys():
            for i in range(len(ctx.WORD())):
                self._fields[ctx.FIELD().getText()].append(ctx.WORD(i).getText())
        else:
            self._fields[ctx.FIELD().getText()] = [ctx.WORD(0).getText()]
            for i in range(1, len(ctx.WORD())):
                self._fields[ctx.FIELD().getText()].append(ctx.WORD(i).getText())
        return self.visitChildren(ctx)

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

