from pytia.framework.hybrid_shape_interfaces.hybrid_shape_direction import (
    HybridShapeDirection,
)
from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.knowledge_interfaces.length import Length
from pytia.framework.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShape3DCurveOffset(HybridShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_3d_curve_offset = com_object

    @property
    def corner_radius_value(self) -> Length:
        return Length(self.hybrid_shape_3d_curve_offset.CornerRadiusValue)

    @corner_radius_value.setter
    def corner_radius_value(self, length: Length):
        self.hybrid_shape_3d_curve_offset.CornerRadiusValue = length.com_object

    @property
    def corner_tension_value(self) -> float:
        return self.hybrid_shape_3d_curve_offset.CornerTensionValue

    @corner_tension_value.setter
    def corner_tension_value(self, value: float):
        self.hybrid_shape_3d_curve_offset.CornerTensionValue = value

    @property
    def curve_to_offset(self) -> Reference:
        return Reference(self.hybrid_shape_3d_curve_offset.CurveToOffset)

    @curve_to_offset.setter
    def curve_to_offset(self, reference_curve: Reference):
        self.hybrid_shape_3d_curve_offset.CurveToOffset = reference_curve.com_object

    @property
    def direction(self) -> HybridShapeDirection:
        return HybridShapeDirection(self.hybrid_shape_3d_curve_offset.Direction)

    @direction.setter
    def direction(self, direction: HybridShapeDirection):
        self.hybrid_shape_3d_curve_offset.Direction = direction.com_object

    @property
    def invert_direction(self) -> bool:
        return self.hybrid_shape_3d_curve_offset.InvertDirection

    @invert_direction.setter
    def invert_direction(self, value: bool):
        self.hybrid_shape_3d_curve_offset.InvertDirection = value

    @property
    def offset_value(self) -> Length:
        return Length(self.hybrid_shape_3d_curve_offset.OffsetValue)

    @offset_value.setter
    def offset_value(self, length: Length):
        self.hybrid_shape_3d_curve_offset.OffsetValue = length

    def __repr__(self):
        return f'HybridShape3DCurveOffset(name="{self.name}")'
