from typing import Callable
from .enums import TmpCounter, Context


class TextGenerator:
    START_TMP = 1
    START_TMP_STR = 1
    START_TMP_FN = 1

    def __init__(self):
        self.__main_text = ""
        self.__header_text = ""
        self.__fn_text = ""

        self.__current_context: Context = Context.MAIN  # FIXME: ?

        self.__tmp = TextGenerator.START_TMP
        self.__tmp_str = TextGenerator.START_TMP_STR
        self.__tmp_fn = TextGenerator.START_TMP_FN

    def generate(self) -> str:
        functions = [self.__fn_text]

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

        return "\n".join(functions + declarations + definitions)

    def append_text(
        self,
        line: str,
        skip_new_line: bool = False,
        context: Context | None = None,
    ):
        context = self.__current_context if context is None else context  # override
        append_context_mappings: dict[Context, Callable[[str], None]] = {
            Context.MAIN: self.__append_to_main_text,
            Context.HEADER: self.__append_to_header_text,
            Context.FUNCTION: self.__append_to_fn_text,
        }
        setter_fn = append_context_mappings.get(context, None)
        if setter_fn is None:
            raise ValueError(f"Type {context} is not supported")
        newline = "" if skip_new_line else "\n"
        setter_fn(f"{line}{newline}")

    def get_incremented(self, counter: TmpCounter = TmpCounter.TMP):
        mappings: dict[TmpCounter, int] = {
            TmpCounter.TMP: self.__tmp,
            TmpCounter.TMP_STR: self.__tmp_str,
            TmpCounter.TMP_FN: self.__tmp_fn,
        }
        incremented_val = mappings.get(counter, None)

        if not incremented_val:
            raise ValueError(f"Type: {counter} not supported")
        incremented_val = (
            self.__tmp_fn
            if self.__current_context == Context.FUNCTION
            else incremented_val
        )
        return incremented_val

    def increment(
        self,
        # counter: TmpCounter = TmpCounter.TMP,
        increment_value: int = 1,
        reset_val: bool = False,
        override_str: bool = False,
    ):
        context = self.__current_context

        mappings: dict[Context, Callable[[int, bool], None]] = {
            # TmpCounter.TMP: self.__increment_tmp,
            # TmpCounter.TMP_STR: self.__increment_str,
            # TmpCounter.TMP_FN: self.__increment_fn,
            Context.MAIN: self.__increment_tmp,
            Context.FUNCTION: self.__increment_fn,
            # Context.HEADER: self.__increment_tmp,
        }
        increment_fn = mappings.get(context, None)
        if override_str:
            increment_fn = self.__increment_str

        if not increment_fn:
            raise ValueError(f"Not supported")
        # increment_fn = (
        #     self.__increment_fn
        #     if self.__current_context == Context.FUNCTION
        #     else increment_fn
        # )
        increment_fn(increment_value, reset_val)

    def set_current_context(self, context: Context):
        self.__current_context = context

    # '''

    # fn
    # ...
    # printf("sdsadasd")
    # a = "sdsds"
    # ...
    # nf

    # declare_global_string
    #   oldContext = FUNCTION
    #     currentContext = HEADER
    #     add string
    #  set_context(oldContext)

    # '''
    def reset_function_counter(self):
        self.__tmp_fn = self.START_TMP_FN

    def get_current_context(self):
        return self.__current_context

    # --------------------------------------------------------------------------------
    # --------------------------- PRIVATE METHODS ------------------------------------
    # --------------------------------------------------------------------------------

    def __increment_tmp(self, increment_value: int, reset_val: bool = False):
        if reset_val:
            self.__tmp = self.START_TMP
            return
        self.__tmp += increment_value

    def __increment_str(self, increment_value: int, reset_val: bool = False):
        if reset_val:
            self.__tmp_str = self.START_TMP_STR
            return
        self.__tmp_str += increment_value

    def __increment_fn(self, increment_value: int, reset_val: bool = False):
        if reset_val:
            self.__tmp_fn = self.START_TMP_FN
            return
        self.__tmp_fn += increment_value

    def __append_to_main_text(self, line: str):
        self.__main_text += line

    def __append_to_header_text(self, line: str):
        self.__header_text += line

    def __append_to_fn_text(self, line: str):
        self.__fn_text += line
