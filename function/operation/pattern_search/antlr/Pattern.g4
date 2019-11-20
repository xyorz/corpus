grammar Pattern;

prog : expr SPL field
     ;

expr :  WORD '(' req ')' expr?
     ;

req : ID ',' op=('>'|'<'|'=') INT   # OP1
    | ID ',' INT op='-' INT         # OP2
    | ID                            # id
    ;

field: FIELD ':' WORD  (SPL WORD)* SPL? field #FIELD0
     | EOF                                    #FIELD1
     ;

WORD : [\u2E80-\u2EFF\u2F00-\u2FDF\u3000-\u303F\u31C0-\u31EF\u3200-\u32FF\u3300-\u33FF\u3400-\u4DBF\u4DC0-\u4DFF\u4E00-\u9FBF\uF900-\uFAFF\uFE30-\uFE4F\uFF00-\uFFEF]+ ;
FIELD : ('dynasty'|'type'|'author'|'section'|'document') ;
ID   : [a-zA-Z]+ ;
INT  : [0-9]+ ;
SPL  : [ |] ;
MOR  : '>' ;
LES  : '<' ;
EQU  : '=' ;
SCO  : '-' ;
WS   : [\t\r\n]+ -> skip ;