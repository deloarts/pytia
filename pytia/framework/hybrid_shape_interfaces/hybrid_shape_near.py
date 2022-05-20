from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeNear(HybridShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_near = com_object

    @property
    def multiple_solution(self) -> Reference:
        return Reference(self.hybrid_shape_near.MultipleSolution)

    @multiple_solution.setter
    def multiple_solution(self, reference: Reference):
        self.hybrid_shape_near.MultipleSolution = reference.com_object

    @property
    def reference_element(self) -> Reference:
        return Reference(self.hybrid_shape_near.ReferenceElement)

    @reference_element.setter
    def reference_element(self, reference_element: Reference):
        self.hybrid_shape_near.ReferenceElement = reference_element.com_object

    def __repr__(self):
        return f'HybridShapeNear(name="{ self.name }")'
