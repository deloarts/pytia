from pytia.framework.hybrid_shape_interfaces.plane import Plane
from pytia.framework.in_interfaces.reference import Reference


class HybridShapePlaneNormal(Plane):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_plane_normal = com_object

    @property
    def curve(self) -> Reference:
        return Reference(self.hybrid_shape_plane_normal.Curve)

    @curve.setter
    def curve(self, reference_curve: Reference):
        self.hybrid_shape_plane_normal.Curve = reference_curve

    @property
    def point(self) -> Reference:
        return Reference(self.hybrid_shape_plane_normal.Point)

    @point.setter
    def point(self, reference_point: Reference):
        self.hybrid_shape_plane_normal.Point = reference_point.com_object

    def __repr__(self):
        return f'HybridShapePlaneNormal(name="{self.name}")'
