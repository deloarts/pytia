from pytia.framework.hybrid_shape_interfaces.line import Line
from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.knowledge_interfaces.angle import Angle
from pytia.framework.knowledge_interfaces.length import Length


class HybridShapeLineAngle(Line):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_line_angle = com_object

    @property
    def angle(self) -> Angle:
        return Angle(self.hybrid_shape_line_angle.Angle)

    @property
    def begin_offset(self) -> Length:
        return Length(self.hybrid_shape_line_angle.BeginOffset)

    @property
    def curve(self) -> Reference:
        return Reference(self.hybrid_shape_line_angle.Curve)

    @curve.setter
    def curve(self, reference_curve: Reference):
        self.hybrid_shape_line_angle.Curve = reference_curve.com_object

    @property
    def end_offset(self) -> Length:
        return Length(self.hybrid_shape_line_angle.EndOffset)

    @property
    def geodesic(self) -> bool:
        return self.hybrid_shape_line_angle.Geodesic

    @geodesic.setter
    def geodesic(self, value: bool):
        self.hybrid_shape_line_angle.Geodesic = value

    @property
    def orientation(self) -> int:
        return self.hybrid_shape_line_angle.Orientation

    @orientation.setter
    def orientation(self, value: int):
        self.hybrid_shape_line_angle.Orientation = value

    @property
    def point(self) -> Reference:
        return Reference(self.hybrid_shape_line_angle.Point)

    @point.setter
    def point(self, reference_point: Reference):
        self.hybrid_shape_line_angle.Point = reference_point.com_object

    @property
    def surface(self) -> Reference:
        return Reference(self.hybrid_shape_line_angle.Surface)

    @surface.setter
    def surface(self, reference_surface: Reference):
        self.hybrid_shape_line_angle.Surface = reference_surface.com_object

    def get_length_type(self) -> int:
        return self.hybrid_shape_line_angle.GetLengthType()

    def get_symmetrical_extension(self) -> bool:
        return self.hybrid_shape_line_angle.GetSymmetricalExtension()

    def set_length_type(self, i_type: int) -> None:
        return self.hybrid_shape_line_angle.SetLengthType(i_type)

    def set_symmetrical_extension(self, i_sym: bool) -> None:
        return self.hybrid_shape_line_angle.SetSymmetricalExtension(i_sym)

    def __repr__(self):
        return f'HybridShapeLineAngle(name="{self.name}")'
