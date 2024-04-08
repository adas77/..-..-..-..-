PY=python3
JAVA=java
LLVM=lli
ANTLR_JAR=./antlr-4.13.1-complete.jar

# ANTLR=$(JAVA) -jar $(ANTLR_JAR) -visitor
ANTLR=$(JAVA) -jar $(ANTLR_JAR)

PATH_ANTLR_OUTPUT=g4
PATH_G4=Expr.g4
PATH_INPUT=input.txt
LLVM_OUTPUT=code.ll

pip:
	pip install -r requirements.txt

antlr4:
	$(ANTLR)

gen:
	$(ANTLR) -Dlanguage=Python3 -o $(PATH_ANTLR_OUTPUT) Expr.g4

run:
	$(PY) main.py $(PATH_INPUT)

ll:
	$(LLVM) $(LLVM_OUTPUT)

cl:
	clear

r: gen run

c: cl gen run ll
