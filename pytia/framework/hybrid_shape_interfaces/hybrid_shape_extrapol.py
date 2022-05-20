from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.knowledge_interfaces.length import Length
from pytia.framework.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeExtrapol(HybridShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_extrapol = com_object

    @property
    def border_type(self) -> int:
        return self.hybrid_shape_extrapol.BorderType

    @border_type.setter
    def border_type(self, value: int):
        self.hybrid_shape_extrapol.BorderType = value

    @property
    def boundary(self) -> Reference:
        return Reference(self.hybrid_shape_extrapol.Boundary)

    @boundary.setter
    def boundary(self, reference_boundary: Reference):
        self.hybrid_shape_extrapol.Boundary = reference_boundary.com_object

    @property
    def constant_length_mode(self) -> bool:
        return self.hybrid_shape_extrapol.ConstantLengthMode

    @constant_length_mode.setter
    def constant_length_mode(self, value: bool):
        self.hybrid_shape_extrapol.ConstantLengthMode = value

    @property
    def continuity_type(self) -> int:
        return self.hybrid_shape_extrapol.ContinuityType

    @continuity_type.setter
    def continuity_type(self, value: int):
        self.hybrid_shape_extrapol.ContinuityType = value

    @property
    def elem_to_extrapol(self) -> Reference:
        return Reference(self.hybrid_shape_extrapol.ElemToExtrapol)

    @elem_to_extrapol.setter
    def elem_to_extrapol(self, reference_element: Reference):
        self.hybrid_shape_extrapol.ElemToExtrapol = reference_element.com_object

    @property
    def elem_until(self) -> Reference:
        return Reference(self.hybrid_shape_extrapol.ElemUntil)

    @elem_until.setter
    def elem_until(self, reference_element: Reference):
        self.hybrid_shape_extrapol.ElemUntil = reference_element.com_object

    @property
    def extend_edges_mode(self) -> bool:
        return self.hybrid_shape_extrapol.ExtendEdgesMode

    @extend_edges_mode.setter
    def extend_edges_mode(self, value: bool):
        self.hybrid_shape_extrapol.ExtendEdgesMode = value

    @property
    def extrapol_both_sides_identically(self) -> bool:
        return self.hybrid_shape_extrapol.ExtrapolBothSidesIdentically

    @extrapol_both_sides_identically.setter
    def extrapol_both_sides_identically(self, value: bool):
        self.hybrid_shape_extrapol.ExtrapolBothSidesIdentically = value

    @property
    def length(self) -> Length:
        return Length(self.hybrid_shape_extrapol.Length)

    @property
    def limit_type(self) -> int:
        return self.hybrid_shape_extrapol.LimitType

    @limit_type.setter
    def limit_type(self, value: int):
        self.hybrid_shape_extrapol.LimitType = value

    @property
    def propagation_mode(self) -> int:
        return self.hybrid_shape_extrapol.PropagationMode

    @propagation_mode.setter
    def propagation_mode(self, value: int):
        self.hybrid_shape_extrapol.PropagationMode = value

    @property
    def support(self) -> Reference:
        return Reference(self.hybrid_shape_extrapol.Support)

    @support.setter
    def support(self, value: Reference):
        self.hybrid_shape_extrapol.Support = value

    def get_boundary(self, i_pos: int) -> Reference:
        return Reference(self.hybrid_shape_extrapol.GetBoundary(i_pos))

    def get_continuity_type(self, i_pos: int) -> int:
        return self.hybrid_shape_extrapol.GetContinuityType(i_pos)

    def get_elem_until(self, i_pos: int) -> Reference:
        return Reference(self.hybrid_shape_extrapol.GetElemUntil(i_pos))

    def get_internal_edges_element(self, i_pos: int) -> Reference:
        return Reference(self.hybrid_shape_extrapol.GetInternalEdgesElement(i_pos))

    def get_length(self, i_pos: int) -> Length:
        return Length(self.hybrid_shape_extrapol.GetLength(i_pos))

    def get_limit_type(self, i_pos: int) -> int:
        return self.hybrid_shape_extrapol.GetLimitType(i_pos)

    def get_number_of_extrapolations(self) -> int:
        return self.hybrid_shape_extrapol.GetNumberOfExtrapolations()

    def is_assemble(self) -> bool:
        return self.hybrid_shape_extrapol.IsAssemble()

    def remove_all_extrapolations_except_the_first_one(self) -> None:
        return self.hybrid_shape_extrapol.RemoveAllExtrapolationsExceptTheFirstOne()

    def remove_all_internal_edges_element(self) -> None:
        return self.hybrid_shape_extrapol.RemoveAllInternalEdgesElement()

    def remove_extrapolation(self, i_pos: int) -> None:
        return self.hybrid_shape_extrapol.RemoveExtrapolation(i_pos)

    def set_assemble(self, i_assemble: bool) -> None:
        return self.hybrid_shape_extrapol.SetAssemble(i_assemble)

    def set_boundary(self, i_pos: int, i_boundary: Reference) -> None:
        return self.hybrid_shape_extrapol.SetBoundary(i_pos, i_boundary.com_object)

    def set_continuity_type(self, i_pos: int, i_lim: int) -> None:
        return self.hybrid_shape_extrapol.SetContinuityType(i_pos, i_lim)

    def set_elem_until(self, i_pos: int, i_elem_until: Reference) -> None:
        return self.hybrid_shape_extrapol.SetElemUntil(i_pos, i_elem_until.com_object)

    def set_length(self, i_pos: int, i_length: Length) -> None:
        return self.hybrid_shape_extrapol.SetLength(i_pos, i_length.com_object)

    def set_length_d(self, i_pos: int, i_length: float) -> None:
        return self.hybrid_shape_extrapol.SetLengthD(i_pos, i_length)

    def set_limit_type(self, i_pos: int, i_lim: int) -> None:
        return self.hybrid_shape_extrapol.SetLimitType(i_pos, i_lim)

    def __repr__(self):
        return f'HybridShapeExtrapol(name="{self.name}")'
