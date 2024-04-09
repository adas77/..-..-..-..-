from enum import Enum
import struct


class Type(Enum):
    INT = "i32",
    DOUBLE = "double",


class LLVMGenerator():
    def __init__(self, file_path: str = "./code.ll"):
        self.file_path = file_path
        self.main_text = ""
        self.tmp = 1
        self.header_text = ""

    def save(self):
        with open(self.file_path, 'w') as f:
            f.write(self.generate())

    def printf_int(self, id_: str):
        self.main_text += f"%{self.tmp} = load i32, i32* %{id_}\n"
        # self.main_text += "%"+self.tmp+" = load i32, i32* %"+id_+"\n"
        self.tmp += 1
        self.main_text += "%"+str(self.tmp) + " = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strp, i32 0, i32 0), i32 %"+str(  # change strp to str argument for others and custom printfs
            self.tmp-1)+")\n"
        self.tmp += 1

    def printf_str(self, id_: str, len: int):
        self.main_text += f"%{self.tmp} = getelementptr inbounds [{len} x i8], [{len} x i8]* @{id_}, i32 0, i32 0\n"
        self.tmp += 1
        self.main_text += "%"+str(self.tmp) + " = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strstr, i32 0, i32 0), i8* %"+str(  # change strp to str argument for others and custom printfs
            self.tmp-1)+")\n"
        self.tmp += 1

    def printf_double(self, id_: str):
        self.main_text += f"%{self.tmp} = load double, double* %{id_}\n"
        self.tmp += 1
        self.main_text += f"%{self.tmp} = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strf, i32 0, i32 0), double %{self.tmp-1})\n"
        self.tmp += 1

    def scanf(self, id_: str):
        self.main_text += f"%{self.tmp} = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @strs, i32 0, i32 0), i32* %{self.id_}\n"
        self.tmp += 1

    def assign_int(self, id_: str, value: int):
        self.main_text += f"store i32 {value}, i32* %{id_}\n"

    def assign_double(self, id_: str, value: float):
        hex_value = struct.pack('>d', float(value)).hex()
        self.main_text += f"store double 0x{hex_value}, double* %{id_}, align 4\n"

    def assign_id_int(self, id_: str, id2_: str):
        self.main_text += f"%{id_} = load i32, i32* %{id2_}\n"

    def assign_id_double(self, id_: str, id2_: str):
        self.main_text += f"%{id_} = load i32, i32* %{id2_}\n"

    def assign_arr(self, id_: str, type_: Type, size: int, index: int, val):
        # %newValue = ...
        # store i32 %newValue, i32* getelementptr inbounds ([5 x i32], [5 x i32]* @myArray, i32 0, i32 <index>)
        try:

            val = int(val) if type_ == Type.INT else float(val)
        except:
            raise ValueError("")
        self.main_text += f"store {type_} %{val} getelementptr ibounds ([{size} x {type_}], [{size} x {type_}]* @{id_}, {type_} 0, {type_} {index})"

    def declare_arr(self, id_: str, type_: Type, size: int):
        init_val = 0 if type_ == Type.INT else .0
        arr = ', '.join([f"{type_} {init_val}" for _ in range(size)])
        self.main_text += f"@{id_} = constant [{size} x {type_}] [{arr}]"

    def access_arr(self):
        # define i32 @accessArrayElement(i32* %arr) {
        # %elementPtr = getelementptr i32, i32* %arr, i64 2
        # %value = load i32, i32* %elementPtr
        # ret i32 %value
        # }
        self.main_text += f""

    def declare_int(self, id_: str):
        self.main_text += f"%{id_} = alloca i32\n"

    def declare_double(self, id_: str):
        self.main_text += f"%{id_} = alloca double\n"

    def generate(self) -> str:
        text = ""
        text += "declare i32 @printf(i8*, ...)\n"
        text += "declare i32 @__isoc99_scanf(i8*, ...)\n"
        text += "@strp = constant [4 x i8] c\"%d\\0A\\00\"\n"
        text += "@strf = constant [4 x i8] c\"%f\\0A\\00\"\n"
        text += "@strs = constant [3 x i8] c\"%d\\00\"\n"
        text += '@strstr = constant [4 x i8] c"%s\\0A\\00"\n'
        text += self.header_text
        text += "define i32 @main() nounwind{\n"
        text += self.main_text
        text += "ret i32 0 }\n"
        return text

    def declare_static_string(self, name: str, value: str):
        self.header_text += f"@{name} = constant [{len(value)+1} x i8] c\"{value}\\00\"\n"

    def declare_str(self, name: str):
        self.main_text += f"%{name} = alloca i8*\n"

    def allocate_str(self, name: str, length: int):
        self.main_text += f"%{name} = alloca [{length+1} x i8]\n"

    # def assign_str(self, id_: str, name: str):
    #     self.main_text += f"store i8* %{id_}, i8* %{name}\n"
