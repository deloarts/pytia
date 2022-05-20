from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeWrapSurface(HybridShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_wrap_surface = com_object

    @property
    def deformation_mode(self) -> int:
        return self.hybrid_shape_wrap_surface.DeformationMode

    @deformation_mode.setter
    def deformation_mode(self, value: int):
        self.hybrid_shape_wrap_surface.DeformationMode = value

    @property
    def reference_surface(self) -> Reference:
        return Reference(self.hybrid_shape_wrap_surface.ReferenceSurface)

    @reference_surface.setter
    def reference_surface(self, reference_surface: Reference):
        self.hybrid_shape_wrap_surface.ReferenceSurface = reference_surface.com_object

    @property
    def surface(self) -> Reference:
        return Reference(self.hybrid_shape_wrap_surface.Surface)

    @surface.setter
    def surface(self, reference_surface: Reference):
        self.hybrid_shape_wrap_surface.Surface = reference_surface.com_object

    @property
    def target_surface(self) -> Reference:
        return Reference(self.hybrid_shape_wrap_surface.TargetSurface)

    @target_surface.setter
    def target_surface(self, reference_surface: Reference):
        self.hybrid_shape_wrap_surface.TargetSurface = reference_surface.com_object

    def __repr__(self):
        return f'HybridShapeWrapSurface(name="{self.name}")'
