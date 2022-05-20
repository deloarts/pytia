from typing import Iterator
from pytia.framework.space_analyses_interfaces.clash import Clash
from pytia.framework.system_interfaces.collection import Collection
from pytia.framework.cat_types.general import cat_variant


class Clashes(Collection):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.clashes = com_object

    def add(self) -> Clash:
        return Clash(self.clashes.Add())

    def add_from_sel(self) -> Clash:
        return Clash(self.clashes.AddFromSel())

    def item(self, i_index: cat_variant) -> Clash:
        return Clash(self.clashes.Item(i_index))

    def remove(self, i_index: cat_variant) -> None:
        return self.clashes.Remove(i_index)

    def __getitem__(self, n: int) -> Clash:
        if (n + 1) > self.count:
            raise StopIteration
        return Clash(self.clashes.item(n + 1))

    def __iter__(self) -> Iterator[Clash]:
        for i in range(self.count):
            yield self.child_object(self.com_object.item(i + 1))

    def __repr__(self):
        return f'Clashes(name="{self.name}")'
