declare i32 @printf(i8*, ...)
@str_int_newline = constant [4 x i8] c"%d\0A\00"

define i32 @add(i32 %a, i32 %b, i32* %c) {
entry:
    %aa = alloca i32
    store i32 10, i32* %aa
    %bb = alloca i32
    store i32 20, i32* %bb

    %val_a = load i32, i32* %aa
    %val_b = load i32, i32* %bb

    store i32 6789, i32* %c

    %sum = add i32 %val_a, %val_b
    ret i32 %sum
}


define i32 @main() {
entry:
    %a = alloca i32
    store i32 10, i32* %a
    %b = alloca i32
    store i32 22, i32* %b

    %c = alloca i32
    store i32 220, i32* %c


    %val_a = load i32, i32* %a
    %val_b = load i32, i32* %b


    %result = call i32 @add(i32 %val_a, i32 %val_b, i32* %c)
    %0 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_int_newline, i32 0, i32 0),i32 %result)

    %1 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_int_newline, i32 0, i32 0),i32 %val_a)
    %2 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_int_newline, i32 0, i32 0),i32 %val_b)
    %val_c = load i32, i32* %c

    %3 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_int_newline, i32 0, i32 0),i32 %val_c)
    ret i32 0
}
