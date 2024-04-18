from enum import Enum

BOOUND_DOUBLE = "[4 x i8], [4 x i8]*"
BOOUND_OTHER = "[3 x i8], [3 x i8]*"


class TmpCounter(Enum):
    TMP = (1,)
    TMP_STR = (2,)
    TMP_FN = (3,)


class Instruction(Enum):
    WHILE = ("while", "while_body", "elihw")
    IF = ("if", "if_body", "fi")


class Type(Enum):
    INT = ("i32",)
    DOUBLE = ("double",)
    STR = ("i8*",)
    FLOAT = ("float",)
    VOID = ("void",)

    def __str__(self):
        return f"{self.value[0]}"

    @staticmethod
    def map_(type_: str):
        types_mappings = {
            "int": Type.INT,
            "double": Type.DOUBLE,
            "string": Type.STR,
            "float": Type.FLOAT,
            "void": Type.VOID,
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

    def get_print_str(self, newline: bool = False) -> str:
        # TODO:
        newline_str = "_newline" if newline else ""
        print_mappings: dict[Type, tuple[str, str]] = {
            Type.INT: ("@str_int", BOOUND_OTHER),
            Type.DOUBLE: ("@str_int", BOOUND_DOUBLE),
            Type.FLOAT: ("@str_float", BOOUND_OTHER),
            Type.STR: ("@str_string", BOOUND_OTHER),
        }
        res = print_mappings.get(self, None)
        if res is None:
            raise ValueError(f"Cannot get printstr for type: {self}")
        return f"{res}{newline_str}"


class Context(Enum):
    HEADER = (1,)
    MAIN = (2,)
    FUNCTION = (3,)

    def get_context_sign(self) -> str:
        return "%" if self == Context.FUNCTION else "@"
