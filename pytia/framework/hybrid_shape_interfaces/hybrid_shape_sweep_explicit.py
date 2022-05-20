from pytia.framework.hybrid_shape_interfaces.hybrid_shape_direction import (
    HybridShapeDirection,
)
from pytia.framework.hybrid_shape_interfaces.hybrid_shape_sweep import (
    HybridShapeSweep,
)
from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.knowledge_interfaces.angle import Angle
from pytia.framework.knowledge_interfaces.length import Length


class HybridShapeSweepExplicit(HybridShapeSweep):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_sweep_explicit = com_object

    @property
    def angle_law(self) -> Reference:
        return Reference(self.hybrid_shape_sweep_explicit.AngleLaw)

    @angle_law.setter
    def angle_law(self, reference_law: Reference):
        self.hybrid_shape_sweep_explicit.AngleLaw = reference_law.com_object

    @property
    def angle_law_inversion(self) -> int:
        return self.hybrid_shape_sweep_explicit.AngleLawInversion

    @angle_law_inversion.setter
    def angle_law_inversion(self, value: int):
        self.hybrid_shape_sweep_explicit.AngleLawInversion = value

    @property
    def angle_law_type(self) -> int:
        return self.hybrid_shape_sweep_explicit.AngleLawType

    @angle_law_type.setter
    def angle_law_type(self, value: int):
        self.hybrid_shape_sweep_explicit.AngleLawType = value

    @property
    def canonical_detection(self) -> int:
        return self.hybrid_shape_sweep_explicit.CanonicalDetection

    @canonical_detection.setter
    def canonical_detection(self, value: int):
        self.hybrid_shape_sweep_explicit.CanonicalDetection = value

    @property
    def context(self) -> int:
        return self.hybrid_shape_sweep_explicit.Context

    @context.setter
    def context(self, value: int):
        self.hybrid_shape_sweep_explicit.Context = value

    @property
    def first_guide_crv(self) -> Reference:
        return Reference(self.hybrid_shape_sweep_explicit.FirstGuideCrv)

    @first_guide_crv.setter
    def first_guide_crv(self, reference_curve: Reference):
        self.hybrid_shape_sweep_explicit.FirstGuideCrv = reference_curve.com_object

    @property
    def guide_deviation(self) -> Length:
        return Length(self.hybrid_shape_sweep_explicit.GuideDeviation)

    @property
    def guide_deviation_activity(self) -> bool:
        return self.hybrid_shape_sweep_explicit.GuideDeviationActivity

    @guide_deviation_activity.setter
    def guide_deviation_activity(self, value: bool):
        self.hybrid_shape_sweep_explicit.GuideDeviationActivity = value

    @property
    def guide_projection(self) -> bool:
        return self.hybrid_shape_sweep_explicit.GuideProjection

    @guide_projection.setter
    def guide_projection(self, value: bool):
        self.hybrid_shape_sweep_explicit.GuideProjection = value

    @property
    def mode(self) -> int:
        return self.hybrid_shape_sweep_explicit.Mode

    @mode.setter
    def mode(self, value: int):
        self.hybrid_shape_sweep_explicit.Mode = value

    @property
    def position_mode(self) -> int:
        return self.hybrid_shape_sweep_explicit.PositionMode

    @position_mode.setter
    def position_mode(self, value: int):
        self.hybrid_shape_sweep_explicit.PositionMode = value

    @property
    def positioned_profile(self) -> Reference:
        return Reference(self.hybrid_shape_sweep_explicit.PositionedProfile)

    @positioned_profile.setter
    def positioned_profile(self, reference_profile: Reference):
        self.hybrid_shape_sweep_explicit.PositionedProfile = (
            reference_profile.com_object
        )

    @property
    def profile(self) -> Reference:
        return Reference(self.hybrid_shape_sweep_explicit.Profile)

    @profile.setter
    def profile(self, reference_profile: Reference):
        self.hybrid_shape_sweep_explicit.Profile = reference_profile.com_object

    @property
    def profile_x_axis_computation_mode(self) -> int:
        return self.hybrid_shape_sweep_explicit.ProfileXAxisComputationMode

    @profile_x_axis_computation_mode.setter
    def profile_x_axis_computation_mode(self, value: int):
        self.hybrid_shape_sweep_explicit.ProfileXAxisComputationMode = value

    @property
    def pulling_direction(self) -> HybridShapeDirection:
        return HybridShapeDirection(self.hybrid_shape_sweep_explicit.PullingDirection)

    @pulling_direction.setter
    def pulling_direction(self, direction: HybridShapeDirection):
        self.hybrid_shape_sweep_explicit.PullingDirection = direction.com_object

    @property
    def reference(self) -> Reference:
        return Reference(self.hybrid_shape_sweep_explicit.Reference)

    @reference.setter
    def reference(self, reference: Reference):
        self.hybrid_shape_sweep_explicit.Reference = reference.com_object

    @property
    def second_guide_crv(self) -> Reference:
        return Reference(self.hybrid_shape_sweep_explicit.SecondGuideCrv)

    @second_guide_crv.setter
    def second_guide_crv(self, reference_curve: Reference):
        self.hybrid_shape_sweep_explicit.SecondGuideCrv = reference_curve.com_object

    @property
    def smooth_activity(self) -> bool:
        return self.hybrid_shape_sweep_explicit.SmoothActivity

    @smooth_activity.setter
    def smooth_activity(self, value: bool):
        self.hybrid_shape_sweep_explicit.SmoothActivity = value

    @property
    def smooth_angle_threshold(self) -> Angle:
        return Angle(self.hybrid_shape_sweep_explicit.SmoothAngleThreshold)

    @property
    def solution_no(self) -> int:
        return self.hybrid_shape_sweep_explicit.SolutionNo

    @solution_no.setter
    def solution_no(self, value: int):
        self.hybrid_shape_sweep_explicit.SolutionNo = value

    @property
    def spine(self) -> Reference:
        return Reference(self.hybrid_shape_sweep_explicit.Spine)

    @spine.setter
    def spine(self, reference_spine: Reference):
        self.hybrid_shape_sweep_explicit.Spine = reference_spine.com_object

    @property
    def sub_type(self) -> int:
        return self.hybrid_shape_sweep_explicit.SubType

    @sub_type.setter
    def sub_type(self, value: int):
        self.hybrid_shape_sweep_explicit.SubType = value

    def get_angle_ref(self, ii: int) -> Angle:
        return Angle(self.hybrid_shape_sweep_explicit.GetAngleRef(ii))

    def get_fitting_points(
        self, op_ia_elem_a: Reference, op_ia_elem_b: Reference
    ) -> None:
        return self.hybrid_shape_sweep_explicit.GetFittingPoints(
            op_ia_elem_a.com_object, op_ia_elem_b.com_object
        )

    def get_longitudinal_relimiters(
        self, op_ia_elem_a: Reference, op_ia_elem_b: Reference
    ) -> None:
        return self.hybrid_shape_sweep_explicit.GetLongitudinalRelimiters(
            op_ia_elem_a.com_object, op_ia_elem_b.com_object
        )

    def get_nb_angle(self, o_ang: int) -> None:
        return self.hybrid_shape_sweep_explicit.GetNbAngle(o_ang)

    def get_nb_guide(self, o_num: int) -> None:
        return self.hybrid_shape_sweep_explicit.GetNbGuide(o_num)

    def get_nb_pos_angle(self, o_pos_ang: int) -> None:
        return self.hybrid_shape_sweep_explicit.GetNbPosAngle(o_pos_ang)

    def get_nb_pos_coord(self, o_pos_coord: int) -> None:
        return self.hybrid_shape_sweep_explicit.GetNbPosCoord(o_pos_coord)

    def get_pos_angle(self, ii: int) -> Angle:
        return Angle(self.hybrid_shape_sweep_explicit.GetPosAngle(ii))

    def get_pos_coord(self, ii: int) -> Length:
        return Length(self.hybrid_shape_sweep_explicit.GetPosCoord(ii))

    def get_pos_direction(self, ii: int) -> Reference:
        return Reference(self.hybrid_shape_sweep_explicit.GetPosDirection(ii))

    def get_pos_point(self, ii: int) -> Reference:
        return Reference(self.hybrid_shape_sweep_explicit.GetPosPoint(ii))

    def get_pos_swap_axes(self, ii: int) -> int:
        return self.hybrid_shape_sweep_explicit.GetPosSwapAxes(ii)

    def get_relimiters(
        self,
        op_ia_elem1: Reference,
        op_orient1: int,
        op_ia_elem2: Reference,
        op_orient2: int,
    ) -> None:
        return self.hybrid_shape_sweep_explicit.GetRelimiters(
            op_ia_elem1.com_object, op_orient1, op_ia_elem2.com_object, op_orient2
        )

    def is_sketch_axis_used_as_default(self, o_boolean: bool) -> None:
        return self.hybrid_shape_sweep_explicit.IsSketchAxisUsedAsDefault(o_boolean)

    def remove_angle(self) -> None:
        return self.hybrid_shape_sweep_explicit.RemoveAngle()

    def remove_fitting_points(self) -> None:
        return self.hybrid_shape_sweep_explicit.RemoveFittingPoints()

    def remove_guide(self) -> None:
        return self.hybrid_shape_sweep_explicit.RemoveGuide()

    def set_angle_ref(self, ii: int, elem: float) -> None:
        return self.hybrid_shape_sweep_explicit.SetAngleRef(ii, elem)

    def set_fitting_points(
        self, ip_ia_elem_a: Reference, ip_ia_elem_b: Reference
    ) -> None:
        return self.hybrid_shape_sweep_explicit.SetFittingPoints(
            ip_ia_elem_a.com_object, ip_ia_elem_b.com_object
        )

    def set_guide_deviation(self, i_length: float) -> None:
        return self.hybrid_shape_sweep_explicit.SetGuideDeviation(i_length)

    def set_longitudinal_relimiters(
        self, ip_ia_elem_a: Reference, ip_ia_elem_b: Reference
    ) -> None:
        return self.hybrid_shape_sweep_explicit.SetLongitudinalRelimiters(
            ip_ia_elem_a.com_object, ip_ia_elem_b.com_object
        )

    def set_pos_angle(self, ii: int, elem: float) -> None:
        return self.hybrid_shape_sweep_explicit.SetPosAngle(ii, elem)

    def set_pos_coord(self, ii: int, elem: float) -> None:
        return self.hybrid_shape_sweep_explicit.SetPosCoord(ii, elem)

    def set_pos_direction(self, ii: int, elem: Reference) -> None:
        return self.hybrid_shape_sweep_explicit.SetPosDirection(ii, elem.com_object)

    def set_pos_point(self, ii: int, elem: Reference) -> None:
        return self.hybrid_shape_sweep_explicit.SetPosPoint(ii, elem.com_object)

    def set_pos_swap_axes(self, ii: int, elem: int) -> None:
        return self.hybrid_shape_sweep_explicit.SetPosSwapAxes(ii, elem)

    def set_relimiters(
        self,
        ip_ia_elem1: Reference,
        ip_orient1: int,
        ip_ia_elem2: Reference,
        ip_orient2: int,
    ) -> None:
        return self.hybrid_shape_sweep_explicit.SetRelimiters(
            ip_ia_elem1.com_object, ip_orient1, ip_ia_elem2.com_object, ip_orient2
        )

    def set_smooth_angle_threshold(self, i_angle: float) -> None:
        return self.hybrid_shape_sweep_explicit.SetSmoothAngleThreshold(i_angle)

    def use_sketch_axis_as_default(self, i_boolean: bool) -> None:
        return self.hybrid_shape_sweep_explicit.UseSketchAxisAsDefault(i_boolean)

    def __repr__(self):
        return f'HybridShapeSweepExplicit(name="{self.name}")'
