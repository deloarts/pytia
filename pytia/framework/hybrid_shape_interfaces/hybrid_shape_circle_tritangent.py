from pytia.framework.hybrid_shape_interfaces.hybrid_shape_circle import (
    HybridShapeCircle,
)
from pytia.framework.in_interfaces.reference import Reference


class HybridShapeCircleTritangent(HybridShapeCircle):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_circle_tritangent = com_object

    @property
    def begin_of_circle(self) -> int:
        return self.hybrid_shape_circle_tritangent.BeginOfCircle

    @begin_of_circle.setter
    def begin_of_circle(self, value: int):
        self.hybrid_shape_circle_tritangent.BeginOfCircle = value

    @property
    def curve1(self) -> Reference:
        return Reference(self.hybrid_shape_circle_tritangent.Curve1)

    @curve1.setter
    def curve1(self, reference_curve: Reference):
        self.hybrid_shape_circle_tritangent.Curve1 = reference_curve.com_object

    @property
    def curve2(self) -> Reference:
        return Reference(self.hybrid_shape_circle_tritangent.Curve2)

    @curve2.setter
    def curve2(self, reference_curve: Reference):
        self.hybrid_shape_circle_tritangent.Curve2 = reference_curve.com_object

    @property
    def curve3(self) -> Reference:
        return Reference(self.hybrid_shape_circle_tritangent.Curve3)

    @curve3.setter
    def curve3(self, reference_curve: Reference):
        self.hybrid_shape_circle_tritangent.Curve3 = reference_curve.com_object

    @property
    def discrimination_index(self) -> int:
        return self.hybrid_shape_circle_tritangent.DiscriminationIndex

    @discrimination_index.setter
    def discrimination_index(self, value: int):
        self.hybrid_shape_circle_tritangent.DiscriminationIndex = value

    @property
    def orientation1(self) -> int:
        return self.hybrid_shape_circle_tritangent.Orientation1

    @orientation1.setter
    def orientation1(self, value: int):
        self.hybrid_shape_circle_tritangent.Orientation1 = value

    @property
    def orientation2(self) -> int:
        return self.hybrid_shape_circle_tritangent.Orientation2

    @orientation2.setter
    def orientation2(self, value: int):
        self.hybrid_shape_circle_tritangent.Orientation2 = value

    @property
    def orientation3(self) -> int:
        return self.hybrid_shape_circle_tritangent.Orientation3

    @orientation3.setter
    def orientation3(self, value: int):
        self.hybrid_shape_circle_tritangent.Orientation3 = value

    @property
    def support(self) -> Reference:
        return Reference(self.hybrid_shape_circle_tritangent.Support)

    @support.setter
    def support(self, reference_support: Reference):
        self.hybrid_shape_circle_tritangent.Support = reference_support.com_object

    @property
    def tangent_orientation1(self) -> int:
        return self.hybrid_shape_circle_tritangent.TangentOrientation1

    @tangent_orientation1.setter
    def tangent_orientation1(self, value: int):
        self.hybrid_shape_circle_tritangent.TangentOrientation1 = value

    @property
    def tangent_orientation2(self) -> int:
        return self.hybrid_shape_circle_tritangent.TangentOrientation2

    @tangent_orientation2.setter
    def tangent_orientation2(self, value: int):
        self.hybrid_shape_circle_tritangent.TangentOrientation2 = value

    @property
    def tangent_orientation3(self) -> int:
        return self.hybrid_shape_circle_tritangent.TangentOrientation3

    @tangent_orientation3.setter
    def tangent_orientation3(self, value: int):
        self.hybrid_shape_circle_tritangent.TangentOrientation3 = value

    @property
    def trim_mode(self) -> int:
        return self.hybrid_shape_circle_tritangent.TrimMode

    @trim_mode.setter
    def trim_mode(self, value: int):
        self.hybrid_shape_circle_tritangent.TrimMode = value

    def __repr__(self):
        return f'HybridShapeCircleTritangent(name="{ self.name }")'
