from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.knowledge_interfaces.length import Length
from pytia.framework.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeLoft(HybridShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_loft = com_object

    @property
    def area_law(self) -> Reference:
        return Reference(self.hybrid_shape_loft.AreaLaw)

    @area_law.setter
    def area_law(self, reference_law: Reference):
        self.hybrid_shape_loft.AreaLaw = reference_law.com_object

    @property
    def area_law_tolerance(self) -> float:
        return self.hybrid_shape_loft.AreaLawTolerance

    @area_law_tolerance.setter
    def area_law_tolerance(self, value: float):
        self.hybrid_shape_loft.AreaLawTolerance = value

    @property
    def boolean_operation(self) -> int:
        return self.hybrid_shape_loft.BooleanOperation

    @boolean_operation.setter
    def boolean_operation(self, value: int):
        self.hybrid_shape_loft.BooleanOperation = value

    @property
    def canonical_detection(self) -> int:
        return self.hybrid_shape_loft.CanonicalDetection

    @canonical_detection.setter
    def canonical_detection(self, value: int):
        self.hybrid_shape_loft.CanonicalDetection = value

    @property
    def comp_end_section_tangent(self) -> int:
        return self.hybrid_shape_loft.CompEndSectionTangent

    @comp_end_section_tangent.setter
    def comp_end_section_tangent(self, value: int):
        self.hybrid_shape_loft.CompEndSectionTangent = value

    @property
    def comp_start_section_tangent(self) -> int:
        return self.hybrid_shape_loft.CompStartSectionTangent

    @comp_start_section_tangent.setter
    def comp_start_section_tangent(self, value: int):
        self.hybrid_shape_loft.CompStartSectionTangent = value

    @property
    def context(self) -> int:
        return self.hybrid_shape_loft.Context

    @context.setter
    def context(self, value: int):
        self.hybrid_shape_loft.Context = value

    @property
    def relimitation(self) -> int:
        return self.hybrid_shape_loft.Relimitation

    @relimitation.setter
    def relimitation(self, value: int):
        self.hybrid_shape_loft.Relimitation = value

    @property
    def section_coupling(self) -> int:
        return self.hybrid_shape_loft.SectionCoupling

    @section_coupling.setter
    def section_coupling(self, value: int):
        self.hybrid_shape_loft.SectionCoupling = value

    @property
    def smooth_angle_threshold(self) -> float:
        return self.hybrid_shape_loft.SmoothAngleThreshold

    @smooth_angle_threshold.setter
    def smooth_angle_threshold(self, value: float):
        self.hybrid_shape_loft.SmoothAngleThreshold = value

    @property
    def smooth_angle_threshold_activity(self) -> bool:
        return self.hybrid_shape_loft.SmoothAngleThresholdActivity

    @smooth_angle_threshold_activity.setter
    def smooth_angle_threshold_activity(self, value: bool):
        self.hybrid_shape_loft.SmoothAngleThresholdActivity = value

    @property
    def smooth_deviation(self) -> float:
        return self.hybrid_shape_loft.SmoothDeviation

    @smooth_deviation.setter
    def smooth_deviation(self, value: float):
        self.hybrid_shape_loft.SmoothDeviation = value

    @property
    def smooth_deviation_activity(self) -> bool:
        return self.hybrid_shape_loft.SmoothDeviationActivity

    @smooth_deviation_activity.setter
    def smooth_deviation_activity(self, value: bool):
        self.hybrid_shape_loft.SmoothDeviationActivity = value

    def add_guide(self, i_guide: Reference) -> None:
        return self.hybrid_shape_loft.AddGuide(i_guide.com_object)

    def add_guide_with_tangent(self, i_guide: Reference, i_tangent: Reference) -> None:
        return self.hybrid_shape_loft.AddGuideWithTangent(
            i_guide.com_object, i_tangent.com_object
        )

    def add_section_to_loft(
        self, i_crv: Reference, i_ori: int, i_point: Reference
    ) -> None:
        return self.hybrid_shape_loft.AddSectionToLoft(
            i_crv.com_object, i_ori, i_point.com_object
        )

    def get_area_law_tolerance_parameter(self) -> Length:
        return Length(self.hybrid_shape_loft.GetAreaLawToleranceParameter())

    def get_faces_for_closing(
        self, o_start_face: Reference, o_end_face: Reference
    ) -> None:
        return self.hybrid_shape_loft.GetFacesForClosing(
            o_start_face.com_object, o_end_face.com_object
        )

    def get_guide(
        self, i_pos: int, o_guide: Reference, o_guide_tangent: Reference
    ) -> None:
        return self.hybrid_shape_loft.GetGuide(
            i_pos, o_guide.com_object, o_guide_tangent.com_object
        )

    def get_nb_of_guides(self) -> int:
        return self.hybrid_shape_loft.GetNbOfGuides()

    def get_section_from_loft(
        self, i_rank: int, o_crv: Reference, o_ori: int, o_point: Reference
    ) -> None:
        return self.hybrid_shape_loft.GetSectionFromLoft(
            i_rank, o_crv.com_object, o_ori, o_point.com_object
        )

    def get_spine(self, o_spine_type: int, o_spine: Reference) -> None:
        return self.hybrid_shape_loft.GetSpine(o_spine_type, o_spine.com_object)

    def get_start_and_end_section_tangent(
        self, o_start_section_tangent: Reference, o_end_section_tangent: Reference
    ) -> None:
        return self.hybrid_shape_loft.GetStartAndEndSectionTangent(
            o_start_section_tangent.com_object, o_end_section_tangent.com_object
        )

    def insert_coupling(self, i_position: int) -> None:
        return self.hybrid_shape_loft.InsertCoupling(i_position)

    def insert_coupling_point(
        self, i_coupling_index: int, i_position: int, i_point: Reference
    ) -> None:
        return self.hybrid_shape_loft.InsertCouplingPoint(
            i_coupling_index, i_position, i_point.com_object
        )

    def insert_section_to_loft(
        self,
        i_type: bool,
        i_crv: Reference,
        i_ori: int,
        i_point: Reference,
        i_section_ref: Reference,
    ) -> None:
        return self.hybrid_shape_loft.InsertSectionToLoft(
            i_type,
            i_crv.com_object,
            i_ori,
            i_point.com_object,
            i_section_ref.com_object,
        )

    def modify_guide_curve(self, i_guide: Reference, i_new_guide: Reference) -> None:
        return self.hybrid_shape_loft.ModifyGuideCurve(
            i_guide.com_object, i_new_guide.com_object
        )

    def modify_section_curve(
        self,
        i_section: Reference,
        i_new_section: Reference,
        o_curve_section: Reference,
        o_closing_point: Reference,
        o_pt_diag: int,
    ) -> None:
        return self.hybrid_shape_loft.ModifySectionCurve(
            i_section.com_object,
            i_new_section.com_object,
            o_curve_section.com_object,
            o_closing_point.com_object,
            o_pt_diag,
        )

    def modify_section_orient(self, i_section: Reference, i_orient: int) -> None:
        return self.hybrid_shape_loft.ModifySectionOrient(
            i_section.com_object, i_orient
        )

    def remove_face_for_closing(self, i_section: Reference) -> None:
        return self.hybrid_shape_loft.RemoveFaceForClosing(i_section.com_object)

    def remove_guide(self, i_guide: Reference) -> None:
        return self.hybrid_shape_loft.RemoveGuide(i_guide.com_object)

    def remove_guide_tangent(self, i_guide: Reference) -> None:
        return self.hybrid_shape_loft.RemoveGuideTangent(i_guide.com_object)

    def remove_section(self, i_section: Reference) -> None:
        return self.hybrid_shape_loft.RemoveSection(i_section.com_object)

    def remove_section_point(self, i_section: Reference) -> None:
        return self.hybrid_shape_loft.RemoveSectionPoint(i_section.com_object)

    def remove_section_tangent(self, i_section: Reference) -> None:
        return self.hybrid_shape_loft.RemoveSectionTangent(i_section.com_object)

    def set_end_face_for_closing(self, i_face: Reference) -> None:
        return self.hybrid_shape_loft.SetEndFaceForClosing(i_face.com_object)

    def set_end_section_tangent(self, i_tangent_section: Reference) -> None:
        return self.hybrid_shape_loft.SetEndSectionTangent(i_tangent_section.com_object)

    def set_spine(self, i_spine: Reference) -> None:
        return self.hybrid_shape_loft.SetSpine(i_spine.com_object)

    def set_start_face_for_closing(self, i_face: Reference) -> None:
        return self.hybrid_shape_loft.SetStartFaceForClosing(i_face.com_object)

    def set_start_section_tangent(self, i_tangent_section: Reference) -> None:
        return self.hybrid_shape_loft.SetStartSectionTangent(
            i_tangent_section.com_object
        )

    def __repr__(self):
        return f'HybridShapeLoft(name="{self.name}")'
