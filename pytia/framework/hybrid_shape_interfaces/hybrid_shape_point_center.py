from pytia.framework.hybrid_shape_interfaces.point import Point
from pytia.framework.in_interfaces.reference import Reference


class HybridShapePointCenter(Point):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_point_center = com_object

    @property
    def element(self) -> Reference:
        return Reference(self.hybrid_shape_point_center.Element)

    @element.setter
    def element(self, reference_element: Reference):
        self.hybrid_shape_point_center.Element = reference_element.com_object

    def __repr__(self):
        return f'HybridShapePointCenter(name="{self.name}")'
