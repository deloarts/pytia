from pytia.framework.hybrid_shape_interfaces.line import Line
from pytia.framework.in_interfaces.reference import Reference


class HybridShapeLineBiTangent(Line):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_line_bi_tangent = com_object

    @property
    def curve1(self) -> Reference:
        return Reference(self.hybrid_shape_line_bi_tangent.Curve1)

    @curve1.setter
    def curve1(self, reference_curve: Reference):
        self.hybrid_shape_line_bi_tangent.Curve1 = reference_curve.com_object

    @property
    def element2(self) -> Reference:
        return Reference(self.hybrid_shape_line_bi_tangent.Element2)

    @element2.setter
    def element2(self, reference_element: Reference):
        self.hybrid_shape_line_bi_tangent.Element2 = reference_element.com_object

    @property
    def support(self) -> Reference:
        return Reference(self.hybrid_shape_line_bi_tangent.Support)

    @support.setter
    def support(self, reference_support: Reference):
        self.hybrid_shape_line_bi_tangent.Support = reference_support.com_object

    def get_choice_no(
        self, val1: int, val2: int, val3: int, val4: int, val5: int
    ) -> None:
        return self.hybrid_shape_line_bi_tangent.GetChoiceNo(
            val1, val2, val3, val4, val5
        )

    def get_length_type(self) -> int:
        return self.hybrid_shape_line_bi_tangent.GetLengthType()

    def set_choice_no(
        self, val1: int, val2: int, val3: int, val4: int, val5: int
    ) -> None:
        return self.hybrid_shape_line_bi_tangent.SetChoiceNo(
            val1, val2, val3, val4, val5
        )

    def set_length_type(self, i_type: int) -> None:
        return self.hybrid_shape_line_bi_tangent.SetLengthType(i_type)

    def __repr__(self):
        return f'HybridShapeLineBiTangent(name="{self.name}")'
