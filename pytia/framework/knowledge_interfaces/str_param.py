from pytia.framework.knowledge_interfaces.parameter import Parameter


class StrParam(Parameter):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.str_param = com_object

    @property
    def value(self) -> str:
        return self.str_param.Value

    @value.setter
    def value(self, value: str):
        self.str_param.Value = value

    def get_enumerate_values(self, o_safe_array: tuple) -> None:
        return self.str_param.GetEnumerateValues(o_safe_array)

    def get_enumerate_values_size(self) -> int:
        return self.str_param.GetEnumerateValuesSize()

    def set_enumerate_values(self, i_safe_array: tuple) -> None:
        return self.str_param.SetEnumerateValues(i_safe_array)

    def suppress_enumerate_values(self) -> None:
        return self.str_param.SuppressEnumerateValues()

    def __repr__(self):
        return f'StrParam(name="{ self.name }")'
