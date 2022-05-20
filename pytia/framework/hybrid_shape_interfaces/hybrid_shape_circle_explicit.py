from pytia.framework.hybrid_shape_interfaces.hybrid_shape_circle import (
    HybridShapeCircle,
)


class HybridShapeCircleExplicit(HybridShapeCircle):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_circle_explicit = com_object

    def __repr__(self):
        return f'HybridShapeCircleExplicit(name="{self.name}")'
