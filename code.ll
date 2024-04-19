define i32 @foobar(i32 %0, i32 %1, i32 %2) {
%var8 = alloca i32
store i32 %0, i32* %var8
%var9 = alloca i32
store i32 %1, i32* %var9
%var10 = alloca i32
store i32 %2, i32* %var10
%4 = alloca i32
store i32 3721, i32* %4, align 4
%5 = load i32, i32* %4
store i32 %5, i32* @var6
%6 = alloca i8*
%7 = getelementptr inbounds [9 x i8], [9 x i8]* @string_33619, i32 0, i32 0
store i8* %7, i8** %6
%8 = load i8*, i8** %6
%9  = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_string_newline, i32 0, i32 0),i8* %8)
%10 = load i32, i32* @var6
%11 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_int_newline, i32 0, i32 0),i32 %10)
%12 = alloca i32
store i32 67, i32* %12, align 4
%13 = load i32, i32* %12
store i32 %13, i32* %var10
%14 = alloca i8*
%15 = getelementptr inbounds [4 x i8], [4 x i8]* @string_11102, i32 0, i32 0
store i8* %15, i8** %14
%16 = load i8*, i8** %14
%17  = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_string_newline, i32 0, i32 0),i8* %16)
%18 = load i32, i32* %var10
%19 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_int_newline, i32 0, i32 0),i32 %18)
%20 = load i32, i32* %var8
%21 = load i32, i32* %var8
%22 = mul i32 %20, %21
%23 = load i32, i32* %var9
%24 = add i32 %22, %23
store i32 %24, i32* %var8
%25 = load i32, i32* %var8
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
@genrator_it_442 = global i32 0
@var2 = global i32 0
%struct.s1 = type { float, i32 }
@var3 = global %struct.s1 zeroinitializer
@var4 = global i32 0
@var5 = global float 0.0
@var6 = global i32 0
@string_33619 = constant [9 x i8] c"globalna\00"
@string_11102 = constant [4 x i8] c"arg\00"
@var11 = global i32 0
@var12 = global i32 0
@string_20 = constant [11 x i8] c"arg before\00"
@var13 = global i32 0
@string_23288 = constant [10 x i8] c"arg after\00"
@string_542 = constant [10 x i8] c"resfoobar\00"
@var14 = global i32 0
@string_56756 = constant [12 x i8] c"dynamic int\00"
@string_85204 = constant [11 x i8] c"now string\00"
@var15 = global i8* null
@string_73154 = constant [15 x i8] c"dynamic string\00"
@var16 = global i32 0
@string_24389 = constant [10 x i8] c"logical a\00"
@var17 = global i32 0
@var18 = global double 0.0
@string_35196 = constant [10 x i8] c"logical a\00"
@var19 = global i32 0
@var20 = global i32 0
@var21 = global i32 0
@string_67315 = constant [11 x i8] c"logical cc\00"
@var22 = global i32 0
@var23 = global i32 0
@string_6348 = constant [4 x i8] c"---\00"
@string_19949 = constant [18 x i8] c"Jestem if w while\00"
@var24 = global i32 0
@string_43759 = constant [15 x i8] c"Jestem if w if\00"
@string_88137 = constant [26 x i8] c"Jestem while w if w while\00"
@string_28027 = constant [12 x i8] c"Nie ma mnie\00"
@var25 = global double 0.0
@string_86413 = constant [4 x i8] c"dou\00"
@string_93340 = constant [8 x i8] c"readstr\00"
@var26 = global i8* null
@var27 = global i32 0
@var28 = global float 0.0
@var31 = global i32 0
@var32 = global i32 0

define i32 @main() nounwind {
%garr = alloca [2 x i32], align 8
%1 = alloca i32
store i32 0, i32* %1, align 4
%2 = load i32, i32* %1
%3 = alloca i32
store i32 123, i32* %3, align 4
%4 = load i32, i32* %3
%5 = getelementptr [2 x i32], [2 x i32]* %garr, i32 0, i32 0
store i32 123, i32* %5
%6 = alloca i32
store i32 1, i32* %6, align 4
%7 = load i32, i32* %6
%8 = alloca i32
store i32 345, i32* %8, align 4
%9 = load i32, i32* %8
%10 = getelementptr [2 x i32], [2 x i32]* %garr, i32 0, i32 1
store i32 345, i32* %10
%11 = getelementptr [2 x i32], [2 x i32]* %garr, i32 0, i32 0
%12 = load i32, i32* %11
store i32 %12, i32* @var2
%13 = load i32, i32* @var2
%14 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_int_newline, i32 0, i32 0),i32 %13)
%15 = getelementptr [2 x i32], [2 x i32]* %garr, i32 0, i32 1
%16 = load i32, i32* %15
store i32 %16, i32* @var2
%17 = load i32, i32* @var2
%18 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_int_newline, i32 0, i32 0),i32 %17)
%19 = alloca i32
store i32 10, i32* %19, align 4
%20 = load i32, i32* %19
%21 = alloca float
store float 0x3fe4937400000000, float* %21, align 4
%22 = load float, float* %21
%23 = getelementptr %struct.s1, %struct.s1* @var3, i32 0, i32 0
store float %22, float* %23
%24 = getelementptr %struct.s1, %struct.s1* @var3, i32 0, i32 1
store i32 %20, i32* %24
%25 = alloca i32
store i32 123, i32* %25, align 4
%26 = load i32, i32* %25
%27 = getelementptr %struct.s1, %struct.s1* @var3, i32 0, i32 1
store i32 %26, i32* %27
%28 = getelementptr %struct.s1, %struct.s1* @var3, i32 0, i32 1
%29 = load i32, i32* %28
store i32 %29, i32* @var4
%30 = getelementptr %struct.s1, %struct.s1* @var3, i32 0, i32 0
%31 = load float, float* %30
store float %31, float* @var5
%32 = load i32, i32* @var4
%33 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_int_newline, i32 0, i32 0),i32 %32)
%34 = load float, float* @var5
%35 = fpext float %34 to double
%36 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_float_newline, i32 0, i32 0),double %35)
%37 = alloca i32
store i32 4, i32* %37, align 4
%38 = load i32, i32* %37
store i32 %38, i32* @var6
%39 = alloca i32
store i32 5, i32* %39, align 4
%40 = load i32, i32* %39
store i32 %40, i32* @var11
%41 = alloca i32
store i32 5, i32* %41, align 4
%42 = load i32, i32* %41
store i32 %42, i32* @var12
%43 = alloca i8*
%44 = getelementptr inbounds [11 x i8], [11 x i8]* @string_20, i32 0, i32 0
store i8* %44, i8** %43
%45 = load i8*, i8** %43
%46  = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_string_newline, i32 0, i32 0),i8* %45)
%47 = load i32, i32* @var12
%48 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_int_newline, i32 0, i32 0),i32 %47)
%49 = load i32, i32* @var11
%50 = alloca i32
store i32 4, i32* %50, align 4
%51 = load i32, i32* %50
%52 = load i32, i32* @var12
%53 = call i32 @foobar(i32 %49, i32 %51, i32 %52)
store i32 %53, i32* @var13
%54 = alloca i8*
%55 = getelementptr inbounds [10 x i8], [10 x i8]* @string_23288, i32 0, i32 0
store i8* %55, i8** %54
%56 = load i8*, i8** %54
%57  = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_string_newline, i32 0, i32 0),i8* %56)
%58 = load i32, i32* @var12
%59 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_int_newline, i32 0, i32 0),i32 %58)
%60 = alloca i8*
%61 = getelementptr inbounds [10 x i8], [10 x i8]* @string_542, i32 0, i32 0
store i8* %61, i8** %60
%62 = load i8*, i8** %60
%63  = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_string_newline, i32 0, i32 0),i8* %62)
%64 = load i32, i32* @var13
%65 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_int_newline, i32 0, i32 0),i32 %64)
%66 = alloca i32
store i32 3456, i32* %66, align 4
%67 = load i32, i32* %66
store i32 %67, i32* @var14
%68 = alloca i8*
%69 = getelementptr inbounds [12 x i8], [12 x i8]* @string_56756, i32 0, i32 0
store i8* %69, i8** %68
%70 = load i8*, i8** %68
%71  = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_string_newline, i32 0, i32 0),i8* %70)
%72 = load i32, i32* @var14
%73 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_int_newline, i32 0, i32 0),i32 %72)
%74 = alloca i8*
%75 = getelementptr inbounds [11 x i8], [11 x i8]* @string_85204, i32 0, i32 0
store i8* %75, i8** %74
%76 = load i8*, i8** %74
store i8* %76, i8** @var15
%77 = alloca i8*
%78 = getelementptr inbounds [15 x i8], [15 x i8]* @string_73154, i32 0, i32 0
store i8* %78, i8** %77
%79 = load i8*, i8** %77
%80  = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_string_newline, i32 0, i32 0),i8* %79)
%81 = load i8*, i8** @var15
%82  = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_string_newline, i32 0, i32 0),i8* %81)
%83 = alloca i32
store i32 1, i32* %83, align 4
%84 = load i32, i32* %83
%85 = alloca i32
store i32 0, i32* %85, align 4
%86 = load i32, i32* %85
%87 = and i32 %84, %86
store i32 %87, i32* @var16
%88 = alloca i8*
%89 = getelementptr inbounds [10 x i8], [10 x i8]* @string_24389, i32 0, i32 0
store i8* %89, i8** %88
%90 = load i8*, i8** %88
%91  = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_string_newline, i32 0, i32 0),i8* %90)
%92 = load i32, i32* @var16
%93 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_int_newline, i32 0, i32 0),i32 %92)
%94 = load i32, i32* @var16
%95 = alloca i32
store i32 2, i32* %95, align 4
%96 = load i32, i32* %95
%97 = alloca i32
store i32 4, i32* %97, align 4
%98 = load i32, i32* %97
%99 = alloca i32
store i32 6, i32* %99, align 4
%100 = load i32, i32* %99
%101 = alloca i32
store i32 1, i32* %101, align 4
%102 = load i32, i32* %101
%103 = sub i32 %100, %102
%104 = add i32 %98, %103
%105 = add i32 %96, %104
%106 = add i32 %94, %105
store i32 %106, i32* @var17
%107 = alloca double
store double 0x3ff0000000000000, double* %107, align 4
%108 = load double, double* %107
%109 = alloca double
store double 0x4000020c49ba5e35, double* %109, align 4
%110 = load double, double* %109
%111 = fsub double %108, %110
store double %111, double* @var18
%112 = load i32, i32* @var17
%113 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_int_newline, i32 0, i32 0),i32 %112)
%114 = load double, double* @var18
%115 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([5 x i8], [5 x i8]* @str_double_newline, i32 0, i32 0),double %114)
%116 = alloca i32
store i32 1, i32* %116, align 4
%117 = load i32, i32* %116
%118 = alloca i32
store i32 0, i32* %118, align 4
%119 = load i32, i32* %118
%120 = or i32 %117, %119
store i32 %120, i32* @var16
%121 = alloca i8*
%122 = getelementptr inbounds [10 x i8], [10 x i8]* @string_35196, i32 0, i32 0
store i8* %122, i8** %121
%123 = load i8*, i8** %121
%124  = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_string_newline, i32 0, i32 0),i8* %123)
%125 = load i32, i32* @var16
%126 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_int_newline, i32 0, i32 0),i32 %125)
%127 = alloca i32
store i32 11, i32* %127, align 4
%128 = load i32, i32* %127
store i32 %128, i32* @var19
%129 = alloca i32
store i32 21, i32* %129, align 4
%130 = load i32, i32* %129
store i32 %130, i32* @var20
%131 = load i32, i32* @var19
%132 = load i32, i32* @var20
%133 = and i32 %131, %132
store i32 %133, i32* @var21
%134 = alloca i8*
%135 = getelementptr inbounds [11 x i8], [11 x i8]* @string_67315, i32 0, i32 0
store i8* %135, i8** %134
%136 = load i8*, i8** %134
%137  = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_string_newline, i32 0, i32 0),i8* %136)
%138 = load i32, i32* @var21
%139 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_int_newline, i32 0, i32 0),i32 %138)
%140 = alloca i32
store i32 10, i32* %140, align 4
%141 = load i32, i32* %140
store i32 %141, i32* @var22
br label %while1
while1:
%142 = load i32, i32* @var22
%143 = alloca i32
store i32 2, i32* %143, align 4
%144 = load i32, i32* %143
%145 = add i32 %142, %144
%146 = icmp ne i32 %145, 0
br i1 %146, label %while_body1, label %elihw1
while_body1:
%147 = load i32, i32* @var22
%148 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_int_newline, i32 0, i32 0),i32 %147)
%149 = load i32, i32* @var22
%150 = alloca i32
store i32 2, i32* %150, align 4
%151 = load i32, i32* %150
%152 = sub i32 %149, %151
store i32 %152, i32* @var22
%153 = alloca i32
store i32 3, i32* %153, align 4
%154 = load i32, i32* %153
store i32 %154, i32* @var23
%155 = load i32, i32* @var22
%156 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_int_newline, i32 0, i32 0),i32 %155)
%157 = alloca i8*
%158 = getelementptr inbounds [4 x i8], [4 x i8]* @string_6348, i32 0, i32 0
store i8* %158, i8** %157
%159 = load i8*, i8** %157
%160  = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_string_newline, i32 0, i32 0),i8* %159)
%161 = alloca i32
store i32 1, i32* %161, align 4
%162 = load i32, i32* %161
%163 = icmp ne i32 %162, 0
br i1 %163, label %if1, label %fi1
if1:
%164 = alloca i8*
%165 = getelementptr inbounds [18 x i8], [18 x i8]* @string_19949, i32 0, i32 0
store i8* %165, i8** %164
%166 = load i8*, i8** %164
%167  = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_string_newline, i32 0, i32 0),i8* %166)
%168 = alloca i32
store i32 5, i32* %168, align 4
%169 = load i32, i32* %168
store i32 %169, i32* @var24
%170 = alloca i32
store i32 1, i32* %170, align 4
%171 = load i32, i32* %170
%172 = icmp ne i32 %171, 0
br i1 %172, label %if2, label %fi2
if2:
%173 = alloca i8*
%174 = getelementptr inbounds [15 x i8], [15 x i8]* @string_43759, i32 0, i32 0
store i8* %174, i8** %173
%175 = load i8*, i8** %173
%176  = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_string_newline, i32 0, i32 0),i8* %175)
br label %fi2
fi2:
br label %while2
while2:
%177 = load i32, i32* @var24
%178 = icmp ne i32 %177, 0
br i1 %178, label %while_body2, label %elihw2
while_body2:
%179 = alloca i8*
%180 = getelementptr inbounds [26 x i8], [26 x i8]* @string_88137, i32 0, i32 0
store i8* %180, i8** %179
%181 = load i8*, i8** %179
%182  = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_string_newline, i32 0, i32 0),i8* %181)
%183 = load i32, i32* @var24
%184 = alloca i32
store i32 1, i32* %184, align 4
%185 = load i32, i32* %184
%186 = sub i32 %183, %185
store i32 %186, i32* @var24
br label %while2
elihw2:
br label %fi1
fi1:
br label %while1
elihw1:
br label %while3
while3:
%187 = alloca i32
store i32 0, i32* %187, align 4
%188 = load i32, i32* %187
%189 = icmp ne i32 %188, 0
br i1 %189, label %while_body3, label %elihw3
while_body3:
%190 = alloca i8*
%191 = getelementptr inbounds [12 x i8], [12 x i8]* @string_28027, i32 0, i32 0
store i8* %191, i8** %190
%192 = load i8*, i8** %190
%193  = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_string_newline, i32 0, i32 0),i8* %192)
br label %while3
elihw3:
%194 = alloca double
store double 0x3f50624dd2f1a9fc, double* %194, align 4
%195 = load double, double* %194
%196 = alloca double
store double 0x3ff0000000000000, double* %196, align 4
%197 = load double, double* %196
%198 = fadd double %195, %197
%199 = alloca double
store double 0x40091eb851eb851f, double* %199, align 4
%200 = load double, double* %199
%201 = fdiv double %198, %200
store double %201, double* @var25
%202 = alloca i8*
%203 = getelementptr inbounds [4 x i8], [4 x i8]* @string_86413, i32 0, i32 0
store i8* %203, i8** %202
%204 = load i8*, i8** %202
%205  = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_string_newline, i32 0, i32 0),i8* %204)
%206 = load double, double* @var25
%207 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([5 x i8], [5 x i8]* @str_double_newline, i32 0, i32 0),double %206)
%208 = alloca i8*
%209 = getelementptr inbounds [8 x i8], [8 x i8]* @string_93340, i32 0, i32 0
store i8* %209, i8** %208
%210 = load i8*, i8** %208
store i8* %210, i8** @var26
%211 = alloca i32
store i32 56, i32* %211, align 4
%212 = load i32, i32* %211
store i32 %212, i32* @var27
%213 = alloca float
store float 0x0000000000000000, float* %213, align 4
%214 = load float, float* %213
store float %214, float* @var28
%215 = alloca i8, i32 100
%216 = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @str_string, i32 0, i32 0),i8* %215)
store i8* %215, i8** @var26
%217 = load i8*, i8** @var26
%218  = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_string_newline, i32 0, i32 0),i8* %217)
%219 = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @str_int, i32 0, i32 0),i32* @var27)
%220 = load i32, i32* @var27
%221 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_int_newline, i32 0, i32 0),i32 %220)
%222 = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @str_float, i32 0, i32 0),float* @var28)
%223 = load float, float* @var28
%224 = fpext float %223 to double
%225 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_float_newline, i32 0, i32 0),double %224)
%arr = alloca [6 x i32], align 8
%arr2 = alloca [2 x i32], align 8
%226 = alloca i32
store i32 1, i32* %226, align 4
%227 = load i32, i32* %226
%228 = alloca i32
store i32 309, i32* %228, align 4
%229 = load i32, i32* %228
%230 = getelementptr [2 x i32], [2 x i32]* %arr2, i32 0, i32 1
store i32 309, i32* %230
%231 = alloca i32
store i32 0, i32* %231, align 4
%232 = load i32, i32* %231
%233 = alloca i32
store i32 0, i32* %233, align 4
%234 = load i32, i32* %233
%235 = alloca i32
store i32 0, i32* %235, align 4
%236 = load i32, i32* %235
%237 = getelementptr [6 x i32], [6 x i32]* %arr, i32 0, i32 0
store i32 0, i32* %237
%238 = alloca i32
store i32 0, i32* %238, align 4
%239 = load i32, i32* %238
%240 = alloca i32
store i32 1, i32* %240, align 4
%241 = load i32, i32* %240
%242 = alloca i32
store i32 0, i32* %242, align 4
%243 = load i32, i32* %242
%244 = getelementptr [6 x i32], [6 x i32]* %arr, i32 0, i32 1
store i32 0, i32* %244
%245 = alloca i32
store i32 0, i32* %245, align 4
%246 = load i32, i32* %245
%247 = alloca i32
store i32 2, i32* %247, align 4
%248 = load i32, i32* %247
%249 = alloca i32
store i32 0, i32* %249, align 4
%250 = load i32, i32* %249
%251 = getelementptr [6 x i32], [6 x i32]* %arr, i32 0, i32 2
store i32 0, i32* %251
%252 = alloca i32
store i32 1, i32* %252, align 4
%253 = load i32, i32* %252
%254 = alloca i32
store i32 0, i32* %254, align 4
%255 = load i32, i32* %254
%256 = alloca i32
store i32 0, i32* %256, align 4
%257 = load i32, i32* %256
%258 = getelementptr [6 x i32], [6 x i32]* %arr, i32 0, i32 3
store i32 0, i32* %258
%259 = alloca i32
store i32 1, i32* %259, align 4
%260 = load i32, i32* %259
%261 = alloca i32
store i32 1, i32* %261, align 4
%262 = load i32, i32* %261
%263 = alloca i32
store i32 30, i32* %263, align 4
%264 = load i32, i32* %263
%265 = getelementptr [6 x i32], [6 x i32]* %arr, i32 0, i32 4
store i32 30, i32* %265
%266 = alloca i32
store i32 1, i32* %266, align 4
%267 = load i32, i32* %266
%268 = alloca i32
store i32 2, i32* %268, align 4
%269 = load i32, i32* %268
%270 = alloca i32
store i32 0, i32* %270, align 4
%271 = load i32, i32* %270
%272 = getelementptr [6 x i32], [6 x i32]* %arr, i32 0, i32 5
store i32 0, i32* %272
%273 = alloca i32
store i32 1, i32* %273, align 4
%274 = load i32, i32* %273
%275 = alloca i32
store i32 1, i32* %275, align 4
%276 = load i32, i32* %275
%277 = getelementptr [6 x i32], [6 x i32]* %arr, i32 0, i32 4
%278 = load i32, i32* %277
store i32 %278, i32* @var31
%279 = alloca i32
store i32 1, i32* %279, align 4
%280 = load i32, i32* %279
%281 = getelementptr [2 x i32], [2 x i32]* %arr2, i32 0, i32 1
%282 = load i32, i32* %281
store i32 %282, i32* @var32
%283 = load i32, i32* @var31
%284 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_int_newline, i32 0, i32 0),i32 %283)
%285 = load i32, i32* @var32
%286 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_int_newline, i32 0, i32 0),i32 %285)

ret i32 0 }