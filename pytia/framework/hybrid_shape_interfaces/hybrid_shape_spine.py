from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeSpine(HybridShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_spine = com_object

    @property
    def orientation(self) -> int:
        return self.hybrid_shape_spine.Orientation

    @orientation.setter
    def orientation(self, value: int):
        self.hybrid_shape_spine.Orientation = value

    @property
    def start_point(self) -> Reference:
        return Reference(self.hybrid_shape_spine.StartPoint)

    @start_point.setter
    def start_point(self, reference_point: Reference):
        self.hybrid_shape_spine.StartPoint = reference_point.com_object

    def add_guide(self, i_guide: Reference) -> None:
        return self.hybrid_shape_spine.AddGuide(i_guide.com_object)

    def add_section(self, i_section: Reference) -> None:
        return self.hybrid_shape_spine.AddSection(i_section.com_object)

    def get_guide(self, i_idx: int, op_ia_guide: Reference) -> None:
        return self.hybrid_shape_spine.GetGuide(i_idx, op_ia_guide.com_object)

    def get_number_of_guides(self) -> int:
        return self.hybrid_shape_spine.GetNumberOfGuides()

    def get_number_of_sections(self) -> int:
        return self.hybrid_shape_spine.GetNumberOfSections()

    def get_section(self, i_idx: int, o_section: Reference) -> None:
        return self.hybrid_shape_spine.GetSection(i_idx, o_section.com_object)

    def modify_guide_curve(
        self, ip_ia_guide: Reference, ip_ia_new_guide: Reference
    ) -> None:
        return self.hybrid_shape_spine.ModifyGuideCurve(
            ip_ia_guide.com_object, ip_ia_new_guide.com_object
        )

    def modify_section_curve(
        self, ip_ia_section: Reference, ip_ia_new_section: Reference
    ) -> None:
        return self.hybrid_shape_spine.ModifySectionCurve(
            ip_ia_section.com_object, ip_ia_new_section.com_object
        )

    def remove_guide(self, i_guide: Reference) -> None:
        return self.hybrid_shape_spine.RemoveGuide(i_guide.com_object)

    def remove_section(self, i_section: Reference) -> None:
        return self.hybrid_shape_spine.RemoveSection(i_section.com_object)

    def set_start_point(self, i_point: Reference) -> None:
        return self.hybrid_shape_spine.SetStartPoint(i_point.com_object)

    def __repr__(self):
        return f'HybridShapeSpine(name="{self.name}")'
