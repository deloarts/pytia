from pytia.framework.hybrid_shape_interfaces.hybrid_shape_sweep import (
    HybridShapeSweep,
)
from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.knowledge_interfaces.angle import Angle
from pytia.framework.knowledge_interfaces.length import Length


class HybridShapeSweepConic(HybridShapeSweep):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_sweep_conic = com_object

    @property
    def canonical_detection(self) -> int:
        return self.hybrid_shape_sweep_conic.CanonicalDetection

    @canonical_detection.setter
    def canonical_detection(self, value: int):
        self.hybrid_shape_sweep_conic.CanonicalDetection = value

    @property
    def fifth_guide_crv(self) -> Reference:
        return Reference(self.hybrid_shape_sweep_conic.FifthGuideCrv)

    @fifth_guide_crv.setter
    def fifth_guide_crv(self, reference_curve: Reference):
        self.hybrid_shape_sweep_conic.FifthGuideCrv = reference_curve.com_object

    @property
    def first_guide_crv(self) -> Reference:
        return Reference(self.hybrid_shape_sweep_conic.FirstGuideCrv)

    @first_guide_crv.setter
    def first_guide_crv(self, reference_curve: Reference):
        self.hybrid_shape_sweep_conic.FirstGuideCrv = reference_curve.com_object

    @property
    def fourth_guide_crv(self) -> Reference:
        return Reference(self.hybrid_shape_sweep_conic.FourthGuideCrv)

    @fourth_guide_crv.setter
    def fourth_guide_crv(self, reference_curve: Reference):
        self.hybrid_shape_sweep_conic.FourthGuideCrv = reference_curve.com_object

    @property
    def guide_deviation(self) -> Length:
        return Length(self.hybrid_shape_sweep_conic.GuideDeviation)

    @property
    def guide_deviation_activity(self) -> bool:
        return self.hybrid_shape_sweep_conic.GuideDeviationActivity

    @guide_deviation_activity.setter
    def guide_deviation_activity(self, value: bool):
        self.hybrid_shape_sweep_conic.GuideDeviationActivity = value

    @property
    def parameter(self) -> float:
        return self.hybrid_shape_sweep_conic.Parameter

    @parameter.setter
    def parameter(self, value: float):
        self.hybrid_shape_sweep_conic.Parameter = value

    @property
    def parameter_law(self) -> Reference:
        return Reference(self.hybrid_shape_sweep_conic.ParameterLaw)

    @parameter_law.setter
    def parameter_law(self, reference_law: Reference):
        self.hybrid_shape_sweep_conic.ParameterLaw = reference_law.com_object

    @property
    def parameter_law_inversion(self) -> bool:
        return self.hybrid_shape_sweep_conic.ParameterLawInversion

    @parameter_law_inversion.setter
    def parameter_law_inversion(self, value: bool):
        self.hybrid_shape_sweep_conic.ParameterLawInversion = value

    @property
    def parameter_law_type(self) -> int:
        return self.hybrid_shape_sweep_conic.ParameterLawType

    @parameter_law_type.setter
    def parameter_law_type(self, value: int):
        self.hybrid_shape_sweep_conic.ParameterLawType = value

    @property
    def second_guide_crv(self) -> Reference:
        return Reference(self.hybrid_shape_sweep_conic.SecondGuideCrv)

    @second_guide_crv.setter
    def second_guide_crv(self, reference_curve: Reference):
        self.hybrid_shape_sweep_conic.SecondGuideCrv = reference_curve.com_object

    @property
    def smooth_activity(self) -> bool:
        return self.hybrid_shape_sweep_conic.SmoothActivity

    @smooth_activity.setter
    def smooth_activity(self, value: bool):
        self.hybrid_shape_sweep_conic.SmoothActivity = value

    @property
    def smooth_angle_threshold(self) -> Angle:
        return Angle(self.hybrid_shape_sweep_conic.SmoothAngleThreshold)

    @property
    def spine(self) -> Reference:
        return Reference(self.hybrid_shape_sweep_conic.Spine)

    @spine.setter
    def spine(self, reference_spine: Reference):
        self.hybrid_shape_sweep_conic.Spine = reference_spine.com_object

    @property
    def third_guide_crv(self) -> Reference:
        return Reference(self.hybrid_shape_sweep_conic.ThirdGuideCrv)

    @third_guide_crv.setter
    def third_guide_crv(self, reference_curve: Reference):
        self.hybrid_shape_sweep_conic.ThirdGuideCrv = reference_curve.com_object

    def get_longitudinal_relimiters(
        self, op_ia_elem1: Reference, op_ia_elem2: Reference
    ) -> None:
        return self.hybrid_shape_sweep_conic.GetLongitudinalRelimiters(
            op_ia_elem1.com_object, op_ia_elem2.com_object
        )

    def get_nb_guides(self, o_num: int) -> None:
        return self.hybrid_shape_sweep_conic.GetNbGuides(o_num)

    def get_parameter_law(
        self, o_param_start: float, o_param_end: float, o_law_type: int
    ) -> None:
        return self.hybrid_shape_sweep_conic.GetParameterLaw(
            o_param_start, o_param_end, o_law_type
        )

    def get_relimiters(
        self,
        op_ia_elem1: Reference,
        op_orient1: int,
        op_ia_elem2: Reference,
        op_orient2: int,
    ) -> None:
        return self.hybrid_shape_sweep_conic.GetRelimiters(
            op_ia_elem1.com_object, op_orient1, op_ia_elem2.com_object, op_orient2
        )

    def get_tangency(
        self,
        op_ia_elem: Reference,
        op_ia_angle_start: Angle,
        op_ia_angle_end: Angle,
        o_law_type: int,
        i_index: int,
    ) -> None:
        return self.hybrid_shape_sweep_conic.GetTangency(
            op_ia_elem.com_object,
            op_ia_angle_start.com_object,
            op_ia_angle_end.com_object,
            o_law_type,
            i_index,
        )

    def get_tangency_angle_law_inversion(self, i_index: int, o_inversion: int) -> None:
        return self.hybrid_shape_sweep_conic.GetTangencyAngleLawInversion(
            i_index, o_inversion
        )

    def get_tangency_law(
        self, op_ia_elem: Reference, op_ia_law: Reference, i_index: int
    ) -> None:
        return self.hybrid_shape_sweep_conic.GetTangencyLaw(
            op_ia_elem.com_object, op_ia_law.com_object, i_index
        )

    def remove_guide(self, i_index: int) -> None:
        return self.hybrid_shape_sweep_conic.RemoveGuide(i_index)

    def remove_parameter(self) -> None:
        return self.hybrid_shape_sweep_conic.RemoveParameter()

    def remove_tangency(self, i_index: int) -> None:
        return self.hybrid_shape_sweep_conic.RemoveTangency(i_index)

    def set_guide_deviation(self, i_length: float) -> None:
        return self.hybrid_shape_sweep_conic.SetGuideDeviation(i_length)

    def set_longitudinal_relimiters(
        self, ip_ia_elem1: Reference, ip_ia_elem2: Reference
    ) -> None:
        return self.hybrid_shape_sweep_conic.SetLongitudinalRelimiters(
            ip_ia_elem1.com_object, ip_ia_elem2.com_object
        )

    def set_parameter_law(
        self, i_param_start: float, i_param_end: float, i_law_type: int
    ) -> None:
        return self.hybrid_shape_sweep_conic.SetParameterLaw(
            i_param_start, i_param_end, i_law_type
        )

    def set_relimiters(
        self,
        ip_ia_elem1: Reference,
        ip_orient1: int,
        ip_ia_elem2: Reference,
        ip_orient2: int,
    ) -> None:
        return self.hybrid_shape_sweep_conic.SetRelimiters(
            ip_ia_elem1.com_object, ip_orient1, ip_ia_elem2.com_object, ip_orient2
        )

    def set_smooth_angle_threshold(self, i_angle: float) -> None:
        return self.hybrid_shape_sweep_conic.SetSmoothAngleThreshold(i_angle)

    def set_tangency(
        self,
        ip_ia_elem: Reference,
        i_angle_start: float,
        i_angle_end: float,
        ilaw_type: int,
        i_index: int,
    ) -> None:
        return self.hybrid_shape_sweep_conic.SetTangency(
            ip_ia_elem.com_object, i_angle_start, i_angle_end, ilaw_type, i_index
        )

    def set_tangency_angle_law_inversion(self, i_index: int, i_inversion: int) -> None:
        return self.hybrid_shape_sweep_conic.SetTangencyAngleLawInversion(
            i_index, i_inversion
        )

    def set_tangency_law(
        self, ip_ia_elem: Reference, ip_ia_law: Reference, i_index: int
    ) -> None:
        return self.hybrid_shape_sweep_conic.SetTangencyLaw(
            ip_ia_elem.com_object, ip_ia_law.com_object, i_index
        )

    def __repr__(self):
        return f'HybridShapeSweepConic(name="{self.name}")'
