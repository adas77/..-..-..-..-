from enum import Enum

from LLVMGenerator import LLVMGenerator, Type


class VarType(Enum):
    GLOBAL_VAR = ("global_var",)
    LOCAL_VAR = ("local_var",)
    FN_VAR = ("fn_var",)
    STRUCT_VAR = ("struct_var",)
    ARRAY_VAR = ("array_var",)


class Memory:
    def __init__(self):
        self.global_variables: dict[str, dict] = {}
        self.local_variables: dict[str, dict] = {}
        self.functions: dict[str, dict] = {}
        self.structs: dict[str, dict] = {}
        self.arrays: dict[str, dict] = {}

        self.stack: list[tuple[str, Type]] = []
        self.__global_context: bool = True  # FIXME: __global_context is never mutated
        # self.value_: tuple[str, Type] | None = None
        # self.function_: str = ""

    def get(self, id_: str, var_type: VarType):
        var_type_dict = self._get_var_type(var_type)
        if var_type_dict is None:
            raise ValueError(f"{var_type} does not exist")
        value = var_type_dict.get(id_, None)
        if value is None:
            raise ValueError(f"Variable with ID: {id_} does not exist")
        return value

    def get_arr(self, id_: str):
        arr_val = self.arrays.get(id_)
        if arr_val is None:
            raise ValueError(f"Array with ID: {id_} does not exist")
        arr_data = arr_val.get("data", None)
        if arr_data is None:
            raise Exception("Array does not have data property")
        return arr_data

    def get_variable(self, id_: str):
        local_variable = self.local_variables.get(id_, None)
        global_variable = self.global_variables.get(id_, None)

        if local_variable is not None:
            final_id = ("%", id_, local_variable)
        elif global_variable is not None:
            final_id = ("@", id_, global_variable)
        else:
            raise ValueError(f"{id_} not found")

        return final_id

    def add(
        self, id_: str, type_: Type, var_type: VarType, locked_type: bool, data=None
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
            "data": data,
        }

    def set_variable(
        self,
        generator: LLVMGenerator,
        id_: str,
        assign_type: Type,
        locked_type: bool = False,
    ):
        context_sign, var_type, dict_variables = (
            ("@", VarType.GLOBAL_VAR, self.global_variables)
            if self.__global_context
            else ("%", VarType.LOCAL_VAR, self.local_variables)
        )
        variable = dict_variables.get(id_, None)
        if variable is None:
            self.add(id_, assign_type, var_type, locked_type)
            generator.declare_variable(id_, assign_type, self.__global_context)
            variable = self.global_variables.get(id_, None)
            if variable is None:
                raise Exception("variable is None")
        else:
            if variable["locked_type"]:
                if variable["type_"] != assign_type:
                    raise ValueError(
                        f"Types: {variable['type_']} must match {assign_type}"
                    )

        return context_sign, id_, variable

    def _get_var_type(self, var_type: VarType) -> dict | None:
        var_type_mappings = {
            VarType.GLOBAL_VAR: self.global_variables,
            VarType.LOCAL_VAR: self.local_variables,
            VarType.FN_VAR: self.functions,
            VarType.STRUCT_VAR: self.structs,
            VarType.ARRAY_VAR: self.arrays,
        }
        var_type_dict = var_type_mappings.get(var_type, None)
        return var_type_dict
