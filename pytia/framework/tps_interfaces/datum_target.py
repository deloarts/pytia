from pytia.framework.system_interfaces.any_object import AnyObject
from pytia.framework.tps_interfaces.user_surface import UserSurface


class DatumTarget(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.datum_target = com_object

    @property
    def datum(self) -> AnyObject:
        return AnyObject(self.datum_target.Datum)

    @property
    def label(self) -> str:
        return self.datum_target.Label

    @label.setter
    def label(self, value: str):
        self.datum_target.Label = value

    def get_area_form(self, o_area_form: str) -> None:
        return self.datum_target.GetAreaForm(o_area_form)

    def get_circular_area_size(self, o_area_size: float) -> None:
        return self.datum_target.GetCircularAreaSize(o_area_size)

    def get_movable_direction_ttrs(self, op_direction_ttrs: UserSurface) -> None:
        return self.datum_target.GetMovableDirectionTTRS(op_direction_ttrs.com_object)

    def get_rectangular_area_size(self, o_length: float, o_width: float) -> None:
        return self.datum_target.GetRectangularAreaSize(o_length, o_width)

    def set_area_form(self, i_area_form: str) -> None:
        return self.datum_target.SetAreaForm(i_area_form)

    def set_circular_area_size(self, i_area_size: float) -> None:
        return self.datum_target.SetCircularAreaSize(i_area_size)

    def set_movable_direction_ttrs(self, ip_direction_ttrs: UserSurface) -> None:
        return self.datum_target.SetMovableDirectionTTRS(ip_direction_ttrs.com_object)

    def set_rectangular_area_size(self, i_length: float, i_width: float) -> None:
        return self.datum_target.SetRectangularAreaSize(i_length, i_width)

    def __repr__(self):
        return f'DatumTarget(name="{self.name}")'
