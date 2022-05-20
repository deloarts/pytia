from pytia.framework.mec_mod_interfaces.hybrid_shape import HybridShape
from pytia.framework.mec_mod_interfaces.shape import Shape


class AxisToAxis(Shape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.axis_to_axis = com_object

    @property
    def hybrid_shape(self) -> HybridShape:
        return HybridShape(self.axis_to_axis.HybridShape)

    def __repr__(self):
        return f'AxisToAxis(name="{ self.name }")'
