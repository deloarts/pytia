from pytia.framework.hybrid_shape_interfaces.hybrid_shape_direction import (
    HybridShapeDirection,
)
from pytia.framework.hybrid_shape_interfaces.hybrid_shape_sweep import (
    HybridShapeSweep,
)
from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.knowledge_interfaces.angle import Angle
from pytia.framework.knowledge_interfaces.length import Length


class HybridShapeSweepLine(HybridShapeSweep):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_sweep_line = com_object

    @property
    def angle_law(self) -> Reference:
        return Reference(self.hybrid_shape_sweep_line.AngleLaw)

    @angle_law.setter
    def angle_law(self, reference_law: Reference):
        self.hybrid_shape_sweep_line.AngleLaw = reference_law.com_object

    @property
    def angle_law_inversion(self) -> int:
        return self.hybrid_shape_sweep_line.AngleLawInversion

    @angle_law_inversion.setter
    def angle_law_inversion(self, value: int):
        self.hybrid_shape_sweep_line.AngleLawInversion = value

    @property
    def angle_law_type(self) -> int:
        return self.hybrid_shape_sweep_line.AngleLawType

    @angle_law_type.setter
    def angle_law_type(self, value: int):
        self.hybrid_shape_sweep_line.AngleLawType = value

    @property
    def canonical_detection(self) -> int:
        return self.hybrid_shape_sweep_line.CanonicalDetection

    @canonical_detection.setter
    def canonical_detection(self, value: int):
        self.hybrid_shape_sweep_line.CanonicalDetection = value

    @property
    def context(self) -> int:
        return self.hybrid_shape_sweep_line.Context

    @context.setter
    def context(self, value: int):
        self.hybrid_shape_sweep_line.Context = value

    @property
    def draft_computation_mode(self) -> int:
        return self.hybrid_shape_sweep_line.DraftComputationMode

    @draft_computation_mode.setter
    def draft_computation_mode(self, value: int):
        self.hybrid_shape_sweep_line.DraftComputationMode = value

    @property
    def draft_direction(self) -> HybridShapeDirection:
        return HybridShapeDirection(self.hybrid_shape_sweep_line.DraftDirection)

    @draft_direction.setter
    def draft_direction(self, direction: HybridShapeDirection):
        self.hybrid_shape_sweep_line.DraftDirection = direction.com_object

    @property
    def first_guide_crv(self) -> Reference:
        return Reference(self.hybrid_shape_sweep_line.FirstGuideCrv)

    @first_guide_crv.setter
    def first_guide_crv(self, reference_curve: Reference):
        self.hybrid_shape_sweep_line.FirstGuideCrv = reference_curve.com_object

    @property
    def first_guide_surf(self) -> Reference:
        return Reference(self.hybrid_shape_sweep_line.FirstGuideSurf)

    @first_guide_surf.setter
    def first_guide_surf(self, reference_surface: Reference):
        self.hybrid_shape_sweep_line.FirstGuideSurf = reference_surface.com_object

    @property
    def first_length_law(self) -> Reference:
        return Reference(self.hybrid_shape_sweep_line.FirstLengthLaw)

    @first_length_law.setter
    def first_length_law(self, reference_law: Reference):
        self.hybrid_shape_sweep_line.FirstLengthLaw = reference_law.com_object

    @property
    def first_length_law_inversion(self) -> int:
        return self.hybrid_shape_sweep_line.FirstLengthLawInversion

    @first_length_law_inversion.setter
    def first_length_law_inversion(self, value: int):
        self.hybrid_shape_sweep_line.FirstLengthLawInversion = value

    @property
    def guide_deviation(self) -> Length:
        return Length(self.hybrid_shape_sweep_line.GuideDeviation)

    @property
    def guide_deviation_activity(self) -> bool:
        return self.hybrid_shape_sweep_line.GuideDeviationActivity

    @guide_deviation_activity.setter
    def guide_deviation_activity(self, value: bool):
        self.hybrid_shape_sweep_line.GuideDeviationActivity = value

    @property
    def mode(self) -> int:
        return self.hybrid_shape_sweep_line.Mode

    @mode.setter
    def mode(self, value: int):
        self.hybrid_shape_sweep_line.Mode = value

    @property
    def second_guide_crv(self) -> Reference:
        return Reference(self.hybrid_shape_sweep_line.SecondGuideCrv)

    @second_guide_crv.setter
    def second_guide_crv(self, reference_curve: Reference):
        self.hybrid_shape_sweep_line.SecondGuideCrv = reference_curve.com_object

    @property
    def second_guide_surf(self) -> Reference:
        return Reference(self.hybrid_shape_sweep_line.SecondGuideSurf)

    @second_guide_surf.setter
    def second_guide_surf(self, reference_surface: Reference):
        self.hybrid_shape_sweep_line.SecondGuideSurf = reference_surface.com_object

    @property
    def second_length_law(self) -> Reference:
        return Reference(self.hybrid_shape_sweep_line.SecondLengthLaw)

    @second_length_law.setter
    def second_length_law(self, reference_law: Reference):
        self.hybrid_shape_sweep_line.SecondLengthLaw = reference_law.com_object

    @property
    def second_length_law_inversion(self) -> int:
        return self.hybrid_shape_sweep_line.SecondLengthLawInversion

    @second_length_law_inversion.setter
    def second_length_law_inversion(self, value: int):
        self.hybrid_shape_sweep_line.SecondLengthLawInversion = value

    @property
    def second_trim_option(self) -> int:
        return self.hybrid_shape_sweep_line.SecondTrimOption

    @second_trim_option.setter
    def second_trim_option(self, value: int):
        self.hybrid_shape_sweep_line.SecondTrimOption = value

    @property
    def smooth_activity(self) -> bool:
        return self.hybrid_shape_sweep_line.SmoothActivity

    @smooth_activity.setter
    def smooth_activity(self, value: bool):
        self.hybrid_shape_sweep_line.SmoothActivity = value

    @property
    def smooth_angle_threshold(self) -> Angle:
        return Angle(self.hybrid_shape_sweep_line.SmoothAngleThreshold)

    @property
    def solution_no(self) -> int:
        return self.hybrid_shape_sweep_line.SolutionNo

    @solution_no.setter
    def solution_no(self, value: int):
        self.hybrid_shape_sweep_line.SolutionNo = value

    @property
    def spine(self) -> Reference:
        return Reference(self.hybrid_shape_sweep_line.Spine)

    @spine.setter
    def spine(self, reference_spine: Reference):
        self.hybrid_shape_sweep_line.Spine = reference_spine.com_object

    @property
    def trim_option(self) -> int:
        return self.hybrid_shape_sweep_line.TrimOption

    @trim_option.setter
    def trim_option(self, value: int):
        self.hybrid_shape_sweep_line.TrimOption = value

    def add_draft_angle_definition_location(
        self, ip_ia_loc_elem: Reference, i_ang: float
    ) -> None:
        return self.hybrid_shape_sweep_line.AddDraftAngleDefinitionLocation(
            ip_ia_loc_elem.com_object, i_ang
        )

    def get_angle(self, i_i: int) -> Angle:
        return Angle(self.hybrid_shape_sweep_line.GetAngle(i_i))

    def get_angular_law(
        self, op_start_ang: Angle, op_end_ang: Angle, o_law_type: int
    ) -> None:
        return self.hybrid_shape_sweep_line.GetAngularLaw(
            op_start_ang.com_object, op_end_ang.com_object, o_law_type
        )

    def get_choice_nb_surfaces(
        self,
        o_surf_ori1: int,
        o_surf_ori2: int,
        o_surf_coupl_ori1: int,
        o_surf_coupl_ori2: int,
        o_no: int,
    ) -> None:
        return self.hybrid_shape_sweep_line.GetChoiceNbSurfaces(
            o_surf_ori1, o_surf_ori2, o_surf_coupl_ori1, o_surf_coupl_ori2, o_no
        )

    def get_choice_no(self, o_val1: int, o_val2: int, o_val3: int) -> None:
        return self.hybrid_shape_sweep_line.GetChoiceNo(o_val1, o_val2, o_val3)

    def get_draft_angle_definition_location(
        self, i_loc: int, op_ia_element: Reference, o_angle: Angle
    ) -> None:
        return self.hybrid_shape_sweep_line.GetDraftAngleDefinitionLocation(
            i_loc, op_ia_element.com_object, o_angle.com_object
        )

    def get_draft_angle_definition_locations_nb(self, o_count: int) -> None:
        return self.hybrid_shape_sweep_line.GetDraftAngleDefinitionLocationsNb(o_count)

    def get_first_length_definition_type(
        self, o_first_type: int, op_ia_elem: Reference
    ) -> None:
        return self.hybrid_shape_sweep_line.GetFirstLengthDefinitionType(
            o_first_type, op_ia_elem.com_object
        )

    def get_first_length_law(
        self, o_length1: Length, o_length2: Length, o_law_type: int
    ) -> None:
        return self.hybrid_shape_sweep_line.GetFirstLengthLaw(
            o_length1.com_object, o_length2.com_object, o_law_type
        )

    def get_length(self, i_i: int) -> Length:
        return Length(self.hybrid_shape_sweep_line.GetLength(i_i))

    def get_length_law_types(self, o_first_type: int, o_second_type: int) -> None:
        return self.hybrid_shape_sweep_line.GetLengthLawTypes(
            o_first_type, o_second_type
        )

    def get_longitudinal_relimiters(
        self, op_ia_elem1: Reference, op_ia_elem2: Reference
    ) -> None:
        return self.hybrid_shape_sweep_line.GetLongitudinalRelimiters(
            op_ia_elem1.com_object, op_ia_elem2.com_object
        )

    def get_nb_angle(self, o_ang: int) -> None:
        return self.hybrid_shape_sweep_line.GetNbAngle(o_ang)

    def get_nb_guide_crv(self, o_num: int) -> None:
        return self.hybrid_shape_sweep_line.GetNbGuideCrv(o_num)

    def get_nb_guide_sur(self, o_num: int) -> None:
        return self.hybrid_shape_sweep_line.GetNbGuideSur(o_num)

    def get_nb_length(self, o_len: int) -> None:
        return self.hybrid_shape_sweep_line.GetNbLength(o_len)

    def get_relimiters(
        self,
        op_ia_elem1: Reference,
        op_orient1: int,
        op_ia_elem2: Reference,
        op_orient2: int,
    ) -> None:
        return self.hybrid_shape_sweep_line.GetRelimiters(
            op_ia_elem1.com_object, op_orient1, op_ia_elem2.com_object, op_orient2
        )

    def get_second_length_definition_type(
        self, o_second_type: int, op_ia_elem: Reference
    ) -> None:
        return self.hybrid_shape_sweep_line.GetSecondLengthDefinitionType(
            o_second_type, op_ia_elem.com_object
        )

    def get_second_length_law(
        self, o_length1: Length, o_length2: Length, o_law_type: int
    ) -> None:
        return self.hybrid_shape_sweep_line.GetSecondLengthLaw(
            o_length1.com_object, o_length2.com_object, o_law_type
        )

    def insert_draft_angle_definition_location(
        self, i_elem: Reference, i_angle: Angle, i_pos: int
    ) -> None:
        return self.hybrid_shape_sweep_line.InsertDraftAngleDefinitionLocation(
            i_elem.com_object, i_angle.com_object, i_pos
        )

    def remove_all_draft_angle_definition_locations(self) -> None:
        return self.hybrid_shape_sweep_line.RemoveAllDraftAngleDefinitionLocations()

    def remove_angle(self) -> None:
        return self.hybrid_shape_sweep_line.RemoveAngle()

    def remove_draft_angle_definition_location_position(self, i_pos: int) -> None:
        return self.hybrid_shape_sweep_line.RemoveDraftAngleDefinitionLocationPosition(
            i_pos
        )

    def remove_guide_crv(self) -> None:
        return self.hybrid_shape_sweep_line.RemoveGuideCrv()

    def remove_guide_sur(self) -> None:
        return self.hybrid_shape_sweep_line.RemoveGuideSur()

    def remove_length(self) -> None:
        return self.hybrid_shape_sweep_line.RemoveLength()

    def set_angle(self, i_i: int, i_elem: float) -> None:
        return self.hybrid_shape_sweep_line.SetAngle(i_i, i_elem)

    def set_angular_law(
        self, i_start_ang: float, i_end_ang: float, i_law_type: int
    ) -> None:
        return self.hybrid_shape_sweep_line.SetAngularLaw(
            i_start_ang, i_end_ang, i_law_type
        )

    def set_choice_nb_surfaces(
        self,
        i_surf_ori1: int,
        i_surf_ori2: int,
        i_surf_coupl_ori1: int,
        i_surf_coupl_ori2: int,
        i_no: int,
    ) -> None:
        return self.hybrid_shape_sweep_line.SetChoiceNbSurfaces(
            i_surf_ori1, i_surf_ori2, i_surf_coupl_ori1, i_surf_coupl_ori2, i_no
        )

    def set_choice_no(self, i_val1: int, i_val2: int, i_val3: int) -> None:
        return self.hybrid_shape_sweep_line.SetChoiceNo(i_val1, i_val2, i_val3)

    def set_first_length_definition_type(
        self, i_first_type: int, ip_ia_elem: Reference
    ) -> None:
        return self.hybrid_shape_sweep_line.SetFirstLengthDefinitionType(
            i_first_type, ip_ia_elem.com_object
        )

    def set_first_length_law(
        self, i_length1: float, i_length2: float, i_law_type: int
    ) -> None:
        return self.hybrid_shape_sweep_line.SetFirstLengthLaw(
            i_length1, i_length2, i_law_type
        )

    def set_guide_deviation(self, i_length: float) -> None:
        return self.hybrid_shape_sweep_line.SetGuideDeviation(i_length)

    def set_length(self, i_i: int, i_elem: float) -> None:
        return self.hybrid_shape_sweep_line.SetLength(i_i, i_elem)

    def set_length_law_types(self, i_first_type: int, i_second_type: int) -> None:
        return self.hybrid_shape_sweep_line.SetLengthLawTypes(
            i_first_type, i_second_type
        )

    def set_longitudinal_relimiters(
        self, ip_ia_elem1: Reference, ip_ia_elem2: Reference
    ) -> None:
        return self.hybrid_shape_sweep_line.SetLongitudinalRelimiters(
            ip_ia_elem1.com_object, ip_ia_elem2.com_object
        )

    def set_relimiters(
        self,
        ip_ia_elem1: Reference,
        ip_orient1: int,
        ip_ia_elem2: Reference,
        ip_orient2: int,
    ) -> None:
        return self.hybrid_shape_sweep_line.SetRelimiters(
            ip_ia_elem1.com_object, ip_orient1, ip_ia_elem2.com_object, ip_orient2
        )

    def set_second_length_definition_type(
        self, i_second_type: int, ip_ia_elem: Reference
    ) -> None:
        return self.hybrid_shape_sweep_line.SetSecondLengthDefinitionType(
            i_second_type, ip_ia_elem.com_object
        )

    def set_second_length_law(
        self, i_length1: float, i_length2: float, i_law_type: int
    ) -> None:
        return self.hybrid_shape_sweep_line.SetSecondLengthLaw(
            i_length1, i_length2, i_law_type
        )

    def set_smooth_angle_threshold(self, i_angle: float) -> None:
        return self.hybrid_shape_sweep_line.SetSmoothAngleThreshold(i_angle)

    def __repr__(self):
        return f'HybridShapeSweepLine(name="{self.name}")'
