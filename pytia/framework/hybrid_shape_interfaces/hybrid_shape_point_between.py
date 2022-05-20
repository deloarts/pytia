from pytia.framework.hybrid_shape_interfaces.point import Point
from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.knowledge_interfaces.real_param import RealParam


class HybridShapePointBetween(Point):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_point_between = com_object

    @property
    def first_point(self) -> Reference:
        return Reference(self.hybrid_shape_point_between.FirstPoint)

    @first_point.setter
    def first_point(self, reference_point: Reference):
        self.hybrid_shape_point_between.FirstPoint = reference_point.com_object

    @property
    def orientation(self) -> int:
        return self.hybrid_shape_point_between.Orientation

    @orientation.setter
    def orientation(self, value: int):
        self.hybrid_shape_point_between.Orientation = value

    @property
    def ratio(self) -> RealParam:
        return RealParam(self.hybrid_shape_point_between.Ratio)

    @property
    def second_point(self) -> Reference:
        return Reference(self.hybrid_shape_point_between.SecondPoint)

    @second_point.setter
    def second_point(self, reference_point: Reference):
        self.hybrid_shape_point_between.SecondPoint = reference_point.com_object

    @property
    def support(self) -> Reference:
        return Reference(self.hybrid_shape_point_between.Support)

    @support.setter
    def support(self, reference_support: Reference):
        self.hybrid_shape_point_between.Support = reference_support.com_object

    def __repr__(self):
        return f'HybridShapePointBetween(name="{self.name}")'
