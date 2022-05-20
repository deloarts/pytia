from pytia.framework.hybrid_shape_interfaces.hybrid_shape_circle import (
    HybridShapeCircle,
)
from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.knowledge_interfaces.length import Length


class HybridShapeCircle2PointsRad(HybridShapeCircle):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_circle2_points_rad = com_object

    @property
    def diameter(self) -> Length:
        return Length(self.hybrid_shape_circle2_points_rad.Diameter)

    @property
    def diameter_mode(self) -> bool:
        return self.hybrid_shape_circle2_points_rad.DiameterMode

    @diameter_mode.setter
    def diameter_mode(self, value: bool):
        self.hybrid_shape_circle2_points_rad.DiameterMode = value

    @property
    def orientation(self) -> int:
        return self.hybrid_shape_circle2_points_rad.Orientation

    @orientation.setter
    def orientation(self, value: int):
        self.hybrid_shape_circle2_points_rad.Orientation = value

    @property
    def pt1(self) -> Reference:
        return Reference(self.hybrid_shape_circle2_points_rad.Pt1)

    @pt1.setter
    def pt1(self, reference_point: Reference):
        self.hybrid_shape_circle2_points_rad.Pt1 = reference_point.com_object

    @property
    def pt2(self) -> Reference:
        return Reference(self.hybrid_shape_circle2_points_rad.Pt2)

    @pt2.setter
    def pt2(self, reference_point: Reference):
        self.hybrid_shape_circle2_points_rad.Pt2 = reference_point.com_object

    @property
    def radius(self) -> Length:
        return Length(self.hybrid_shape_circle2_points_rad.Radius)

    @property
    def support(self) -> Reference:
        return Reference(self.hybrid_shape_circle2_points_rad.Support)

    @support.setter
    def support(self, reference_support: Reference):
        self.hybrid_shape_circle2_points_rad.Support = reference_support

    def is_geodesic(self) -> bool:
        return self.hybrid_shape_circle2_points_rad.IsGeodesic()

    def set_geometry_on_support(self) -> None:
        return self.hybrid_shape_circle2_points_rad.SetGeometryOnSupport()

    def unset_geometry_on_support(self) -> None:
        return self.hybrid_shape_circle2_points_rad.UnsetGeometryOnSupport()

    def __repr__(self):
        return f'HybridShapeCircle2PointsRad(name="{self.name}")'
