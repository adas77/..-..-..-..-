define i32 @foobar(i32 %0, float %1) {
%var2 = alloca i32
store i32 %0, i32* %var2
%var3 = alloca float
store float %1, float* %var3
%3 = load i32, i32* %var2
%4 = load i32, i32* %var2
%5 = mul i32 %3, %4
%6 = alloca i32
store i32 1, i32* %6, align 4
%7 = load i32, i32* %6
%8 = alloca i32
store i32 6, i32* %8, align 4
%9 = load i32, i32* %8
%10 = add i32 %7, %9
%11 = add i32 %5, %10
store i32 %11, i32* %var2
%12 = load i32, i32* %var2
ret i32 %12
}
define void @foobar4(i32 %0, float %1) {
%var5 = alloca i32
store i32 %0, i32* %var5
%var6 = alloca float
store float %1, float* %var6
%3 = load i32, i32* %var5
%4 = load i32, i32* %var5
%5 = mul i32 %3, %4
store i32 %5, i32* %var5
ret void
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
@var7 = global i32 0
@var8 = global i32 0

define i32 @main() nounwind {
%1 = alloca i32
store i32 5, i32* %1, align 4
%2 = load i32, i32* %1
store i32 %2, i32* @var7
%3 = load i32, i32* @var7
%4 = alloca float
store float 0x4010000000000000, float* %4, align 4
%5 = load float, float* %4
%6 = call i32 @foobar(i32 %3, float %5)
store i32 %6, i32* @var8
%7 = load i32, i32* @var8
%8 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_int_newline, i32 0, i32 0),i32 %7)

ret i32 0 }