from pytia.framework.hybrid_shape_interfaces.hybrid_shape_direction import (
    HybridShapeDirection,
)
from pytia.framework.hybrid_shape_interfaces.point import Point
from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.knowledge_interfaces.length import Length
from pytia.framework.knowledge_interfaces.real_param import RealParam


class HybridShapePointOnCurve(Point):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_point_on_curve = com_object

    @property
    def curve(self) -> Reference:
        return Reference(self.hybrid_shape_point_on_curve.Curve)

    @curve.setter
    def curve(self, reference_curve: Reference):
        self.hybrid_shape_point_on_curve.Curve = reference_curve.com_object

    @property
    def direction(self) -> HybridShapeDirection:
        return HybridShapeDirection(self.hybrid_shape_point_on_curve.Direction)

    @direction.setter
    def direction(self, direction: HybridShapeDirection):
        self.hybrid_shape_point_on_curve.Direction = direction.com_object

    @property
    def distance_type(self) -> int:
        return self.hybrid_shape_point_on_curve.DistanceType

    @distance_type.setter
    def distance_type(self, value: int):
        self.hybrid_shape_point_on_curve.DistanceType = value

    @property
    def offset(self) -> Length:
        return Length(self.hybrid_shape_point_on_curve.Offset)

    @property
    def on_curve_type(self) -> int:
        return self.hybrid_shape_point_on_curve.OnCurveType

    @on_curve_type.setter
    def on_curve_type(self, value: int):
        self.hybrid_shape_point_on_curve.OnCurveType = value

    @property
    def orientation(self) -> int:
        return self.hybrid_shape_point_on_curve.Orientation

    @orientation.setter
    def orientation(self, value: int):
        self.hybrid_shape_point_on_curve.Orientation = value

    @property
    def point(self) -> Reference:
        return Reference(self.hybrid_shape_point_on_curve.Point)

    @point.setter
    def point(self, reference_point: Reference):
        self.hybrid_shape_point_on_curve.Point = reference_point.com_object

    @property
    def ratio(self) -> RealParam:
        return RealParam(self.hybrid_shape_point_on_curve.Ratio)

    @property
    def type(self) -> int:
        return self.hybrid_shape_point_on_curve.Type

    def __repr__(self):
        return f'HybridShapePointOnCurve(name="{self.name}")'
