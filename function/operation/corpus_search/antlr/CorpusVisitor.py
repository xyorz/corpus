# Generated from Corpus.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CorpusParser import CorpusParser
else:
    from CorpusParser import CorpusParser

# This class defines a complete generic visitor for a parse tree produced by CorpusParser.

class CorpusVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CorpusParser#prog.
    def visitProg(self, ctx:CorpusParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CorpusParser#OP1.
    def visitOP1(self, ctx:CorpusParser.OP1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CorpusParser#OP2.
    def visitOP2(self, ctx:CorpusParser.OP2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CorpusParser#OP3.
    def visitOP3(self, ctx:CorpusParser.OP3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CorpusParser#SOLO.
    def visitSOLO(self, ctx:CorpusParser.SOLOContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CorpusParser#op2.
    def visitOp2(self, ctx:CorpusParser.Op2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CorpusParser#SP0.
    def visitSP0(self, ctx:CorpusParser.SP0Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CorpusParser#SP1.
    def visitSP1(self, ctx:CorpusParser.SP1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CorpusParser#FIELD0.
    def visitFIELD0(self, ctx:CorpusParser.FIELD0Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CorpusParser#FIELD1.
    def visitFIELD1(self, ctx:CorpusParser.FIELD1Context):
        return self.visitChildren(ctx)



del CorpusParser