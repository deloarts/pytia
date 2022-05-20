from pytia.framework.hybrid_shape_interfaces.line import Line
from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.knowledge_interfaces.length import Length


class HybridShapeLineBisecting(Line):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_line_bisecting = com_object

    @property
    def begin_offset(self) -> Length:
        return Length(self.hybrid_shape_line_bisecting.BeginOffset)

    @property
    def elem1(self) -> Reference:
        return Reference(self.hybrid_shape_line_bisecting.Elem1)

    @elem1.setter
    def elem1(self, reference_element: Reference):
        self.hybrid_shape_line_bisecting.Elem1 = reference_element

    @property
    def elem2(self) -> Reference:
        return Reference(self.hybrid_shape_line_bisecting.Elem2)

    @elem2.setter
    def elem2(self, reference_element: Reference):
        self.hybrid_shape_line_bisecting.Elem2 = reference_element.com_object

    @property
    def end_offset(self) -> Length:
        return Length(self.hybrid_shape_line_bisecting.EndOffset)

    @property
    def orientation(self) -> int:
        return self.hybrid_shape_line_bisecting.Orientation

    @orientation.setter
    def orientation(self, value: int):
        self.hybrid_shape_line_bisecting.Orientation = value

    @property
    def ref_point(self) -> Reference:
        return Reference(self.hybrid_shape_line_bisecting.RefPoint)

    @ref_point.setter
    def ref_point(self, reference_point: Reference):
        self.hybrid_shape_line_bisecting.RefPoint = reference_point.com_object

    @property
    def solution_type(self) -> bool:
        return self.hybrid_shape_line_bisecting.SolutionType

    @solution_type.setter
    def solution_type(self, value: bool):
        self.hybrid_shape_line_bisecting.SolutionType = value

    @property
    def support(self) -> Reference:
        return Reference(self.hybrid_shape_line_bisecting.Support)

    @support.setter
    def support(self, reference_support: Reference):
        self.hybrid_shape_line_bisecting.Support = reference_support.com_object

    def get_length_type(self) -> int:
        return self.hybrid_shape_line_bisecting.GetLengthType()

    def get_symmetrical_extension(self) -> bool:
        return self.hybrid_shape_line_bisecting.GetSymmetricalExtension()

    def set_length_type(self, i_type: int) -> None:
        return self.hybrid_shape_line_bisecting.SetLengthType(i_type)

    def set_symmetrical_extension(self, i_sym: bool) -> None:
        return self.hybrid_shape_line_bisecting.SetSymmetricalExtension(i_sym)

    def __repr__(self):
        return f'HybridShapeLineBisecting(name="{self.name}")'
