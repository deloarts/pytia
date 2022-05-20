from pytia.framework.hybrid_shape_interfaces.hybrid_shape_direction import (
    HybridShapeDirection,
)
from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.knowledge_interfaces.angle import Angle
from pytia.framework.knowledge_interfaces.length import Length
from pytia.framework.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeExtremumPolar(HybridShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_extremum_polar = com_object

    @property
    def angle(self) -> Angle:
        return Angle(self.hybrid_shape_extremum_polar.Angle)

    @property
    def contour(self) -> Reference:
        return Reference(self.hybrid_shape_extremum_polar.Contour)

    @contour.setter
    def contour(self, reference_contour: Reference):
        self.hybrid_shape_extremum_polar.Contour = reference_contour.com_object

    @property
    def dir(self) -> HybridShapeDirection:
        return HybridShapeDirection(self.hybrid_shape_extremum_polar.Dir)

    @dir.setter
    def dir(self, direction: HybridShapeDirection):
        self.hybrid_shape_extremum_polar.Dir = direction.com_object

    @property
    def extremum_type(self) -> int:
        return self.hybrid_shape_extremum_polar.ExtremumType

    @extremum_type.setter
    def extremum_type(self, value: int):
        self.hybrid_shape_extremum_polar.ExtremumType = value

    @property
    def origin(self) -> Reference:
        return Reference(self.hybrid_shape_extremum_polar.Origin)

    @origin.setter
    def origin(self, reference_origin: Reference):
        self.hybrid_shape_extremum_polar.Origin = reference_origin.com_object

    @property
    def radius(self) -> Length:
        return Length(self.hybrid_shape_extremum_polar.Radius)

    @property
    def support(self) -> Reference:
        return Reference(self.hybrid_shape_extremum_polar.Support)

    @support.setter
    def support(self, reference_support: Reference):
        self.hybrid_shape_extremum_polar.Support = reference_support.com_object

    def __repr__(self):
        return f'HybridShapeExtremumPolar(name="{ self.name }")'
