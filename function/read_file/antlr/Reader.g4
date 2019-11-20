grammar Reader;

prog : sec;

sec : '--s' s_info '\n' ('\r')? '\n' ('\r')? para ('\n' ('\r')? '\n' ('\r')? sec)? (('\n'('\r')?)+)? EOF?;

data : WORD
     | WORD '\n' data
     ;

para: '--p' p_info '\n' ('\r')? data ('\n' ('\r')? para)?;

d_info : info=(TITLE|AUTHOR|DYNASTY|CATEGORY)+;

s_info : info=(TITLE|AUTHOR|DYNASTY|CATEGORY)+;

p_info : info=(AUTHOR|DYNASTY|CATEGORY)*;

TITLE: ('-t' WORD);
AUTHOR: ('-a' WORD);
DYNASTY: ('-d' WORD);
CATEGORY: ('-c' WORD);


WORD : [\u4E00-\u9FA5 \u3002\uff1f\uff01\uff0c\u3001\uff1b\uff1a\u201c\u201d\u2018\u2019\uff08\uff09\u300a\u300b\u3008\u3009\u3010\u3011\u300e\u300f\u300c\u300d\ufe43\ufe44\u3014\u3015\u2026\u2014\uff5e\ufe4f\uffe5]+ ;
ID   : [a-zA-Z]+ ;
INT  : [0-9]+ ;