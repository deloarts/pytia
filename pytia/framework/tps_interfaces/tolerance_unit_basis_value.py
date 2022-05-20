from pytia.framework.system_interfaces.any_object import AnyObject


class ToleranceUnitBasisValue(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.tolerance_unit_basis_value = com_object

    def set_values(self, i_value1: float, i_value2: float) -> None:
        return self.tolerance_unit_basis_value.SetValues(i_value1, i_value2)

    def values(self, o_value1: float, o_value2: float) -> None:
        return self.tolerance_unit_basis_value.Values(o_value1, o_value2)

    def __repr__(self):
        return f'ToleranceUnitBasisValue(name="{ self.name }")'
