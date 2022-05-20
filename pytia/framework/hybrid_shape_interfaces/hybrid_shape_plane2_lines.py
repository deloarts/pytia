from pytia.framework.hybrid_shape_interfaces.plane import Plane
from pytia.framework.in_interfaces.reference import Reference


class HybridShapePlane2Lines(Plane):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_plane2_lines = com_object

    @property
    def first(self) -> Reference:
        return Reference(self.hybrid_shape_plane2_lines.First)

    @first.setter
    def first(self, reference_line: Reference):
        self.hybrid_shape_plane2_lines.First = reference_line.com_object

    @property
    def forbid_non_coplanar_lines(self) -> bool:
        return self.hybrid_shape_plane2_lines.ForbidNonCoplanarLines()

    @forbid_non_coplanar_lines.setter
    def forbid_non_coplanar_lines(self, value: bool):
        self.hybrid_shape_plane2_lines.ForbidNonCoplanarLines = value

    @property
    def second(self) -> Reference:
        return Reference(self.hybrid_shape_plane2_lines.Second)

    @second.setter
    def second(self, reference_line: Reference):
        self.hybrid_shape_plane2_lines.Second = reference_line.com_object

    def __repr__(self):
        return f'HybridShapePlane2Lines(name="{self.name}")'
