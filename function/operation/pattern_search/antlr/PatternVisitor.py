# Generated from Pattern.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PatternParser import PatternParser
else:
    from PatternParser import PatternParser

# This class defines a complete generic visitor for a parse tree produced by PatternParser.

class PatternVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PatternParser#prog.
    def visitProg(self, ctx:PatternParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PatternParser#expr.
    def visitExpr(self, ctx:PatternParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PatternParser#OP0.
    def visitOP0(self, ctx:PatternParser.OP0Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PatternParser#FIELD0.
    def visitFIELD0(self, ctx:PatternParser.FIELD0Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PatternParser#FIELD1.
    def visitFIELD1(self, ctx:PatternParser.FIELD1Context):
        return self.visitChildren(ctx)



del PatternParser