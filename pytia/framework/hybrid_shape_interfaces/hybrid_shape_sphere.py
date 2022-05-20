from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.knowledge_interfaces.angle import Angle
from pytia.framework.knowledge_interfaces.length import Length
from pytia.framework.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeSphere(HybridShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_sphere = com_object

    @property
    def axis(self) -> Reference:
        return Reference(self.hybrid_shape_sphere.Axis)

    @axis.setter
    def axis(self, reference_axis: Reference):
        self.hybrid_shape_sphere.Axis = reference_axis.com_object

    @property
    def begin_meridian_angle(self) -> Angle:
        return Angle(self.hybrid_shape_sphere.BeginMeridianAngle)

    @property
    def begin_parallel_angle(self) -> Angle:
        return Angle(self.hybrid_shape_sphere.BeginParallelAngle)

    @property
    def center(self) -> Reference:
        return Reference(self.hybrid_shape_sphere.Center)

    @center.setter
    def center(self, reference: Reference):
        self.hybrid_shape_sphere.Center = reference.com_object

    @property
    def end_meridian_angle(self) -> Angle:
        return Angle(self.hybrid_shape_sphere.EndMeridianAngle)

    @property
    def end_parallel_angle(self) -> Angle:
        return Angle(self.hybrid_shape_sphere.EndParallelAngle)

    @property
    def limitation(self) -> bool:
        return self.hybrid_shape_sphere.Limitation

    @limitation.setter
    def limitation(self, value: bool):
        self.hybrid_shape_sphere.Limitation = value

    @property
    def radius(self) -> Length:
        return Length(self.hybrid_shape_sphere.Radius)

    def set_begin_meridian_angle(self, i_angle: float) -> None:
        return self.hybrid_shape_sphere.SetBeginMeridianAngle(i_angle)

    def set_begin_parallel_angle(self, i_angle: float) -> None:
        return self.hybrid_shape_sphere.SetBeginParallelAngle(i_angle)

    def set_end_meridian_angle(self, i_angle: float) -> None:
        return self.hybrid_shape_sphere.SetEndMeridianAngle(i_angle)

    def set_end_parallel_angle(self, i_angle: float) -> None:
        return self.hybrid_shape_sphere.SetEndParallelAngle(i_angle)

    def set_radius(self, i_radius: float) -> None:
        return self.hybrid_shape_sphere.SetRadius(i_radius)

    def __repr__(self):
        return f'HybridShapeSphere(name="{self.name}")'
