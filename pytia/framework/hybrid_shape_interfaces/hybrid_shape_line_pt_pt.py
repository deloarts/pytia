from pytia.framework.hybrid_shape_interfaces.line import Line
from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.knowledge_interfaces.length import Length


class HybridShapeLinePtPt(Line):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_line_pt_pt = com_object

    @property
    def begin_offset(self) -> Length:
        return Length(self.hybrid_shape_line_pt_pt.BeginOffset)

    @property
    def end_offset(self) -> Length:
        return Length(self.hybrid_shape_line_pt_pt.EndOffset)

    @property
    def pt_extremity(self) -> Reference:
        return Reference(self.hybrid_shape_line_pt_pt.PtExtremity)

    @pt_extremity.setter
    def pt_extremity(self, pt_reference: Reference):
        self.hybrid_shape_line_pt_pt.PtExtremity = pt_reference.com_object

    @property
    def pt_origin(self) -> Reference:
        return Reference(self.hybrid_shape_line_pt_pt.PtOrigine)

    @pt_origin.setter
    def pt_origin(self, pt_reference: Reference):
        self.hybrid_shape_line_pt_pt.PtOrigine = pt_reference.com_object

    @property
    def support(self) -> Reference:
        return Reference(self.hybrid_shape_line_pt_pt.Support)

    @support.setter
    def support(self, support_reference: Reference):
        self.hybrid_shape_line_pt_pt.Support = support_reference.com_object

    def get_length_type(self) -> int:
        return self.hybrid_shape_line_pt_pt.GetLengthType()

    def get_symmetrical_extension(self) -> bool:
        return self.hybrid_shape_line_pt_pt.GetSymmetricalExtension()

    def remove_support(self) -> None:
        return self.hybrid_shape_line_pt_pt.RemoveSupport()

    def set_length_type(self, i_type: int) -> None:
        return self.hybrid_shape_line_pt_pt.SetLengthType(i_type)

    def set_symmetrical_extension(self, i_sym: bool) -> None:
        return self.hybrid_shape_line_pt_pt.SetSymmetricalExtension(i_sym)

    def __repr__(self):
        return f'HybridShapeLinePtPt(name="{self.name}")'
