from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.knowledge_interfaces.angle import Angle
from pytia.framework.knowledge_interfaces.length import Length
from pytia.framework.knowledge_interfaces.real_param import RealParam
from pytia.framework.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeHelix(HybridShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_helix = com_object

    @property
    def axis(self) -> Reference:
        return Reference(self.hybrid_shape_helix.Axis)

    @axis.setter
    def axis(self, reference_axis: Reference):
        self.hybrid_shape_helix.Axis = reference_axis.com_object

    @property
    def clockwise_revolution(self) -> bool:
        return self.hybrid_shape_helix.ClockwiseRevolution

    @clockwise_revolution.setter
    def clockwise_revolution(self, value: bool):
        self.hybrid_shape_helix.ClockwiseRevolution = value

    @property
    def height(self) -> Length:
        return Length(self.hybrid_shape_helix.Height)

    @property
    def invert_axis(self) -> bool:
        return self.hybrid_shape_helix.InvertAxis

    @invert_axis.setter
    def invert_axis(self, value: bool):
        self.hybrid_shape_helix.InvertAxis = value

    @property
    def pitch(self) -> Length:
        return Length(self.hybrid_shape_helix.Pitch)

    @property
    def pitch2(self) -> Length:
        return Length(self.hybrid_shape_helix.Pitch2)

    @property
    def pitch_law_type(self) -> int:
        return self.hybrid_shape_helix.PitchLawType

    @pitch_law_type.setter
    def pitch_law_type(self, value: int):
        self.hybrid_shape_helix.PitchLawType = value

    @property
    def profile(self) -> Reference:
        return Reference(self.hybrid_shape_helix.Profile)

    @profile.setter
    def profile(self, reference_profile: Reference):
        self.hybrid_shape_helix.Profile = reference_profile.com_object

    @property
    def revol_number(self) -> RealParam:
        return RealParam(self.hybrid_shape_helix.RevolNumber)

    @property
    def starting_angle(self) -> Angle:
        return Angle(self.hybrid_shape_helix.StartingAngle)

    @property
    def starting_point(self) -> Reference:
        return Reference(self.hybrid_shape_helix.StartingPoint)

    @starting_point.setter
    def starting_point(self, reference_point: Reference):
        self.hybrid_shape_helix.StartingPoint = reference_point.com_object

    @property
    def taper_angle(self) -> Angle:
        return Angle(self.hybrid_shape_helix.TaperAngle)

    @property
    def taper_outward(self) -> bool:
        return self.hybrid_shape_helix.TaperOutward

    @taper_outward.setter
    def taper_outward(self, value: bool):
        self.hybrid_shape_helix.TaperOutward = value

    def set_height(self, i_height: float) -> None:
        return self.hybrid_shape_helix.SetHeight(i_height)

    def set_pitch(self, i_pitch: float) -> None:
        return self.hybrid_shape_helix.SetPitch(i_pitch)

    def set_pitch2(self, i_pitch2: float) -> None:
        return self.hybrid_shape_helix.SetPitch2(i_pitch2)

    def set_revolution_number(self, i_nb_revol: float) -> None:
        return self.hybrid_shape_helix.SetRevolutionNumber(i_nb_revol)

    def set_starting_angle(self, i_starting_angle: float) -> None:
        return self.hybrid_shape_helix.SetStartingAngle(i_starting_angle)

    def set_taper_angle(self, i_taper_angle: float) -> None:
        return self.hybrid_shape_helix.SetTaperAngle(i_taper_angle)

    def __repr__(self):
        return f'HybridShapeHelix(name="{ self.name }")'
