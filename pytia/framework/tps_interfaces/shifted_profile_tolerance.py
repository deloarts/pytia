from pytia.framework.system_interfaces.any_object import AnyObject


class ShiftedProfileTolerance(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.shifted_profile_tolerance = com_object

    @property
    def shift_value(self) -> float:
        return self.shifted_profile_tolerance.ShiftValue

    @shift_value.setter
    def shift_value(self, value: float):
        self.shifted_profile_tolerance.ShiftValue = value

    def get_shift_direction(self, op_direction: tuple) -> tuple:
        return self.shifted_profile_tolerance.GetShiftDirection(op_direction)

    def get_shift_side(self, op_point: tuple) -> tuple:
        return self.shifted_profile_tolerance.GetShiftSide(op_point)

    def __repr__(self):
        return f'ShiftedProfileTolerance(name="{ self.name }")'
