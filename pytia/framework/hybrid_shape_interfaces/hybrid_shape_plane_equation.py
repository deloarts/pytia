from pytia.framework.hybrid_shape_interfaces.plane import Plane
from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.knowledge_interfaces.length import Length
from pytia.framework.knowledge_interfaces.real_param import RealParam


class HybridShapePlaneEquation(Plane):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_plane_equation = com_object

    @property
    def a(self) -> RealParam:
        return RealParam(self.hybrid_shape_plane_equation.A)

    @property
    def b(self) -> RealParam:
        return RealParam(self.hybrid_shape_plane_equation.B)

    @property
    def c(self) -> RealParam:
        return RealParam(self.hybrid_shape_plane_equation.C)

    @property
    def d(self) -> Length:
        return Length(self.hybrid_shape_plane_equation.D)

    @property
    def ref_axis_system(self) -> Reference:
        return Reference(self.hybrid_shape_plane_equation.RefAxisSystem)

    @ref_axis_system.setter
    def ref_axis_system(self, reference_axis: Reference):
        self.hybrid_shape_plane_equation.RefAxisSystem = reference_axis

    def get_reference_point(self) -> Reference:
        return Reference(self.hybrid_shape_plane_equation.GetReferencePoint())

    def set_reference_point(self, i_reference_point: Reference) -> None:
        return self.hybrid_shape_plane_equation.SetReferencePoint(
            i_reference_point.com_object
        )

    def __repr__(self):
        return f'HybridShapePlaneEquation(name="{self.name}")'
