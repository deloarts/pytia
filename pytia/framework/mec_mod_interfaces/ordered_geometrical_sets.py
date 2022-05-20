from typing import Iterator
from pytia.framework.mec_mod_interfaces.ordered_geometrical_set import (
    OrderedGeometricalSet,
)
from pytia.framework.system_interfaces.collection import Collection
from pytia.framework.cat_types.general import cat_variant


class OrderedGeometricalSets(Collection):
    def __init__(self, com_object):
        super().__init__(com_object, child_object=OrderedGeometricalSet)
        self.ordered_geometrical_sets = com_object

    def add(self) -> OrderedGeometricalSet:
        return OrderedGeometricalSet(self.ordered_geometrical_sets.Add())

    def item(self, i_index: cat_variant) -> OrderedGeometricalSet:
        return OrderedGeometricalSet(self.ordered_geometrical_sets.Item(i_index))

    def __getitem__(self, n: int) -> OrderedGeometricalSet:
        if (n + 1) > self.count:
            raise StopIteration
        return OrderedGeometricalSet(self.ordered_geometrical_sets.item(n + 1))

    def __iter__(self) -> Iterator[OrderedGeometricalSet]:
        for i in range(self.count):
            yield self.child_object(self.com_object.item(i + 1))

    def __repr__(self):
        return f'OrderedGeometricalSets(name="{self.name}")'
