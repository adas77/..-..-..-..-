from enum import Enum

from LLVMGenerator import Type


class VarType(Enum):
    GLOBAL_VAR = ("global_var",)
    LOCAL_VAR = ("local_var",)
    FN_VAR = ("fn_var",)
    STRUCT_VAR = ("struct_var",)


class Memory:
    def __init__(self):
        self.global_variables: dict[str, object] = {}
        self.local_variables: dict[str, object] = {}
        self.functions: dict[str, object] = {}
        self.structs: dict[str, object] = {}

        self.stack: list[tuple[str, Type]] = []
        self.global_context: bool = True
        self.value_: tuple[str, Type] = None
        self.function_: str = ""

    def get(self, id_: str, var_type: VarType):
        var_type_dict = self._get_var_type(var_type)
        if var_type_dict is None:
            raise ValueError(f"{var_type} does not exist")
        value = var_type_dict.get(id_, None)
        if value is None:
            raise ValueError(f"Variable with ID: {id_} does not exist")
        return value

    def add_variable(
        self, id_: str, type_: str, var_type: VarType, locked_type: bool, data=None
    ):
        var_type_dict = self._get_var_type(var_type)
        if var_type_dict is None:
            raise ValueError(f"{var_type} does not exist")
        id_exists = var_type_dict.get(id_, None) is not None
        if id_exists:
            raise ValueError(f"Variable with ID: {id_} already exist")
        var_type_dict[id_] = {
            "type_": type_,
            "locked_type": locked_type,
            data: data,
        }

    def _get_var_type(self, var_type: VarType) -> dict | None:
        var_type_mappings = {
            VarType.GLOBAL_VAR: self.global_variables,
            VarType.LOCAL_VAR: self.local_variables,
            VarType.FN_VAR: self.functions,
            VarType.STRUCT_VAR: self.structs,
        }
        var_type_dict = var_type_mappings.get(var_type, None)
        return var_type_dict

    # def get_variable(self, id_:str):
    #     if not self.variable_exists(id_):
    #         raise ValueError(f"{id_} not found")
    #     return self.memory.get(id_)

    # def add_variable(self, id_:str, type_:str, locked_type:bool, data = None):
    #     if self.variable_exists(id_):
    #         raise ValueError(f"{id_} already declared")
    #     self.memory[id_] = {
    #         "type": type_,
    #         "locked_type": locked_type,
    #         "data": data
    #     }
