from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.knowledge_interfaces.real_param import RealParam
from pytia.framework.mec_mod_interfaces.shape import Shape


class Scaling2(Shape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.scaling2 = com_object

    @property
    def center(self) -> Reference:
        return Reference(self.scaling2.Center)

    @center.setter
    def center(self, value: Reference):
        self.scaling2.Center = value

    @property
    def ratio(self) -> RealParam:
        return RealParam(self.scaling2.Ratio)

    @property
    def ratio_value(self) -> float:
        return self.scaling2.RatioValue

    @ratio_value.setter
    def ratio_value(self, value: float):
        self.scaling2.RatioValue = value

    def __repr__(self):
        return f'Scaling2(name="{ self.name }")'
