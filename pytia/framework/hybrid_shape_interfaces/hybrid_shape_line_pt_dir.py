from pytia.framework.hybrid_shape_interfaces.hybrid_shape_direction import (
    HybridShapeDirection,
)
from pytia.framework.hybrid_shape_interfaces.line import Line
from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.knowledge_interfaces.length import Length


class HybridShapeLinePtDir(Line):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_line_pt_dir = com_object

    @property
    def begin_offset(self) -> Length:
        return Length(self.hybrid_shape_line_pt_dir.BeginOffset)

    @property
    def dir(self) -> HybridShapeDirection:
        return HybridShapeDirection(self.hybrid_shape_line_pt_dir.Dir)

    @dir.setter
    def dir(self, direction: HybridShapeDirection):
        self.hybrid_shape_line_pt_dir.Dir = direction.com_object

    @property
    def end_offset(self) -> Length:
        return Length(self.hybrid_shape_line_pt_dir.EndOffset)

    @property
    def orientation(self) -> int:
        return self.hybrid_shape_line_pt_dir.Orientation

    @orientation.setter
    def orientation(self, value: int):
        self.hybrid_shape_line_pt_dir.Orientation = value

    @property
    def point(self) -> Reference:
        return Reference(self.hybrid_shape_line_pt_dir.Point)

    @point.setter
    def point(self, reference_point: Reference):
        self.hybrid_shape_line_pt_dir.Point = reference_point

    @property
    def support(self) -> Reference:
        return Reference(self.hybrid_shape_line_pt_dir.Support)

    @support.setter
    def support(self, reference_support: Reference):
        self.hybrid_shape_line_pt_dir.Support = reference_support

    def get_length_type(self) -> int:
        return self.hybrid_shape_line_pt_dir.GetLengthType()

    def get_symmetrical_extension(self) -> bool:
        return self.hybrid_shape_line_pt_dir.GetSymmetricalExtension()

    def remove_support(self) -> None:
        return self.hybrid_shape_line_pt_dir.RemoveSupport()

    def set_length_type(self, i_type: int) -> None:
        return self.hybrid_shape_line_pt_dir.SetLengthType(i_type)

    def set_symmetrical_extension(self, i_sym: bool) -> None:
        return self.hybrid_shape_line_pt_dir.SetSymmetricalExtension(i_sym)

    def __repr__(self):
        return f'HybridShapeLinePtDir(name="{self.name}")'
