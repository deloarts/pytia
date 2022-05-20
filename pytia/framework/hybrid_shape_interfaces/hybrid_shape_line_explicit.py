from pytia.framework.hybrid_shape_interfaces.line import Line


class HybridShapeLineExplicit(Line):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_line_explicit = com_object

    def __repr__(self):
        return f'HybridShapeLineExplicit(name="{self.name}")'
