from pytia.framework.hybrid_shape_interfaces.plane import Plane
from pytia.framework.in_interfaces.reference import Reference


class HybridShapePlaneOffsetPt(Plane):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_plane_offset_pt = com_object

    @property
    def ref_plane(self) -> Reference:
        return Reference(self.hybrid_shape_plane_offset_pt.Plane)

    @ref_plane.setter
    def ref_plane(self, reference_plane: Reference):
        self.hybrid_shape_plane_offset_pt.Plane = reference_plane.com_object

    @property
    def point(self) -> Reference:
        return Reference(self.hybrid_shape_plane_offset_pt.Point)

    @point.setter
    def point(self, reference_point: Reference):
        self.hybrid_shape_plane_offset_pt.Point = reference_point.com_object

    def __repr__(self):
        return f'HybridShapePlaneOffsetPt(name="{self.name}")'
