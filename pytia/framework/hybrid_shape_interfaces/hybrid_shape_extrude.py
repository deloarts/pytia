from pytia.framework.hybrid_shape_interfaces.hybrid_shape_direction import (
    HybridShapeDirection,
)
from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.knowledge_interfaces.length import Length
from pytia.framework.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeExtrude(HybridShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_extrude = com_object

    @property
    def begin_offset(self) -> Length:
        return Length(self.hybrid_shape_extrude.BeginOffset)

    @property
    def context(self) -> int:
        return self.hybrid_shape_extrude.Context

    @context.setter
    def context(self, value: int):
        self.hybrid_shape_extrude.Context = value

    @property
    def direction(self) -> HybridShapeDirection:
        return HybridShapeDirection(self.hybrid_shape_extrude.Direction)

    @direction.setter
    def direction(self, direction: HybridShapeDirection):
        self.hybrid_shape_extrude.Direction = direction.com_object

    @property
    def end_offset(self) -> Length:
        return Length(self.hybrid_shape_extrude.EndOffset)

    @property
    def extruded_object(self) -> Reference:
        return Reference(self.hybrid_shape_extrude.ExtrudedObject)

    @extruded_object.setter
    def extruded_object(self, reference_object: Reference):
        self.hybrid_shape_extrude.ExtrudedObject = reference_object.com_object

    @property
    def first_limit_type(self) -> int:
        return self.hybrid_shape_extrude.FirstLimitType

    @first_limit_type.setter
    def first_limit_type(self, value: int):
        self.hybrid_shape_extrude.FirstLimitType = value

    @property
    def first_upto_element(self) -> Reference:
        return Reference(self.hybrid_shape_extrude.FirstUptoElement)

    @first_upto_element.setter
    def first_upto_element(self, reference_element: Reference):
        self.hybrid_shape_extrude.FirstUptoElement = reference_element

    @property
    def orientation(self) -> bool:
        return self.hybrid_shape_extrude.Orientation

    @orientation.setter
    def orientation(self, value: bool):
        self.hybrid_shape_extrude.Orientation = value

    @property
    def second_limit_type(self) -> int:
        return self.hybrid_shape_extrude.SecondLimitType

    @second_limit_type.setter
    def second_limit_type(self, value: int):
        self.hybrid_shape_extrude.SecondLimitType = value

    @property
    def second_upto_element(self) -> Reference:
        return Reference(self.hybrid_shape_extrude.SecondUptoElement)

    @second_upto_element.setter
    def second_upto_element(self, reference_element: Reference):
        self.hybrid_shape_extrude.SecondUptoElement = reference_element.com_object

    @property
    def symmetrical_extension(self) -> bool:
        return self.hybrid_shape_extrude.SymmetricalExtension

    @symmetrical_extension.setter
    def symmetrical_extension(self, value: bool):
        self.hybrid_shape_extrude.SymmetricalExtension = value

    def __repr__(self):
        return f'HybridShapeExtrude(name="{self.name}")'
