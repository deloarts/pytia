from pytia.framework.hybrid_shape_interfaces.hybrid_shape_sweep import (
    HybridShapeSweep,
)
from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.knowledge_interfaces.angle import Angle
from pytia.framework.knowledge_interfaces.length import Length


class HybridShapeSweepCircle(HybridShapeSweep):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_sweep_circle = com_object

    @property
    def canonical_detection(self) -> int:
        return self.hybrid_shape_sweep_circle.CanonicalDetection

    @canonical_detection.setter
    def canonical_detection(self, value: int):
        self.hybrid_shape_sweep_circle.CanonicalDetection = value

    @property
    def choice_no(self) -> int:
        return self.hybrid_shape_sweep_circle.ChoiceNo

    @choice_no.setter
    def choice_no(self, value: int):
        self.hybrid_shape_sweep_circle.ChoiceNo = value

    @property
    def context(self) -> int:
        return self.hybrid_shape_sweep_circle.Context

    @context.setter
    def context(self, value: int):
        self.hybrid_shape_sweep_circle.Context = value

    @property
    def first_angle_law(self) -> Reference:
        return Reference(self.hybrid_shape_sweep_circle.FirstAngleLaw)

    @first_angle_law.setter
    def first_angle_law(self, reference_law: Reference):
        self.hybrid_shape_sweep_circle.FirstAngleLaw = reference_law.com_object

    @property
    def first_angle_law_inversion(self) -> int:
        return self.hybrid_shape_sweep_circle.FirstAngleLawInversion

    @first_angle_law_inversion.setter
    def first_angle_law_inversion(self, value: int):
        self.hybrid_shape_sweep_circle.FirstAngleLawInversion = value

    @property
    def first_guide_crv(self) -> Reference:
        return Reference(self.hybrid_shape_sweep_circle.FirstGuideCrv)

    @first_guide_crv.setter
    def first_guide_crv(self, reference_curve: Reference):
        self.hybrid_shape_sweep_circle.FirstGuideCrv = reference_curve.com_object

    @property
    def guide_deviation(self) -> Length:
        return Length(self.hybrid_shape_sweep_circle.GuideDeviation)

    @property
    def guide_deviation_activity(self) -> bool:
        return self.hybrid_shape_sweep_circle.GuideDeviationActivity

    @guide_deviation_activity.setter
    def guide_deviation_activity(self, value: bool):
        self.hybrid_shape_sweep_circle.GuideDeviationActivity = value

    @property
    def mode(self) -> int:
        return self.hybrid_shape_sweep_circle.Mode

    @mode.setter
    def mode(self, value: int):
        self.hybrid_shape_sweep_circle.Mode = value

    @property
    def radius_law(self) -> Reference:
        return Reference(self.hybrid_shape_sweep_circle.RadiusLaw)

    @radius_law.setter
    def radius_law(self, reference_law: Reference):
        self.hybrid_shape_sweep_circle.RadiusLaw = reference_law.com_object

    @property
    def radius_law_inversion(self) -> int:
        return self.hybrid_shape_sweep_circle.RadiusLawInversion

    @radius_law_inversion.setter
    def radius_law_inversion(self, value: int):
        self.hybrid_shape_sweep_circle.RadiusLawInversion = value

    @property
    def radius_law_type(self) -> int:
        return self.hybrid_shape_sweep_circle.RadiusLawType

    @radius_law_type.setter
    def radius_law_type(self, value: int):
        self.hybrid_shape_sweep_circle.RadiusLawType = value

    @property
    def reference(self) -> Reference:
        return Reference(self.hybrid_shape_sweep_circle.Reference)

    @reference.setter
    def reference(self, reference: Reference):
        self.hybrid_shape_sweep_circle.Reference = reference.com_object

    @property
    def second_angle_law(self) -> Reference:
        return Reference(self.hybrid_shape_sweep_circle.SecondAngleLaw)

    @second_angle_law.setter
    def second_angle_law(self, reference_law: Reference):
        self.hybrid_shape_sweep_circle.SecondAngleLaw = reference_law.com_object

    @property
    def second_angle_law_inversion(self) -> int:
        return self.hybrid_shape_sweep_circle.SecondAngleLawInversion

    @second_angle_law_inversion.setter
    def second_angle_law_inversion(self, value: int):
        self.hybrid_shape_sweep_circle.SecondAngleLawInversion = value

    @property
    def second_guide_crv(self) -> Reference:
        return Reference(self.hybrid_shape_sweep_circle.SecondGuideCrv)

    @second_guide_crv.setter
    def second_guide_crv(self, reference_curve: Reference):
        self.hybrid_shape_sweep_circle.SecondGuideCrv = reference_curve.com_object

    @property
    def smooth_activity(self) -> bool:
        return self.hybrid_shape_sweep_circle.SmoothActivity

    @smooth_activity.setter
    def smooth_activity(self, value: bool):
        self.hybrid_shape_sweep_circle.SmoothActivity = value

    @property
    def smooth_angle_threshold(self) -> Angle:
        return Angle(self.hybrid_shape_sweep_circle.SmoothAngleThreshold)

    @property
    def spine(self) -> Reference:
        return Reference(self.hybrid_shape_sweep_circle.Spine)

    @spine.setter
    def spine(self, reference_spine: Reference):
        self.hybrid_shape_sweep_circle.Spine = reference_spine.com_object

    @property
    def third_guide_crv(self) -> Reference:
        return Reference(self.hybrid_shape_sweep_circle.ThirdGuideCrv)

    @third_guide_crv.setter
    def third_guide_crv(self, reference_curve: Reference):
        self.hybrid_shape_sweep_circle.ThirdGuideCrv = reference_curve.com_object

    @property
    def trim_option(self) -> int:
        return self.hybrid_shape_sweep_circle.TrimOption

    @trim_option.setter
    def trim_option(self, value: int):
        self.hybrid_shape_sweep_circle.TrimOption = value

    def get_angle(self, i_i: int) -> Angle:
        return Angle(self.hybrid_shape_sweep_circle.GetAngle(i_i))

    def get_angle_law_types(self, o_first_type: int, o_second_type: int) -> None:
        return self.hybrid_shape_sweep_circle.GetAngleLawTypes(
            o_first_type, o_second_type
        )

    def get_first_angle_law(
        self, o_elem1: Angle, o_elem2: Angle, ol_law_type: int
    ) -> None:
        return self.hybrid_shape_sweep_circle.GetFirstAngleLaw(
            o_elem1.com_object, o_elem2.com_object, ol_law_type
        )

    def get_longitudinal_relimiters(
        self, op_ia_elem1: Reference, op_ia_elem2: Reference
    ) -> None:
        return self.hybrid_shape_sweep_circle.GetLongitudinalRelimiters(
            op_ia_elem1.com_object, op_ia_elem2.com_object
        )

    def get_nb_angle(self, o_ang: int) -> None:
        return self.hybrid_shape_sweep_circle.GetNbAngle(o_ang)

    def get_nb_guide(self, o_num: int) -> None:
        return self.hybrid_shape_sweep_circle.GetNbGuide(o_num)

    def get_nb_radius(self, o_rad: int) -> None:
        return self.hybrid_shape_sweep_circle.GetNbRadius(o_rad)

    def get_radius(self, i_i: int) -> Length:
        return Length(self.hybrid_shape_sweep_circle.GetRadius(i_i))

    def get_relimiters(
        self,
        op_ia_elem1: Reference,
        op_orient1: int,
        op_ia_elem2: Reference,
        op_orient2: int,
    ) -> None:
        return self.hybrid_shape_sweep_circle.GetRelimiters(
            op_ia_elem1.com_object, op_orient1, op_ia_elem2.com_object, op_orient2
        )

    def get_second_angle_law(
        self, o_elem1: Angle, o_elem2: Angle, ol_law_type: int
    ) -> None:
        return self.hybrid_shape_sweep_circle.GetSecondAngleLaw(
            o_elem1.com_object, o_elem2.com_object, ol_law_type
        )

    def get_tangency_choice_no(
        self, o_no: int, o_shell_ori: int, o_guide_ori: int
    ) -> None:
        return self.hybrid_shape_sweep_circle.GetTangencyChoiceNo(
            o_no, o_shell_ori, o_guide_ori
        )

    def remove_angle(self) -> None:
        return self.hybrid_shape_sweep_circle.RemoveAngle()

    def remove_guide(self) -> None:
        return self.hybrid_shape_sweep_circle.RemoveGuide()

    def remove_radius(self) -> None:
        return self.hybrid_shape_sweep_circle.RemoveRadius()

    def set_angle(self, i_i: int, i_elem: float) -> None:
        return self.hybrid_shape_sweep_circle.SetAngle(i_i, i_elem)

    def set_angle_law_types(self, i_first_type: int, i_second_type: int) -> None:
        return self.hybrid_shape_sweep_circle.SetAngleLawTypes(
            i_first_type, i_second_type
        )

    def set_first_angle_law(
        self, i_elem1: float, i_elem2: float, il_law_type: int
    ) -> None:
        return self.hybrid_shape_sweep_circle.SetFirstAngleLaw(
            i_elem1, i_elem2, il_law_type
        )

    def set_guide_deviation(self, i_length: float) -> None:
        return self.hybrid_shape_sweep_circle.SetGuideDeviation(i_length)

    def set_longitudinal_relimiters(
        self, ip_ia_elem1: Reference, ip_ia_elem2: Reference
    ) -> None:
        return self.hybrid_shape_sweep_circle.SetLongitudinalRelimiters(
            ip_ia_elem1.com_object, ip_ia_elem2.com_object
        )

    def set_radius(self, i_i: int, i_radius: float) -> None:
        return self.hybrid_shape_sweep_circle.SetRadius(i_i, i_radius)

    def set_relimiters(
        self,
        ip_ia_elem1: Reference,
        ip_orient1: int,
        ip_ia_elem2: Reference,
        ip_orient2: int,
    ) -> None:
        return self.hybrid_shape_sweep_circle.SetRelimiters(
            ip_ia_elem1.com_object, ip_orient1, ip_ia_elem2.com_object, ip_orient2
        )

    def set_second_angle_law(
        self, i_elem1: float, i_elem2: float, il_law_type: int
    ) -> None:
        return self.hybrid_shape_sweep_circle.SetSecondAngleLaw(
            i_elem1, i_elem2, il_law_type
        )

    def set_smooth_angle_threshold(self, i_angle: float) -> None:
        return self.hybrid_shape_sweep_circle.SetSmoothAngleThreshold(i_angle)

    def set_tangency_choice_no(
        self, i_shell_ori: int, i_guide_ori: int, i_no: int
    ) -> None:
        return self.hybrid_shape_sweep_circle.SetTangencyChoiceNo(
            i_shell_ori, i_guide_ori, i_no
        )

    def __repr__(self):
        return f'HybridShapeSweepCircle(name="{self.name}")'
