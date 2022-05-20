from pytia.framework.system_interfaces.any_object import AnyObject


class DrawingDimExtLine(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.drawing_dim_ext_line = com_object

    @property
    def color(self) -> int:
        return self.drawing_dim_ext_line.Color

    @color.setter
    def color(self, value: int):
        self.drawing_dim_ext_line.Color = value

    @property
    def ext_line_slant(self) -> float:
        return self.drawing_dim_ext_line.ExtLineSlant

    @ext_line_slant.setter
    def ext_line_slant(self, value: float):
        self.drawing_dim_ext_line.ExtLineSlant = value

    @property
    def ext_line_type(self) -> int:
        return self.drawing_dim_ext_line.ExtLineType

    @property
    def thickness(self) -> float:
        return self.drawing_dim_ext_line.Thickness

    @thickness.setter
    def thickness(self, value: float):
        self.drawing_dim_ext_line.Thickness = value

    def add_interrupt(self, i_index: int, i_two_points: tuple) -> None:
        return self.drawing_dim_ext_line.AddInterrupt(i_index, i_two_points)

    def get_funnel(
        self, i_index: int, o_mode: int, o_angle: float, o_height: float, o_width: float
    ) -> None:
        return self.drawing_dim_ext_line.GetFunnel(
            i_index, o_mode, o_angle, o_height, o_width
        )

    def get_gap(self, i_index: int) -> float:
        return self.drawing_dim_ext_line.GetGap(i_index)

    def get_geom_info(self, i_index: int, o_geom_infos: tuple) -> None:
        return self.drawing_dim_ext_line.GetGeomInfo(i_index, o_geom_infos)

    def get_interrupt(self, i_index: int) -> int:
        return self.drawing_dim_ext_line.GetInterrupt(i_index)

    def get_overrun(self, i_index: int) -> float:
        return self.drawing_dim_ext_line.GetOverrun(i_index)

    def get_visibility(self, i_index: int) -> int:
        return self.drawing_dim_ext_line.GetVisibility(i_index)

    def remove_interrupt(self, i_index: int) -> None:
        return self.drawing_dim_ext_line.RemoveInterrupt(i_index)

    def set_funnel(
        self, i_index: int, i_mode: int, i_angle: float, i_height: float, i_width: float
    ) -> None:
        return self.drawing_dim_ext_line.SetFunnel(
            i_index, i_mode, i_angle, i_height, i_width
        )

    def set_gap(self, i_index: int, i_gap: float) -> None:
        return self.drawing_dim_ext_line.SetGap(i_index, i_gap)

    def set_overrun(self, i_index: int, i_overrun: float) -> None:
        return self.drawing_dim_ext_line.SetOverrun(i_index, i_overrun)

    def set_visibility(self, i_index: int, i_extline_visibility: int) -> None:
        return self.drawing_dim_ext_line.SetVisibility(i_index, i_extline_visibility)

    def __repr__(self):
        return f'DrawingDimExtLine(name="{self.name}")'
