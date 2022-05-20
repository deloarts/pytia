from pytia.framework.hybrid_shape_interfaces.hybrid_shape_direction import (
    HybridShapeDirection,
)
from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.knowledge_interfaces.length import Length
from pytia.framework.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeCorner(HybridShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_corner = com_object

    @property
    def begin_of_corner(self) -> int:
        return self.hybrid_shape_corner.BeginOfCorner

    @begin_of_corner.setter
    def begin_of_corner(self, value: int):
        self.hybrid_shape_corner.BeginOfCorner = value

    @property
    def corner_type(self) -> int:
        return self.hybrid_shape_corner.CornerType

    @corner_type.setter
    def corner_type(self, value: int):
        self.hybrid_shape_corner.CornerType = value

    @property
    def direction(self) -> HybridShapeDirection:
        return HybridShapeDirection(self.hybrid_shape_corner.Direction)

    @direction.setter
    def direction(self, direction: HybridShapeDirection):
        self.hybrid_shape_corner.Direction = direction.com_object

    @property
    def discrimination_index(self) -> int:
        return self.hybrid_shape_corner.DiscriminationIndex

    @discrimination_index.setter
    def discrimination_index(self, value: int):
        self.hybrid_shape_corner.DiscriminationIndex = value

    @property
    def first_elem(self) -> Reference:
        return Reference(self.hybrid_shape_corner.FirstElem)

    @first_elem.setter
    def first_elem(self, reference_element: Reference):
        self.hybrid_shape_corner.FirstElem = reference_element.com_object

    @property
    def first_orientation(self) -> int:
        return self.hybrid_shape_corner.FirstOrientation

    @first_orientation.setter
    def first_orientation(self, value: int):
        self.hybrid_shape_corner.FirstOrientation = value

    @property
    def first_tangent_orientation(self) -> int:
        return self.hybrid_shape_corner.FirstTangentOrientation

    @first_tangent_orientation.setter
    def first_tangent_orientation(self, value: int):
        self.hybrid_shape_corner.FirstTangentOrientation = value

    @property
    def on_vertex(self) -> bool:
        return self.hybrid_shape_corner.OnVertex

    @on_vertex.setter
    def on_vertex(self, value: bool):
        self.hybrid_shape_corner.OnVertex = value

    @property
    def radius(self) -> Length:
        return Length(self.hybrid_shape_corner.Radius)

    @property
    def second_elem(self) -> Reference:
        return Reference(self.hybrid_shape_corner.SecondElem)

    @second_elem.setter
    def second_elem(self, reference_element: Reference):
        self.hybrid_shape_corner.SecondElem = reference_element.com_object

    @property
    def second_orientation(self) -> int:
        return self.hybrid_shape_corner.SecondOrientation

    @second_orientation.setter
    def second_orientation(self, value: int):
        self.hybrid_shape_corner.SecondOrientation = value

    @property
    def second_tangent_orientation(self) -> int:
        return self.hybrid_shape_corner.SecondTangentOrientation

    @second_tangent_orientation.setter
    def second_tangent_orientation(self, value: int):
        self.hybrid_shape_corner.SecondTangentOrientation = value

    @property
    def support(self) -> Reference:
        return Reference(self.hybrid_shape_corner.Support)

    @support.setter
    def support(self, reference_support: Reference):
        self.hybrid_shape_corner.Support = reference_support.com_object

    @property
    def trim(self) -> bool:
        return self.hybrid_shape_corner.Trim

    @trim.setter
    def trim(self, value: bool):
        self.hybrid_shape_corner.Trim = value

    @property
    def trim_mode(self) -> int:
        return self.hybrid_shape_corner.TrimMode

    @trim_mode.setter
    def trim_mode(self, value: int):
        self.hybrid_shape_corner.TrimMode = value

    def invert_first_orientation(self) -> None:
        return self.hybrid_shape_corner.InvertFirstOrientation()

    def invert_second_orientation(self) -> None:
        return self.hybrid_shape_corner.InvertSecondOrientation()

    def __repr__(self):
        return f'HybridShapeCorner(name="{ self.name }")'
