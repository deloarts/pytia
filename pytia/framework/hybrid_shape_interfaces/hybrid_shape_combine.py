from pytia.framework.hybrid_shape_interfaces.hybrid_shape_direction import (
    HybridShapeDirection,
)
from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeCombine(HybridShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_combine = com_object

    @property
    def direction1(self) -> HybridShapeDirection:
        return HybridShapeDirection(self.hybrid_shape_combine.Direction1)

    @direction1.setter
    def direction1(self, direction: HybridShapeDirection):
        self.hybrid_shape_combine.Direction1 = direction.com_object

    @property
    def direction2(self) -> HybridShapeDirection:
        return HybridShapeDirection(self.hybrid_shape_combine.Direction2)

    @direction2.setter
    def direction2(self, direction: HybridShapeDirection):
        self.hybrid_shape_combine.Direction2 = direction.com_object

    @property
    def elem1(self) -> Reference:
        return Reference(self.hybrid_shape_combine.Elem1)

    @elem1.setter
    def elem1(self, reference_element: Reference):
        self.hybrid_shape_combine.Elem1 = reference_element.com_object

    @property
    def elem2(self) -> Reference:
        return Reference(self.hybrid_shape_combine.Elem2)

    @elem2.setter
    def elem2(self, reference_element: Reference):
        self.hybrid_shape_combine.Elem2 = reference_element.com_object

    @property
    def nearest_solution(self) -> int:
        return self.hybrid_shape_combine.NearestSolution

    @nearest_solution.setter
    def nearest_solution(self, value: int):
        self.hybrid_shape_combine.NearestSolution = value

    @property
    def solution_type_combine(self) -> int:
        return self.hybrid_shape_combine.SolutionTypeCombine

    @solution_type_combine.setter
    def solution_type_combine(self, value: int):
        self.hybrid_shape_combine.SolutionTypeCombine = value

    def __repr__(self):
        return f'HybridShapeCombine(name="{self.name}")'
