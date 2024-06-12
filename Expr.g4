grammar Expr;
r: ((stat | function | generator | struct | while | if)? NEWLINE)*;

stat:
	TYPE? ID '=' expr											# assign
	| TYPE ID '[' INT ']'										# arrayDeclaration
	| ID '[' arrayIndexExpr ']' '=' expr						# arrayAssign
	| TYPE ID '[' INT ']' '[' INT ']'							# array2dDeclaration
	| ID '[' arrayIndexExpr ']' '[' arrayIndexExpr ']' '=' expr	# array2dAssign
	| 'print' '(' value ')'										# print
	| 'read' '(' ID ')'											# read
	| ID '=' structId '{' structArgs '}'						# structAssign
	| ID '.' structField '=' expr								# structFieldAssign
	| COMMENT_SINGLELINE										# comment
	| 'global' ID												# globalDeclaration
	| 'del' ID													# deleteVariable
	| structId 'method' functionId								# methodDeclaration;

expr:
	term									# singleTerm
	| term op = ('&&' | '||') expr			# logicalAndOr
	| term op = ('+' | '-') expr			# addSub
	| term op = ('&' | '|' | '^') expr		# bitAndOrXor
	| term '!' expr							# logicalNot
	| '~' expr								# bitNot
	| expr op = ('&&' | '||') expr			# logicalAndOr
	| '!' expr								# logicalNot
	| value									# single
	| ID '[' expr ']'						# arrayAccess
	| ID '[' expr ']' '[' expr ']'			# array2dAccess
	| ID '.' structField					# structAccess
	| ID functionArgsCall					# functionCall
	| generatorId '<>'						# generatorCall
	| ID '.' classMethodId functionArgsCall	# methodCall;

functionId: ID;

classMethodId: ID;
structField: ID;
structArgs: (expr (',' expr)*)?;

arrayIndexExpr: expr;
icmpExpr: expr;
term:
	factor							# singleFactor
	| factor op = ('*' | '/') term	# mulDiv;
factor: value | '(' expr ')';

generator: 'gen' generatorId '(' arrayId ')';
generatorId: ID;
arrayId: ID;

function:
	STARTFUNCTION functionParam functionArgs ':' TYPE functionBlock functionReturn ENDFUNCTION;
functionParam: ID;
functionBlock: ( stat? NEWLINE)*;
functionReturn: ( 'return' ID? NEWLINE+)?;
functionArgs: '(' (functionArg (',' functionArg)*)? ')';
functionArg: ID ':' MUTABLE? TYPE;
MUTABLE: 'mut';
functionArgsCall: '(' (value (',' value)*)? ')';
STARTFUNCTION: 'fn';
ENDFUNCTION: 'nf';

struct: STARTSTRUCT structId NEWLINE structBlock ENDSTRUCT;
structId: ID;
structBlock: (TYPE ID NEWLINE)*;
STARTSTRUCT: 'struct';
ENDSTRUCT: 'tcurts';

while: STARTWHILE icmpExpr whileBlock ENDWHILE;
whileBlock: ( (stat | if | while)? NEWLINE)*;
STARTWHILE: 'while';
ENDWHILE: 'elihw';

if: STARTIF icmpExpr ifBlock ENDIF;
ifBlock: ( (stat | if | while)? NEWLINE)*;
STARTIF: 'if';
ENDIF: 'fi';

value:
	INT			# int
	| DOUBLE	# double
	| ID		# id
	| STR		# str
	| FLOAT		# float;

TYPE: 'int' | 'double' | 'string' | 'float' | 'void';
MUL: '*'; // assigns token name to '*' used above in grammar
DIV: '/';
ADD: '+';
SUB: '-';
STR: '"' ( ~('\\' | '"'))* '"';
BIT_AND: '&';
BIT_OR: '|';
BIT_XOR: '^';
BIT_NOT: '~';

LOGICAL_AND: '&&';
LOGICAL_OR: '||';
LOGICAL_NOT: '!';

ID: ([a-zA-Z][a-zA-Z0-9]*);

INT: [-]? [0-9]+;
DOUBLE: [-]? [0-9]* '.' [0-9]+;
FLOAT: [-]? [0-9]* '.' [0-9]+ [f];
COMMENT_SINGLELINE: '#' ~[\n]*;
NEWLINE:
	'\r'? '\n'
	| EOF; // return newlines to parser (is end-statement signal)
WS: [ \t]+ -> skip; // toss out whitespace