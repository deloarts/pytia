from pytia.framework.hybrid_shape_interfaces.plane import Plane
from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.knowledge_interfaces.angle import Angle


class HybridShapePlaneAngle(Plane):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_plane_angle = com_object

    @property
    def angle(self) -> Angle:
        return Angle(self.hybrid_shape_plane_angle.Angle)

    @property
    def orientation(self) -> int:
        return self.hybrid_shape_plane_angle.Orientation

    @orientation.setter
    def orientation(self, value: int):
        self.hybrid_shape_plane_angle.Orientation = value

    @property
    def plane(self) -> Reference:
        return Reference(self.hybrid_shape_plane_angle.Plane)

    @plane.setter
    def plane(self, reference_plane: Reference):
        self.hybrid_shape_plane_angle.Plane = reference_plane.com_object

    @property
    def projection_mode(self) -> bool:
        return self.hybrid_shape_plane_angle.ProjectionMode

    @projection_mode.setter
    def projection_mode(self, value: bool):
        self.hybrid_shape_plane_angle.ProjectionMode = value

    @property
    def revol_axis(self) -> Reference:
        return Reference(self.hybrid_shape_plane_angle.RevolAxis)

    @revol_axis.setter
    def revol_axis(self, reference_axis: Reference):
        self.hybrid_shape_plane_angle.RevolAxis = reference_axis.com_object

    def __repr__(self):
        return f'HybridShapePlaneAngle(name="{self.name}")'
