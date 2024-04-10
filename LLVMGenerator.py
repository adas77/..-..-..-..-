from enum import Enum
import struct


class Type(Enum):
    INT = "i32",
    DOUBLE = "double",
    STR = "i8*"

    def map_(type_:str):
        types_mappings = {
            "int":Type.INT,
            "double":Type.DOUBLE,
            "string":Type.STR,
        }
        res = types_mappings.get(type_,None)
        if res is None:
            raise ValueError(f"{type_} is not a valid type") 
        return res

class LLVMGenerator():
    def __init__(self, file_path: str = "./code.ll"):
        self.file_path = file_path
        self.main_text = ""
        self.tmp = 1
        self.main_tmp = 1
        self.br = 0
        self.br_stack = []
        self.header_text = ""

    def save(self):
        with open(self.file_path, 'w') as f:
            f.write(self.generate())

    def printf_int(self, id_: str):
        self.main_text += f"%{self.tmp} = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strp, i32 0, i32 0), i32 {id_})\n"
        self.tmp += 1

    def printf_str(self, id_: str, len: int):
        self.main_text += f"%{self.tmp} = getelementptr inbounds [{len+1} x i8], [{len+1} x i8]* @{id_}, i32 0, i32 0\n"
        self.tmp += 1
        self.main_text += "%"+str(self.tmp) + " = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strstr, i32 0, i32 0), i8* %"+str(  # change strp to str argument for others and custom printfs
            self.tmp-1)+")\n"
        self.tmp += 1

    def printf_double(self, id_: str):
        self.main_text += f"%{self.tmp} = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strf, i32 0, i32 0), double {id_})\n"
        self.tmp += 1

    def scanf(self, id_: str):
        self.main_text += f"%{self.tmp} = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @strs, i32 0, i32 0), i32* %{self.id_}\n"
        self.tmp += 1
    
    def assign_int_anonymous(self, value: int)->str:
        self.main_text += f"%{self.tmp} = alloca i32\n"
        self.tmp += 1
        self.main_text += f"store i32 {value}, i32* %{self.tmp-1}\n"
        return f"%{self.tmp-1}"

    def assign_anonymous(self, value: int,type_:Type)->str:
        type_ = type_.value[0]
        self.main_text += f"%{self.tmp} = alloca {type_}\n"
        self.tmp += 1
        if type_ == Type.DOUBLE:
            hex_value = struct.pack('>d', float(value)).hex()
            self.main_text += f"store double 0x{hex_value}, double* %{self.tmp-1}, align 4\n"
        else:
            self.main_text += f"store {type_} {value}, {type_}* %{self.tmp-1}\n"
        return f"%{self.tmp-1}"

    def assign_int(self, id_: str, value: int):
        self.main_text += f"store i32 {value}, i32* {id_}\n"

    def assign_double(self, id_: str, value: float):
         self.main_text += f"store double {value}, double* {id_}\n"

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

    def assign_int_to_int(self, id_: str, id2_: str):
        self.main_text += f"%{self.tmp} = load i32, i32* %{id2_}\n"
        self.tmp += 1
        self.main_text += f"store i32 %{self.tmp-1}, i32* %{id_}\n"
    
    def assign_double_to_double(self, id_: str, id2_: str):
        self.main_text += f"%{self.tmp} = load double, double* %{id2_}\n"
        self.tmp += 1
        self.main_text += f"store double %{self.tmp-1}, double* %{id_}\n"


    def add(self,id_1: str, id_2: str,type_:Type)->str:
        type_ = type_.value[0]
        self.main_text += f"%{self.tmp} = add {type_} {id_1}, {id_2}\n"
        self.tmp+=1
        return f"%{self.tmp-1}"

    def mul(self,id_1: str, id_2: str,type_:Type)->str:
        type_ = type_.value[0]
        self.main_text += f"%{self.tmp} = mul {type_} {id_1}, {id_2}\n"
        self.tmp+=1
        return f"%{self.tmp-1}"

    def sub(self,id_1: str, id_2: str,type_:Type)->str:
        type_ = type_.value[0]
        self.main_text += f"%{self.tmp} = sub {type_} {id_1}, {id_2}\n"
        self.tmp+=1
        return f"%{self.tmp-1}"

    def div(self,id_1: str, id_2: str,type_:Type)->str:
        
        ops = {
            Type.DOUBLE:"fdiv",
            Type.INT:"sdiv",
        }
        print(f"Type: {type_} ops: {ops}")
        div = ops.get(type_,None)
        if div is None:
            raise ValueError(f"Type {type_} is not supported")
        type_ = type_.value[0]
        self.main_text += f"%{self.tmp} = {div} {type_} {id_1}, {id_2}\n"
        self.tmp+=1
        return f"%{self.tmp-1}"

    def assign(self, id_:str, value_:'tuple[str,Type]'):
        if value_[1] == Type.INT:
            self.assign_int(id_,value_[0])
        elif value_[1] == Type.DOUBLE:
            self.assign_double(id_,value_[0])
    
    def load(self,id_:str,type_:Type):
        type_ = type_.value[0]
        self.main_text += f"%{self.tmp} = load {type_}, {type_}* {id_}\n"
        self.tmp+=1
        return f"%{self.tmp-1}"
    
    def declare_variable(self, id_:str, type_:Type, is_global:bool)->str:
        zero = '0' if type_ == Type.INT else '0.0'
        type_ = type_.value[0]
        if is_global:
            self.header_text += f"@{id_} = global {type_} {zero}\n"
            return f'@{id_}'
        else:
            self.main_text += f"%{id_} = alloca {type_}\n"
            return f'%{id_}'