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
store i32 1, i32* %i
%arr = alloca [3 x double], align 8
%arrr = alloca [6 x i32], align 8
%1 = getelementptr inbounds [6 x i32], [6 x i32]* %arrr, i32 0, i32 2
store i32 11, i32* %1
%2 = getelementptr inbounds [6 x i32], [6 x i32]* %arrr, i32 0, i32 2
%3 = load i32, i32* %2
%4 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strp, i32 0, i32 0), i32 %3)
%5 = getelementptr inbounds [6 x i32], [6 x i32]* %arrr, i32 0, i32 5
%6 = load i32, i32* %5
%7 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strp, i32 0, i32 0), i32 %6)
%8 = getelementptr inbounds [3 x double], [3 x double]* %arr, i32 0, i32 1
store double 4.20691, double* %8
%9 = getelementptr inbounds [3 x double], [3 x double]* %arr, i32 0, i32 1
%10 = load double, double* %9
%11 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strf, i32 0, i32 0), double %10)
%12 = getelementptr inbounds [3 x double], [3 x double]* %arr, i32 0, i32 2
%13 = load double, double* %12
%14 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strf, i32 0, i32 0), double %13)
store i32 2137, i32* %i
store double 0x40091eb851eb851f, double* %f, align 4
store double 0x4010cccccccccccd, double* %f, align 4
store double 0x4010ccccd382c973, double* %f, align 4
%15 = load i32, i32* %i
%16 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strp, i32 0, i32 0), i32 %15)
%17 = load double, double* %f
%18 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strf, i32 0, i32 0), double %17)
%19 = getelementptr inbounds [12 x i8], [12 x i8]* @s, i32 0, i32 0
%20 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strstr, i32 0, i32 0), i8* %19)
ret i32 0 }
