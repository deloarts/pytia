from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeSymmetry(HybridShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_symmetry = com_object

    @property
    def creation_mode(self) -> bool:
        return self.hybrid_shape_symmetry.CreationMode

    @creation_mode.setter
    def creation_mode(self, value: bool):
        self.hybrid_shape_symmetry.CreationMode = value

    @property
    def elem_to_symmetry(self) -> Reference:
        return Reference(self.hybrid_shape_symmetry.ElemToSymmetry)

    @elem_to_symmetry.setter
    def elem_to_symmetry(self, reference_element: Reference):
        self.hybrid_shape_symmetry.ElemToSymmetry = reference_element.com_object

    @property
    def reference(self) -> Reference:
        return Reference(self.hybrid_shape_symmetry.Reference)

    @reference.setter
    def reference(self, reference: Reference):
        self.hybrid_shape_symmetry.Reference = reference.com_object

    @property
    def volume_result(self) -> bool:
        return self.hybrid_shape_symmetry.VolumeResult

    @volume_result.setter
    def volume_result(self, value: bool):
        self.hybrid_shape_symmetry.VolumeResult = value

    def __repr__(self):
        return f'HybridShapeSymmetry(name="{self.name}")'
