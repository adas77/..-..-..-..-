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
            Type.STR: "null",
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

        self.__main_text = ""
        self.__header_text = ""

        self.tmp = 1
        self.str_tmp = 1

        self.br = 0
        self.br_stack = []

        self.br_while = 0
        self.br_while_stack = []

    def save(self):
        with open(self.file_path, "w+") as f:
            f.write(self.__generate())

    def scanf(self, id_: str, type_: Type):
        if type_ == Type.INT:
            # self.main_text += f"%{self.tmp} = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @str_int, i32 0, i32 0),i32* {id_})\n"
            self.__append_text_main(
                f"%{self.tmp} = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @str_int, i32 0, i32 0),i32* {id_})"
            )
        elif type_ == Type.DOUBLE:
            # self.main_text += f"%{self.tmp} = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_double, i32 0, i32 0),double* {id_})\n"
            self.__append_text_main(
                f"%{self.tmp} = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_double, i32 0, i32 0),double* {id_})"
            )
        elif type_ == Type.FLOAT:
            # self.main_text += f"%{self.tmp} = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @str_float, i32 0, i32 0),float* {id_})\n"
            self.__append_text_main(
                f"%{self.tmp} = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @str_float, i32 0, i32 0),float* {id_})"
            )
        else:
            raise ValueError(f"Type {type_} scanning is not supported")
        self.tmp += 1

    def printf(self, id_: str, type_: Type):
        if type_ == Type.INT:
            # self.main_text += f"%{self.tmp} = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_int_newline, i32 0, i32 0),i32 {id_})\n"
            self.__append_text_main(
                f"%{self.tmp} = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_int_newline, i32 0, i32 0),i32 {id_})"
            )
        elif type_ == Type.DOUBLE:
            # self.main_text += f"%{self.tmp} = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([5 x i8], [5 x i8]* @str_double_newline, i32 0, i32 0),double {id_})\n"
            self.__append_text_main(
                f"%{self.tmp} = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([5 x i8], [5 x i8]* @str_double_newline, i32 0, i32 0),double {id_})"
            )
        elif type_ == Type.FLOAT:
            # self.main_text += f"%{self.tmp} = fpext float {id_} to double\n"
            self.__append_text_main(f"%{self.tmp} = fpext float {id_} to double")
            self.tmp += 1
            # self.main_text += f"%{self.tmp} = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_float_newline, i32 0, i32 0),double %{self.tmp-1})\n"
            self.__append_text_main(
                f"%{self.tmp} = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_float_newline, i32 0, i32 0),double %{self.tmp-1})"
            )
        elif type_ == Type.STR:
            # self.main_text += f"%{self.tmp} = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_string_newline, i32 0, i32 0),i8* {id_})\n"
            self.__append_text_main(
                f"%{self.tmp} = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_string_newline, i32 0, i32 0),i8* {id_})"
            )
        else:
            raise ValueError(f"Type {type_} printing is not supported")
        self.tmp += 1

    def load(
        self, id_new: str, type_: Type, id_old: str | None = None, str_length: int = 0
    ) -> str:
        scope_sign = "%"
        if type_ == Type.STR:
            return f"{scope_sign}{self.tmp-1}"
        if id_old is None:
            # self.main_text += f"%{self.tmp} = load {type_}, {type_}* {id_new}\n"
            self.__append_text_main(f"%{self.tmp} = load {type_}, {type_}* {id_new}")
            self.tmp += 1
            return f"{scope_sign}{self.tmp-1}"
        else:
            # self.main_text += f"%{id_old} = load {type_}, {type_}* {id_new}\n"
            self.__append_text_main(f"%{id_old} = load {type_}, {type_}* {id_new}")
            return f"{scope_sign}{id_old}"

    def assign_anonymous(self, value, type_: Type) -> str:
        # self.main_text += f"%{self.tmp} = alloca {type_}\n"
        self.__append_text_main(f"%{self.tmp} = alloca {type_}")
        self.tmp += 1
        if type_ == Type.DOUBLE:
            hex_value = struct.pack(">d", float(value)).hex()
            # self.main_text += (
            #     f"store double 0x{hex_value}, double* %{self.tmp-1}, align 4\n"
            # )
            self.__append_text_main(
                f"store double 0x{hex_value}, double* %{self.tmp-1}, align 4"
            )
        elif type_ == Type.FLOAT:
            hex_value = struct.pack(">d", float(value)).hex()[0:8] + "00000000"
            # self.main_text += (
            #     f"store float 0x{hex_value}, float* %{self.tmp-1}, align 4\n"
            # )
            self.__append_text_main(
                f"store float 0x{hex_value}, float* %{self.tmp-1}, align 4"
            )
        elif type_ == Type.INT:
            # self.main_text += f"store i32 {value}, i32* %{self.tmp-1}, align 4\n"
            self.__append_text_main(f"store i32 {value}, i32* %{self.tmp-1}, align 4")
        elif type_ == Type.STR:
            # declare global string then load into anonymous pointer
            global_string_id = self.__declare_global_string(
                f"string_{self.str_tmp}", str(value)
            )
            self.str_tmp += 1
            str_length = len(str(value))
            # self.main_text += f"%{self.tmp} = getelementptr inbounds [{str_length+1} x i8], [{str_length+1} x i8]* {global_string_id}, i32 0, i32 0\n"
            self.__append_text_main(
                f"%{self.tmp} = getelementptr inbounds [{str_length+1} x i8], [{str_length+1} x i8]* {global_string_id}, i32 0, i32 0"
            )
            self.tmp += 1
        else:
            # self.main_text += f"store {type_} {value}, {type_}* %{self.tmp-1}\n"
            self.__append_text_main(f"store {type_} {value}, {type_}* %{self.tmp-1}")
        return f"%{self.tmp-1}"

    def assign_arr(self, id_: str, type_: Type, size: int, index: int, val):
        self.__validate_arr_size(size, index)
        # self.main_text += f"%{self.tmp} = getelementptr [{size} x {type_}], [{size} x {type_}]* %{id_}, i32 0, i32 {index}\n"
        # self.main_text += f"store {type_} {val}, {type_}* %{self.tmp}\n"

        self.__append_text_main(
            f"%{self.tmp} = getelementptr [{size} x {type_}], [{size} x {type_}]* %{id_}, i32 0, i32 {index}"
        )
        self.__append_text_main(f"store {type_} {val}, {type_}* %{self.tmp}")

        self.tmp += 1
        return f"%{self.tmp-1}"

    def declare_arr(self, id_: str, type_: Type, size: int):
        # self.main_text += f"%{id_} = alloca [{size} x {type_}], align 8\n"
        self.__append_text_main(f"%{id_} = alloca [{size} x {type_}], align 8")

    def access_arr(self, id_, type_: Type, size: int, index: int):
        self.__validate_arr_size(size, index)
        # self.main_text += f"%{self.tmp} = getelementptr [{size} x {type_}], [{size} x {type_}]* %{id_}, i32 0, i32 {index}\n"
        self.__append_text_main(
            f"%{self.tmp} = getelementptr [{size} x {type_}], [{size} x {type_}]* %{id_}, i32 0, i32 {index}"
        )
        self.tmp += 1
        # self.main_text += f"%{self.tmp} = load {type_}, {type_}* %{self.tmp-1}\n"
        self.__append_text_main(f"%{self.tmp} = load {type_}, {type_}* %{self.tmp-1}")
        self.tmp += 1
        return f"%{self.tmp-1}"

    def assign_arr2d(
        self, id_: str, type_: Type, rows: int, cols: int, r: int, c: int, val
    ):
        self.__validate_2d_size(rows, cols, r, c)
        size = rows * cols
        index = r * cols + c
        # self.main_text += f"%{self.tmp} = getelementptr [{size} x {type_}], [{size} x {type_}]* %{id_}, i32 0, i32 {index}\n"
        # self.main_text += f"store {type_} {val}, {type_}* %{self.tmp}\n"

        self.__append_text_main(
            f"%{self.tmp} = getelementptr [{size} x {type_}], [{size} x {type_}]* %{id_}, i32 0, i32 {index}"
        )
        self.__append_text_main(f"store {type_} {val}, {type_}* %{self.tmp}")

        self.tmp += 1
        return f"%{self.tmp-1}"

    def declare_arr2d(self, id_: str, type_: Type, rows: int, cols: int):
        size = rows * cols
        # self.main_text += f"%{id_} = alloca [{size} x {type_}], align 8\n"
        self.__append_text_main(f"%{id_} = alloca [{size} x {type_}], align 8")

    def access_arr2d(self, id_, type_: Type, rows: int, cols: int, r: int, c: int):
        self.__validate_2d_size(rows, cols, r, c)
        size = rows * cols
        index = r * cols + c
        # self.main_text += f"%{self.tmp} = getelementptr [{size} x {type_}], [{size} x {type_}]* %{id_}, i32 0, i32 {index}\n"
        self.__append_text_main(
            f"%{self.tmp} = getelementptr [{size} x {type_}], [{size} x {type_}]* %{id_}, i32 0, i32 {index}"
        )
        self.tmp += 1
        # self.main_text += f"%{self.tmp} = load {type_}, {type_}* %{self.tmp-1}\n"
        self.__append_text_main(f"%{self.tmp} = load {type_}, {type_}* %{self.tmp-1}")
        self.tmp += 1
        return f"%{self.tmp-1}"

    def add(self, id_1: str, id_2: str, type_: Type) -> str:
        ops = {
            Type.DOUBLE: "fadd",
            Type.INT: "add",
            Type.FLOAT: "fadd",
        }
        add_op = ops.get(type_, None)
        if add_op is None:
            raise ValueError(f"Type {type_} adding is not supported")
        # self.main_text += f"%{self.tmp} = {add_op} {type_} {id_1}, {id_2}\n"
        self.__append_text_main(f"%{self.tmp} = {add_op} {type_} {id_1}, {id_2}")
        self.tmp += 1
        return f"%{self.tmp-1}"

    def mul(self, id_1: str, id_2: str, type_: Type) -> str:
        ops = {
            Type.DOUBLE: "fmul",
            Type.INT: "mul",
            Type.FLOAT: "fmul",
        }
        mul_op = ops.get(type_, None)
        if mul_op is None:
            raise ValueError(f"Type {type_} multiplication is not supported")
        # self.main_text += f"%{self.tmp} = {mul_op} {type_} {id_1}, {id_2}\n"
        self.__append_text_main(f"%{self.tmp} = {mul_op} {type_} {id_1}, {id_2}")
        self.tmp += 1
        return f"%{self.tmp-1}"

    def sub(self, id_1: str, id_2: str, type_: Type) -> str:
        ops = {
            Type.DOUBLE: "fsub",
            Type.INT: "sub",
            Type.FLOAT: "fsub",
        }
        sub_op = ops.get(type_, None)
        if sub_op is None:
            raise ValueError(f"Type {type_} sub is not supported")
        # self.main_text += f"%{self.tmp} = {sub_op} {type_} {id_1}, {id_2}\n"
        self.__append_text_main(f"%{self.tmp} = {sub_op} {type_} {id_1}, {id_2}")
        self.tmp += 1
        return f"%{self.tmp-1}"

    def div(self, id_1: str, id_2: str, type_: Type) -> str:
        ops = {
            Type.DOUBLE: "fdiv",
            Type.INT: "sdiv",
            Type.FLOAT: "fdiv",
        }
        div_op = ops.get(type_, None)
        if div_op is None:
            raise ValueError(f"Type {type_} div is not supported")
        # self.main_text += f"%{self.tmp} = {div_op} {type_} {id_1}, {id_2}\n"
        self.__append_text_main(f"%{self.tmp} = {div_op} {type_} {id_1}, {id_2}")
        self.tmp += 1
        return f"%{self.tmp-1}"

    def bit_and(self, id_1: str, id_2: str, type_: Type) -> str:
        # self.main_text += f"%{self.tmp} = and {type_} {id_1}, {id_2}\n"
        self.__append_text_main(f"%{self.tmp} = and {type_} {id_1}, {id_2}")
        self.tmp += 1
        return f"%{self.tmp-1}"

    def bit_or(self, id_1: str, id_2: str, type_: Type) -> str:
        # self.main_text += f"%{self.tmp} = or {type_} {id_1}, {id_2}\n"
        self.__append_text_main(f"%{self.tmp} = or {type_} {id_1}, {id_2}")
        self.tmp += 1
        return f"%{self.tmp-1}"

    def bit_xor(self, id_1: str, id_2: str, type_: Type) -> str:
        # self.main_text += f"%{self.tmp} = xor {type_} {id_1}, {id_2}\n"
        self.__append_text_main(f"%{self.tmp} = xor {type_} {id_1}, {id_2}")
        self.tmp += 1
        return f"%{self.tmp-1}"

    def bit_not(self, id_: str, type_: Type) -> str:
        # self.main_text += f"%{self.tmp} = xor {type_} {id_}, -1\n"

        self.__append_text_main(f"%{self.tmp} = xor {type_} {id_}, -1")
        self.tmp += 1
        return f"%{self.tmp-1}"

    def logical_not(self, r_id: str, type_: Type) -> str:
        raise NotImplementedError()

    def assign(self, id_: str, value: tuple[str, Type]):
        id_value, type_ = value
        self.__store(id_, id_value, type_)

    def declare_variable(self, id_: str, type_: Type, is_global: bool) -> str:
        zero_str = type_.get_zero_str()
        context_sign, alloc_type, zero_str, append_text_fn = (
            ("@", "global", type_.get_zero_str(), self.__append_text_header)
            if is_global
            else ("%", "alloca", "", self.__append_text_main)
        )

        append_text_fn(f"{context_sign}{id_} = {alloc_type} {type_} {zero_str}\n")
        return f"{context_sign}{id_}"

    def if_start(self):
        l, _, r = Instruction.IF.value
        self.br += 1
        # self.main_text += (
        #     f"br i1 %{self.tmp-1}, label %{l}{self.br}, label %{r}{self.br}\n"
        # )
        # self.main_text += f"{l}{self.br}:\n"

        self.__append_text_main(
            f"br i1 %{self.tmp-1}, label %{l}{self.br}, label %{r}{self.br}"
        )
        self.__append_text_main(f"{l}{self.br}:")

        self.br_stack.append(self.br)

    def if_end(self):
        _, _, r = Instruction.IF.value
        br = self.br_stack.pop()
        # self.main_text += f"br label %{r}{br}\n"
        # self.main_text += f"{r}{br}:\n"

        self.__append_text_main(f"br label %{r}{br}")
        self.__append_text_main(f"{r}{br}:")

    def while_start_block(self):
        l, m, r = Instruction.WHILE.value
        br_while = self.br_while_stack[-1]
        # self.main_text += (
        #     f"br i1 %{self.tmp-1}, label %{m}{br_while}, label %{r}{br_while}\n"
        # )
        # self.main_text += f"{m}{br_while}:\n"

        self.__append_text_main(
            f"br i1 %{self.tmp-1}, label %{m}{br_while}, label %{r}{br_while}"
        )
        self.__append_text_main(f"{m}{br_while}:")

    def while_end(self):
        l, m, r = Instruction.WHILE.value
        br_while = self.br_while_stack.pop()
        # self.main_text += f"br label %{l}{br_while}\n"
        # self.main_text += f"{r}{br_while}:\n"

        self.__append_text_main(f"br label %{l}{br_while}")
        self.__append_text_main(f"{r}{br_while}:")

    def while_start(self):
        l, m, r = Instruction.WHILE.value
        self.br_while += 1
        # self.main_text += f"br label %{l}{self.br_while}\n"
        # self.main_text += f"{l}{self.br_while}:\n"

        self.__append_text_main(f"br label %{l}{self.br_while}")
        self.__append_text_main(f"{l}{self.br_while}:")

        self.br_while_stack.append(self.br_while)

    def icmp(self, id_: str, type_: Type):
        zero = type_.get_zero_str()
        compare, not_equal = type_.get_icmp()
        # self.main_text += f"%{self.tmp} = {compare} {not_equal} {type_} {id_}, {zero}\n"
        self.__append_text_main(
            f"%{self.tmp} = {compare} {not_equal} {type_} {id_}, {zero}"
        )
        self.tmp += 1
        return f"%{self.tmp-1}"

    def fn_start(self, id_: str, type_: Type, args: list[tuple[str, Type]]):
        params_str = ", ".join([f"{type_} %{id_}" for id_, type_ in args])
        # self.main_text += f"define {type_} @{id_}({params_str}) {'{'}\n"
        self.__append_text_main(f"define {type_} @{id_}({params_str}) {'{'}")

    def fn_end(self, id_: str | None, type_: Type):
        return_str = "void" if id_ is None else f"{type_} %{id_}"
        # self.main_text += f"ret {return_str}\n{'}'}\n"
        self.__append_text_main(f"ret {return_str}\n{'}'}")

    def fn_call(self, id_: str, type_returned: Type, args: list[tuple[Type, str]]):
        params_str = ", ".join([f"{type_} {val}" for type_, val in args])
        # self.main_text += f"%{self.tmp} = call {type_returned} @{id_}({params_str})\n"
        self.__append_text_main(
            f"%{self.tmp} = call {type_returned} @{id_}({params_str})"
        )
        self.tmp += 1

    # --------------------------------------------------------------------------------
    # ---------------------------PRIVATE METHODS -------------------------------------
    # --------------------------------------------------------------------------------

    def __store(self, id_: str, value: str, type_: Type):
        # self.main_text += f"store {type_} {value}, {type_}* {id_}\n"
        self.__append_text_main(f"store {type_} {value}, {type_}* {id_}")

    def __declare_global_string(self, name: str, value: str) -> str:
        # self.header_text += f'@{name} = constant [{len(value)+1} x i8] c"{value}\\00"\n'
        self.__append_text_header(
            f'@{name} = constant [{len(value)+1} x i8] c"{value}\\00"'
        )
        return f"@{name}"

    def __validate_2d_size(self, rows: int, cols: int, r: int, c: int):
        if r >= rows or c >= cols:
            raise ValueError(f"Out of bounds for column: {c} row: {r}")

    def __validate_arr_size(self, index: int, i: int):
        if i >= index:
            raise ValueError(f"Out of bounds for index: {i}")

    def __append_text_header(self, line: str, skip_new_line: bool = False):
        newline = "" if skip_new_line else "\n"
        self.__header_text += f"{line}{newline}"

    def __append_text_main(self, line: str, skip_new_line: bool = False):
        newline = "" if skip_new_line else "\n"
        self.__main_text += f"{line}{newline}"

    def __generate(self) -> str:
        declarations = [
            "declare i32 @printf(i8*, ...)",
            "declare i32 @__isoc99_scanf(i8*, ...)",
            '@strp = constant [4 x i8] c"%d\\0A\\00"',
            '@strlf = constant [4 x i8] c"%lf\\00"',
            '@strlfn = constant [5 x i8] c"%lf\\0A\\00"',
            '@strs = constant [3 x i8] c"%d\\00"',
            '@strstr = constant [4 x i8] c"%s\\0A\\00"',
            '@str_int_newline = constant [4 x i8] c"%d\\0A\\00"',
            '@str_double_newline = constant [5 x i8] c"%lf\\0A\\00"',
            '@str_string_newline = constant [4 x i8] c"%s\\0A\\00"',
            '@str_float_newline = constant [4 x i8] c"%f\\0A\\00"',
            '@str_int = constant [3 x i8] c"%d\\00"',
            '@str_double = constant [4 x i8] c"%lf\\00"',
            '@str_string = constant [3 x i8] c"%s\\00"',
            '@str_float = constant [3 x i8] c"%f\\00"',
        ]

        definitions = [
            self.__header_text,
            "define i32 @main() nounwind {",
            self.__main_text,
            "ret i32 0 }",
        ]

        return "\n".join(declarations + definitions)
