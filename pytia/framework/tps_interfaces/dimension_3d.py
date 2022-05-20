from pytia.framework.drafting_interfaces.drawing_dimension import DrawingDimension
from pytia.framework.system_interfaces.any_object import AnyObject
from pytia.framework.tps_interfaces.controlled_radius import ControlledRadius
from pytia.framework.tps_interfaces.dimension_limit import DimensionLimit
from pytia.framework.tps_interfaces.dimension_pattern import DimensionPattern
from pytia.framework.tps_interfaces.envelope_condition import EnvelopeCondition


class Dimension3D(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.dimension_3d = com_object

    def controled_radius(self) -> ControlledRadius:
        return ControlledRadius(self.dimension_3d.ControlledRadius())

    def dimension_limit(self) -> DimensionLimit:
        return DimensionLimit(self.dimension_3d.DimensionLimit())

    def dimension_pattern(self) -> DimensionPattern:
        return DimensionPattern(self.dimension_3d.DimensionPattern())

    def envelope_condition(self) -> EnvelopeCondition:
        return EnvelopeCondition(self.dimension_3d.EnvelopeCondition())

    def get_2d_annot(self) -> DrawingDimension:
        return DrawingDimension(self.dimension_3d.Get2dAnnot())

    def has_a_controlled_radius(self) -> bool:
        return self.dimension_3d.HasAControledRadius()

    def has_an_envelope_condition(self) -> bool:
        return self.dimension_3d.HasAnEnvelopCondition()

    def has_dimension_limit(self) -> bool:
        return self.dimension_3d.HasDimensionLimit()

    def is_a_dimension_pattern(self) -> bool:
        return self.dimension_3d.IsADimensionPattern()

    def move_value(
        self, x: float, y: float, sub_part: int, dim_angle_behavior: int
    ) -> None:
        return self.dimension_3d.MoveValue(x, y, sub_part, dim_angle_behavior)

    def __repr__(self):
        return f'Dimension3D(name="{self.name}")'
