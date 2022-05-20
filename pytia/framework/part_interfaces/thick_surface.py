from pytia.framework.knowledge_interfaces.length import Length
from pytia.framework.part_interfaces.surface_based_shape import SurfaceBasedShape


class ThickSurface(SurfaceBasedShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.thick_surface = com_object

    @property
    def bot_offset(self) -> Length:
        return Length(self.thick_surface.BotOffset)

    @property
    def offset_side(self) -> int:
        return self.thick_surface.OffsetSide

    @property
    def top_offset(self) -> Length:
        return Length(self.thick_surface.TopOffset)

    def swap_offset_side(self) -> None:
        return self.thick_surface.swap_OffsetSide()

    def __repr__(self):
        return f'ThickSurface(name="{ self.name }")'
