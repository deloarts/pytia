from pytia.framework.hybrid_shape_interfaces.hybrid_shape_circle import (
    HybridShapeCircle,
)
from pytia.framework.in_interfaces.reference import Reference


class HybridShapeCircleBitangentPoint(HybridShapeCircle):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_circle_bitangent_point = com_object

    @property
    def begin_of_circle(self) -> int:
        return self.hybrid_shape_circle_bitangent_point.BeginOfCircle

    @begin_of_circle.setter
    def begin_of_circle(self, value: int):
        self.hybrid_shape_circle_bitangent_point.BeginOfCircle = value

    @property
    def curve1(self) -> Reference:
        return Reference(self.hybrid_shape_circle_bitangent_point.Curve1)

    @curve1.setter
    def curve1(self, reference_curve: Reference):
        self.hybrid_shape_circle_bitangent_point.Curve1 = reference_curve.com_object

    @property
    def curve2(self) -> Reference:
        return Reference(self.hybrid_shape_circle_bitangent_point.Curve2)

    @curve2.setter
    def curve2(self, reference_curve: Reference):
        self.hybrid_shape_circle_bitangent_point.Curve2 = reference_curve.com_object

    @property
    def discrimination_index(self) -> int:
        return self.hybrid_shape_circle_bitangent_point.DiscriminationIndex

    @discrimination_index.setter
    def discrimination_index(self, value: int):
        self.hybrid_shape_circle_bitangent_point.DiscriminationIndex = value

    @property
    def orientation1(self) -> int:
        return self.hybrid_shape_circle_bitangent_point.Orientation1

    @orientation1.setter
    def orientation1(self, value: int):
        self.hybrid_shape_circle_bitangent_point.Orientation1 = value

    @property
    def orientation2(self) -> int:
        return self.hybrid_shape_circle_bitangent_point.Orientation2

    @orientation2.setter
    def orientation2(self, value: int):
        self.hybrid_shape_circle_bitangent_point.Orientation2 = value

    @property
    def pt(self) -> Reference:
        return Reference(self.hybrid_shape_circle_bitangent_point.Pt)

    @pt.setter
    def pt(self, reference_point: Reference):
        self.hybrid_shape_circle_bitangent_point.Pt = reference_point.com_object

    @property
    def support(self) -> Reference:
        return Reference(self.hybrid_shape_circle_bitangent_point.Support)

    @support.setter
    def support(self, reference_support: Reference):
        self.hybrid_shape_circle_bitangent_point.Support = reference_support.com_object

    @property
    def tangent_orientation1(self) -> int:
        return self.hybrid_shape_circle_bitangent_point.TangentOrientation1

    @tangent_orientation1.setter
    def tangent_orientation1(self, value: int):
        self.hybrid_shape_circle_bitangent_point.TangentOrientation1 = value

    @property
    def tangent_orientation2(self) -> int:
        return self.hybrid_shape_circle_bitangent_point.TangentOrientation2

    @tangent_orientation2.setter
    def tangent_orientation2(self, value: int):
        self.hybrid_shape_circle_bitangent_point.TangentOrientation2 = value

    @property
    def trim_mode(self) -> int:
        return self.hybrid_shape_circle_bitangent_point.TrimMode

    @trim_mode.setter
    def trim_mode(self, value: int):
        self.hybrid_shape_circle_bitangent_point.TrimMode = value

    def __repr__(self):
        return f'HybridShapeCircleBitangentPoint(name="{self.name}")'
