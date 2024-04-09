declare i32 @printf(i8*, ...)
declare i32 @__isoc99_scanf(i8*, ...)
@strp = constant [4 x i8] c"%d\0A\00"
@strf = constant [4 x i8] c"%f\0A\00"
@strs = constant [3 x i8] c"%d\00"
@strstr = constant [4 x i8] c"%s\0A\00"
@s = constant [12 x i8] c"Hello world\00"
define i32 @main() nounwind{
%i = alloca i32
%f = alloca double
store i32 2137, i32* %i
store double 0x40091eb851eb851f, double* %f, align 4
store double 0x4010cccccccccccd, double* %f, align 4
store double 0x4010ccccd382c973, double* %f, align 4
%1 = load i32, i32* %i
%2 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strp, i32 0, i32 0), i32 %1)
%3 = load double, double* %f
%4 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strf, i32 0, i32 0), double %3)
%5 = getelementptr inbounds [12 x i8], [12 x i8]* @s, i32 0, i32 0
%6 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strstr, i32 0, i32 0), i8* %5)
ret i32 0 }
