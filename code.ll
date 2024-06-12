define i32 @foobar(i32 %0, float %1, i32 %2) {
%var2 = alloca i32
store i32 %0, i32* %var2
%var3 = alloca float
store float %1, float* %var3
%var4 = alloca i32
store i32 %2, i32* %var4
%4 = load i32, i32* %var2
ret i32 %4
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
%struct.s1 = type { float, i32 }
@var5 = global %struct.s1 zeroinitializer
@var6 = global i32 0

define i32 @main() nounwind {
%1 = alloca i32
store i32 10, i32* %1, align 4
%2 = load i32, i32* %1
%3 = alloca float
store float 0x3fe4937400000000, float* %3, align 4
%4 = load float, float* %3
%5 = getelementptr %struct.s1, %struct.s1* @var5, i32 0, i32 0
store float %4, float* %5
%6 = getelementptr %struct.s1, %struct.s1* @var5, i32 0, i32 1
store i32 %2, i32* %6
%7 = alloca i32
store i32 123, i32* %7, align 4
%8 = load i32, i32* %7
%9 = getelementptr %struct.s1, %struct.s1* @var5, i32 0, i32 1
store i32 %8, i32* %9
%10 = alloca i32
store i32 621, i32* %10, align 4
%11 = load i32, i32* %10
%12 = getelementptr %struct.s1, %struct.s1* @var5, i32 0, i32 0
%13 = load float, float* %12
%14 = getelementptr %struct.s1, %struct.s1* @var5, i32 0, i32 1
%15 = load i32, i32* %14
%16 = alloca i32
store i32 621, i32* %16, align 4
%17 = load i32, i32* %16
%18 = call i32 @foobar(i32 %15, float %13, i32 %17)
store i32 %18, i32* @var6
%19 = load i32, i32* @var6
%20 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_int_newline, i32 0, i32 0),i32 %19)

ret i32 0 }