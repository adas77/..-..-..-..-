declare i32 @printf(i8*, ...)
declare i32 @__isoc99_scanf(i8*, ...)
@strp = constant [4 x i8] c"%d\0A\00"

define void @main() {
    %arrayPtr = alloca [10 x i32], align 8


    %elementPtr2 = getelementptr inbounds [10 x i32], [10 x i32]* %arrayPtr, i32 0, i32 2
    store i32 619, i32* %elementPtr2



    %elementPtr = getelementptr inbounds [10 x i32], [10 x i32]* %arrayPtr, i32 0, i32 2
    %value = load i32, i32* %elementPtr

    %1 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strp, i32 0, i32 0), i32 %value)
    ret void
}


