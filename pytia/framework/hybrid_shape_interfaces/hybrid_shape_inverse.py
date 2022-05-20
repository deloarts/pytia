from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeInverse(HybridShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_inverse = com_object

    @property
    def element(self) -> Reference:
        return Reference(self.hybrid_shape_inverse.Element)

    @element.setter
    def element(self, reference_element: Reference):
        self.hybrid_shape_inverse.Element = reference_element.com_object

    @property
    def orientation(self) -> int:
        return self.hybrid_shape_inverse.Orientation

    @orientation.setter
    def orientation(self, value: int):
        self.hybrid_shape_inverse.Orientation = value

    def __repr__(self):
        return f'HybridShapeInverse(name="{self.name}")'
