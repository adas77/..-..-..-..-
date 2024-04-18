from .text_generator import TextGenerator
from .generator import LLVMGenerator, Type
from .enums import Context


class Memory:
    def __init__(self):
        self.t = TextGenerator()

        self.__global_variables: dict[str, dict] = {}
        self.__local_variables: dict[str, dict] = {}
        # self.__functions: dict[str, dict] = {}
        # self.__structs: dict[str, dict] = {}
        # self.__arrays: dict[str, dict] = {}

        self.stack: list[tuple[str, Type]] = []

    def get(self, id_: str, var_type: Context):
        var_type_dict = self.__get_var_type(var_type)
        if var_type_dict is None:
            raise ValueError(f"{var_type} does not exist")
        value = var_type_dict.get(id_, None)
        if value is None:
            raise ValueError(f"Variable with ID: {id_} does not exist")
        return value

    def get_arr(self, id_: str):
        # arr_val = self.__arrays.get(id_)
        context = self.t.get_current_context()
        arr_val = self.get(id_, context)

        if arr_val is None:
            raise ValueError(f"Array with ID: {id_} does not exist")
        arr_data = arr_val.get("data", None)
        if arr_data is None:
            raise Exception("Array does not have data property")
        return arr_data

    def get_variable(self, id_: str):
        context = self.t.get_current_context()
        variable = self.get(id_, context)
        return context.get_context_sign(), id_, variable

        # pass
        # local_variable = self.__local_variables.get(id_, None)
        # global_variable = self.__global_variables.get(id_, None)
        # # functions = self.__functions.get(id_, None)
        # # arrays = self.__arrays.get(id_, None)

        # if local_variable is not None:
        #     final_id = ("%", id_, local_variable)
        # elif global_variable is not None:
        #     final_id = ("@", id_, global_variable)

        # else:
        #     raise ValueError(f"{id_} not found")

        # return final_id

    def copy_global_to_local(self, id_: str):
        global_variable = self.__global_variables.get(id_, None)
        if global_variable is None:
            raise ValueError(f"{id_} not found")
        local_variable = self.__local_variables.get(id_, None)
        if local_variable is not None:
            raise ValueError(f"{id_} already exists in local variables")
        self.__local_variables[id_] = global_variable

    def add(
        self,
        id_: str,
        type_: Type,
        locked_type: bool,
        data=None,
        # context
    ):
        context = self.t.get_current_context()
        var_type_dict = self.__get_var_type(context)
        if var_type_dict is None:
            raise ValueError(f"{context} does not exist")
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
        context = self.t.get_current_context()
        dict_variables = self.__get_var_type(context)
        if dict_variables is None:
            raise Exception()
        variable = dict_variables.get(id_, None)
        if variable is None:
            self.add(id_, assign_type, locked_type)
            generator.declare_variable(id_, assign_type)
            variable = self.get(id_, context)
        else:
            if variable["locked_type"]:
                if variable["type_"] != assign_type:
                    raise ValueError(
                        f"Types: {variable['type_']} must match {assign_type}"
                    )
        return context.get_context_sign(), id_, variable

    def __get_var_type(self, context: Context) -> dict | None:
        var_type_mappings = {
            Context.FUNCTION: self.__local_variables,  # TODO: remove from memory after exiting function
            Context.HEADER: self.__global_variables,
            Context.MAIN: self.__global_variables,
        }
        var_type_dict = var_type_mappings.get(context, None)
        return var_type_dict
