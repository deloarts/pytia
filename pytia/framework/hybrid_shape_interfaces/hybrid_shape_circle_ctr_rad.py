from pytia.framework.hybrid_shape_interfaces.hybrid_shape_circle import (
    HybridShapeCircle,
)
from pytia.framework.hybrid_shape_interfaces.hybrid_shape_direction import (
    HybridShapeDirection,
)
from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.knowledge_interfaces.length import Length


class HybridShapeCircleCtrRad(HybridShapeCircle):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_circle_ctr_rad = com_object

    @property
    def center(self) -> Reference:
        return Reference(self.hybrid_shape_circle_ctr_rad.Center)

    @center.setter
    def center(self, reference_center: Reference):
        self.hybrid_shape_circle_ctr_rad.Center = reference_center.com_object

    @property
    def diameter(self) -> Length:
        return Length(self.hybrid_shape_circle_ctr_rad.Diameter)

    @property
    def diameter_mode(self) -> bool:
        return self.hybrid_shape_circle_ctr_rad.DiameterMode

    @diameter_mode.setter
    def diameter_mode(self, value: bool):
        self.hybrid_shape_circle_ctr_rad.DiameterMode = value

    @property
    def first_direction(self) -> HybridShapeDirection:
        return HybridShapeDirection(self.hybrid_shape_circle_ctr_rad.FirstDirection)

    @first_direction.setter
    def first_direction(self, direction: HybridShapeDirection):
        self.hybrid_shape_circle_ctr_rad.FirstDirection = direction.com_object

    @property
    def radius(self) -> Length:
        return Length(self.hybrid_shape_circle_ctr_rad.Radius)

    @property
    def support(self) -> Reference:
        return Reference(self.hybrid_shape_circle_ctr_rad.Support)

    @support.setter
    def support(self, support_reference: Reference):
        self.hybrid_shape_circle_ctr_rad.Support = support_reference.com_object

    def get_second_direction(
        self, o_dir_x: float, o_dir_y: float, o_dir_z: float
    ) -> None:
        return self.hybrid_shape_circle_ctr_rad.GetSecondDirection(
            o_dir_x, o_dir_y, o_dir_z
        )

    def is_geodesic(self) -> bool:
        return self.hybrid_shape_circle_ctr_rad.IsGeodesic()

    def set_geometry_on_support(self) -> None:
        return self.hybrid_shape_circle_ctr_rad.SetGeometryOnSupport()

    def set_second_direction(
        self, i_dir_x: float, i_dir_y: float, i_dir_z: float
    ) -> None:
        return self.hybrid_shape_circle_ctr_rad.SetSecondDirection(
            i_dir_x, i_dir_y, i_dir_z
        )

    def unset_geometry_on_support(self) -> None:
        return self.hybrid_shape_circle_ctr_rad.UnsetGeometryOnSupport()

    def __repr__(self):
        return f'HybridShapeCircleCtrRad(name="{ self.name }")'
