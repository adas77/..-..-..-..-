define i32 @foobar(i32 %0, i32 %1, i32 %2) {
%var6 = alloca i32
store i32 %0, i32* %var6
%var7 = alloca i32
store i32 %1, i32* %var7
%var8 = alloca i32
store i32 %2, i32* %var8
%4 = alloca i32
store i32 3721, i32* %4, align 4
%5 = load i32, i32* %4
store i32 %5, i32* @var4
%6 = alloca i8*
%7 = getelementptr inbounds [9 x i8], [9 x i8]* @string_95337, i32 0, i32 0
store i8* %7, i8** %6
%8 = load i8*, i8** %6
%9  = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_string_newline, i32 0, i32 0),i8* %8)
%10 = load i32, i32* @var4
%11 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_int_newline, i32 0, i32 0),i32 %10)
%12 = alloca i32
store i32 67, i32* %12, align 4
%13 = load i32, i32* %12
store i32 %13, i32* %var8
%14 = alloca i8*
%15 = getelementptr inbounds [4 x i8], [4 x i8]* @string_89164, i32 0, i32 0
store i8* %15, i8** %14
%16 = load i8*, i8** %14
%17  = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_string_newline, i32 0, i32 0),i8* %16)
%18 = load i32, i32* %var8
%19 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_int_newline, i32 0, i32 0),i32 %18)
%20 = load i32, i32* %var6
%21 = load i32, i32* %var6
%22 = mul i32 %20, %21
%23 = load i32, i32* %var7
%24 = add i32 %22, %23
store i32 %24, i32* %var6
%25 = load i32, i32* %var6
ret i32 %25
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
@var1 = global %struct.s1 zeroinitializer
@var2 = global i32 0
@var3 = global float 0.0
@var4 = global i32 0
@string_95337 = constant [9 x i8] c"globalna\00"
@string_89164 = constant [4 x i8] c"arg\00"
@var9 = global i32 0
@var10 = global i32 0
@string_89604 = constant [11 x i8] c"arg before\00"
@var11 = global i32 0
@string_66190 = constant [10 x i8] c"arg after\00"
@string_45396 = constant [10 x i8] c"resfoobar\00"
@var12 = global i32 0
@string_89873 = constant [12 x i8] c"dynamic int\00"
@string_72179 = constant [11 x i8] c"now string\00"
@var13 = global i8* null
@string_28660 = constant [15 x i8] c"dynamic string\00"
@var14 = global i32 0
@string_94424 = constant [10 x i8] c"logical a\00"
@var15 = global i32 0
@var16 = global double 0.0
@string_79169 = constant [10 x i8] c"logical a\00"
@var17 = global i32 0
@var18 = global i32 0
@var19 = global i32 0
@string_85319 = constant [11 x i8] c"logical cc\00"
@var20 = global i32 0
@var21 = global i32 0
@string_45160 = constant [4 x i8] c"---\00"
@string_595 = constant [18 x i8] c"Jestem if w while\00"
@var22 = global i32 0
@string_42931 = constant [15 x i8] c"Jestem if w if\00"
@string_83044 = constant [26 x i8] c"Jestem while w if w while\00"
@string_21033 = constant [12 x i8] c"Nie ma mnie\00"
@var23 = global double 0.0
@string_68878 = constant [4 x i8] c"dou\00"
@string_95435 = constant [8 x i8] c"readstr\00"
@var24 = global i8* null
@var25 = global i32 0
@var26 = global float 0.0
@var29 = global i32 0
@var30 = global i32 0

define i32 @main() nounwind {
%1 = alloca i32
store i32 10, i32* %1, align 4
%2 = load i32, i32* %1
%3 = alloca float
store float 0x3fe4937400000000, float* %3, align 4
%4 = load float, float* %3
%5 = getelementptr %struct.s1, %struct.s1* @var1, i32 0, i32 0
store float %4, float* %5
%6 = getelementptr %struct.s1, %struct.s1* @var1, i32 0, i32 1
store i32 %2, i32* %6
%7 = alloca i32
store i32 123, i32* %7, align 4
%8 = load i32, i32* %7
%9 = getelementptr %struct.s1, %struct.s1* @var1, i32 0, i32 1
store i32 %8, i32* %9
%10 = getelementptr %struct.s1, %struct.s1* @var1, i32 0, i32 1
%11 = load i32, i32* %10
store i32 %11, i32* @var2
%12 = getelementptr %struct.s1, %struct.s1* @var1, i32 0, i32 0
%13 = load float, float* %12
store float %13, float* @var3
%14 = load i32, i32* @var2
%15 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_int_newline, i32 0, i32 0),i32 %14)
%16 = load float, float* @var3
%17 = fpext float %16 to double
%18 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_float_newline, i32 0, i32 0),double %17)
%19 = alloca i32
store i32 4, i32* %19, align 4
%20 = load i32, i32* %19
store i32 %20, i32* @var4
%21 = alloca i32
store i32 5, i32* %21, align 4
%22 = load i32, i32* %21
store i32 %22, i32* @var9
%23 = alloca i32
store i32 5, i32* %23, align 4
%24 = load i32, i32* %23
store i32 %24, i32* @var10
%25 = alloca i8*
%26 = getelementptr inbounds [11 x i8], [11 x i8]* @string_89604, i32 0, i32 0
store i8* %26, i8** %25
%27 = load i8*, i8** %25
%28  = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_string_newline, i32 0, i32 0),i8* %27)
%29 = load i32, i32* @var10
%30 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_int_newline, i32 0, i32 0),i32 %29)
%31 = load i32, i32* @var9
%32 = alloca i32
store i32 4, i32* %32, align 4
%33 = load i32, i32* %32
%34 = load i32, i32* @var10
%35 = call i32 @foobar(i32 %31, i32 %33, i32 %34)
store i32 %35, i32* @var11
%36 = alloca i8*
%37 = getelementptr inbounds [10 x i8], [10 x i8]* @string_66190, i32 0, i32 0
store i8* %37, i8** %36
%38 = load i8*, i8** %36
%39  = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_string_newline, i32 0, i32 0),i8* %38)
%40 = load i32, i32* @var10
%41 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_int_newline, i32 0, i32 0),i32 %40)
%42 = alloca i8*
%43 = getelementptr inbounds [10 x i8], [10 x i8]* @string_45396, i32 0, i32 0
store i8* %43, i8** %42
%44 = load i8*, i8** %42
%45  = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_string_newline, i32 0, i32 0),i8* %44)
%46 = load i32, i32* @var11
%47 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_int_newline, i32 0, i32 0),i32 %46)
%48 = alloca i32
store i32 3456, i32* %48, align 4
%49 = load i32, i32* %48
store i32 %49, i32* @var12
%50 = alloca i8*
%51 = getelementptr inbounds [12 x i8], [12 x i8]* @string_89873, i32 0, i32 0
store i8* %51, i8** %50
%52 = load i8*, i8** %50
%53  = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_string_newline, i32 0, i32 0),i8* %52)
%54 = load i32, i32* @var12
%55 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_int_newline, i32 0, i32 0),i32 %54)
%56 = alloca i8*
%57 = getelementptr inbounds [11 x i8], [11 x i8]* @string_72179, i32 0, i32 0
store i8* %57, i8** %56
%58 = load i8*, i8** %56
store i8* %58, i8** @var13
%59 = alloca i8*
%60 = getelementptr inbounds [15 x i8], [15 x i8]* @string_28660, i32 0, i32 0
store i8* %60, i8** %59
%61 = load i8*, i8** %59
%62  = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_string_newline, i32 0, i32 0),i8* %61)
%63 = load i8*, i8** @var13
%64  = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_string_newline, i32 0, i32 0),i8* %63)
%65 = alloca i32
store i32 1, i32* %65, align 4
%66 = load i32, i32* %65
%67 = alloca i32
store i32 0, i32* %67, align 4
%68 = load i32, i32* %67
%69 = and i32 %66, %68
store i32 %69, i32* @var14
%70 = alloca i8*
%71 = getelementptr inbounds [10 x i8], [10 x i8]* @string_94424, i32 0, i32 0
store i8* %71, i8** %70
%72 = load i8*, i8** %70
%73  = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_string_newline, i32 0, i32 0),i8* %72)
%74 = load i32, i32* @var14
%75 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_int_newline, i32 0, i32 0),i32 %74)
%76 = load i32, i32* @var14
%77 = alloca i32
store i32 2, i32* %77, align 4
%78 = load i32, i32* %77
%79 = alloca i32
store i32 4, i32* %79, align 4
%80 = load i32, i32* %79
%81 = alloca i32
store i32 6, i32* %81, align 4
%82 = load i32, i32* %81
%83 = alloca i32
store i32 1, i32* %83, align 4
%84 = load i32, i32* %83
%85 = sub i32 %82, %84
%86 = add i32 %80, %85
%87 = add i32 %78, %86
%88 = add i32 %76, %87
store i32 %88, i32* @var15
%89 = alloca double
store double 0x3ff0000000000000, double* %89, align 4
%90 = load double, double* %89
%91 = alloca double
store double 0x4000020c49ba5e35, double* %91, align 4
%92 = load double, double* %91
%93 = fsub double %90, %92
store double %93, double* @var16
%94 = load i32, i32* @var15
%95 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_int_newline, i32 0, i32 0),i32 %94)
%96 = load double, double* @var16
%97 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([5 x i8], [5 x i8]* @str_double_newline, i32 0, i32 0),double %96)
%98 = alloca i32
store i32 1, i32* %98, align 4
%99 = load i32, i32* %98
%100 = alloca i32
store i32 0, i32* %100, align 4
%101 = load i32, i32* %100
%102 = or i32 %99, %101
store i32 %102, i32* @var14
%103 = alloca i8*
%104 = getelementptr inbounds [10 x i8], [10 x i8]* @string_79169, i32 0, i32 0
store i8* %104, i8** %103
%105 = load i8*, i8** %103
%106  = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_string_newline, i32 0, i32 0),i8* %105)
%107 = load i32, i32* @var14
%108 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_int_newline, i32 0, i32 0),i32 %107)
%109 = alloca i32
store i32 11, i32* %109, align 4
%110 = load i32, i32* %109
store i32 %110, i32* @var17
%111 = alloca i32
store i32 21, i32* %111, align 4
%112 = load i32, i32* %111
store i32 %112, i32* @var18
%113 = load i32, i32* @var17
%114 = load i32, i32* @var18
%115 = and i32 %113, %114
store i32 %115, i32* @var19
%116 = alloca i8*
%117 = getelementptr inbounds [11 x i8], [11 x i8]* @string_85319, i32 0, i32 0
store i8* %117, i8** %116
%118 = load i8*, i8** %116
%119  = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_string_newline, i32 0, i32 0),i8* %118)
%120 = load i32, i32* @var19
%121 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_int_newline, i32 0, i32 0),i32 %120)
%122 = alloca i32
store i32 10, i32* %122, align 4
%123 = load i32, i32* %122
store i32 %123, i32* @var20
br label %while1
while1:
%124 = load i32, i32* @var20
%125 = alloca i32
store i32 2, i32* %125, align 4
%126 = load i32, i32* %125
%127 = add i32 %124, %126
%128 = icmp ne i32 %127, 0
br i1 %128, label %while_body1, label %elihw1
while_body1:
%129 = load i32, i32* @var20
%130 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_int_newline, i32 0, i32 0),i32 %129)
%131 = load i32, i32* @var20
%132 = alloca i32
store i32 2, i32* %132, align 4
%133 = load i32, i32* %132
%134 = sub i32 %131, %133
store i32 %134, i32* @var20
%135 = alloca i32
store i32 3, i32* %135, align 4
%136 = load i32, i32* %135
store i32 %136, i32* @var21
%137 = load i32, i32* @var20
%138 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_int_newline, i32 0, i32 0),i32 %137)
%139 = alloca i8*
%140 = getelementptr inbounds [4 x i8], [4 x i8]* @string_45160, i32 0, i32 0
store i8* %140, i8** %139
%141 = load i8*, i8** %139
%142  = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_string_newline, i32 0, i32 0),i8* %141)
%143 = alloca i32
store i32 1, i32* %143, align 4
%144 = load i32, i32* %143
%145 = icmp ne i32 %144, 0
br i1 %145, label %if1, label %fi1
if1:
%146 = alloca i8*
%147 = getelementptr inbounds [18 x i8], [18 x i8]* @string_595, i32 0, i32 0
store i8* %147, i8** %146
%148 = load i8*, i8** %146
%149  = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_string_newline, i32 0, i32 0),i8* %148)
%150 = alloca i32
store i32 5, i32* %150, align 4
%151 = load i32, i32* %150
store i32 %151, i32* @var22
%152 = alloca i32
store i32 1, i32* %152, align 4
%153 = load i32, i32* %152
%154 = icmp ne i32 %153, 0
br i1 %154, label %if2, label %fi2
if2:
%155 = alloca i8*
%156 = getelementptr inbounds [15 x i8], [15 x i8]* @string_42931, i32 0, i32 0
store i8* %156, i8** %155
%157 = load i8*, i8** %155
%158  = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_string_newline, i32 0, i32 0),i8* %157)
br label %fi2
fi2:
br label %while2
while2:
%159 = load i32, i32* @var22
%160 = icmp ne i32 %159, 0
br i1 %160, label %while_body2, label %elihw2
while_body2:
%161 = alloca i8*
%162 = getelementptr inbounds [26 x i8], [26 x i8]* @string_83044, i32 0, i32 0
store i8* %162, i8** %161
%163 = load i8*, i8** %161
%164  = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_string_newline, i32 0, i32 0),i8* %163)
%165 = load i32, i32* @var22
%166 = alloca i32
store i32 1, i32* %166, align 4
%167 = load i32, i32* %166
%168 = sub i32 %165, %167
store i32 %168, i32* @var22
br label %while2
elihw2:
br label %fi1
fi1:
br label %while1
elihw1:
br label %while3
while3:
%169 = alloca i32
store i32 0, i32* %169, align 4
%170 = load i32, i32* %169
%171 = icmp ne i32 %170, 0
br i1 %171, label %while_body3, label %elihw3
while_body3:
%172 = alloca i8*
%173 = getelementptr inbounds [12 x i8], [12 x i8]* @string_21033, i32 0, i32 0
store i8* %173, i8** %172
%174 = load i8*, i8** %172
%175  = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_string_newline, i32 0, i32 0),i8* %174)
br label %while3
elihw3:
%176 = alloca double
store double 0x3f50624dd2f1a9fc, double* %176, align 4
%177 = load double, double* %176
%178 = alloca double
store double 0x3ff0000000000000, double* %178, align 4
%179 = load double, double* %178
%180 = fadd double %177, %179
%181 = alloca double
store double 0x40091eb851eb851f, double* %181, align 4
%182 = load double, double* %181
%183 = fdiv double %180, %182
store double %183, double* @var23
%184 = alloca i8*
%185 = getelementptr inbounds [4 x i8], [4 x i8]* @string_68878, i32 0, i32 0
store i8* %185, i8** %184
%186 = load i8*, i8** %184
%187  = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_string_newline, i32 0, i32 0),i8* %186)
%188 = load double, double* @var23
%189 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([5 x i8], [5 x i8]* @str_double_newline, i32 0, i32 0),double %188)
%190 = alloca i8*
%191 = getelementptr inbounds [8 x i8], [8 x i8]* @string_95435, i32 0, i32 0
store i8* %191, i8** %190
%192 = load i8*, i8** %190
store i8* %192, i8** @var24
%193 = alloca i32
store i32 56, i32* %193, align 4
%194 = load i32, i32* %193
store i32 %194, i32* @var25
%195 = alloca float
store float 0x0000000000000000, float* %195, align 4
%196 = load float, float* %195
store float %196, float* @var26
%197 = alloca i8, i32 100
%198 = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @str_string, i32 0, i32 0),i8* %197)
store i8* %197, i8** @var24
%199 = load i8*, i8** @var24
%200  = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_string_newline, i32 0, i32 0),i8* %199)
%201 = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @str_int, i32 0, i32 0),i32* @var25)
%202 = load i32, i32* @var25
%203 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_int_newline, i32 0, i32 0),i32 %202)
%204 = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @str_float, i32 0, i32 0),float* @var26)
%205 = load float, float* @var26
%206 = fpext float %205 to double
%207 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_float_newline, i32 0, i32 0),double %206)
%arr = alloca [6 x i32], align 8
%arr2 = alloca [2 x i32], align 8
%208 = alloca i32
store i32 1, i32* %208, align 4
%209 = load i32, i32* %208
%210 = alloca i32
store i32 309, i32* %210, align 4
%211 = load i32, i32* %210
%212 = getelementptr [2 x i32], [2 x i32]* %arr2, i32 0, i32 1
store i32 309, i32* %212
%213 = alloca i32
store i32 0, i32* %213, align 4
%214 = load i32, i32* %213
%215 = alloca i32
store i32 0, i32* %215, align 4
%216 = load i32, i32* %215
%217 = alloca i32
store i32 0, i32* %217, align 4
%218 = load i32, i32* %217
%219 = getelementptr [6 x i32], [6 x i32]* %arr, i32 0, i32 0
store i32 0, i32* %219
%220 = alloca i32
store i32 0, i32* %220, align 4
%221 = load i32, i32* %220
%222 = alloca i32
store i32 1, i32* %222, align 4
%223 = load i32, i32* %222
%224 = alloca i32
store i32 0, i32* %224, align 4
%225 = load i32, i32* %224
%226 = getelementptr [6 x i32], [6 x i32]* %arr, i32 0, i32 1
store i32 0, i32* %226
%227 = alloca i32
store i32 0, i32* %227, align 4
%228 = load i32, i32* %227
%229 = alloca i32
store i32 2, i32* %229, align 4
%230 = load i32, i32* %229
%231 = alloca i32
store i32 0, i32* %231, align 4
%232 = load i32, i32* %231
%233 = getelementptr [6 x i32], [6 x i32]* %arr, i32 0, i32 2
store i32 0, i32* %233
%234 = alloca i32
store i32 1, i32* %234, align 4
%235 = load i32, i32* %234
%236 = alloca i32
store i32 0, i32* %236, align 4
%237 = load i32, i32* %236
%238 = alloca i32
store i32 0, i32* %238, align 4
%239 = load i32, i32* %238
%240 = getelementptr [6 x i32], [6 x i32]* %arr, i32 0, i32 3
store i32 0, i32* %240
%241 = alloca i32
store i32 1, i32* %241, align 4
%242 = load i32, i32* %241
%243 = alloca i32
store i32 1, i32* %243, align 4
%244 = load i32, i32* %243
%245 = alloca i32
store i32 30, i32* %245, align 4
%246 = load i32, i32* %245
%247 = getelementptr [6 x i32], [6 x i32]* %arr, i32 0, i32 4
store i32 30, i32* %247
%248 = alloca i32
store i32 1, i32* %248, align 4
%249 = load i32, i32* %248
%250 = alloca i32
store i32 2, i32* %250, align 4
%251 = load i32, i32* %250
%252 = alloca i32
store i32 0, i32* %252, align 4
%253 = load i32, i32* %252
%254 = getelementptr [6 x i32], [6 x i32]* %arr, i32 0, i32 5
store i32 0, i32* %254
%255 = alloca i32
store i32 1, i32* %255, align 4
%256 = load i32, i32* %255
%257 = alloca i32
store i32 1, i32* %257, align 4
%258 = load i32, i32* %257
%259 = getelementptr [6 x i32], [6 x i32]* %arr, i32 0, i32 4
%260 = load i32, i32* %259
store i32 %260, i32* @var29
%261 = alloca i32
store i32 1, i32* %261, align 4
%262 = load i32, i32* %261
%263 = getelementptr [2 x i32], [2 x i32]* %arr2, i32 0, i32 1
%264 = load i32, i32* %263
store i32 %264, i32* @var30
%265 = load i32, i32* @var29
%266 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_int_newline, i32 0, i32 0),i32 %265)
%267 = load i32, i32* @var30
%268 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_int_newline, i32 0, i32 0),i32 %267)

ret i32 0 }