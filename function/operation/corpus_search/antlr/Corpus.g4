grammar Corpus;

prog : expr SPL field
     ;

expr : sim KEY1 INT sim        # OP1
     | op2                     # OP2
     | sim KEY3 INT sim        # OP3
     | sim                     # SOLO
     ;

op2 : sim KEY2 INT op2
    | sim
    ;

sim  : WORD SPL sim             #SP0
     | WORD                     #SP1
     ;

field: FIELD ':' WORD  (SPL WORD)* SPL? field #FIELD0
     | EOF                                      #FIELD1
     ;



WORD : '!'?[\u2E80-\u2EFF\u2F00-\u2FDF\u3000-\u303F\u31C0-\u31EF\u3200-\u32FF\u3300-\u33FF\u3400-\u4DBF\u4DC0-\u4DFF\u4E00-\u9FBF\uF900-\uFAFF\uFE30-\uFE4F\uFF00-\uFFEF]+  ;
FIELD : ('dynasty'|'type'|'author'|'section'|'document'|'area') ;
SPL  : [ |] ;
KEY1 : '#' ;
KEY2 : [+$] ;
KEY3 : [-~] ;
IMP  : '!' ;
ID   : [a-zA-Z]+ ;
INT  : [0-9]+ ;
WS   : [\t\r\n]+ -> skip ;