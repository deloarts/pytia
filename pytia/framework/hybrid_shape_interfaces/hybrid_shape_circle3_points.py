from pytia.framework.hybrid_shape_interfaces.hybrid_shape_circle import (
    HybridShapeCircle,
)
from pytia.framework.in_interfaces.reference import Reference


class HybridShapeCircle3Points(HybridShapeCircle):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_circle3_points = com_object

    @property
    def element1(self) -> Reference:
        return Reference(self.hybrid_shape_circle3_points.Element1)

    @element1.setter
    def element1(self, reference_element: Reference):
        self.hybrid_shape_circle3_points.Element1 = reference_element.com_object

    @property
    def element2(self) -> Reference:
        return Reference(self.hybrid_shape_circle3_points.Element2)

    @element2.setter
    def element2(self, reference_element: Reference):
        self.hybrid_shape_circle3_points.Element2 = reference_element.com_object

    @property
    def element3(self) -> Reference:
        return Reference(self.hybrid_shape_circle3_points.Element3)

    @element3.setter
    def element3(self, reference_element: Reference):
        self.hybrid_shape_circle3_points.Element3 = reference_element.com_object

    @property
    def support(self) -> Reference:
        return Reference(self.hybrid_shape_circle3_points.Support)

    @support.setter
    def support(self, reference_support: Reference):
        self.hybrid_shape_circle3_points.Support = reference_support.com_object

    def remove_support(self) -> None:
        return self.hybrid_shape_circle3_points.RemoveSupport()

    def __repr__(self):
        return f'HybridShapeCircle3Points(name="{self.name}")'
