from pytia.framework.knowledge_interfaces.parameter import Parameter


class RealParam(Parameter):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.real_param = com_object

    @property
    def maximum_tolerance(self) -> float:
        return self.real_param.MaximumTolerance

    @maximum_tolerance.setter
    def maximum_tolerance(self, value: float):
        self.real_param.MaximumTolerance = value

    @property
    def minimum_tolerance(self) -> float:
        return self.real_param.MinimumTolerance

    @minimum_tolerance.setter
    def minimum_tolerance(self, value: float):
        self.real_param.MinimumTolerance = value

    @property
    def range_max(self) -> float:
        return self.real_param.RangeMax

    @range_max.setter
    def range_max(self, value: float):
        self.real_param.RangeMax = value

    @property
    def range_max_validity(self) -> int:
        return self.real_param.RangeMaxValidity

    @range_max_validity.setter
    def range_max_validity(self, value: int):
        self.real_param.RangeMaxValidity = value

    @property
    def range_min(self) -> float:
        return self.real_param.RangeMin

    @range_min.setter
    def range_min(self, value: float):
        self.real_param.RangeMin = value

    @property
    def range_min_validity(self) -> int:
        return self.real_param.RangeMinValidity

    @range_min_validity.setter
    def range_min_validity(self, value: int):
        self.real_param.RangeMinValidity = value

    @property
    def value(self) -> float:
        return self.real_param.Value

    @value.setter
    def value(self, value: float):
        self.real_param.Value = value

    def get_enumerate_values(self, o_safe_array: tuple) -> None:
        return self.real_param.GetEnumerateValues(o_safe_array)

    def get_enumerate_values_size(self) -> int:
        return self.real_param.GetEnumerateValuesSize()

    def is_equal_to(self, i_value_to_compare: float) -> bool:
        return self.real_param.IsEqualTo(i_value_to_compare)

    def set_enumerate_values(self, i_safe_array: tuple) -> None:
        return self.real_param.SetEnumerateValues(i_safe_array)

    def suppress_enumerate_values(self) -> None:
        return self.real_param.SuppressEnumerateValues()

    def __repr__(self):
        return f'RealParam(name="{ self.name }")'
