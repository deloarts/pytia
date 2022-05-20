from pytia.framework.hybrid_shape_interfaces.hybrid_shape_circle import (
    HybridShapeCircle,
)
from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.knowledge_interfaces.length import Length


class HybridShapeCircleCenterTangent(HybridShapeCircle):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_circle_center_tangent = com_object

    @property
    def begin_of_circle(self) -> int:
        return self.hybrid_shape_circle_center_tangent.BeginOfCircle

    @begin_of_circle.setter
    def begin_of_circle(self, value: int):
        self.hybrid_shape_circle_center_tangent.BeginOfCircle = value

    @property
    def center_elem(self) -> Reference:
        return Reference(self.hybrid_shape_circle_center_tangent.CenterElem)

    @center_elem.setter
    def center_elem(self, reference_elem: Reference):
        self.hybrid_shape_circle_center_tangent.CenterElem = reference_elem.com_object

    @property
    def diameter(self) -> Length:
        return Length(self.hybrid_shape_circle_center_tangent.Diameter)

    @property
    def diameter_mode(self) -> bool:
        return self.hybrid_shape_circle_center_tangent.DiameterMode

    @diameter_mode.setter
    def diameter_mode(self, value: bool):
        self.hybrid_shape_circle_center_tangent.DiameterMode = value

    @property
    def discrimination_index(self) -> int:
        return self.hybrid_shape_circle_center_tangent.DiscriminationIndex

    @discrimination_index.setter
    def discrimination_index(self, value: int):
        self.hybrid_shape_circle_center_tangent.DiscriminationIndex = value

    @property
    def orientation1(self) -> int:
        return self.hybrid_shape_circle_center_tangent.Orientation1

    @orientation1.setter
    def orientation1(self, value: int):
        self.hybrid_shape_circle_center_tangent.Orientation1 = value

    @property
    def orientation2(self) -> int:
        return self.hybrid_shape_circle_center_tangent.Orientation2

    @orientation2.setter
    def orientation2(self, value: int):
        self.hybrid_shape_circle_center_tangent.Orientation2 = value

    @property
    def radius(self) -> Length:
        return Length(self.hybrid_shape_circle_center_tangent.Radius)

    @property
    def support(self) -> Reference:
        return Reference(self.hybrid_shape_circle_center_tangent.Support)

    @support.setter
    def support(self, reference_support: Reference):
        self.hybrid_shape_circle_center_tangent.Support = reference_support.com_object

    @property
    def tangent_curve(self) -> Reference:
        return Reference(self.hybrid_shape_circle_center_tangent.TangentCurve)

    @tangent_curve.setter
    def tangent_curve(self, reference_curve: Reference):
        self.hybrid_shape_circle_center_tangent.TangentCurve = (
            reference_curve.com_object
        )

    @property
    def tangent_orientation1(self) -> int:
        return self.hybrid_shape_circle_center_tangent.TangentOrientation1

    @tangent_orientation1.setter
    def tangent_orientation1(self, value: int):
        self.hybrid_shape_circle_center_tangent.TangentOrientation1 = value

    @property
    def tangent_orientation2(self) -> int:
        return self.hybrid_shape_circle_center_tangent.TangentOrientation2

    @tangent_orientation2.setter
    def tangent_orientation2(self, value: int):
        self.hybrid_shape_circle_center_tangent.TangentOrientation2 = value

    def __repr__(self):
        return f'HybridShapeCircleCenterTangent(name="{self.name}")'
