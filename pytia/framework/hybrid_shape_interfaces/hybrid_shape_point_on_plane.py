from pytia.framework.hybrid_shape_interfaces.hybrid_shape_direction import (
    HybridShapeDirection,
)
from pytia.framework.hybrid_shape_interfaces.point import Point
from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.knowledge_interfaces.length import Length


class HybridShapePointOnPlane(Point):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_point_on_plane = com_object

    @property
    def first_direction(self) -> HybridShapeDirection:
        return HybridShapeDirection(self.hybrid_shape_point_on_plane.FirstDirection)

    @first_direction.setter
    def first_direction(self, direction: HybridShapeDirection):
        self.hybrid_shape_point_on_plane.FirstDirection = direction.com_object

    @property
    def plane(self) -> Reference:
        return Reference(self.hybrid_shape_point_on_plane.Plane)

    @plane.setter
    def plane(self, reference_plane: Reference):
        self.hybrid_shape_point_on_plane.Plane = reference_plane.com_object

    @property
    def point(self) -> Reference:
        return Reference(self.hybrid_shape_point_on_plane.Point)

    @point.setter
    def point(self, reference_point: Reference):
        self.hybrid_shape_point_on_plane.Point = reference_point.com_object

    @property
    def projection_surface(self) -> Reference:
        return Reference(self.hybrid_shape_point_on_plane.ProjectionSurface)

    @projection_surface.setter
    def projection_surface(self, reference_surface: Reference):
        self.hybrid_shape_point_on_plane.ProjectionSurface = (
            reference_surface.com_object
        )

    @property
    def x_offset(self) -> Length:
        return Length(self.hybrid_shape_point_on_plane.XOffset)

    @property
    def y_offset(self) -> Length:
        return Length(self.hybrid_shape_point_on_plane.YOffset)

    def get_second_direction(
        self, o_dir_x: float, o_dir_y: float, o_dir_z: float
    ) -> None:
        return self.hybrid_shape_point_on_plane.GetSecondDirection(
            o_dir_x, o_dir_y, o_dir_z
        )

    def set_second_direction(
        self, i_dir_x: float, i_dir_y: float, i_dir_z: float
    ) -> None:
        return self.hybrid_shape_point_on_plane.SetSecondDirection(
            i_dir_x, i_dir_y, i_dir_z
        )

    def __repr__(self):
        return f'HybridShapePointOnPlane(name="{self.name}")'
