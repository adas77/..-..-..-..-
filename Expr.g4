grammar Expr;
r: stat+;

stat:
	expr NEWLINE											# printExpr
	| ID '=' expr NEWLINE									# assign
	| ID '=' arr NEWLINE									# array
	| 'print' '(' op = (ID | INT | FLOAT | STR) ')' NEWLINE	# print
	| NEWLINE												# blank;

expr:
	expr op = ('*' | '/') expr		# MulDiv
	| expr op = ('+' | '-') expr	# AddSub
	| INT							# int
	| FLOAT							# float
	| ID							# id
	| '(' expr ')'					# parens;

arr: '{' val (',' val)* '}' # value;

val: INT | FLOAT;
STR: '"' ID '"';

MUL: '*'; // assigns token name to '*' used above in grammar
DIV: '/';
ADD: '+';
SUB: '-';
ID: [a-zA-Z]+; // match identifiers
INT: [0-9]+; // match integers
FLOAT: [0-9]+ '.' [0-9]+; // match integers
NEWLINE:
	'\r'? '\n'; // return newlines to parser (is end-statement signal)
WS: [ \t]+ -> skip; // toss out whitespace