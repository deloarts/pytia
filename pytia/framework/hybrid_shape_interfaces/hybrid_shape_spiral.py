from pytia.framework.hybrid_shape_interfaces.hybrid_shape_direction import (
    HybridShapeDirection,
)
from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.knowledge_interfaces.angle import Angle
from pytia.framework.knowledge_interfaces.length import Length
from pytia.framework.knowledge_interfaces.real_param import RealParam
from pytia.framework.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeSpiral(HybridShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_spiral = com_object

    @property
    def axis(self) -> HybridShapeDirection:
        return HybridShapeDirection(self.hybrid_shape_spiral.Axis)

    @axis.setter
    def axis(self, reference_axis: HybridShapeDirection):
        self.hybrid_shape_spiral.Axis = reference_axis.com_object

    @property
    def center_point(self) -> Reference:
        return Reference(self.hybrid_shape_spiral.CenterPoint)

    @center_point.setter
    def center_point(self, reference_point: Reference):
        self.hybrid_shape_spiral.CenterPoint = reference_point.com_object

    @property
    def clockwise_revolution(self) -> bool:
        return self.hybrid_shape_spiral.ClockwiseRevolution

    @clockwise_revolution.setter
    def clockwise_revolution(self, value: bool):
        self.hybrid_shape_spiral.ClockwiseRevolution = value

    @property
    def ending_angle(self) -> Angle:
        return Angle(self.hybrid_shape_spiral.EndingAngle)

    @ending_angle.setter
    def ending_angle(self, angle: Angle):
        self.hybrid_shape_spiral.EndingAngle = angle.com_object

    @property
    def ending_radius(self) -> Length:
        return Length(self.hybrid_shape_spiral.EndingRadius)

    @ending_radius.setter
    def ending_radius(self, length: Length):
        self.hybrid_shape_spiral.EndingRadius = length.com_object

    @property
    def invert_axis(self) -> bool:
        return self.hybrid_shape_spiral.InvertAxis

    @invert_axis.setter
    def invert_axis(self, value: bool):
        self.hybrid_shape_spiral.InvertAxis = value

    @property
    def pitch(self) -> Length:
        return Length(self.hybrid_shape_spiral.Pitch)

    @pitch.setter
    def pitch(self, length: Length):
        self.hybrid_shape_spiral.Pitch = length.com_object

    @property
    def revol_number(self) -> RealParam:
        return RealParam(self.hybrid_shape_spiral.RevolNumber)

    @revol_number.setter
    def revol_number(self, real_param: RealParam):
        self.hybrid_shape_spiral.RevolNumber = real_param.com_object

    @property
    def starting_radius(self) -> Length:
        return Length(self.hybrid_shape_spiral.StartingRadius)

    @starting_radius.setter
    def starting_radius(self, length: Length):
        self.hybrid_shape_spiral.StartingRadius = length.com_object

    @property
    def support(self) -> Reference:
        return Reference(self.hybrid_shape_spiral.Support)

    @support.setter
    def support(self, reference_support: Reference):
        self.hybrid_shape_spiral.Support = reference_support.com_object

    @property
    def type(self) -> int:
        return self.hybrid_shape_spiral.Type

    @type.setter
    def type(self, value: int):
        self.hybrid_shape_spiral.Type = value

    def set_angle_pitch_param(
        self, i_end_angle: float, i_revol_number: float, i_pitch: float
    ) -> None:
        return self.hybrid_shape_spiral.SetAnglePitchParam(
            i_end_angle, i_revol_number, i_pitch
        )

    def set_angle_radius_param(
        self, i_end_angle: float, i_revol_number: float, i_end_radius: float
    ) -> None:
        return self.hybrid_shape_spiral.SetAngleRadiusParam(
            i_end_angle, i_revol_number, i_end_radius
        )

    def set_radius_pitch_param(self, i_end_radius: float, i_pitch: float) -> None:
        return self.hybrid_shape_spiral.SetRadiusPitchParam(i_end_radius, i_pitch)

    def __repr__(self):
        return f'HybridShapeSpiral(name="{self.name}")'
