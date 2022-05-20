from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeIntersection(HybridShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_intersection = com_object

    @property
    def element1(self) -> Reference:
        return Reference(self.hybrid_shape_intersection.Element1)

    @element1.setter
    def element1(self, reference_element: Reference):
        self.hybrid_shape_intersection.Element1 = reference_element.com_object

    @property
    def element2(self) -> Reference:
        return Reference(self.hybrid_shape_intersection.Element2)

    @element2.setter
    def element2(self, reference_element: Reference):
        self.hybrid_shape_intersection.Element2 = reference_element.com_object

    @property
    def extend_mode(self) -> int:
        return self.hybrid_shape_intersection.ExtendMode

    @extend_mode.setter
    def extend_mode(self, value: int):
        self.hybrid_shape_intersection.ExtendMode = value

    @property
    def extrapolate_mode(self) -> bool:
        return self.hybrid_shape_intersection.ExtrapolateMode

    @extrapolate_mode.setter
    def extrapolate_mode(self, value: bool):
        self.hybrid_shape_intersection.ExtrapolateMode = value

    @property
    def intersect_mode(self) -> bool:
        return self.hybrid_shape_intersection.IntersectMode

    @intersect_mode.setter
    def intersect_mode(self, value: bool):
        self.hybrid_shape_intersection.IntersectMode = value

    @property
    def point_type(self) -> int:
        return self.hybrid_shape_intersection.PointType

    @point_type.setter
    def point_type(self, value: int):
        self.hybrid_shape_intersection.PointType = value

    @property
    def solid_mode(self) -> bool:
        return self.hybrid_shape_intersection.SolidMode

    @solid_mode.setter
    def solid_mode(self, value: bool):
        self.hybrid_shape_intersection.SolidMode = value

    def __repr__(self):
        return f'HybridShapeIntersection(name="{ self.name }")'
