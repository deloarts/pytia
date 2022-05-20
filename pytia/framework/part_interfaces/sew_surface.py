from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.part_interfaces.surface_based_shape import SurfaceBasedShape


class SewSurface(SurfaceBasedShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.sew_surface = com_object

    @property
    def deviation(self) -> float:
        return self.sew_surface.Deviation

    @deviation.setter
    def deviation(self, value: float):
        self.sew_surface.Deviation = value

    @property
    def deviation_mode(self) -> int:
        return self.sew_surface.DeviationMode

    @deviation_mode.setter
    def deviation_mode(self, value: int):
        self.sew_surface.DeviationMode = value

    @property
    def sewing_intersection_mode(self) -> int:
        return self.sew_surface.SewingIntersectionMode

    @sewing_intersection_mode.setter
    def sewing_intersection_mode(self, value: int):
        self.sew_surface.SewingIntersectionMode = value

    @property
    def sewing_side(self) -> int:
        return self.sew_surface.SewingSide

    @sewing_side.setter
    def sewing_side(self, value: int):
        self.sew_surface.SewingSide = value

    def set_surface_support(self, i_support_surface: Reference) -> None:
        return self.sew_surface.SetSurfaceSupport(i_support_surface.com_object)

    def set_volume_support(self, i_volume: Reference) -> None:
        return self.sew_surface.SetVolumeSupport(i_volume.com_object)

    def __repr__(self):
        return f'SewSurface(name="{self.name}")'
