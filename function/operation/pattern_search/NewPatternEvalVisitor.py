import sys
import os
from antlr4 import *
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from PatternVisitor import PatternVisitor
from PatternParser import PatternParser
from PatternLexer import PatternLexer

# This class defines a complete generic visitor for a parse tree produced by PatternParser.

class PatternEvalVisitor(PatternVisitor):
    def __init__(self):
        self._flagsInfo = {}
        self._flagsList = []
        self._haveSomeFlag = False
        self._fields = {}

    # Visit a parse tree produced by PatternParser#prog.
    def visitProg(self, ctx:PatternParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PatternParser#expr.
    def visitExpr(self, ctx:PatternParser.ExprContext):
        if ctx.WORD():
            self._flagsList.append({
                "type": "word",
                "content": ctx.WORD().getText()
            })
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PatternParser#OP.
    def visitOP0(self, ctx:PatternParser.OP0Context):
        op = None
        if ctx.LES():
            op = "<"
        elif ctx.EQU():
            op = "="
        elif ctx.SCO():
            op = "-"
        if op:
            num = [int(ctx.INT(0).getText())]
            if ctx.INT(1):
                num.append(int(ctx.INT(1).getText()))
            info = {
                "num": num,
                "op": op
            }
        else:
            if ctx.ID().getText() in self._flagsInfo:
                info = self._flagsInfo[ctx.ID().getText()]
                self._haveSomeFlag = True
            else:
                info = {
                    "num": [10],
                    "op": "<"
                }
        self._flagsInfo[ctx.ID().getText()] = info
        self._flagsList.append({
            "type": "flag",
            "content": ctx.ID().getText(),
        })
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PatternParser#FIELD0.
    def visitFIELD0(self, ctx:PatternParser.FIELD0Context):
        if ctx.FIELD().getText() in self._fields.keys():
            for i in range(len(ctx.WORD())):
                self._fields[ctx.FIELD().getText()].append(ctx.WORD(i).getText())
        else:
            self._fields[ctx.FIELD().getText()] = [ctx.WORD(0).getText()]
            for i in range(1, len(ctx.WORD())):
                self._fields[ctx.FIELD().getText()].append(ctx.WORD(i).getText())
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PatternParser#FIELD1.
    def visitFIELD1(self, ctx:PatternParser.FIELD1Context):
        return self.visitChildren(ctx)

    def getFields(self):
        return self._fields

    def getFlagsInfo(self):
        return self._flagsInfo

    def getFlagsList(self):
        return self._flagsList

    def getHaveSomeFlag(self):
        return self._haveSomeFlag


del PatternParser