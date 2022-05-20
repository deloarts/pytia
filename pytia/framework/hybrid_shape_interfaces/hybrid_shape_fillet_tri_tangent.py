from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeFilletTriTangent(HybridShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_fillet_tri_tangent = com_object

    @property
    def first_elem(self) -> Reference:
        return Reference(self.hybrid_shape_fillet_tri_tangent.FirstElem)

    @first_elem.setter
    def first_elem(self, reference_element: Reference):
        self.hybrid_shape_fillet_tri_tangent.FirstElem = reference_element.com_object

    @property
    def first_orientation(self) -> int:
        return self.hybrid_shape_fillet_tri_tangent.FirstOrientation

    @first_orientation.setter
    def first_orientation(self, value: int):
        self.hybrid_shape_fillet_tri_tangent.FirstOrientation = value

    @property
    def remove_elem(self) -> Reference:
        return Reference(self.hybrid_shape_fillet_tri_tangent.RemoveElem)

    @remove_elem.setter
    def remove_elem(self, reference_element: Reference):
        self.hybrid_shape_fillet_tri_tangent.RemoveElem = reference_element.com_object

    @property
    def remove_orientation(self) -> int:
        return self.hybrid_shape_fillet_tri_tangent.RemoveOrientation

    @remove_orientation.setter
    def remove_orientation(self, value: int):
        self.hybrid_shape_fillet_tri_tangent.RemoveOrientation = value

    @property
    def ribbon_relimitation_mode(self) -> int:
        return self.hybrid_shape_fillet_tri_tangent.RibbonRelimitationMode

    @ribbon_relimitation_mode.setter
    def ribbon_relimitation_mode(self, value: int):
        self.hybrid_shape_fillet_tri_tangent.RibbonRelimitationMode = value

    @property
    def second_elem(self) -> Reference:
        return Reference(self.hybrid_shape_fillet_tri_tangent.SecondElem)

    @second_elem.setter
    def second_elem(self, reference_element: Reference):
        self.hybrid_shape_fillet_tri_tangent.SecondElem = reference_element.com_object

    @property
    def second_orientation(self) -> int:
        return self.hybrid_shape_fillet_tri_tangent.SecondOrientation

    @second_orientation.setter
    def second_orientation(self, value: int):
        self.hybrid_shape_fillet_tri_tangent.SecondOrientation = value

    @property
    def supports_trim_mode(self) -> int:
        return self.hybrid_shape_fillet_tri_tangent.SupportsTrimMode

    @supports_trim_mode.setter
    def supports_trim_mode(self, value: int):
        self.hybrid_shape_fillet_tri_tangent.SupportsTrimMode = value

    def invert_first_orientation(self) -> None:
        return self.hybrid_shape_fillet_tri_tangent.InvertFirstOrientation()

    def invert_remove_orientation(self) -> None:
        return self.hybrid_shape_fillet_tri_tangent.InvertRemoveOrientation()

    def invert_second_orientation(self) -> None:
        return self.hybrid_shape_fillet_tri_tangent.InvertSecondOrientation()

    def __repr__(self):
        return f'HybridShapeFilletTriTangent(name="{ self.name }")'
