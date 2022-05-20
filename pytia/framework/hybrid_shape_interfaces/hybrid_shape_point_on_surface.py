from pytia.framework.hybrid_shape_interfaces.hybrid_shape_direction import (
    HybridShapeDirection,
)
from pytia.framework.hybrid_shape_interfaces.point import Point
from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.knowledge_interfaces.length import Length


class HybridShapePointOnSurface(Point):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_point_on_surface = com_object

    @property
    def direction(self) -> HybridShapeDirection:
        return HybridShapeDirection(self.hybrid_shape_point_on_surface.Direction)

    @direction.setter
    def direction(self, direction: HybridShapeDirection):
        self.hybrid_shape_point_on_surface.Direction = direction.com_object

    @property
    def offset(self) -> Length:
        return Length(self.hybrid_shape_point_on_surface.Offset)

    @property
    def point(self) -> Reference:
        return Reference(self.hybrid_shape_point_on_surface.Point)

    @point.setter
    def point(self, reference_point: Reference):
        self.hybrid_shape_point_on_surface.Point = reference_point.com_object

    @property
    def surface(self) -> Reference:
        return Reference(self.hybrid_shape_point_on_surface.Surface)

    @surface.setter
    def surface(self, reference_surface: Reference):
        self.hybrid_shape_point_on_surface.Surface = reference_surface.com_object

    def __repr__(self):
        return f'HybridShapePointOnSurface(name="{self.name}")'
