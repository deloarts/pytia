from pytia.framework.hybrid_shape_interfaces.hybrid_shape_direction import (
    HybridShapeDirection,
)
from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.knowledge_interfaces.length import Length
from pytia.framework.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeCylinder(HybridShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_cylinder = com_object

    @property
    def center(self) -> Reference:
        return Reference(self.hybrid_shape_cylinder.Center)

    @center.setter
    def center(self, reference_center: Reference):
        self.hybrid_shape_cylinder.Center = reference_center.com_object

    @property
    def direction(self) -> HybridShapeDirection:
        return HybridShapeDirection(self.hybrid_shape_cylinder.Direction)

    @direction.setter
    def direction(self, direction: HybridShapeDirection):
        self.hybrid_shape_cylinder.Direction = direction.com_object

    @property
    def length1(self) -> Length:
        return Length(self.hybrid_shape_cylinder.Length1)

    @length1.setter
    def length1(self, length: Length):
        self.hybrid_shape_cylinder.Length1 = length.com_object

    @property
    def length2(self) -> Length:
        return Length(self.hybrid_shape_cylinder.Length2)

    @length2.setter
    def length2(self, length: Length):
        self.hybrid_shape_cylinder.Length2 = length.com_object

    @property
    def orientation(self) -> bool:
        return self.hybrid_shape_cylinder.Orientation

    @orientation.setter
    def orientation(self, value: bool):
        self.hybrid_shape_cylinder.Orientation = value

    @property
    def radius(self) -> Length:
        return Length(self.hybrid_shape_cylinder.Radius)

    @radius.setter
    def radius(self, length: Length):
        self.hybrid_shape_cylinder.Radius = length.com_object

    @property
    def symmetrical_extension(self) -> bool:
        return self.hybrid_shape_cylinder.SymmetricalExtension

    @symmetrical_extension.setter
    def symmetrical_extension(self, value: bool):
        self.hybrid_shape_cylinder.SymmetricalExtension = value

    def invert_orientation(self) -> None:
        return self.hybrid_shape_cylinder.InvertOrientation()

    def __repr__(self):
        return f'HybridShapeCylinder(name="{self.name}")'
