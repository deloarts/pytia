from pytia.framework.hybrid_shape_interfaces.line import Line
from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.knowledge_interfaces.length import Length


class HybridShapeLineNormal(Line):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_line_normal = com_object

    @property
    def begin_offset(self) -> Length:
        return Length(self.hybrid_shape_line_normal.BeginOffset)

    @property
    def end_offset(self) -> Length:
        return Length(self.hybrid_shape_line_normal.EndOffset)

    @property
    def orientation(self) -> int:
        return self.hybrid_shape_line_normal.Orientation

    @orientation.setter
    def orientation(self, value: int):
        self.hybrid_shape_line_normal.Orientation = value

    @property
    def point(self) -> Reference:
        return Reference(self.hybrid_shape_line_normal.Point)

    @point.setter
    def point(self, reference_point: Reference):
        self.hybrid_shape_line_normal.Point = reference_point.com_object

    @property
    def surface(self) -> Reference:
        return Reference(self.hybrid_shape_line_normal.Surface)

    @surface.setter
    def surface(self, surface_reference: Reference):
        self.hybrid_shape_line_normal.Surface = surface_reference.com_object

    def get_length_type(self) -> int:
        return self.hybrid_shape_line_normal.GetLengthType()

    def get_symmetrical_extension(self) -> bool:
        return self.hybrid_shape_line_normal.GetSymmetricalExtension()

    def set_length_type(self, i_type: int) -> None:
        return self.hybrid_shape_line_normal.SetLengthType(i_type)

    def set_symmetrical_extension(self, i_sym: bool) -> None:
        return self.hybrid_shape_line_normal.SetSymmetricalExtension(i_sym)

    def __repr__(self):
        return f'HybridShapeLineNormal(name="{self.name}")'
