grammar Expr;
r: ( (stat | function | struct | while)? NEWLINE)*;

stat:
	TYPE? ID '=' expr						# assign
	| TYPE ID '[' INT ']'					# arrayDeclaration
	| ID '[' arrayIndexExpr ']' '=' expr	# arrayAssign
	| 'print' '(' value ')'					# print
	| ID '=' 'read' '(' ')'					# read
	| ID '=' '{' expr (',' expr)* '}'		# structAssign
	| ID '.' structField '=' expr			# structFieldAssign
	| COMMENT_SINGLELINE					# comment;

expr:
	term							# singleTerm
	| term op = ('+' | '-') expr	# addSub
	| value							# single
	| ID '[' expr ']'				# arrayAccess
	| ID '.' structField			# structAccess
	| ID '()'						# functionCall;

structField: ID;

arrayIndexExpr: expr;

term:
	factor								# singleFactor
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

value: INT # int | DOUBLE # double | ID # id | STR # str;

TYPE: 'int' | 'double' | 'string';
MUL: '*'; // assigns token name to '*' used above in grammar
DIV: '/';
ADD: '+';
SUB: '-';
STR: '"' ( ~('\\' | '"'))* '"';

ID: ([a-zA-Z][a-zA-Z0-9]*) | ([a-zA-Z0-9][a-zA-Z]+);
INT: [-]? [0-9]+;
DOUBLE: [-]? [0-9]* '.' [0-9]+;
COMMENT_SINGLELINE: '#' ~[\n]*;
NEWLINE:
	'\r'? '\n'
	| EOF; // return newlines to parser (is end-statement signal)
WS: [ \t]+ -> skip; // toss out whitespace