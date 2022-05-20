from typing import Iterator
from pytia.framework.knowledge_interfaces.unit import Unit
from pytia.framework.system_interfaces.collection import Collection
from pytia.framework.cat_types.general import cat_variant


class Units(Collection):
    def __init__(self, com_object):
        super().__init__(com_object, child_object=Unit)
        self.units = com_object

    def item(self, i_index: cat_variant) -> Unit:
        return Unit(self.units.Item(i_index))

    def __getitem__(self, n: int) -> Unit:
        if (n + 1) > self.count:
            raise StopIteration
        return Unit(self.units.item(n + 1))

    def __iter__(self) -> Iterator[Unit]:
        for i in range(self.count):
            yield self.child_object(self.com_object.item(i + 1))

    def __repr__(self):
        return f'Units(name="{self.name}")'
