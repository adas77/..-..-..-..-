define i32 @foobar(i32 %0, i32 %1, i32 %2) {
%var5 = alloca i32
store i32 %0, i32* %var5
%var6 = alloca i32
store i32 %1, i32* %var6
%var7 = alloca i32
store i32 %2, i32* %var7
%4 = alloca i32
store i32 67, i32* %4, align 4
%5 = load i32, i32* %4
store i32 %5, i32* %var7
%6 = load i32, i32* %var7
%7 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_int_newline, i32 0, i32 0),i32 %6)
%8 = load i32, i32* %var5
%9 = load i32, i32* %var5
%10 = mul i32 %8, %9
%11 = load i32, i32* %var6
%12 = add i32 %10, %11
store i32 %12, i32* %var5
%13 = load i32, i32* %var5
ret i32 %13
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
@var8 = global i32 0
@var9 = global i32 0
@string_1 = constant [11 x i8] c"arg before\00"
@var10 = global i32 0
@string_2 = constant [10 x i8] c"arg after\00"
@string_3 = constant [10 x i8] c"resfoobar\00"
@var11 = global i32 0
@string_4 = constant [12 x i8] c"dynamic int\00"
@string_5 = constant [11 x i8] c"now string\00"
@var12 = global i8* null
@string_6 = constant [15 x i8] c"dynamic string\00"
@var13 = global i32 0
@string_7 = constant [10 x i8] c"logical a\00"
@var14 = global i32 0
@var15 = global double 0.0
@string_8 = constant [10 x i8] c"logical a\00"
@var16 = global i32 0
@var17 = global i32 0
@var18 = global i32 0
@string_9 = constant [11 x i8] c"logical cc\00"
@var19 = global i32 0
@var20 = global i32 0
@string_10 = constant [4 x i8] c"---\00"
@string_11 = constant [18 x i8] c"Jestem if w while\00"
@var21 = global i32 0
@string_12 = constant [15 x i8] c"Jestem if w if\00"
@string_13 = constant [26 x i8] c"Jestem while w if w while\00"
@string_14 = constant [12 x i8] c"Nie ma mnie\00"
@var22 = global double 0.0
@string_15 = constant [4 x i8] c"dou\00"
@string_16 = constant [8 x i8] c"readstr\00"
@var23 = global i8* null
@var24 = global i32 0
@var25 = global float 0.0
@var28 = global i32 0
@var29 = global i32 0

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
store i32 5, i32* %19, align 4
%20 = load i32, i32* %19
store i32 %20, i32* @var8
%21 = alloca i32
store i32 5, i32* %21, align 4
%22 = load i32, i32* %21
store i32 %22, i32* @var9
%23 = alloca i8*
%24 = getelementptr inbounds [11 x i8], [11 x i8]* @string_1, i32 0, i32 0
store i8* %24, i8** %23
%25 = load i8*, i8** %23
%26  = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_string_newline, i32 0, i32 0),i8* %25)
%27 = load i32, i32* @var9
%28 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_int_newline, i32 0, i32 0),i32 %27)
%29 = load i32, i32* @var8
%30 = alloca i32
store i32 4, i32* %30, align 4
%31 = load i32, i32* %30
%32 = load i32, i32* @var9
%33 = call i32 @foobar(i32 %29, i32 %31, i32 %32)
store i32 %33, i32* @var10
%34 = alloca i8*
%35 = getelementptr inbounds [10 x i8], [10 x i8]* @string_2, i32 0, i32 0
store i8* %35, i8** %34
%36 = load i8*, i8** %34
%37  = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_string_newline, i32 0, i32 0),i8* %36)
%38 = load i32, i32* @var9
%39 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_int_newline, i32 0, i32 0),i32 %38)
%40 = alloca i8*
%41 = getelementptr inbounds [10 x i8], [10 x i8]* @string_3, i32 0, i32 0
store i8* %41, i8** %40
%42 = load i8*, i8** %40
%43  = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_string_newline, i32 0, i32 0),i8* %42)
%44 = load i32, i32* @var10
%45 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_int_newline, i32 0, i32 0),i32 %44)
%46 = alloca i32
store i32 3456, i32* %46, align 4
%47 = load i32, i32* %46
store i32 %47, i32* @var11
%48 = alloca i8*
%49 = getelementptr inbounds [12 x i8], [12 x i8]* @string_4, i32 0, i32 0
store i8* %49, i8** %48
%50 = load i8*, i8** %48
%51  = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_string_newline, i32 0, i32 0),i8* %50)
%52 = load i32, i32* @var11
%53 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_int_newline, i32 0, i32 0),i32 %52)
%54 = alloca i8*
%55 = getelementptr inbounds [11 x i8], [11 x i8]* @string_5, i32 0, i32 0
store i8* %55, i8** %54
%56 = load i8*, i8** %54
store i8* %56, i8** @var12
%57 = alloca i8*
%58 = getelementptr inbounds [15 x i8], [15 x i8]* @string_6, i32 0, i32 0
store i8* %58, i8** %57
%59 = load i8*, i8** %57
%60  = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_string_newline, i32 0, i32 0),i8* %59)
%61 = load i8*, i8** @var12
%62  = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_string_newline, i32 0, i32 0),i8* %61)
%63 = alloca i32
store i32 1, i32* %63, align 4
%64 = load i32, i32* %63
%65 = alloca i32
store i32 0, i32* %65, align 4
%66 = load i32, i32* %65
%67 = and i32 %64, %66
store i32 %67, i32* @var13
%68 = alloca i8*
%69 = getelementptr inbounds [10 x i8], [10 x i8]* @string_7, i32 0, i32 0
store i8* %69, i8** %68
%70 = load i8*, i8** %68
%71  = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_string_newline, i32 0, i32 0),i8* %70)
%72 = load i32, i32* @var13
%73 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_int_newline, i32 0, i32 0),i32 %72)
%74 = load i32, i32* @var13
%75 = alloca i32
store i32 2, i32* %75, align 4
%76 = load i32, i32* %75
%77 = alloca i32
store i32 4, i32* %77, align 4
%78 = load i32, i32* %77
%79 = alloca i32
store i32 6, i32* %79, align 4
%80 = load i32, i32* %79
%81 = alloca i32
store i32 1, i32* %81, align 4
%82 = load i32, i32* %81
%83 = sub i32 %80, %82
%84 = add i32 %78, %83
%85 = add i32 %76, %84
%86 = add i32 %74, %85
store i32 %86, i32* @var14
%87 = alloca double
store double 0x3ff0000000000000, double* %87, align 4
%88 = load double, double* %87
%89 = alloca double
store double 0x4000020c49ba5e35, double* %89, align 4
%90 = load double, double* %89
%91 = fsub double %88, %90
store double %91, double* @var15
%92 = load i32, i32* @var14
%93 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_int_newline, i32 0, i32 0),i32 %92)
%94 = load double, double* @var15
%95 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([5 x i8], [5 x i8]* @str_double_newline, i32 0, i32 0),double %94)
%96 = alloca i32
store i32 1, i32* %96, align 4
%97 = load i32, i32* %96
%98 = alloca i32
store i32 0, i32* %98, align 4
%99 = load i32, i32* %98
%100 = or i32 %97, %99
store i32 %100, i32* @var13
%101 = alloca i8*
%102 = getelementptr inbounds [10 x i8], [10 x i8]* @string_8, i32 0, i32 0
store i8* %102, i8** %101
%103 = load i8*, i8** %101
%104  = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_string_newline, i32 0, i32 0),i8* %103)
%105 = load i32, i32* @var13
%106 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_int_newline, i32 0, i32 0),i32 %105)
%107 = alloca i32
store i32 11, i32* %107, align 4
%108 = load i32, i32* %107
store i32 %108, i32* @var16
%109 = alloca i32
store i32 21, i32* %109, align 4
%110 = load i32, i32* %109
store i32 %110, i32* @var17
%111 = load i32, i32* @var16
%112 = load i32, i32* @var17
%113 = and i32 %111, %112
store i32 %113, i32* @var18
%114 = alloca i8*
%115 = getelementptr inbounds [11 x i8], [11 x i8]* @string_9, i32 0, i32 0
store i8* %115, i8** %114
%116 = load i8*, i8** %114
%117  = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_string_newline, i32 0, i32 0),i8* %116)
%118 = load i32, i32* @var18
%119 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_int_newline, i32 0, i32 0),i32 %118)
%120 = alloca i32
store i32 10, i32* %120, align 4
%121 = load i32, i32* %120
store i32 %121, i32* @var19
br label %while1
while1:
%122 = load i32, i32* @var19
%123 = alloca i32
store i32 2, i32* %123, align 4
%124 = load i32, i32* %123
%125 = add i32 %122, %124
%126 = icmp ne i32 %125, 0
br i1 %126, label %while_body1, label %elihw1
while_body1:
%127 = load i32, i32* @var19
%128 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_int_newline, i32 0, i32 0),i32 %127)
%129 = load i32, i32* @var19
%130 = alloca i32
store i32 2, i32* %130, align 4
%131 = load i32, i32* %130
%132 = sub i32 %129, %131
store i32 %132, i32* @var19
%133 = alloca i32
store i32 3, i32* %133, align 4
%134 = load i32, i32* %133
store i32 %134, i32* @var20
%135 = load i32, i32* @var19
%136 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_int_newline, i32 0, i32 0),i32 %135)
%137 = alloca i8*
%138 = getelementptr inbounds [4 x i8], [4 x i8]* @string_10, i32 0, i32 0
store i8* %138, i8** %137
%139 = load i8*, i8** %137
%140  = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_string_newline, i32 0, i32 0),i8* %139)
%141 = alloca i32
store i32 1, i32* %141, align 4
%142 = load i32, i32* %141
%143 = icmp ne i32 %142, 0
br i1 %143, label %if1, label %fi1
if1:
%144 = alloca i8*
%145 = getelementptr inbounds [18 x i8], [18 x i8]* @string_11, i32 0, i32 0
store i8* %145, i8** %144
%146 = load i8*, i8** %144
%147  = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_string_newline, i32 0, i32 0),i8* %146)
%148 = alloca i32
store i32 5, i32* %148, align 4
%149 = load i32, i32* %148
store i32 %149, i32* @var21
%150 = alloca i32
store i32 1, i32* %150, align 4
%151 = load i32, i32* %150
%152 = icmp ne i32 %151, 0
br i1 %152, label %if2, label %fi2
if2:
%153 = alloca i8*
%154 = getelementptr inbounds [15 x i8], [15 x i8]* @string_12, i32 0, i32 0
store i8* %154, i8** %153
%155 = load i8*, i8** %153
%156  = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_string_newline, i32 0, i32 0),i8* %155)
br label %fi2
fi2:
br label %while2
while2:
%157 = load i32, i32* @var21
%158 = icmp ne i32 %157, 0
br i1 %158, label %while_body2, label %elihw2
while_body2:
%159 = alloca i8*
%160 = getelementptr inbounds [26 x i8], [26 x i8]* @string_13, i32 0, i32 0
store i8* %160, i8** %159
%161 = load i8*, i8** %159
%162  = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_string_newline, i32 0, i32 0),i8* %161)
%163 = load i32, i32* @var21
%164 = alloca i32
store i32 1, i32* %164, align 4
%165 = load i32, i32* %164
%166 = sub i32 %163, %165
store i32 %166, i32* @var21
br label %while2
elihw2:
br label %fi1
fi1:
br label %while1
elihw1:
br label %while3
while3:
%167 = alloca i32
store i32 0, i32* %167, align 4
%168 = load i32, i32* %167
%169 = icmp ne i32 %168, 0
br i1 %169, label %while_body3, label %elihw3
while_body3:
%170 = alloca i8*
%171 = getelementptr inbounds [12 x i8], [12 x i8]* @string_14, i32 0, i32 0
store i8* %171, i8** %170
%172 = load i8*, i8** %170
%173  = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_string_newline, i32 0, i32 0),i8* %172)
br label %while3
elihw3:
%174 = alloca double
store double 0x3f50624dd2f1a9fc, double* %174, align 4
%175 = load double, double* %174
%176 = alloca double
store double 0x3ff0000000000000, double* %176, align 4
%177 = load double, double* %176
%178 = fadd double %175, %177
%179 = alloca double
store double 0x40091eb851eb851f, double* %179, align 4
%180 = load double, double* %179
%181 = fdiv double %178, %180
store double %181, double* @var22
%182 = alloca i8*
%183 = getelementptr inbounds [4 x i8], [4 x i8]* @string_15, i32 0, i32 0
store i8* %183, i8** %182
%184 = load i8*, i8** %182
%185  = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_string_newline, i32 0, i32 0),i8* %184)
%186 = load double, double* @var22
%187 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([5 x i8], [5 x i8]* @str_double_newline, i32 0, i32 0),double %186)
%188 = alloca i8*
%189 = getelementptr inbounds [8 x i8], [8 x i8]* @string_16, i32 0, i32 0
store i8* %189, i8** %188
%190 = load i8*, i8** %188
store i8* %190, i8** @var23
%191 = alloca i32
store i32 56, i32* %191, align 4
%192 = load i32, i32* %191
store i32 %192, i32* @var24
%193 = alloca float
store float 0x0000000000000000, float* %193, align 4
%194 = load float, float* %193
store float %194, float* @var25
%195 = alloca i8, i32 100
%196 = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @str_string, i32 0, i32 0),i8* %195)
store i8* %195, i8** @var23
%197 = load i8*, i8** @var23
%198  = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_string_newline, i32 0, i32 0),i8* %197)
%199 = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @str_int, i32 0, i32 0),i32* @var24)
%200 = load i32, i32* @var24
%201 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_int_newline, i32 0, i32 0),i32 %200)
%202 = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @str_float, i32 0, i32 0),float* @var25)
%203 = load float, float* @var25
%204 = fpext float %203 to double
%205 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_float_newline, i32 0, i32 0),double %204)
%arr = alloca [6 x i32], align 8
%arr2 = alloca [2 x i32], align 8
%206 = alloca i32
store i32 1, i32* %206, align 4
%207 = load i32, i32* %206
%208 = alloca i32
store i32 309, i32* %208, align 4
%209 = load i32, i32* %208
%210 = getelementptr [2 x i32], [2 x i32]* %arr2, i32 0, i32 1
store i32 309, i32* %210
%211 = alloca i32
store i32 0, i32* %211, align 4
%212 = load i32, i32* %211
%213 = alloca i32
store i32 0, i32* %213, align 4
%214 = load i32, i32* %213
%215 = alloca i32
store i32 0, i32* %215, align 4
%216 = load i32, i32* %215
%217 = getelementptr [6 x i32], [6 x i32]* %arr, i32 0, i32 0
store i32 0, i32* %217
%218 = alloca i32
store i32 0, i32* %218, align 4
%219 = load i32, i32* %218
%220 = alloca i32
store i32 1, i32* %220, align 4
%221 = load i32, i32* %220
%222 = alloca i32
store i32 0, i32* %222, align 4
%223 = load i32, i32* %222
%224 = getelementptr [6 x i32], [6 x i32]* %arr, i32 0, i32 1
store i32 0, i32* %224
%225 = alloca i32
store i32 0, i32* %225, align 4
%226 = load i32, i32* %225
%227 = alloca i32
store i32 2, i32* %227, align 4
%228 = load i32, i32* %227
%229 = alloca i32
store i32 0, i32* %229, align 4
%230 = load i32, i32* %229
%231 = getelementptr [6 x i32], [6 x i32]* %arr, i32 0, i32 2
store i32 0, i32* %231
%232 = alloca i32
store i32 1, i32* %232, align 4
%233 = load i32, i32* %232
%234 = alloca i32
store i32 0, i32* %234, align 4
%235 = load i32, i32* %234
%236 = alloca i32
store i32 0, i32* %236, align 4
%237 = load i32, i32* %236
%238 = getelementptr [6 x i32], [6 x i32]* %arr, i32 0, i32 3
store i32 0, i32* %238
%239 = alloca i32
store i32 1, i32* %239, align 4
%240 = load i32, i32* %239
%241 = alloca i32
store i32 1, i32* %241, align 4
%242 = load i32, i32* %241
%243 = alloca i32
store i32 30, i32* %243, align 4
%244 = load i32, i32* %243
%245 = getelementptr [6 x i32], [6 x i32]* %arr, i32 0, i32 4
store i32 30, i32* %245
%246 = alloca i32
store i32 1, i32* %246, align 4
%247 = load i32, i32* %246
%248 = alloca i32
store i32 2, i32* %248, align 4
%249 = load i32, i32* %248
%250 = alloca i32
store i32 0, i32* %250, align 4
%251 = load i32, i32* %250
%252 = getelementptr [6 x i32], [6 x i32]* %arr, i32 0, i32 5
store i32 0, i32* %252
%253 = alloca i32
store i32 1, i32* %253, align 4
%254 = load i32, i32* %253
%255 = alloca i32
store i32 1, i32* %255, align 4
%256 = load i32, i32* %255
%257 = getelementptr [6 x i32], [6 x i32]* %arr, i32 0, i32 4
%258 = load i32, i32* %257
store i32 %258, i32* @var28
%259 = alloca i32
store i32 1, i32* %259, align 4
%260 = load i32, i32* %259
%261 = getelementptr [2 x i32], [2 x i32]* %arr2, i32 0, i32 1
%262 = load i32, i32* %261
store i32 %262, i32* @var29
%263 = load i32, i32* @var28
%264 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_int_newline, i32 0, i32 0),i32 %263)
%265 = load i32, i32* @var29
%266 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_int_newline, i32 0, i32 0),i32 %265)

ret i32 0 }