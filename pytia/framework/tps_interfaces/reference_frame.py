from typing import TYPE_CHECKING
from pytia.framework.system_interfaces.any_object import AnyObject
from pytia.framework.tps_interfaces.user_surface import UserSurface
from pytia.framework.cat_types.general import cat_variant

if TYPE_CHECKING:
    from pytia.framework.tps_interfaces.annotations import Annotations


class ReferenceFrame(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.reference_frame = com_object

    @property
    def all_datums_simple(self) -> "Annotations":
        from pytia.framework.tps_interfaces.annotations import Annotations

        return Annotations(self.reference_frame.AllDatumsSimple)

    def frame(self, o_first_box: str, o_second_box: str, o_third_box: str) -> None:
        return self.reference_frame.Frame(o_first_box, o_second_box, o_third_box)

    def get_axis_system_ttrs(self, op_axis_system_ttrs: UserSurface) -> None:
        return self.reference_frame.GetAxisSystemTTRS(op_axis_system_ttrs.com_object)

    def get_degrees_of_freedom(self, in_box: cat_variant, o_value: str) -> None:
        return self.reference_frame.GetDegreesOfFreedom(in_box, o_value)

    def set_axis_system_ttrs(self, ip_axis_system_ttrs: UserSurface) -> None:
        return self.reference_frame.SetAxisSystemTTRS(ip_axis_system_ttrs.com_object)

    def set_degrees_of_freedom(self, in_box: cat_variant, i_value: str) -> None:
        return self.reference_frame.SetDegreesOfFreedom(in_box, i_value)

    def set_frame(self, i_first_box: str, i_second_box: str, i_third_box: str) -> None:
        return self.reference_frame.SetFrame(i_first_box, i_second_box, i_third_box)

    def __repr__(self):
        return f'ReferenceFrame(name="{self.name}")'
