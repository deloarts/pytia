from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.knowledge_interfaces.length import Length
from pytia.framework.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeMidSurface(HybridShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_mid_surface = com_object

    @property
    def auto_thickness_threshold(self) -> int:
        return self.hybrid_shape_mid_surface.AutoThicknessThreshold

    @auto_thickness_threshold.setter
    def auto_thickness_threshold(self, value: int):
        self.hybrid_shape_mid_surface.AutoThicknessThreshold = value

    @property
    def creation_mode(self) -> int:
        return self.hybrid_shape_mid_surface.CreationMode

    @creation_mode.setter
    def creation_mode(self, value: int):
        self.hybrid_shape_mid_surface.CreationMode = value

    @property
    def support(self) -> Reference:
        return Reference(self.hybrid_shape_mid_surface.Support)

    @support.setter
    def support(self, reference_support: Reference):
        self.hybrid_shape_mid_surface.Support = reference_support.com_object

    @property
    def threshold(self) -> Length:
        return Length(self.hybrid_shape_mid_surface.Threshold)

    @threshold.setter
    def threshold(self, value: Length):
        self.hybrid_shape_mid_surface.Threshold = value

    def __repr__(self):
        return f'HybridShapeMidSurface(name="{self.name}")'
