from pytia.framework.system_interfaces.any_object import AnyObject
from pytia.framework.tps_interfaces.tps_parallel_on_screen import TPSParallelOnScreen


class Roughness(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.roughness = com_object

    @property
    def applicability(self) -> int:
        return self.roughness.Applicability

    @applicability.setter
    def applicability(self, value: int):
        self.roughness.Applicability = value

    @property
    def obtention(self) -> int:
        return self.roughness.Obtention

    @obtention.setter
    def obtention(self, value: int):
        self.roughness.Obtention = value

    def field(self, i_index: int) -> str:
        return self.roughness.Field(i_index)

    def set_field(self, i_index: int, i_field: str) -> None:
        return self.roughness.SetField(i_index, i_field)

    def tps_parallel_on_screen(self) -> TPSParallelOnScreen:
        return TPSParallelOnScreen(self.roughness.TPSParallelOnScreen())

    def __repr__(self):
        return f'Roughness(name="{self.name}")'
