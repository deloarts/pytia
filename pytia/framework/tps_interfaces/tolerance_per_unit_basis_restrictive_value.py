from pytia.framework.system_interfaces.any_object import AnyObject


class TolerancePerUnitBasisRestrictiveValue(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.tolerance_per_unit_basis_restrictive_value = com_object

    @property
    def value(self) -> float:
        return self.tolerance_per_unit_basis_restrictive_value.Value

    @value.setter
    def value(self, value: float):
        self.tolerance_per_unit_basis_restrictive_value.Value = value

    def __repr__(self):
        return f'TolerancePerUnitBasisRestrictiveValue(name="{ self.name }")'
