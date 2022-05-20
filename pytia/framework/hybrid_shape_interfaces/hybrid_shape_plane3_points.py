from pytia.framework.hybrid_shape_interfaces.plane import Plane
from pytia.framework.in_interfaces.reference import Reference


class HybridShapePlane3Points(Plane):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_plane3_points = com_object

    @property
    def first(self) -> Reference:
        return Reference(self.hybrid_shape_plane3_points.First)

    @first.setter
    def first(self, reference_point: Reference):
        self.hybrid_shape_plane3_points.First = reference_point.com_object

    @property
    def second(self) -> Reference:
        return Reference(self.hybrid_shape_plane3_points.Second)

    @second.setter
    def second(self, reference_point: Reference):
        self.hybrid_shape_plane3_points.Second = reference_point.com_object

    @property
    def third(self) -> Reference:
        return Reference(self.hybrid_shape_plane3_points.Third)

    @third.setter
    def third(self, reference_point: Reference):
        self.hybrid_shape_plane3_points.Third = reference_point

    def __repr__(self):
        return f'HybridShapePlane3Points(name="{self.name}")'
