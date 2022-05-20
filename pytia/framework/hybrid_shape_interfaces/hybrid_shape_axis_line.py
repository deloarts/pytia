from pytia.framework.hybrid_shape_interfaces.hybrid_shape_direction import (
    HybridShapeDirection,
)
from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeAxisLine(HybridShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_axis_line = com_object

    @property
    def axis_line_type(self) -> int:
        return self.hybrid_shape_axis_line.AxisLineType

    @axis_line_type.setter
    def axis_line_type(self, value: int):
        self.hybrid_shape_axis_line.AxisLineType = value

    @property
    def direction(self) -> HybridShapeDirection:
        return HybridShapeDirection(self.hybrid_shape_axis_line.Direction)

    @direction.setter
    def direction(self, value: HybridShapeDirection):
        self.hybrid_shape_axis_line.Direction = value

    @property
    def element(self) -> Reference:
        return Reference(self.hybrid_shape_axis_line.Element)

    @element.setter
    def element(self, value: Reference):
        self.hybrid_shape_axis_line.Element = value

    def __repr__(self):
        return f'HybridShapeAxisLine(name="{ self.name }")'
