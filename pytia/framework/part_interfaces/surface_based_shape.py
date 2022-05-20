from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.mec_mod_interfaces.shape import Shape


class SurfaceBasedShape(Shape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.surface_based_shape = com_object

    @property
    def surface(self) -> Reference:
        return Reference(self.surface_based_shape.Surface)

    @surface.setter
    def surface(self, value: Reference):
        self.surface_based_shape.Surface = value

    def __repr__(self):
        return f'SurfaceBasedShape(name="{ self.name }")'
