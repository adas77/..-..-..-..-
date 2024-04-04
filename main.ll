target triple = "x86_64-pc-linux-gnu"

@pfmt = constant [4 x i8] c"%d\0A\00"
declare i32 @printf(i8*,...)

; LLVM IR code demonstrating basic variable operations

; Define a function named main that takes no arguments and returns an integer
define i32 @main() {
  ; Declare variables
  %a = alloca i32
  %b = alloca i32
  %result = alloca i32
  
  ; Store integer values into variables
  store i32 10, i32* %a
  store i32 20, i32* %b
  
  ; Load values from variables
  %val_a = load i32, i32* %a
  %val_b = load i32, i32* %b
  
  ; Perform arithmetic operations
  %sum = add i32 %val_a, %val_b
  %sub = sub i32 %val_a, %val_b
  %mul = mul i32 %val_a, %val_b
  %div = sdiv i32 %val_a, %val_b
  
  ; Store results into result variable
  store i32 %sum, i32* %result
  
  call i32(i8*,...) @printf(i8* getelementptr([4 x i8], [4 x i8]* @pfmt, i32 0, i32 0), i32 %sum)
  call i32(i8*,...) @printf(i8* getelementptr([4 x i8], [4 x i8]* @pfmt, i32 0, i32 0), i32 %sub)
  call i32(i8*,...) @printf(i8* getelementptr([4 x i8], [4 x i8]* @pfmt, i32 0, i32 0), i32 %mul)
  call i32(i8*,...) @printf(i8* getelementptr([4 x i8], [4 x i8]* @pfmt, i32 0, i32 0), i32 %div)
  
  call i32(i8*,...) @printf(i8* getelementptr([4 x i8], [4 x i8]* @pfmt, i32 0, i32 0), i32 %div)
  call i32(i8*,...) @printf(i8* getelementptr([4 x i8], [4 x i8]* @pfmt, i32 0, i32 0), i32 %div)
  call i32(i8*,...) @printf(i8* getelementptr([4 x i8], [4 x i8]* @pfmt, i32 0, i32 0), i32 %div)

  ; Return the result
  ret i32 %sum
}