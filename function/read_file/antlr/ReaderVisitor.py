# Generated from Reader.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ReaderParser import ReaderParser
else:
    from ReaderParser import ReaderParser

# This class defines a complete generic visitor for a parse tree produced by ReaderParser.

class ReaderVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ReaderParser#prog.
    def visitProg(self, ctx:ReaderParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ReaderParser#sec.
    def visitSec(self, ctx:ReaderParser.SecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ReaderParser#data.
    def visitData(self, ctx:ReaderParser.DataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ReaderParser#para.
    def visitPara(self, ctx:ReaderParser.ParaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ReaderParser#d_info.
    def visitD_info(self, ctx:ReaderParser.D_infoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ReaderParser#s_info.
    def visitS_info(self, ctx:ReaderParser.S_infoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ReaderParser#p_info.
    def visitP_info(self, ctx:ReaderParser.P_infoContext):
        return self.visitChildren(ctx)



del ReaderParser