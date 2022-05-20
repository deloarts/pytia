from pytia.framework.hybrid_shape_interfaces.point import Point
from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.knowledge_interfaces.length import Length


class HybridShapePointCoord(Point):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_point_coord = com_object

    @property
    def pt_ref(self) -> Reference:
        return Reference(self.hybrid_shape_point_coord.PtRef)

    @pt_ref.setter
    def pt_ref(self, reference_point: Reference):
        self.hybrid_shape_point_coord.PtRef = reference_point.com_object

    @property
    def ref_axis_system(self) -> Reference:
        return Reference(self.hybrid_shape_point_coord.RefAxisSystem)

    @ref_axis_system.setter
    def ref_axis_system(self, reference_axis: Reference):
        self.hybrid_shape_point_coord.RefAxisSystem = reference_axis.com_object

    @property
    def x(self) -> Length:
        return Length(self.hybrid_shape_point_coord.X)

    @property
    def y(self) -> Length:
        return Length(self.hybrid_shape_point_coord.Y)

    @property
    def z(self) -> Length:
        return Length(self.hybrid_shape_point_coord.Z)

    def __repr__(self):
        return f'HybridShapePointCoord(name="{self.name}")'
