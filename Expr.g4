grammar Expr;
r: ( (stat | function | struct | while)? NEWLINE)*;

stat:
	TYPE? ID '=' expr											# assign
	| TYPE ID '[' INT ']'										# arrayDeclaration
	| ID '[' arrayIndexExpr ']' '=' expr						# arrayAssign
	| TYPE ID '[' INT ']' '[' INT ']'							# array2dDeclaration
	| ID '[' arrayIndexExpr ']' '[' arrayIndexExpr ']' '=' expr	# array2dAssign
	| 'print' '(' value ')'										# print
	| 'read' '(' ID ')'											# read
	| ID '=' '{' expr (',' expr)* '}'							# structAssign
	| ID '.' structField '=' expr								# structFieldAssign
	| COMMENT_SINGLELINE										# comment;

expr:
	term								# singleTerm
	| term op = ('+' | '-') expr		# addSub
	| term op = ('&' | '|' | '^') expr	# bitAndOrXor
	| '~' expr							# bitNot
	| value								# single
	| ID '[' expr ']'					# arrayAccess
	| ID '[' expr ']' '[' expr ']'		# array2dAccess
	| ID '.' structField				# structAccess
	| ID '()'							# functionCall;

structField: ID;

arrayIndexExpr: expr;

term:
	factor							# singleFactor
	| factor op = ('*' | '/') term	# mulDiv;
factor: value | '(' expr ')';

function: STARTFUNCTION functionParam functionBlock ENDFUNCTION;
functionParam: ID;
functionBlock: ( stat? NEWLINE)*;
STARTFUNCTION: 'fn';
ENDFUNCTION: 'nf';

struct: STARTSTRUCT structId structBlock ENDSTRUCT;
structId: ID;
structBlock: (TYPE ID NEWLINE)*;
STARTSTRUCT: 'struct';
ENDSTRUCT: 'tcurts';

while: STARTWHILE expr whileBlock ENDWHILE;
whileBlock: ( stat? NEWLINE)*;
STARTWHILE: 'while';
ENDWHILE: 'elihw';

if: STARTIF expr ifBlock ENDIF;
ifBlock: ( stat? NEWLINE)*;
STARTIF: 'if';
ENDIF: 'fi';

value:
	INT			# int
	| DOUBLE	# double
	| ID		# id
	| STR		# str
	| FLOAT		# float;

TYPE: 'int' | 'double' | 'string' | 'float';
MUL: '*'; // assigns token name to '*' used above in grammar
DIV: '/';
ADD: '+';
SUB: '-';
STR: '"' ( ~('\\' | '"'))* '"';
BIT_AND: '&';
BIT_OR: '|';
BIT_XOR: '^';
BIT_NOT: '~';

ID: ([a-zA-Z][a-zA-Z0-9]*);

INT: [-]? [0-9]+;
DOUBLE: [-]? [0-9]* '.' [0-9]+;
FLOAT: [-]? [0-9]* '.' [0-9]+ [f];
COMMENT_SINGLELINE: '#' ~[\n]*;
NEWLINE:
	'\r'? '\n'
	| EOF; // return newlines to parser (is end-statement signal)
WS: [ \t]+ -> skip; // toss out whitespace