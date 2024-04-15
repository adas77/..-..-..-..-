from enum import Enum
import struct


class Instruction(Enum):
    WHILE = ("while", "while_body", "elihw")
    IF = ("if", "if_body", "fi")


class Type(Enum):
    INT = ("i32",)
    DOUBLE = ("double",)
    STR = ("i8*",)
    FLOAT = ("float",)

    def __str__(self):
        return f"{self.value[0]}"

    @staticmethod
    def map_(type_: str):
        types_mappings = {
            "int": Type.INT,
            "double": Type.DOUBLE,
            "string": Type.STR,
            "float": Type.FLOAT,
        }
        res = types_mappings.get(type_, None)
        if res is None:
            raise ValueError(f"{type_} is not a valid type")
        return res

    def get_zero_str(self) -> str:
        zero_mappings: dict[Type, str] = {
            Type.INT: "0",
            Type.DOUBLE: "0.0",
            Type.FLOAT: "0.0",
        }
        res = zero_mappings.get(self, None)
        if res is None:
            raise ValueError(f"Cannot get zero for type: {self}")
        return res

    def get_icmp(self) -> tuple[str, str]:
        zero_mappings: dict[Type, tuple[str, str]] = {
            Type.INT: ("icmp", "ne"),
            Type.DOUBLE: ("fcmp", "one"),
            Type.FLOAT: ("fcmp", "one"),
        }
        res = zero_mappings.get(self, None)
        if res is None:
            raise ValueError(f"Cannot get icmp operation for type: {self}")
        return res


class LLVMGenerator:
    def __init__(self, file_path: str = "./code.ll"):
        self.file_path = file_path

        self.main_text = ""
        self.header_text = ""

        self.tmp = 1
        self.str_tmp = 1
        self.main_tmp = 1

        self.br = 0
        self.br_stack = []

        self.br_while = 0
        self.br_while_stack = []

    def save(self):
        with open(self.file_path, "w+") as f:
            f.write(self.generate())

    def scanf(self, id_: str, type_: Type):
        if type_ == Type.INT:
            self.main_text += f"%{self.tmp} = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @str_int, i32 0, i32 0),i32* {id_})\n"
        elif type_ == Type.DOUBLE:
            self.main_text += f"%{self.tmp} = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_double, i32 0, i32 0),double* {id_})\n"
        elif type_ == Type.FLOAT:
            self.main_text += f"%{self.tmp} = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @str_float, i32 0, i32 0),float* {id_})\n"
        elif type_ == Type.STR:
            self.main_text += f"%{self.tmp} = alloca i8, i32 100\n"
            self.tmp += 1
            self.main_text += f"%{self.tmp} = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @str_string, i32 0, i32 0),i8* %{self.tmp-1})\n"
            self.main_text += f"store i8* %{self.tmp-1}, i8** {id_}\n"
        else:
            raise ValueError(f"Type {type_} scanning is not supported")
        self.tmp += 1

    def printf(self, id_: str, type_: Type):
        if type_ == Type.INT:
            self.main_text += f"%{self.tmp} = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_int_newline, i32 0, i32 0),i32 {id_})\n"
        elif type_ == Type.DOUBLE:
            self.main_text += f"%{self.tmp} = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([5 x i8], [5 x i8]* @str_double_newline, i32 0, i32 0),double {id_})\n"
        elif type_ == Type.FLOAT:
            self.main_text += f"%{self.tmp} = fpext float {id_} to double\n"
            self.tmp += 1
            self.main_text += f"%{self.tmp} = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_float_newline, i32 0, i32 0),double %{self.tmp-1})\n"
        elif type_ == Type.STR:
            self.main_text += f"%{self.tmp} = load i8*, i8** {id_}\n"
            self.tmp += 1
            self.main_text += f"%{self.tmp} = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_string_newline, i32 0, i32 0),i8* %{self.tmp-1})\n"
        else:
            raise ValueError(f"Type {type_} printing is not supported")
        self.tmp += 1

    def assign_anonymous(self, value, type_: Type) -> str:
        type_stringified = type_.value[0]
        self.main_text += f"%{self.tmp} = alloca {type_stringified}\n"
        self.tmp += 1
        if type_ == Type.DOUBLE:
            hex_value = struct.pack(">d", float(value)).hex()
            self.main_text += (
                f"store double 0x{hex_value}, double* %{self.tmp-1}, align 4\n"
            )
        elif type_ == Type.FLOAT:
            hex_value = struct.pack(">d", float(value)).hex()[0:8] + "00000000"
            self.main_text += (
                f"store float 0x{hex_value}, float* %{self.tmp-1}, align 4\n"
            )
        elif type_ == Type.INT:
            self.main_text += f"store i32 {value}, i32* %{self.tmp-1}, align 4\n"
        elif type_ == Type.STR:
            # declare global string then load into anonymous pointer
            global_string_id = self.declare_global_string(
                f"string_{self.str_tmp}", str(value)
            )
            self.str_tmp += 1
            str_length = len(str(value))
            self.main_text += f"%{self.tmp} = getelementptr inbounds [{str_length+1} x i8], [{str_length+1} x i8]* {global_string_id}, i32 0, i32 0\n"
            self.tmp += 1
            self.main_text += f"store i8* %{self.tmp-1}, i8** %{self.tmp-2}\n"
            return f"%{self.tmp-2}"
        else:
            self.main_text += (
                f"store {type_stringified} {value}, {type_stringified}* %{self.tmp-1}\n"
            )
        return f"%{self.tmp-1}"

    def assign_int(self, id_: str, value: str):
        self.main_text += f"store i32 {value}, i32* {id_}\n"

    def assign_double(self, id_: str, value: str):
        self.main_text += f"store double {value}, double* {id_}\n"

    def assign_float(self, id_: str, value: str):
        self.main_text += f"store float {value}, float* {id_}\n"

    def assign_id_int(self, id_: str, id2_: str):
        self.main_text += f"%{id_} = load i32, i32* %{id2_}\n"

    def assign_id_double(self, id_: str, id2_: str):
        self.main_text += f"%{id_} = load i32, i32* %{id2_}\n"

    def assign_arr(self, id_: str, type_: Type, size: int, index: int, val):
        self._validate_arr_size(size, index)
        self.main_text += f"%{self.tmp} = getelementptr [{size} x {type_}], [{size} x {type_}]* %{id_}, i32 0, i32 {index}\n"
        self.main_text += f"store {type_} {val}, {type_}* %{self.tmp}\n"
        self.tmp += 1
        return f"%{self.tmp-1}"

    def declare_arr(self, id_: str, type_: Type, size: int):
        self.main_text += f"%{id_} = alloca [{size} x {type_}], align 8\n"

    def access_arr(self, id_, type_: Type, size: int, index: int):
        self._validate_arr_size(size, index)
        self.main_text += f"%{self.tmp} = getelementptr [{size} x {type_}], [{size} x {type_}]* %{id_}, i32 0, i32 {index}\n"
        self.tmp += 1
        self.main_text += f"%{self.tmp} = load {type_}, {type_}* %{self.tmp-1}\n"
        self.tmp += 1
        return f"%{self.tmp-1}"

    def assign_arr2d(
        self, id_: str, type_: Type, rows: int, cols: int, r: int, c: int, val
    ):
        self._validate_2d_size(rows, cols, r, c)
        size = rows * cols
        index = r * cols + c
        self.main_text += f"%{self.tmp} = getelementptr [{size} x {type_}], [{size} x {type_}]* %{id_}, i32 0, i32 {index}\n"
        self.main_text += f"store {type_} {val}, {type_}* %{self.tmp}\n"
        self.tmp += 1
        return f"%{self.tmp-1}"

    def declare_arr2d(self, id_: str, type_: Type, rows: int, cols: int):
        size = rows * cols
        self.main_text += f"%{id_} = alloca [{size} x {type_}], align 8\n"

    def access_arr2d(self, id_, type_: Type, rows: int, cols: int, r: int, c: int):
        self._validate_2d_size(rows, cols, r, c)
        size = rows * cols
        index = r * cols + c
        self.main_text += f"%{self.tmp} = getelementptr [{size} x {type_}], [{size} x {type_}]* %{id_}, i32 0, i32 {index}\n"
        self.tmp += 1
        self.main_text += f"%{self.tmp} = load {type_}, {type_}* %{self.tmp-1}\n"
        self.tmp += 1
        return f"%{self.tmp-1}"

    def _validate_2d_size(self, rows: int, cols: int, r: int, c: int):
        if r >= rows or c >= cols:
            raise ValueError(f"Out of bounds for column: {c} row: {r}")

    def _validate_arr_size(self, index: int, i: int):
        if i >= index:
            raise ValueError(f"Out of bounds for index: {i}")

    def declare_int(self, id_: str):
        self.main_text += f"%{id_} = alloca i32\n"

    def declare_double(self, id_: str):
        self.main_text += f"%{id_} = alloca double\n"

    def generate(self) -> str:
        text = ""
        text += "declare i32 @printf(i8*, ...)\n"
        text += "declare i32 @__isoc99_scanf(i8*, ...)\n"
        text += '@strp = constant [4 x i8] c"%d\\0A\\00"\n'
        text += '@strlf = constant [4 x i8] c"%lf\\00"\n'
        text += '@strlfn = constant [5 x i8] c"%lf\\0A\\00"\n'
        text += '@strs = constant [3 x i8] c"%d\\00"\n'
        text += '@strstr = constant [4 x i8] c"%s\\0A\\00"\n'

        text += '@str_int_newline = constant [4 x i8] c"%d\\0A\\00"\n'
        text += '@str_double_newline = constant [5 x i8] c"%lf\\0A\\00"\n'
        text += '@str_string_newline = constant [4 x i8] c"%s\\0A\\00"\n'
        text += '@str_float_newline = constant [4 x i8] c"%f\\0A\\00"\n'

        text += '@str_int = constant [3 x i8] c"%d\\00"\n'
        text += '@str_double = constant [4 x i8] c"%lf\\00"\n'
        text += '@str_string = constant [3 x i8] c"%s\\00"\n'
        text += '@str_float = constant [3 x i8] c"%f\\00"\n'

        text += self.header_text
        text += "\ndefine i32 @main() nounwind{\n"
        text += self.main_text
        text += "ret i32 0 }\n"
        return text

    def declare_global_string(self, name: str, value: str) -> str:
        self.header_text += f'@{name} = constant [{len(value)+1} x i8] c"{value}\\00"\n'
        return f"@{name}"

    def declare_str(self, name: str, length: int):
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

    def add(self, id_1: str, id_2: str, type_: Type) -> str:
        if type_ == Type.INT:
            self.main_text += f"%{self.tmp} = add i32 {id_1}, {id_2}\n"
        elif type_ == Type.DOUBLE:
            self.main_text += f"%{self.tmp} = fadd double {id_1}, {id_2}\n"
        elif type_ == Type.FLOAT:
            self.main_text += f"%{self.tmp} = fadd float {id_1}, {id_2}\n"
        else:
            raise ValueError(f"Type {type_} adding is not supported")
        self.tmp += 1
        return f"%{self.tmp-1}"

    def mul(self, id_1: str, id_2: str, type_: Type) -> str:
        ops = {
            Type.DOUBLE: "fmul",
            Type.INT: "mul",
            Type.FLOAT: "fmul",
        }
        mul = ops.get(type_, None)
        if mul is None:
            raise ValueError(f"Type {type_} multiplication is not supported")
        self.main_text += f"%{self.tmp} = {mul} {type_} {id_1}, {id_2}\n"
        self.tmp += 1
        return f"%{self.tmp-1}"

    def sub(self, id_1: str, id_2: str, type_: Type) -> str:
        self.main_text += f"%{self.tmp} = sub {type_} {id_1}, {id_2}\n"
        self.tmp += 1
        return f"%{self.tmp-1}"

    def div(self, id_1: str, id_2: str, type_: Type) -> str:
        ops = {
            Type.DOUBLE: "fdiv",
            Type.INT: "sdiv",
            Type.FLOAT: "fdiv",
        }
        div = ops.get(type_, None)
        if div is None:
            raise ValueError(f"Type {type_} is not supported")
        self.main_text += f"%{self.tmp} = {div} {type_} {id_1}, {id_2}\n"
        self.tmp += 1
        return f"%{self.tmp-1}"

    def bit_and(self, id_1: str, id_2: str, type_: Type) -> str:
        self.main_text += f"%{self.tmp} = and {type_} {id_1}, {id_2}\n"
        self.tmp += 1
        return f"%{self.tmp-1}"

    def bit_or(self, id_1: str, id_2: str, type_: Type) -> str:
        self.main_text += f"%{self.tmp} = or {type_} {id_1}, {id_2}\n"
        self.tmp += 1
        return f"%{self.tmp-1}"

    def bit_xor(self, id_1: str, id_2: str, type_: Type) -> str:
        self.main_text += f"%{self.tmp} = xor {type_} {id_1}, {id_2}\n"
        self.tmp += 1
        return f"%{self.tmp-1}"

    def bit_not(self, id_: str, type_: Type) -> str:
        self.main_text += f"%{self.tmp} = xor {type_} {id_}, -1\n"
        self.tmp += 1
        return f"%{self.tmp-1}"

    def logical_not(self, r_id: str, type_: Type) -> str:
        raise NotImplementedError()

    def assign(self, id_: str, value_: tuple[str, Type]):
        if value_[1] == Type.INT:
            self.assign_int(id_, value_[0])
        elif value_[1] == Type.DOUBLE:
            self.assign_double(id_, value_[0])
        elif value_[1] == Type.FLOAT:
            self.assign_float(id_, value_[0])
        elif value_[1] == Type.STR:
            # load i8*, i8** %1
            self.main_text += f"%{self.tmp} = load i8*, i8** {value_[0]}\n"
            self.tmp += 1
            self.main_text += f"store i8* %{self.tmp-1}, i8** {id_}\n"
        else:
            raise ValueError(f"Type {value_[1]} assigning is not supported")

    def load(self, id_: str, type_: Type, str_length: int = 0) -> str:
        if type_ == Type.STR:
            # %2 = getelementptr inbounds [12 x i8], [12 x i8]* @string_1, i32 0, i32 0
            # self.main_text += f"%{self.tmp} = getelementptr inbounds [{str_length+1} x i8], [{str_length+1} x i8]* {id_}, i32 0, i32 0\n"
            # self.tmp += 1
            # return f"%{self.tmp-1}"
            # return f"%{self.tmp-1}"
            return id_

        self.main_text += f"%{self.tmp} = load {type_}, {type_}* {id_}\n"
        self.tmp += 1
        return f"%{self.tmp-1}"

    def declare_variable(self, id_: str, type_: Type, is_global: bool) -> str:
        if type_ == Type.STR:
            if is_global:
                self.header_text += f"@{id_} = global i8* null\n"
                return f"@{id_}"
            else:
                self.main_text += f"%{id_} = alloca i8*\n"
                return f"%{id_}"

        zero = "0" if type_ == Type.INT else "0.0"
        if is_global:
            self.header_text += f"@{id_} = global {type_} {zero}\n"
            return f"@{id_}"
        else:
            self.main_text += f"%{id_} = alloca {type_}\n"
            return f"%{id_}"

    def if_start(self):
        l, _, r = Instruction.IF.value
        self.br += 1
        self.main_text += (
            f"br i1 %{self.tmp-1}, label %{l}{self.br}, label %{r}{self.br}\n"
        )
        self.main_text += f"{l}{self.br}:\n"
        self.br_stack.append(self.br)

    def if_end(self):
        _, _, r = Instruction.IF.value
        br = self.br_stack.pop()
        self.main_text += f"br label %{r}{br}\n"
        self.main_text += f"{r}{br}:\n"

    def while_start_block(self):
        l, m, r = Instruction.WHILE.value
        br_while = self.br_while_stack[-1]
        self.main_text += (
            f"br i1 %{self.tmp-1}, label %{m}{br_while}, label %{r}{br_while}\n"
        )
        self.main_text += f"{m}{br_while}:\n"

    def while_end(self):
        l, m, r = Instruction.WHILE.value
        br_while = self.br_while_stack.pop()
        self.main_text += f"br label %{l}{br_while}\n"
        self.main_text += f"{r}{br_while}:\n"

    def while_start(self):
        l, m, r = Instruction.WHILE.value
        self.br_while += 1
        self.main_text += f"br label %{l}{self.br_while}\n"
        self.main_text += f"{l}{self.br_while}:\n"
        self.br_while_stack.append(self.br_while)

    def icmp(self, id_: str, type_: Type):
        zero = type_.get_zero_str()
        compare, not_equal = type_.get_icmp()
        self.main_text += f"%{self.tmp} = {compare} {not_equal} {type_} {id_}, {zero}\n"
        self.tmp += 1
        return f"%{self.tmp-1}"
