from pytia.framework.hybrid_shape_interfaces.hybrid_shape_direction import (
    HybridShapeDirection,
)
from pytia.framework.hybrid_shape_interfaces.point import Point
from pytia.framework.in_interfaces.reference import Reference


class HybridShapePointTangent(Point):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_point_tangent = com_object

    @property
    def curve(self) -> Reference:
        return Reference(self.hybrid_shape_point_tangent.Curve)

    @curve.setter
    def curve(self, reference_curve: Reference):
        self.hybrid_shape_point_tangent.Curve = reference_curve.com_object

    @property
    def direction(self) -> HybridShapeDirection:
        return HybridShapeDirection(self.hybrid_shape_point_tangent.Direction)

    @direction.setter
    def direction(self, direction: HybridShapeDirection):
        self.hybrid_shape_point_tangent.Direction = direction.com_object

    def __repr__(self):
        return f'HybridShapePointTangent(name="{self.name}")'
