define i32 @foobar(i32 %0, float %1) {
%var2 = alloca i32
store i32 %0, i32* %var2
%var3 = alloca float
store float %1, float* %var3
%3 = load i32, i32* %var2
%4 = load i32, i32* %var2
%5 = mul i32 %3, %4
store i32 %5, i32* %var2
%6 = load i32, i32* %var2
ret i32 %6
}

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
@var4 = global i32 0
@var5 = global i32 0

define i32 @main() nounwind {
%1 = alloca i32
store i32 5, i32* %1, align 4
%2 = load i32, i32* %1
store i32 %2, i32* @var4
%3 = alloca i32
store i32 8, i32* %3, align 4
%4 = load i32, i32* %3
%5 = alloca float
store float 0x4010000000000000, float* %5, align 4
%6 = load float, float* %5
%7 = call i32 @foobar(i32 %4, float %6)
store i32 %7, i32* @var5
%8 = load i32, i32* @var5
%9 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_int_newline, i32 0, i32 0),i32 %8)

ret i32 0 }