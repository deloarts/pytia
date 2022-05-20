from pytia.framework.hybrid_shape_interfaces.hybrid_shape_direction import (
    HybridShapeDirection,
)
from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.knowledge_interfaces.angle import Angle
from pytia.framework.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeReflectLine(HybridShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_reflect_line = com_object

    @property
    def angle(self) -> Angle:
        return Angle(self.hybrid_shape_reflect_line.Angle)

    @angle.setter
    def angle(self, angle: Angle):
        self.hybrid_shape_reflect_line.Angle = angle.com_object

    @property
    def direction(self) -> HybridShapeDirection:
        return HybridShapeDirection(self.hybrid_shape_reflect_line.Direction)

    @direction.setter
    def direction(self, direction: HybridShapeDirection):
        self.hybrid_shape_reflect_line.Direction = direction.com_object

    @property
    def orientation_direction(self) -> int:
        return self.hybrid_shape_reflect_line.OrientationDirection

    @orientation_direction.setter
    def orientation_direction(self, value: int):
        self.hybrid_shape_reflect_line.OrientationDirection = value

    @property
    def orientation_support(self) -> int:
        return self.hybrid_shape_reflect_line.OrientationSupport

    @orientation_support.setter
    def orientation_support(self, value: int):
        self.hybrid_shape_reflect_line.OrientationSupport = value

    @property
    def origin(self) -> Reference:
        return Reference(self.hybrid_shape_reflect_line.Origin)

    @origin.setter
    def origin(self, reference_origin: Reference):
        self.hybrid_shape_reflect_line.Origin = reference_origin.com_object

    @property
    def source_type(self) -> int:
        return self.hybrid_shape_reflect_line.SourceType

    @source_type.setter
    def source_type(self, value: int):
        self.hybrid_shape_reflect_line.SourceType = value

    @property
    def support(self) -> Reference:
        return Reference(self.hybrid_shape_reflect_line.Support)

    @support.setter
    def support(self, reference_support: Reference):
        self.hybrid_shape_reflect_line.Support = reference_support.com_object

    @property
    def type_solution(self) -> int:
        return self.hybrid_shape_reflect_line.TypeSolution

    @type_solution.setter
    def type_solution(self, value: int):
        self.hybrid_shape_reflect_line.TypeSolution = value

    def invert_orientation_direction(self) -> None:
        return self.hybrid_shape_reflect_line.InvertOrientationDirection()

    def invert_orientation_support(self) -> None:
        return self.hybrid_shape_reflect_line.InvertOrientationSupport()

    def __repr__(self):
        return f'HybridShapeReflectLine(name="{self.name}")'
