from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeBoundary(HybridShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_boundary = com_object

    @property
    def from_(self) -> Reference:
        return Reference(self.hybrid_shape_boundary.From)

    @from_.setter
    def from_(self, reference: Reference):
        self.hybrid_shape_boundary.From = reference.com_object

    @property
    def from_orientation(self) -> int:
        return self.hybrid_shape_boundary.FromOrientation

    @from_orientation.setter
    def from_orientation(self, value: int):
        self.hybrid_shape_boundary.FromOrientation = value

    @property
    def initial_element(self) -> Reference:
        return Reference(self.hybrid_shape_boundary.InitialElement)

    @initial_element.setter
    def initial_element(self, value: Reference):
        self.hybrid_shape_boundary.InitialElement = value.com_object

    @property
    def propagation(self) -> int:
        return self.hybrid_shape_boundary.Propagation

    @propagation.setter
    def propagation(self, value: int):
        self.hybrid_shape_boundary.Propagation = value

    @property
    def support(self) -> Reference:
        return Reference(self.hybrid_shape_boundary.Support)

    @support.setter
    def support(self, support_reference: Reference):
        self.hybrid_shape_boundary.Support = support_reference.com_object

    @property
    def to(self) -> Reference:
        return Reference(self.hybrid_shape_boundary.To)

    @to.setter
    def to(self, value: Reference):
        self.hybrid_shape_boundary.To = value.com_object

    @property
    def to_orientation(self) -> int:
        return self.hybrid_shape_boundary.ToOrientation

    @to_orientation.setter
    def to_orientation(self, value: int):
        self.hybrid_shape_boundary.ToOrientation = value

    def __repr__(self):
        return f'HybridShapeBoundary(name="{self.name}")'
