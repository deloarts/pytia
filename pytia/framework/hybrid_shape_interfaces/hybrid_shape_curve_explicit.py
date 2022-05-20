from pytia.framework.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeCurveExplicit(HybridShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_curve_explicit = com_object

    def __repr__(self):
        return f'HybridShapeCurveExplicit(name="{self.name}")'
