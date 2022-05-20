from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeAssemble(HybridShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_assemble = com_object

    @property
    def invert(self) -> bool:
        return self.hybrid_shape_assemble.Invert

    @invert.setter
    def invert(self, value: bool):
        self.hybrid_shape_assemble.Invert = value

    def add_element(self, i_element: Reference) -> None:
        return self.hybrid_shape_assemble.AddElement(i_element.com_object)

    def add_sub_element(self, i_sub_element: Reference) -> None:
        return self.hybrid_shape_assemble.AddSubElement(i_sub_element.com_object)

    def append_federated_element(self, i_element: Reference) -> None:
        return self.hybrid_shape_assemble.AppendFederatedElement(i_element.com_object)

    def get_angular_tolerance(self) -> float:
        return self.hybrid_shape_assemble.GetAngularTolerance()

    def get_angular_tolerance_mode(self) -> bool:
        return self.hybrid_shape_assemble.GetAngularToleranceMode()

    def get_connex(self) -> bool:
        return self.hybrid_shape_assemble.GetConnex()

    def get_deviation(self) -> float:
        return self.hybrid_shape_assemble.GetDeviation()

    def get_element(self, i_rank: int) -> Reference:
        return Reference(self.hybrid_shape_assemble.GetElement(i_rank))

    def get_elements_size(self) -> int:
        return self.hybrid_shape_assemble.GetElementsSize()

    def get_federated_element(self, i_rank: int) -> Reference:
        return Reference(self.hybrid_shape_assemble.GetFederatedElement(i_rank))

    def get_federated_elements_size(self) -> int:
        return self.hybrid_shape_assemble.GetFederatedElementsSize()

    def get_federation_propagation(self) -> int:
        return self.hybrid_shape_assemble.GetFederationPropagation()

    def get_manifold(self) -> bool:
        return self.hybrid_shape_assemble.GetManifold()

    def get_simplify(self) -> bool:
        return self.hybrid_shape_assemble.GetSimplify()

    def get_sub_element(self, i_rank: int) -> Reference:
        return Reference(self.hybrid_shape_assemble.GetSubElement(i_rank))

    def get_sub_elements_size(self) -> int:
        return self.hybrid_shape_assemble.GetSubElementsSize()

    def get_suppress_mode(self) -> bool:
        return self.hybrid_shape_assemble.GetSuppressMode()

    def get_tangency_continuity(self) -> bool:
        return self.hybrid_shape_assemble.GetTangencyContinuity()

    def remove_element(self, i_rank: int) -> None:
        return self.hybrid_shape_assemble.RemoveElement(i_rank)

    def remove_federated_element(self, i_rank: int) -> None:
        return self.hybrid_shape_assemble.RemoveFederatedElement(i_rank)

    def remove_sub_element(self, i_rank: int) -> None:
        return self.hybrid_shape_assemble.RemoveSubElement(i_rank)

    def replace_element(self, i_pos: int, i_element: Reference) -> None:
        return self.hybrid_shape_assemble.ReplaceElement(i_pos, i_element.com_object)

    def set_angular_tolerance(self, i_value: float) -> None:
        return self.hybrid_shape_assemble.SetAngularTolerance(i_value)

    def set_angular_tolerance_mode(self, i_value: bool) -> None:
        return self.hybrid_shape_assemble.SetAngularToleranceMode(i_value)

    def set_connex(self, i_connex: bool) -> None:
        return self.hybrid_shape_assemble.SetConnex(i_connex)

    def set_deviation(self, ideviation: float) -> None:
        return self.hybrid_shape_assemble.SetDeviation(ideviation)

    def set_federation_propagation(self, i_mode: int) -> None:
        return self.hybrid_shape_assemble.SetFederationPropagation(i_mode)

    def set_manifold(self, i_manifold: bool) -> None:
        return self.hybrid_shape_assemble.SetManifold(i_manifold)

    def set_simplify(self, i_simplify: bool) -> None:
        return self.hybrid_shape_assemble.SetSimplify(i_simplify)

    def set_suppress_mode(self, i_suppress_mode: bool) -> None:
        return self.hybrid_shape_assemble.SetSuppressMode(i_suppress_mode)

    def set_tangency_continuity(self, i_tangency_continuity: bool) -> None:
        return self.hybrid_shape_assemble.SetTangencyContinuity(i_tangency_continuity)

    def __repr__(self):
        return f'HybridShapeAssemble(name="{ self.name }")'
