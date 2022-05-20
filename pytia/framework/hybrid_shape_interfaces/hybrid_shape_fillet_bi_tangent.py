from pytia.framework.hybrid_shape_interfaces.hybrid_shape_integrated_law import (
    HybridShapeIntegratedLaw,
)
from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.knowledge_interfaces.length import Length
from pytia.framework.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeFilletBiTangent(HybridShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_fillet_bi_tangent = com_object

    @property
    def conical_section_parameter(self) -> float:
        return self.hybrid_shape_fillet_bi_tangent.ConicalSectionParameter

    @conical_section_parameter.setter
    def conical_section_parameter(self, value: float):
        self.hybrid_shape_fillet_bi_tangent.ConicalSectionParameter = value

    @property
    def first_elem(self) -> Reference:
        return Reference(self.hybrid_shape_fillet_bi_tangent.FirstElem)

    @first_elem.setter
    def first_elem(self, reference_element: Reference):
        self.hybrid_shape_fillet_bi_tangent.FirstElem = reference_element.com_object

    @property
    def first_law_relimiter(self) -> Reference:
        return Reference(self.hybrid_shape_fillet_bi_tangent.FirstLawRelimiter)

    @first_law_relimiter.setter
    def first_law_relimiter(self, reference: Reference):
        self.hybrid_shape_fillet_bi_tangent.FirstLawRelimiter = reference.com_object

    @property
    def first_orientation(self) -> int:
        return self.hybrid_shape_fillet_bi_tangent.FirstOrientation

    @first_orientation.setter
    def first_orientation(self, value: int):
        self.hybrid_shape_fillet_bi_tangent.FirstOrientation = value

    @property
    def hold_curve(self) -> Reference:
        return Reference(self.hybrid_shape_fillet_bi_tangent.HoldCurve)

    @hold_curve.setter
    def hold_curve(self, reference_curve: Reference):
        self.hybrid_shape_fillet_bi_tangent.HoldCurve = reference_curve.com_object

    @property
    def integrated_law(self) -> HybridShapeIntegratedLaw:
        return HybridShapeIntegratedLaw(
            self.hybrid_shape_fillet_bi_tangent.IntegratedLaw
        )

    @integrated_law.setter
    def integrated_law(self, law: HybridShapeIntegratedLaw):
        self.hybrid_shape_fillet_bi_tangent.IntegratedLaw = law.com_object

    @property
    def radius(self) -> Length:
        return Length(self.hybrid_shape_fillet_bi_tangent.Radius)

    @property
    def radius_type(self) -> int:
        return self.hybrid_shape_fillet_bi_tangent.RadiusType

    @radius_type.setter
    def radius_type(self, value: int):
        self.hybrid_shape_fillet_bi_tangent.RadiusType = value

    @property
    def radius_value(self) -> float:
        return self.hybrid_shape_fillet_bi_tangent.RadiusValue

    @radius_value.setter
    def radius_value(self, value: float):
        self.hybrid_shape_fillet_bi_tangent.RadiusValue = value

    @property
    def ribbon_relimitation_mode(self) -> int:
        return self.hybrid_shape_fillet_bi_tangent.RibbonRelimitationMode

    @ribbon_relimitation_mode.setter
    def ribbon_relimitation_mode(self, value: int):
        self.hybrid_shape_fillet_bi_tangent.RibbonRelimitationMode = value

    @property
    def second_elem(self) -> Reference:
        return Reference(self.hybrid_shape_fillet_bi_tangent.SecondElem)

    @second_elem.setter
    def second_elem(self, reference_element: Reference):
        self.hybrid_shape_fillet_bi_tangent.SecondElem = reference_element

    @property
    def second_law_relimiter(self) -> Reference:
        return Reference(self.hybrid_shape_fillet_bi_tangent.SecondLawRelimiter)

    @second_law_relimiter.setter
    def second_law_relimiter(self, reference_law: Reference):
        self.hybrid_shape_fillet_bi_tangent.SecondLawRelimiter = (
            reference_law.com_object
        )

    @property
    def second_orientation(self) -> int:
        return self.hybrid_shape_fillet_bi_tangent.SecondOrientation

    @second_orientation.setter
    def second_orientation(self, value: int):
        self.hybrid_shape_fillet_bi_tangent.SecondOrientation = value

    @property
    def section_type(self) -> int:
        return self.hybrid_shape_fillet_bi_tangent.SectionType

    @section_type.setter
    def section_type(self, value: int):
        self.hybrid_shape_fillet_bi_tangent.SectionType = value

    @property
    def spine(self) -> Reference:
        return Reference(self.hybrid_shape_fillet_bi_tangent.Spine)

    @spine.setter
    def spine(self, reference_spine: Reference):
        self.hybrid_shape_fillet_bi_tangent.Spine = reference_spine.com_object

    @property
    def supports_trim_mode(self) -> int:
        return self.hybrid_shape_fillet_bi_tangent.SupportsTrimMode

    @supports_trim_mode.setter
    def supports_trim_mode(self, value: int):
        self.hybrid_shape_fillet_bi_tangent.SupportsTrimMode = value

    def append_new_face_to_keep(self, i_face: Reference) -> None:
        return self.hybrid_shape_fillet_bi_tangent.AppendNewFaceToKeep(
            i_face.com_object
        )

    def get_face_to_keep(self, i_pos: int) -> Reference:
        return Reference(self.hybrid_shape_fillet_bi_tangent.GetFaceToKeep(i_pos))

    def invert_first_orientation(self) -> None:
        return self.hybrid_shape_fillet_bi_tangent.InvertFirstOrientation()

    def invert_second_orientation(self) -> None:
        return self.hybrid_shape_fillet_bi_tangent.InvertSecondOrientation()

    def remove_all_faces_to_keep(self) -> None:
        return self.hybrid_shape_fillet_bi_tangent.RemoveAllFacesToKeep()

    def remove_face_to_keep(self, i_face: Reference) -> None:
        return self.hybrid_shape_fillet_bi_tangent.RemoveFaceToKeep(i_face.com_object)

    def __repr__(self):
        return f'HybridShapeFilletBiTangent(name="{self.name}")'
