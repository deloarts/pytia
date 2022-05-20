from pytia.framework.hybrid_shape_interfaces.plane import Plane
from pytia.framework.in_interfaces.reference import Reference


class HybridShapePlane1Line1Pt(Plane):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_plane1_line1_pt = com_object

    @property
    def line(self) -> Reference:
        return Reference(self.hybrid_shape_plane1_line1_pt.Line)

    @line.setter
    def line(self, reference_line: Reference):
        self.hybrid_shape_plane1_line1_pt.Line = reference_line

    @property
    def point(self) -> Reference:
        return Reference(self.hybrid_shape_plane1_line1_pt.Point)

    @point.setter
    def point(self, reference_point: Reference):
        self.hybrid_shape_plane1_line1_pt.Point = reference_point.com_object

    def __repr__(self):
        return f'HybridShapePlane1Line1Pt(name="{self.name}")'
