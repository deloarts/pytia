from pytia.framework.hybrid_shape_interfaces.hybrid_shape_circle import (
    HybridShapeCircle,
)
from pytia.framework.in_interfaces.reference import Reference


class HybridShapeCircleCtrPt(HybridShapeCircle):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_circle_ctr_pt = com_object

    @property
    def center(self) -> Reference:
        return Reference(self.hybrid_shape_circle_ctr_pt.Center)

    @center.setter
    def center(self, reference_center: Reference):
        self.hybrid_shape_circle_ctr_pt.Center = reference_center.com_object

    @property
    def crossing_point(self) -> Reference:
        return Reference(self.hybrid_shape_circle_ctr_pt.CrossingPoint)

    @crossing_point.setter
    def crossing_point(self, reference_point: Reference):
        self.hybrid_shape_circle_ctr_pt.CrossingPoint = reference_point.com_object

    @property
    def support(self) -> Reference:
        return Reference(self.hybrid_shape_circle_ctr_pt.Support)

    @support.setter
    def support(self, reference_support: Reference):
        self.hybrid_shape_circle_ctr_pt.Support = reference_support.com_object

    def is_geodesic(self) -> bool:
        return self.hybrid_shape_circle_ctr_pt.IsGeodesic()

    def set_geometry_on_support(self) -> None:
        return self.hybrid_shape_circle_ctr_pt.SetGeometryOnSupport()

    def unset_geometry_on_support(self) -> None:
        return self.hybrid_shape_circle_ctr_pt.UnsetGeometryOnSupport()

    def __repr__(self):
        return f'HybridShapeCircleCtrPt(name="{ self.name }")'
