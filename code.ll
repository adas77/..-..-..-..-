
declare i32 @printf(i8*, ...)
declare i32 @__isoc99_scanf(i8*, ...)
@strp = constant [4 x i8] c"%d\0A\00"
@strlf = constant [4 x i8] c"%lf\00"
@strlfn = constant [5 x i8] c"%lf\0A\00"
@strs = constant [3 x i8] c"%d\00"
@strstr = constant [4 x i8] c"%s\0A\00"
@str_int_newline = constant [4 x i8] c"%d\0A\00"
@str_double_newline = constant [5 x i8] c"%lf\0A\00"
@str_string_newline = constant [4 x i8] c"%s\0A\00"
@str_float_newline = constant [4 x i8] c"%f\0A\00"
@str_int = constant [3 x i8] c"%d\00"
@str_double = constant [4 x i8] c"%lf\00"
@str_string = constant [3 x i8] c"%s\00"
@str_float = constant [3 x i8] c"%f\00"
%struct.s1 = type { i32 }
@var1 = global %struct.s1 zeroinitializer
@var2 = global i32 0

define i32 @main() nounwind {
%1 = alloca i32
store i32 10, i32* %1, align 4
%2 = load i32, i32* %1
%3 = getelementptr %struct.s1, %struct.s1* @var1, i32 0, i32 0
store i32 %2, i32* %3
%4 = alloca i32
store i32 123, i32* %4, align 4
%5 = load i32, i32* %4
%6 = getelementptr %struct.s1, %struct.s1* @var1, i32 0, i32 0
store i32 %5, i32* %6
%7 = getelementptr %struct.s1, %struct.s1* @var1, i32 0, i32 0
%8 = load i32, i32* %7
store i32 %8, i32* @var2
%9 = load i32, i32* @var2
%10 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_int_newline, i32 0, i32 0),i32 %9)

ret i32 0 }