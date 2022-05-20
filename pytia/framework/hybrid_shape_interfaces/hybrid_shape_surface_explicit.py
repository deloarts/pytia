from pytia.framework.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeSurfaceExplicit(HybridShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_surface_explicit = com_object

    def __repr__(self):
        return f'HybridShapeSurfaceExplicit(name="{self.name}")'
