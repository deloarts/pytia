from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.knowledge_interfaces.angle import Angle
from pytia.framework.mec_mod_interfaces.hybrid_shape import HybridShape
from pytia.framework.mec_mod_interfaces.shape import Shape


class Rotate(Shape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.rotate = com_object

    @property
    def angle(self) -> Angle:
        return Angle(self.rotate.Angle)

    @property
    def angle_value(self) -> float:
        return self.rotate.AngleValue

    @angle_value.setter
    def angle_value(self, value: float):
        self.rotate.AngleValue = value

    @property
    def axis(self) -> Reference:
        return Reference(self.rotate.Axis)

    @axis.setter
    def axis(self, value: Reference):
        self.rotate.Axis = value

    @property
    def hybrid_shape(self) -> HybridShape:
        return HybridShape(self.rotate.HybridShape)

    def __repr__(self):
        return f'Rotate(name="{ self.name }")'
