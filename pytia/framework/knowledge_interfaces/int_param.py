from pytia.framework.knowledge_interfaces.parameter import Parameter


class IntParam(Parameter):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.int_param = com_object

    @property
    def range_max(self) -> int:
        return self.int_param.RangeMax

    @range_max.setter
    def range_max(self, value: int):
        self.int_param.RangeMax = value

    @property
    def range_max_validity(self) -> int:
        return self.int_param.RangeMaxValidity

    @range_max_validity.setter
    def range_max_validity(self, value: int):
        self.int_param.RangeMaxValidity = value

    @property
    def range_min(self) -> int:
        return self.int_param.RangeMin

    @range_min.setter
    def range_min(self, value: int):
        self.int_param.RangeMin = value

    @property
    def range_min_validity(self) -> int:
        return self.int_param.RangeMinValidity

    @range_min_validity.setter
    def range_min_validity(self, value: int):
        self.int_param.RangeMinValidity = value

    @property
    def value(self) -> int:
        return self.int_param.Value

    @value.setter
    def value(self, value: int):
        self.int_param.Value = value

    def get_enumerate_values(self, o_safe_array: tuple) -> None:
        return self.int_param.GetEnumerateValues(o_safe_array)

    def get_enumerate_values_size(self) -> int:
        return self.int_param.GetEnumerateValuesSize()

    def set_enumerate_values(self, i_safe_array: tuple) -> None:
        return self.int_param.SetEnumerateValues(i_safe_array)

    def suppress_enumerate_values(self) -> None:
        return self.int_param.SuppressEnumerateValues()

    def __repr__(self):
        return f'IntParam(name="{ self.name }")'
