import sys
import os
from antlr4 import *
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from PatternVisitor import PatternVisitor
from PatternParser import PatternParser
from PatternLexer import PatternLexer


class PatternEvalVisitor(PatternVisitor):
    def __init__(self, zh_to_hant_dict=None):
        self.count = 0
        self.memory = {}
        self._fields = {}
        self._words = []
        if not zh_to_hant_dict:
            zh_to_hant_dict = {}
        self._zh_to_hant_dict = zh_to_hant_dict

    def visitProg(self, ctx:PatternParser.ProgContext):
        self.visit(ctx.field())
        return self.visit(ctx.expr())

    def visitExpr(self, ctx:PatternParser.ExprContext):
        if not ctx.WORD():
            return ''
        self._words.append(ctx.WORD().getText())
        word = ctx.WORD().getText()
        d = self._zh_to_hant_dict
        if d:
            word_res = "["
            for w in word:
                word_res += w
                if w in d:
                    for hant in d[w]:
                        word_res += hant
            word_res += "]"
        else:
            word_res = word
        if ctx.expr():
            return word_res + self.visit(ctx.req()) + self.visit(ctx.expr())
        else:
            return word_res + self.visit(ctx.req())

    def visitOP1(self, ctx:PatternParser.OP1Context):
        op = ctx.op.type
        num = ctx.INT().getText()
        id = ctx.ID().getText()
        self.count += 1
        if op == PatternLexer.MOR:
            self.memory[id] = (PatternLexer.MOR, num)
            return '([\u4E00-\u9FA5\uF900-\uFA2D]{' + str(int(num)) + ',})'
        elif op == PatternLexer.LES:
            self.memory[id] = (PatternLexer.LES, num)
            return '([\u4E00-\u9FA5\uF900-\uFA2D]{1,' + str(int(num)) + '})'
        elif op == PatternLexer.EQU:
            self.memory[id] = (PatternLexer.EQU, num)
            return '([\u4E00-\u9FA5\uF900-\uFA2D]{' + str(int(num)) + '})'


    def visitOP2(self, ctx:PatternParser.OP2Context):
        num1 = ctx.INT(0).getText()
        num2 = ctx.INT(1).getText()
        id = ctx.ID().getText()
        self.count += 1
        self.memory[id] = (PatternLexer.SCO, num1, num2)
        return '([\u4E00-\u9FA5\uF900-\uFA2D]{' + str(num1) + ',' + str(num2) + '})'


    def visitId(self, ctx:PatternParser.IdContext):
        id = ctx.ID().getText()
        if id in self.memory.keys():
            return '\\' + str(self.count)
        else:
            self.count += 1
            self.memory[id] = (PatternLexer, '1', '10')
            return '([\u4E00-\u9FA5\uF900-\uFA2D]{1,10})'

    def visitFIELD0(self, ctx:PatternParser.FIELD0Context):
        if ctx.FIELD().getText() in self._fields.keys():
            for i in range(len(ctx.WORD())):
                self._fields[ctx.FIELD().getText()].append(ctx.WORD(i).getText())
        else:
            self._fields[ctx.FIELD().getText()] = [ctx.WORD(0).getText()]
            for i in range(1, len(ctx.WORD())):
                self._fields[ctx.FIELD().getText()].append(ctx.WORD(i).getText())
        return self.visitChildren(ctx)

    def visitFIELD1(self, ctx:PatternParser.FIELD1Context):
        return self.visitChildren(ctx)

    def getFields(self):
        return self._fields

    def getWords(self):
        return self._words
