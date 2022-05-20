from pytia.framework.hybrid_shape_interfaces.point import Point


class HybridShapePointExplicit(Point):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_point_explicit = com_object

    def __repr__(self):
        return f'HybridShapePointExplicit(name="{self.name}")'
