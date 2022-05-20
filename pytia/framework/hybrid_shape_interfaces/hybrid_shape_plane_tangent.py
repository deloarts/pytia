from pytia.framework.hybrid_shape_interfaces.plane import Plane
from pytia.framework.in_interfaces.reference import Reference


class HybridShapePlaneTangent(Plane):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_plane_tangent = com_object

    @property
    def point(self) -> Reference:
        return Reference(self.hybrid_shape_plane_tangent.Point)

    @point.setter
    def point(self, reference_point: Reference):
        self.hybrid_shape_plane_tangent.Point = reference_point.com_object

    @property
    def surface(self) -> Reference:
        return Reference(self.hybrid_shape_plane_tangent.Surface)

    @surface.setter
    def surface(self, reference_surface: Reference):
        self.hybrid_shape_plane_tangent.Surface = reference_surface.com_object

    def __repr__(self):
        return f'HybridShapePlaneTangent(name="{self.name}")'
