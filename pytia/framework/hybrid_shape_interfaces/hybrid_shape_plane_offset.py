from pytia.framework.hybrid_shape_interfaces.plane import Plane
from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.knowledge_interfaces.length import Length


class HybridShapePlaneOffset(Plane):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_plane_offset = com_object

    @property
    def offset(self) -> Length:
        return Length(self.hybrid_shape_plane_offset.Offset)

    @property
    def orientation(self) -> int:
        return self.hybrid_shape_plane_offset.Orientation

    @orientation.setter
    def orientation(self, value: int):
        self.hybrid_shape_plane_offset.Orientation = value

    @property
    def ref_plane(self) -> Reference:
        return Reference(self.hybrid_shape_plane_offset.Plane)

    @ref_plane.setter
    def ref_plane(self, reference_plane: Reference):
        self.hybrid_shape_plane_offset.Plane = reference_plane.com_object

    def __repr__(self):
        return f'HybridShapePlaneOffset(name="{self.name}")'
