import sys
import os
import re
from antlr4 import *
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from ReaderVisitor import ReaderVisitor
from ReaderParser import ReaderParser


class DocReaderVisitor(ReaderVisitor):

    def __init__(self):
        self._id = '0.0.0'
        self._count = 0
        self._info_dict = {}

    # Visit a parse tree produced by ReaderParser#prog.
    def visitProg(self, ctx:ReaderParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ReaderParser#sec.
    def visitSec(self, ctx:ReaderParser.SecContext):
        # print('visit_sec:'+self._id)
        self._id = self._id[0:self._id.rfind('.')]
        counter = int(self._id.split('.')[-1]) + 1
        self._id = self._id[0:self._id.rfind('.')] + '.' + str(counter)

        self._info_dict[self._id] = self.visit(ctx.s_info())
        print('after_visit_sec:' + self._id)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ReaderParser#data.
    def visitData(self, ctx:ReaderParser.DataContext):
        if not ctx.data():
            return ctx.WORD().getText()
        else:
            return ctx.WORD().getText()+self.visit(ctx.data())


    # Visit a parse tree produced by ReaderParser#para.
    def visitPara(self, ctx:ReaderParser.ParaContext):
        # print('visit_para:' + self._id)
        # 刚visit sec
        counter = 0
        if self._id.count('.') == 1:
            counter = 1
            self._id += '.' + str(counter)
        else:
            counter = int(self._id.split('.')[-1]) + 1
            self._id = self._id[0:self._id.rfind('.')] + '.' + str(counter)
        self._info_dict[self._id] = self.visit(ctx.p_info())
        if ctx.data():
            self._info_dict[self._id]['text'] = ctx.data().getText()
        print('after_visit_para:' + self._id)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ReaderParser#d_info.
    def visitD_info(self, ctx:ReaderParser.D_infoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ReaderParser#s_info.
    def visitS_info(self, ctx:ReaderParser.S_infoContext):
        current_dict = {}
        # for i in range(len(ctx.info)):
        if ctx.TITLE():
            current_dict['section'] = ctx.TITLE()[0].getText().replace('-t', '')
        else:
            current_dict['section'] = ''
        if ctx.AUTHOR():
            current_dict['author'] = ctx.AUTHOR()[0].getText().replace('-a', '')
        else:
            current_dict['author'] = ''
        if ctx.DYNASTY():
            current_dict['dynasty'] = ctx.DYNASTY()[0].getText().replace('-d', '')
        else:
            current_dict['dynasty'] = ''
        if ctx.CATEGORY():
            current_dict['category'] = ctx.CATEGORY()[0].getText().replace('-c', '')
        else:
            current_dict['category'] = ''
        return current_dict


    # Visit a parse tree produced by ReaderParser#p_info.
    def visitP_info(self, ctx:ReaderParser.P_infoContext):
        current_dict = {}
        if ctx.AUTHOR():
            current_dict['author'] = ctx.AUTHOR()[0].getText().replace('-a', '')
        else:
            current_dict['author'] = ''
        if ctx.DYNASTY():
            current_dict['dynasty'] = ctx.DYNASTY()[0].getText().replace('-d', '')
        else:
            current_dict['dynasty'] = ''
        if ctx.CATEGORY():
            current_dict['category'] = ctx.CATEGORY()[0].getText().replace('-c', '')
        else:
            current_dict['category'] = ''
        return current_dict

    def getInfoDict(self):
        return self._info_dict



del ReaderParser