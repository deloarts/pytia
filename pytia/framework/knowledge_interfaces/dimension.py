from pytia.framework.knowledge_interfaces.real_param import RealParam
from pytia.framework.knowledge_interfaces.unit import Unit


class Dimension(RealParam):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.dimension = com_object

    @property
    def unit(self) -> Unit:
        return Unit(self.dimension.Unit)

    def value_as_string2(self, i_nb_decimals: int, i_show_trailing_zeros: bool) -> str:
        return self.dimension.ValueAsString2(i_nb_decimals, i_show_trailing_zeros)

    def __repr__(self):
        return f'Dimension(name="{ self.name }")'
