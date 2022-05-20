from pytia.framework.hybrid_shape_interfaces.plane import Plane


class HybridShapePlaneExplicit(Plane):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_plane_explicit = com_object

    def __repr__(self):
        return f'HybridShapePlaneExplicit(name="{self.name}")'
