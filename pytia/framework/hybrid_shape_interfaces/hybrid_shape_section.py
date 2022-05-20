from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeSection(HybridShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_section = com_object

    @property
    def section_plane(self) -> Reference:
        return Reference(self.hybrid_shape_section.SectionPlane)

    @section_plane.setter
    def section_plane(self, reference_plane: Reference):
        self.hybrid_shape_section.SectionPlane = reference_plane.com_object

    def __repr__(self):
        return f'HybridShapeSection(name="{self.name}")'
