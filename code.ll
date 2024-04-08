declare i32 @printf(i8*, ...)
declare i32 @__isoc99_scanf(i8*, ...)
@strp = constant [4 x i8] c"%d\0A\00"
@strf = constant [4 x i8] c"%f\0A\00"
@strs = constant [3 x i8] c"%d\00"
@strstr = constant [3 x i8] c"%s\00"
@s = constant [12 x i8] c"Hello world\00"
define i32 @main() nounwind{
%i = alloca i32
%f = alloca float
store i32 2137, i32* %i
store float 0.5, float* %f, align 4
%1 = load i32, i32* %i
%2 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strp, i32 0, i32 0), i32 %1)
%3 = load float, float* %f
%4 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strf, i32 0, i32 0), float %3)
%5 = load i8*, i8** @s
%6 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @strstr, i32 0, i32 0), i8* %5)
ret i32 0 }
