from pytia.framework.system_interfaces.any_object import AnyObject


class DrawingDimLine(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.drawing_dim_line = com_object

    @property
    def color(self) -> int:
        return self.drawing_dim_line.Color

    @color.setter
    def color(self, value: int):
        self.drawing_dim_line.Color = value

    @property
    def dim_line_graph_rep(self) -> int:
        return self.drawing_dim_line.DimLineGraphRep

    @dim_line_graph_rep.setter
    def dim_line_graph_rep(self, value: int):
        self.drawing_dim_line.DimLineGraphRep = value

    @property
    def dim_line_orientation(self) -> int:
        return self.drawing_dim_line.DimLineOrientation

    @dim_line_orientation.setter
    def dim_line_orientation(self, value: int):
        self.drawing_dim_line.DimLineOrientation = value

    @property
    def dim_line_reference(self):
        return self.drawing_dim_line.DimLineReference

    @dim_line_reference.setter
    def dim_line_reference(self, value: int):
        self.drawing_dim_line.DimLineReference = value

    @property
    def dim_line_rep(self) -> int:
        return self.drawing_dim_line.DimLineRep

    @property
    def dim_line_type(self) -> int:
        return self.drawing_dim_line.DimLineType

    @property
    def thickness(self) -> float:
        return self.drawing_dim_line.Thickness

    @thickness.setter
    def thickness(self, value: float):
        self.drawing_dim_line.Thickness = value

    def get_dim_line_dir(self, o_dir_x: float, o_dir_y: float) -> None:
        return self.drawing_dim_line.GetDimLineDir(o_dir_x, o_dir_y)

    def get_geom_info(self, o_geom_infos: tuple) -> None:
        return self.drawing_dim_line.GetGeomInfo(o_geom_infos)

    def get_symb_color(self, index: int) -> int:
        return self.drawing_dim_line.GetSymbColor(index)

    def get_symb_thickness(self, index: int) -> float:
        return self.drawing_dim_line.GetSymbThickness(index)

    def get_symb_type(self, index: int) -> int:
        return self.drawing_dim_line.GetSymbType(index)

    def set_symb_color(self, index: int, i_color_symb: int) -> None:
        return self.drawing_dim_line.SetSymbColor(index, i_color_symb)

    def set_symb_thickness(self, index: int, i_thick_symb: float) -> None:
        return self.drawing_dim_line.SetSymbThickness(index, i_thick_symb)

    def set_symb_type(self, index: int, i_symb_type: int) -> None:
        return self.drawing_dim_line.SetSymbType(index, i_symb_type)

    def __repr__(self):
        return f'DrawingDimLine(name="{self.name}")'
