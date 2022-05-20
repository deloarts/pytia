from pytia.framework.hybrid_shape_interfaces.hybrid_shape_direction import (
    HybridShapeDirection,
)
from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeExtremum(HybridShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_extremum = com_object

    @property
    def direction(self) -> HybridShapeDirection:
        return HybridShapeDirection(self.hybrid_shape_extremum.Direction)

    @direction.setter
    def direction(self, direction: HybridShapeDirection):
        self.hybrid_shape_extremum.Direction = direction.com_object

    @property
    def direction2(self) -> HybridShapeDirection:
        return HybridShapeDirection(self.hybrid_shape_extremum.Direction2)

    @direction2.setter
    def direction2(self, direction: HybridShapeDirection):
        self.hybrid_shape_extremum.Direction2 = direction.com_object

    @property
    def direction3(self) -> HybridShapeDirection:
        return HybridShapeDirection(self.hybrid_shape_extremum.Direction3)

    @direction3.setter
    def direction3(self, direction: HybridShapeDirection):
        self.hybrid_shape_extremum.Direction3 = direction.com_object

    @property
    def extremum_type(self) -> int:
        return self.hybrid_shape_extremum.ExtremumType

    @extremum_type.setter
    def extremum_type(self, value: int):
        self.hybrid_shape_extremum.ExtremumType = value

    @property
    def extremum_type2(self) -> int:
        return self.hybrid_shape_extremum.ExtremumType2

    @extremum_type2.setter
    def extremum_type2(self, value: int):
        self.hybrid_shape_extremum.ExtremumType2 = value

    @property
    def extremum_type3(self) -> int:
        return self.hybrid_shape_extremum.ExtremumType3

    @extremum_type3.setter
    def extremum_type3(self, value: int):
        self.hybrid_shape_extremum.ExtremumType3 = value

    @property
    def reference_element(self) -> Reference:
        return Reference(self.hybrid_shape_extremum.ReferenceElement)

    @reference_element.setter
    def reference_element(self, reference_element: Reference):
        self.hybrid_shape_extremum.ReferenceElement = reference_element

    def __repr__(self):
        return f'HybridShapeExtremum(name="{ self.name }")'
