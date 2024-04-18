import struct

from .text_generator import TextGenerator
from .enums import Instruction, TmpCounter, Type, Context


class LLVMGenerator:
    def __init__(self, file_path: str = "./code.ll"):
        self.file_path = file_path
        self.text_generator = TextGenerator()

        self.br = 0
        self.br_stack: list[int] = []

        self.br_while = 0
        self.br_while_stack: list[int] = []

    def save(self):
        with open(self.file_path, "w+") as f:
            f.write(self.text_generator.generate())

    def scanf(self, id_: str, type_: Type):
        if type_ == Type.INT:
            self.text_generator.append_text(
                f"%{self.text_generator.get_incremented()} = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @str_int, i32 0, i32 0),i32* {id_})"
            )
        elif type_ == Type.DOUBLE:
            self.text_generator.append_text(
                f"%{self.text_generator.get_incremented()} = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_double, i32 0, i32 0),double* {id_})"
            )
        elif type_ == Type.FLOAT:
            self.text_generator.append_text(
                f"%{self.text_generator.get_incremented()} = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @str_float, i32 0, i32 0),float* {id_})"
            )
        elif type_ == Type.STR:
            self.text_generator.append_text(
                f"%{self.text_generator.get_incremented()} = alloca i8, i32 100"
            )
            self.text_generator.increment()
            self.text_generator.append_text(
                f"%{self.text_generator.get_incremented()} = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @str_string, i32 0, i32 0),i8* %{self.text_generator.get_incremented()-1})"
            )
            self.text_generator.append_text(
                f"store i8* %{self.text_generator.get_incremented()-1}, i8** {id_}"
            )

        else:
            raise ValueError(f"Type {type_} scanning is not supported")
        self.text_generator.increment()

    def printf(self, id_: str, type_: Type):
        if type_ == Type.INT:
            self.text_generator.append_text(
                f"%{self.text_generator.get_incremented()} = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_int_newline, i32 0, i32 0),i32 {id_})"
            )
        elif type_ == Type.DOUBLE:
            self.text_generator.append_text(
                f"%{self.text_generator.get_incremented()} = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([5 x i8], [5 x i8]* @str_double_newline, i32 0, i32 0),double {id_})"
            )
        elif type_ == Type.FLOAT:
            self.text_generator.append_text(
                f"%{self.text_generator.get_incremented()} = fpext float {id_} to double"
            )
            self.text_generator.increment()
            self.text_generator.append_text(
                f"%{self.text_generator.get_incremented()} = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_float_newline, i32 0, i32 0),double %{self.text_generator.get_incremented()-1})"
            )
        elif type_ == Type.STR:
            self.text_generator.append_text(
                f"%{self.text_generator.get_incremented()} = load i8*, i8** {id_}"
            )
            self.text_generator.increment()
            self.text_generator.append_text(
                f"%{self.text_generator.get_incremented()}  = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @str_string_newline, i32 0, i32 0),i8* %{self.text_generator.get_incremented()-1})"
            )

        else:
            raise ValueError(f"Type {type_} printing is not supported")
        self.text_generator.increment()

    def load(
        self, id_new: str, type_: Type, id_old: str | None = None, str_length: int = 0
    ) -> str:
        if type_ == Type.STR:
            return id_new
        if id_old is None:
            # if id_old is not passed, create new id
            self.text_generator.append_text(
                f"%{self.text_generator.get_incremented()} = load {type_}, {type_}* {id_new}"
            )

            self.text_generator.increment()
            return f"%{self.text_generator.get_incremented()-1}"
        else:
            self.text_generator.append_text(
                f"%{id_old} = load {type_}, {type_}* {id_new}"
            )
            return f"%{id_old}"

    def assign_anonymous(self, value: str, type_: Type) -> tuple[str, Type]:
        self.text_generator.append_text(
            f"%{self.text_generator.get_incremented()} = alloca {type_}"
        )
        self.text_generator.increment()

        if type_ == Type.DOUBLE:
            hex_value = struct.pack(">d", float(value)).hex()
            self.text_generator.append_text(
                f"store double 0x{hex_value}, double* %{self.text_generator.get_incremented()-1}, align 4"
            )
        elif type_ == Type.FLOAT:
            hex_value = struct.pack(">d", float(value)).hex()[0:8] + "00000000"
            self.text_generator.append_text(
                f"store float 0x{hex_value}, float* %{self.text_generator.get_incremented()-1}, align 4"
            )
        elif type_ == Type.INT:
            self.text_generator.append_text(
                f"store i32 {value}, i32* %{self.text_generator.get_incremented()-1}, align 4"
            )
        elif type_ == Type.STR:
            global_string_id = self.__declare_global_string(
                f"string_{self.text_generator.get_incremented(TmpCounter.TMP_STR)}",
                str(value),
            )
            self.text_generator.increment(override_str=True)
            str_length = len(str(value))
            self.text_generator.append_text(
                f"%{self.text_generator.get_incremented()} = getelementptr inbounds [{str_length+1} x i8], [{str_length+1} x i8]* {global_string_id}, i32 0, i32 0"
            )
            self.text_generator.increment()
            self.text_generator.append_text(
                f"store i8* %{self.text_generator.get_incremented()-1}, i8** %{self.text_generator.get_incremented()-2}"
            )
            anon_id = f"%{self.text_generator.get_incremented()-2}"
            anon_id = self.load(anon_id, type_, str_length=str_length)
            return anon_id, type_
        else:
            self.text_generator.append_text(
                f"store {type_} {value}, {type_}* %{self.text_generator.get_incremented()-1}"
            )

        anon_id = f"%{self.text_generator.get_incremented()-1}"
        anon_id = self.load(
            anon_id, type_, str_length=len(value) if type_ == Type.STR else 0
        )
        return anon_id, type_

    def assign_arr(self, id_: str, type_: Type, size: int, index: int, val):
        self.__validate_arr_size(size, index)
        self.text_generator.append_text(
            f"%{self.text_generator.get_incremented()} = getelementptr [{size} x {type_}], [{size} x {type_}]* %{id_}, i32 0, i32 {index}"
        )
        self.text_generator.append_text(
            f"store {type_} {val}, {type_}* %{self.text_generator.get_incremented()}"
        )
        self.text_generator.increment()
        return f"%{self.text_generator.get_incremented()-1}"

    def declare_arr(self, id_: str, type_: Type, size: int):
        self.text_generator.append_text(f"%{id_} = alloca [{size} x {type_}], align 8")

    def access_arr(self, id_, type_: Type, size: int, index: int):
        self.__validate_arr_size(size, index)
        self.text_generator.append_text(
            f"%{self.text_generator.get_incremented()} = getelementptr [{size} x {type_}], [{size} x {type_}]* %{id_}, i32 0, i32 {index}"
        )
        self.text_generator.increment()
        self.text_generator.append_text(
            f"%{self.text_generator.get_incremented()} = load {type_}, {type_}* %{self.text_generator.get_incremented()-1}"
        )
        self.text_generator.increment()
        return f"%{self.text_generator.get_incremented()-1}"

    def assign_arr2d(
        self, id_: str, type_: Type, rows: int, cols: int, r: int, c: int, val
    ):
        self.__validate_2d_size(rows, cols, r, c)
        size = rows * cols
        index = r * cols + c
        self.text_generator.append_text(
            f"%{self.text_generator.get_incremented()} = getelementptr [{size} x {type_}], [{size} x {type_}]* %{id_}, i32 0, i32 {index}"
        )
        self.text_generator.append_text(
            f"store {type_} {val}, {type_}* %{self.text_generator.get_incremented()}"
        )
        self.text_generator.increment()
        return f"%{self.text_generator.get_incremented()-1}"

    def declare_arr2d(self, id_: str, type_: Type, rows: int, cols: int):
        size = rows * cols
        self.text_generator.append_text(f"%{id_} = alloca [{size} x {type_}], align 8")

    def access_arr2d(self, id_, type_: Type, rows: int, cols: int, r: int, c: int):
        self.__validate_2d_size(rows, cols, r, c)
        size = rows * cols
        index = r * cols + c
        self.text_generator.append_text(
            f"%{self.text_generator.get_incremented()} = getelementptr [{size} x {type_}], [{size} x {type_}]* %{id_}, i32 0, i32 {index}"
        )
        self.text_generator.increment()
        self.text_generator.append_text(
            f"%{self.text_generator.get_incremented()} = load {type_}, {type_}* %{self.text_generator.get_incremented()-1}"
        )
        self.text_generator.increment()
        return f"%{self.text_generator.get_incremented()-1}"

    def add(self, id_1: str, id_2: str, type_: Type) -> str:
        ops = {
            Type.DOUBLE: "fadd",
            Type.INT: "add",
            Type.FLOAT: "fadd",
        }
        add_op = ops.get(type_, None)
        if add_op is None:
            raise ValueError(f"Type {type_} adding is not supported")
        self.text_generator.append_text(
            f"%{self.text_generator.get_incremented()} = {add_op} {type_} {id_1}, {id_2}"
        )
        self.text_generator.increment()
        return f"%{self.text_generator.get_incremented()-1}"

    def mul(self, id_1: str, id_2: str, type_: Type) -> str:
        ops = {
            Type.DOUBLE: "fmul",
            Type.INT: "mul",
            Type.FLOAT: "fmul",
        }
        mul_op = ops.get(type_, None)
        if mul_op is None:
            raise ValueError(f"Type {type_} multiplication is not supported")
        self.text_generator.append_text(
            f"%{self.text_generator.get_incremented()} = {mul_op} {type_} {id_1}, {id_2}"
        )
        self.text_generator.increment()
        return f"%{self.text_generator.get_incremented()-1}"

    def sub(self, id_1: str, id_2: str, type_: Type) -> str:
        ops = {
            Type.DOUBLE: "fsub",
            Type.INT: "sub",
            Type.FLOAT: "fsub",
        }
        sub_op = ops.get(type_, None)
        if sub_op is None:
            raise ValueError(f"Type {type_} sub is not supported")
        self.text_generator.append_text(
            f"%{self.text_generator.get_incremented()} = {sub_op} {type_} {id_1}, {id_2}"
        )
        self.text_generator.increment()
        return f"%{self.text_generator.get_incremented()-1}"

    def div(self, id_1: str, id_2: str, type_: Type) -> str:
        ops = {
            Type.DOUBLE: "fdiv",
            Type.INT: "sdiv",
            Type.FLOAT: "fdiv",
        }
        div_op = ops.get(type_, None)
        if div_op is None:
            raise ValueError(f"Type {type_} div is not supported")
        self.text_generator.append_text(
            f"%{self.text_generator.get_incremented()} = {div_op} {type_} {id_1}, {id_2}"
        )
        self.text_generator.increment()
        return f"%{self.text_generator.get_incremented()-1}"

    def bit_and(self, id_1: str, id_2: str, type_: Type) -> str:
        self.text_generator.append_text(
            f"%{self.text_generator.get_incremented()} = and {type_} {id_1}, {id_2}"
        )
        self.text_generator.increment()
        return f"%{self.text_generator.get_incremented()-1}"

    def bit_or(self, id_1: str, id_2: str, type_: Type) -> str:
        self.text_generator.append_text(
            f"%{self.text_generator.get_incremented()} = or {type_} {id_1}, {id_2}"
        )
        self.text_generator.increment()
        return f"%{self.text_generator.get_incremented()-1}"

    def bit_xor(self, id_1: str, id_2: str, type_: Type) -> str:
        self.text_generator.append_text(
            f"%{self.text_generator.get_incremented()} = xor {type_} {id_1}, {id_2}"
        )
        self.text_generator.increment()
        return f"%{self.text_generator.get_incremented()-1}"

    def bit_not(self, id_: str, type_: Type) -> str:
        self.text_generator.append_text(
            f"%{self.text_generator.get_incremented()} = xor {type_} {id_}, -1"
        )
        self.text_generator.increment()
        return f"%{self.text_generator.get_incremented()-1}"

    def logical_not(self, r_id: str, type_: Type) -> str:
        raise NotImplementedError()

    def assign(self, id_: str, value: tuple[str, Type]):
        id_value, type_ = value
        if type_ == Type.STR:
            self.text_generator.append_text(
                f"%{self.text_generator.get_incremented()} = load i8*, i8** {id_value}"
            )
            self.text_generator.increment()
            self.text_generator.append_text(
                f"store i8* %{self.text_generator.get_incremented()-1}, i8** {id_}"
            )
            return
        self.__store(id_, id_value, type_)

    def declare_variable(
        self,
        id_: str,
        type_: Type,
    ) -> str:

        context = self.text_generator.get_current_context()
        zero_str = type_.get_zero_str()
        alloc_type, zero_str = (
            ("global", type_.get_zero_str())
            if context != Context.FUNCTION
            else ("alloca", "")
        )

        self.text_generator.append_text(
            f"{id_} = {alloc_type} {type_} {zero_str}",
            context=Context.HEADER if context != Context.FUNCTION else Context.FUNCTION,
        )
        return f"{id_}"

    def if_start(self):
        l, _, r = Instruction.IF.value
        self.br += 1
        self.text_generator.append_text(
            f"br i1 %{self.text_generator.get_incremented()-1}, label %{l}{self.br}, label %{r}{self.br}"
        )
        self.text_generator.append_text(f"{l}{self.br}:")
        self.br_stack.append(self.br)

    def if_end(self):
        _, _, r = Instruction.IF.value
        br = self.br_stack.pop()
        self.text_generator.append_text(f"br label %{r}{br}")
        self.text_generator.append_text(f"{r}{br}:")

    def while_start_block(self):
        _, m, r = Instruction.WHILE.value
        br_while = self.br_while_stack[-1]
        self.text_generator.append_text(
            f"br i1 %{self.text_generator.get_incremented()-1}, label %{m}{br_while}, label %{r}{br_while}"
        )
        self.text_generator.append_text(f"{m}{br_while}:")

    def while_end_block(self):
        l, _, r = Instruction.WHILE.value
        br_while = self.br_while_stack.pop()
        self.text_generator.append_text(f"br label %{l}{br_while}")
        self.text_generator.append_text(f"{r}{br_while}:")

    def while_start(self):
        l, _, _ = Instruction.WHILE.value
        self.br_while += 1
        self.text_generator.append_text(f"br label %{l}{self.br_while}")
        self.text_generator.append_text(f"{l}{self.br_while}:")
        self.br_while_stack.append(self.br_while)

    def icmp(self, id_: str, type_: Type):
        zero = type_.get_zero_str()
        compare, not_equal = type_.get_icmp()
        self.text_generator.append_text(
            f"%{self.text_generator.get_incremented()} = {compare} {not_equal} {type_} {id_}, {zero}"
        )
        self.text_generator.increment()
        return f"%{self.text_generator.get_incremented()-1}"

    def fn_start(self, id_: str, type_: Type, args: list[tuple[str, Type, str | None]]):
        params_str = ""
        start_counter_value = self.text_generator.get_incremented()
        for arg_id_, arg_type_, arg_mut in args:
            params_str += f"{arg_type_} %{self.text_generator.get_incremented()}, "
            self.text_generator.increment()
        params_str = params_str[:-2]

        # self.text_generator.get_incremented()
        # params_str = ", ".join([f"{type_} {}" for id_, type_, mut in args])
        # self.text_generator.append_text(f"define {type_} @{id_}({params_str}) {'{'}")
        self.text_generator.append_text(f"define {type_} @{id_}({params_str}) {{")

        self.text_generator.increment()
        for arg_id_, arg_type_, arg_mut in args:
            self.text_generator.append_text(
                f"{arg_id_} = alloca {arg_type_}", context=Context.FUNCTION
            )  # TODO add alloca for args dor each type
            self.text_generator.append_text(
                f"store {arg_type_} %{start_counter_value}, {arg_type_}* {arg_id_}",
                context=Context.FUNCTION,
            )
            start_counter_value += 1

        # add alloca for args

    def fn_end(self, id_: str | None, type_: Type):
        returned_id = ""
        if id_ is not None:
            returned_id = self.load(f"{id_}", type_)

        return_str = "void" if id_ is None else f"{type_} {returned_id}"
        self.text_generator.append_text(f"ret {return_str}\n{'}'}")

        self.text_generator.set_current_context(Context.MAIN)  # FIXME

    def fn_call(
        self,
        id_: str,
        type_returned: Type,
        args: list[tuple[tuple[str, Type], str, str | None]],
    ):
        params_str = ", ".join(
            [f"{type_} {id_or_val}" for (id_or_val, type_), param_name, mut in args]
        )

        self.text_generator.append_text(
            f"%{self.text_generator.get_incremented()} = call {type_returned} @{id_}({params_str})"
        )
        self.text_generator.increment()

    # --------------------------------------------------------------------------------
    # --------------------------- PRIVATE METHODS ------------------------------------
    # --------------------------------------------------------------------------------

    def __store(self, id_: str, value: str, type_: Type):
        self.text_generator.append_text(f"store {type_} {value}, {type_}* {id_}")

    def __declare_global_string(self, name: str, value: str) -> str:
        old_context = self.text_generator.get_current_context()
        self.text_generator.set_current_context(Context.HEADER)
        self.text_generator.append_text(
            f'@{name} = constant [{len(value)+1} x i8] c"{value}\\00"',
        )
        self.text_generator.set_current_context(old_context)
        return f"@{name}"

    def __validate_2d_size(self, rows: int, cols: int, r: int, c: int):
        if r >= rows or c >= cols:
            raise ValueError(f"Out of bounds for column: {c} row: {r}")

    def __validate_arr_size(self, index: int, i: int):
        if i >= index:
            raise ValueError(f"Out of bounds for index: {i}")
