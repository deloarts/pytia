from typing import Iterator
from pytia.framework.mec_mod_interfaces.axis_system import AxisSystem
from pytia.framework.system_interfaces.collection import Collection
from pytia.framework.cat_types.general import cat_variant


class AxisSystems(Collection):
    def __init__(self, com_object):
        super().__init__(com_object, child_object=AxisSystem)
        self.axis_systems = com_object

    def add(self) -> AxisSystem:
        return AxisSystem(self.axis_systems.Add())

    def item(self, i_index: cat_variant) -> AxisSystem:
        return AxisSystem(self.axis_systems.Item(i_index))

    def __getitem__(self, n: int) -> AxisSystem:
        if (n + 1) > self.count:
            raise StopIteration
        return AxisSystem(self.axis_systems.item(n + 1))

    def __iter__(self) -> Iterator[AxisSystem]:
        for i in range(self.count):
            yield self.child_object(self.com_object.item(i + 1))

    def __repr__(self):
        return f'AxisSystems(name="{self.name}")'
