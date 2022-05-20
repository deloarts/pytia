from pytia.framework.hybrid_shape_interfaces.hybrid_shape_circle import (
    HybridShapeCircle,
)
from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.knowledge_interfaces.length import Length


class HybridShapeCircleCenterAxis(HybridShapeCircle):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_circle_center_axis = com_object

    @property
    def axis(self) -> Reference:
        return Reference(self.hybrid_shape_circle_center_axis.Axis)

    @axis.setter
    def axis(self, reference_axis: Reference):
        self.hybrid_shape_circle_center_axis.Axis = reference_axis.com_object

    @property
    def diameter(self) -> Length:
        return Length(self.hybrid_shape_circle_center_axis.Diameter)

    @property
    def diameter_mode(self) -> bool:
        return self.hybrid_shape_circle_center_axis.DiameterMode

    @diameter_mode.setter
    def diameter_mode(self, value: bool):
        self.hybrid_shape_circle_center_axis.DiameterMode = value

    @property
    def point(self) -> Reference:
        return Reference(self.hybrid_shape_circle_center_axis.Point)

    @point.setter
    def point(self, reference_point: Reference):
        self.hybrid_shape_circle_center_axis.Point = reference_point.com_object

    @property
    def projection_mode(self) -> bool:
        return self.hybrid_shape_circle_center_axis.ProjectionMode

    @projection_mode.setter
    def projection_mode(self, value: bool):
        self.hybrid_shape_circle_center_axis.ProjectionMode = value

    @property
    def radius(self) -> Length:
        return Length(self.hybrid_shape_circle_center_axis.Radius)

    def __repr__(self):
        return f'HybridShapeCircleCenterAxis(name="{self.name}")'
