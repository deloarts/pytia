from pytia.framework.hybrid_shape_interfaces.hybrid_shape_direction import (
    HybridShapeDirection,
)
from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeProject(HybridShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_project = com_object

    @property
    def direction(self) -> HybridShapeDirection:
        return HybridShapeDirection(self.hybrid_shape_project.Direction)

    @direction.setter
    def direction(self, direction: HybridShapeDirection):
        self.hybrid_shape_project.Direction = direction.com_object

    @property
    def elem_to_project(self) -> Reference:
        return Reference(self.hybrid_shape_project.ElemToProject)

    @elem_to_project.setter
    def elem_to_project(self, reference_element: Reference):
        self.hybrid_shape_project.ElemToProject = reference_element.com_object

    @property
    def extrapolation_mode(self) -> int:
        return self.hybrid_shape_project.ExtrapolationMode

    @extrapolation_mode.setter
    def extrapolation_mode(self, value: int):
        self.hybrid_shape_project.ExtrapolationMode = value

    @property
    def maximum_deviation_value(self) -> float:
        return self.hybrid_shape_project.MaximumDeviationValue

    @maximum_deviation_value.setter
    def maximum_deviation_value(self, value: float):
        self.hybrid_shape_project.MaximumDeviationValue = value

    @property
    def normal(self) -> bool:
        return self.hybrid_shape_project.Normal

    @normal.setter
    def normal(self, value: bool):
        self.hybrid_shape_project.Normal = value

    @property
    def smoothing_type(self) -> int:
        return self.hybrid_shape_project.SmoothingType

    @smoothing_type.setter
    def smoothing_type(self, value: int):
        self.hybrid_shape_project.SmoothingType = value

    @property
    def solution_type(self) -> int:
        return self.hybrid_shape_project.SolutionType

    @solution_type.setter
    def solution_type(self, value: int):
        self.hybrid_shape_project.SolutionType = value

    @property
    def support(self) -> Reference:
        return Reference(self.hybrid_shape_project.Support)

    @support.setter
    def support(self, reference_support: Reference):
        self.hybrid_shape_project.Support = reference_support.com_object

    @property
    def p_3d_smoothing(self) -> bool:
        return self.hybrid_shape_project.p3DSmoothing

    @p_3d_smoothing.setter
    def p_3d_smoothing(self, value: bool):
        self.hybrid_shape_project.p3DSmoothing = value

    def __repr__(self):
        return f'HybridShapeProject(name="{self.name}")'
