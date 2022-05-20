from pytia.framework.hybrid_shape_interfaces.hybrid_shape_circle import (
    HybridShapeCircle,
)
from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.knowledge_interfaces.length import Length


class HybridShapeCircleBitangentRadius(HybridShapeCircle):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_circle_bitangent_radius = com_object

    @property
    def begin_of_circle(self) -> int:
        return self.hybrid_shape_circle_bitangent_radius.BeginOfCircle

    @begin_of_circle.setter
    def begin_of_circle(self, value: int):
        self.hybrid_shape_circle_bitangent_radius.BeginOfCircle = value

    @property
    def curve1(self) -> Reference:
        return Reference(self.hybrid_shape_circle_bitangent_radius.Curve1)

    @curve1.setter
    def curve1(self, reference_curve: Reference):
        self.hybrid_shape_circle_bitangent_radius.Curve1 = reference_curve.com_object

    @property
    def curve2(self) -> Reference:
        return Reference(self.hybrid_shape_circle_bitangent_radius.Curve2)

    @curve2.setter
    def curve2(self, reference_curve: Reference):
        self.hybrid_shape_circle_bitangent_radius.Curve2 = reference_curve.com_object

    @property
    def diameter(self) -> Length:
        return Length(self.hybrid_shape_circle_bitangent_radius.Diameter)

    @property
    def diameter_mode(self) -> bool:
        return self.hybrid_shape_circle_bitangent_radius.DiameterMode

    @diameter_mode.setter
    def diameter_mode(self, value: bool):
        self.hybrid_shape_circle_bitangent_radius.DiameterMode = value

    @property
    def discrimination_index(self) -> int:
        return self.hybrid_shape_circle_bitangent_radius.DiscriminationIndex

    @discrimination_index.setter
    def discrimination_index(self, value: int):
        self.hybrid_shape_circle_bitangent_radius.DiscriminationIndex = value

    @property
    def orientation1(self) -> int:
        return self.hybrid_shape_circle_bitangent_radius.Orientation1

    @orientation1.setter
    def orientation1(self, value: int):
        self.hybrid_shape_circle_bitangent_radius.Orientation1 = value

    @property
    def orientation2(self) -> int:
        return self.hybrid_shape_circle_bitangent_radius.Orientation2

    @orientation2.setter
    def orientation2(self, value: int):
        self.hybrid_shape_circle_bitangent_radius.Orientation2 = value

    @property
    def radius(self) -> Length:
        return Length(self.hybrid_shape_circle_bitangent_radius.Radius)

    @property
    def support(self) -> Reference:
        return Reference(self.hybrid_shape_circle_bitangent_radius.Support)

    @support.setter
    def support(self, reference_support: Reference):
        self.hybrid_shape_circle_bitangent_radius.Support = reference_support.com_object

    @property
    def tangent_orientation1(self) -> int:
        return self.hybrid_shape_circle_bitangent_radius.TangentOrientation1

    @tangent_orientation1.setter
    def tangent_orientation1(self, value: int):
        self.hybrid_shape_circle_bitangent_radius.TangentOrientation1 = value

    @property
    def tangent_orientation2(self) -> int:
        return self.hybrid_shape_circle_bitangent_radius.TangentOrientation2

    @tangent_orientation2.setter
    def tangent_orientation2(self, value: int):
        self.hybrid_shape_circle_bitangent_radius.TangentOrientation2 = value

    @property
    def trim_mode(self) -> int:
        return self.hybrid_shape_circle_bitangent_radius.TrimMode

    @trim_mode.setter
    def trim_mode(self, value: int):
        self.hybrid_shape_circle_bitangent_radius.TrimMode = value

    def __repr__(self):
        return f'HybridShapeCircleBitangentRadius(name="{self.name}")'
