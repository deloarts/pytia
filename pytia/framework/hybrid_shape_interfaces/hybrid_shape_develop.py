from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.knowledge_interfaces.angle import Angle
from pytia.framework.knowledge_interfaces.length import Length
from pytia.framework.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeDevelop(HybridShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_develop = com_object

    @property
    def mode(self) -> int:
        return self.hybrid_shape_develop.Mode

    @mode.setter
    def mode(self, value: int):
        self.hybrid_shape_develop.Mode = value

    @property
    def mode_pos(self) -> int:
        return self.hybrid_shape_develop.ModePos

    @mode_pos.setter
    def mode_pos(self, value: int):
        self.hybrid_shape_develop.ModePos = value

    @property
    def plane_axis_direction(self) -> Reference:
        return Reference(self.hybrid_shape_develop.PlaneAxisDirection)

    @plane_axis_direction.setter
    def plane_axis_direction(self, reference_plane: Reference):
        self.hybrid_shape_develop.PlaneAxisDirection = reference_plane.com_object

    @property
    def plane_axis_origin(self) -> Reference:
        return Reference(self.hybrid_shape_develop.PlaneAxisOrigin)

    @plane_axis_origin.setter
    def plane_axis_origin(self, reference_plane: Reference):
        self.hybrid_shape_develop.PlaneAxisOrigin = reference_plane.com_object

    @property
    def point_on_support(self) -> Reference:
        return Reference(self.hybrid_shape_develop.PointOnSupport)

    @point_on_support.setter
    def point_on_support(self, reference_point: Reference):
        self.hybrid_shape_develop.PointOnSupport = reference_point.com_object

    @property
    def positioned_wire(self) -> Reference:
        return Reference(self.hybrid_shape_develop.PositionedWire)

    @positioned_wire.setter
    def positioned_wire(self, value: Reference):
        self.hybrid_shape_develop.PositionedWire = value.com_object

    @property
    def support(self) -> Reference:
        return Reference(self.hybrid_shape_develop.Support)

    @support.setter
    def support(self, reference_support: Reference):
        self.hybrid_shape_develop.Support = reference_support.com_object

    @property
    def wire_to_develop(self) -> Reference:
        return Reference(self.hybrid_shape_develop.WireToDevelop)

    @wire_to_develop.setter
    def wire_to_develop(self, reference: Reference):
        self.hybrid_shape_develop.WireToDevelop = reference.com_object

    def get_plane_axis_angle(self) -> Angle:
        return Angle(self.hybrid_shape_develop.GetPlaneAxisAngle())

    def get_plane_axis_coord(self, i_coor_idx: int) -> Length:
        return Length(self.hybrid_shape_develop.GetPlaneAxisCoord(i_coor_idx))

    def get_plane_axis_swap_axes(self, ii: int) -> int:
        return self.hybrid_shape_develop.GetPlaneAxisSwapAxes(ii)

    def set_plane_axis_angle(self, i_angle: float) -> None:
        return self.hybrid_shape_develop.SetPlaneAxisAngle(i_angle)

    def set_plane_axis_coord(self, i_coor_idx: int, i_coord_value: float) -> None:
        return self.hybrid_shape_develop.SetPlaneAxisCoord(i_coor_idx, i_coord_value)

    def set_plane_axis_swap_axes(self, i_idx: int, i_inversion_value: int) -> None:
        return self.hybrid_shape_develop.SetPlaneAxisSwapAxes(i_idx, i_inversion_value)

    def __repr__(self):
        return f'HybridShapeDevelop(name="{self.name}")'
