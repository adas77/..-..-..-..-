grammar Expr;
r: stat+;

stat:
	expr NEWLINE											# printExpr
	| TYPE ID NEWLINE										# declaration
	| ID '=' expr NEWLINE									# assign
	| TYPE ID '[' INT ']' NEWLINE							# arrayDeclaration
	| ID '[' op = (INT | ID) ']' '=' expr NEWLINE			# arrayAssign
	| 'print' '(' op = (ID | INT | FLOAT | STR) ')' NEWLINE	# print
	| ID '=' 'read' '(' ')' NEWLINE							# read
	| NEWLINE												# blank;
//	| '#' COMMENT NEWLINE									# comment;

expr:
	expr op = ('*' | '/') expr		# MulDiv
	| expr op = ('+' | '-') expr	# AddSub
	| INT							# int
	| FLOAT							# float
	| STR							# str
	| ID							# id
	| '(' expr ')'					# parens
	| ID '[' op = (INT | ID) ']'	# arrayAccess;

// TODO: arr: '{' val (',' val)* '}' # value;

val: INT | FLOAT;

// STR: '"' ID '"';
TYPE: 'int' | 'float' | 'string';
MUL: '*'; // assigns token name to '*' used above in grammar
DIV: '/';
ADD: '+';
SUB: '-';
STR: '"' [a-zA-Z _]+ '"';
ID: [a-zA-Z]+; // match identifiers
INT: [0-9]+; // match integers
FLOAT: [0-9]+ '.' [0-9]+; // match integers
//COMMENT: [a-zA-Z _]+;
NEWLINE:
	'\r'? '\n'
	| EOF; // return newlines to parser (is end-statement signal)
WS: [ \t]+ -> skip; // toss out whitespace