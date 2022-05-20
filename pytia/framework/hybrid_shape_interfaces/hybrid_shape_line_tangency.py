from pytia.framework.hybrid_shape_interfaces.line import Line
from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.knowledge_interfaces.length import Length


class HybridShapeLineTangency(Line):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_line_tangency = com_object

    @property
    def begin_offset(self) -> Length:
        return Length(self.hybrid_shape_line_tangency.BeginOffset)

    @property
    def curve(self) -> Reference:
        return Reference(self.hybrid_shape_line_tangency.Curve)

    @curve.setter
    def curve(self, reference_curve: Reference):
        self.hybrid_shape_line_tangency.Curve = reference_curve.com_object

    @property
    def end_offset(self) -> Length:
        return Length(self.hybrid_shape_line_tangency.EndOffset)

    @property
    def orientation(self) -> int:
        return self.hybrid_shape_line_tangency.Orientation

    @orientation.setter
    def orientation(self, value: int):
        self.hybrid_shape_line_tangency.Orientation = value

    @property
    def point(self) -> Reference:
        return Reference(self.hybrid_shape_line_tangency.Point)

    @point.setter
    def point(self, reference_point: Reference):
        self.hybrid_shape_line_tangency.Point = reference_point.com_object

    @property
    def support(self) -> Reference:
        return Reference(self.hybrid_shape_line_tangency.Support)

    @support.setter
    def support(self, reference_support: Reference):
        self.hybrid_shape_line_tangency.Support = reference_support.com_object

    def get_length_type(self) -> int:
        return self.hybrid_shape_line_tangency.GetLengthType()

    def get_symmetrical_extension(self) -> bool:
        return self.hybrid_shape_line_tangency.GetSymmetricalExtension()

    def remove_support(self) -> None:
        return self.hybrid_shape_line_tangency.RemoveSupport()

    def set_length_type(self, i_type: int) -> None:
        return self.hybrid_shape_line_tangency.SetLengthType(i_type)

    def set_symmetrical_extension(self, i_sym: bool) -> None:
        return self.hybrid_shape_line_tangency.SetSymmetricalExtension(i_sym)

    def __repr__(self):
        return f'HybridShapeLineTangency(name="{self.name}")'
