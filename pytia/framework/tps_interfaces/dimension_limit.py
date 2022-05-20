from pytia.framework.system_interfaces.any_object import AnyObject


class DimensionLimit(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.dimension_limit = com_object

    @property
    def dimension_limit_type(self) -> str:
        return self.dimension_limit.DimensionLimitType

    @dimension_limit_type.setter
    def dimension_limit_type(self, value: str):
        self.dimension_limit.DimensionLimitType = value

    @property
    def modifier(self) -> str:
        return self.dimension_limit.Modifier

    @modifier.setter
    def modifier(self, value: str):
        self.dimension_limit.Modifier = value

    @property
    def nominal_value(self) -> float:
        return self.dimension_limit.Nominalvalue

    @property
    def symetric_value(self) -> bool:
        return self.dimension_limit.SymetricValue

    @symetric_value.setter
    def symetric_value(self, value: bool):
        self.dimension_limit.SymetricValue = value

    @property
    def tabulated_limit(self) -> str:
        return self.dimension_limit.TabulatedLimit

    @tabulated_limit.setter
    def tabulated_limit(self, value: str):
        self.dimension_limit.TabulatedLimit = value

    def limits(self, o_bottom: float, o_up: float) -> None:
        return self.dimension_limit.Limits(o_bottom, o_up)

    def put_limits(self, i_bottom: float, i_up: float) -> None:
        return self.dimension_limit.PutLimits(i_bottom, i_up)

    def __repr__(self):
        return f'DimensionLimit(name="{self.name}")'
