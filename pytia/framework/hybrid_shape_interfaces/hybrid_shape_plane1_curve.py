from pytia.framework.hybrid_shape_interfaces.plane import Plane
from pytia.framework.in_interfaces.reference import Reference


class HybridShapePlane1Curve(Plane):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_plane1_curve = com_object

    @property
    def curve(self) -> Reference:
        return Reference(self.hybrid_shape_plane1_curve.Curve)

    @curve.setter
    def curve(self, reference_curve: Reference):
        self.hybrid_shape_plane1_curve.Curve = reference_curve.com_object

    def __repr__(self):
        return f'HybridShapePlane1Curve(name="{self.name}")'
