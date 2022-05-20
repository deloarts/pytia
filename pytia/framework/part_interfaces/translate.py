from pytia.framework.mec_mod_interfaces.hybrid_shape import HybridShape
from pytia.framework.mec_mod_interfaces.shape import Shape


class Translate(Shape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.translate = com_object

    @property
    def hybrid_shape(self) -> HybridShape:
        return HybridShape(self.translate.HybridShape)

    def __repr__(self):
        return f'Translate(name="{ self.name }")'
