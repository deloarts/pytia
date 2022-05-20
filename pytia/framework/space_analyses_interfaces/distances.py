from typing import Iterator
from pytia.framework.space_analyses_interfaces.distance import Distance
from pytia.framework.system_interfaces.collection import Collection
from pytia.framework.cat_types.general import cat_variant


class Distances(Collection):
    def __init__(self, com_object):
        super().__init__(com_object, child_object=Distance)
        self.distances = com_object

    def add(self) -> Distance:
        return Distance(self.distances.Add())

    def add_from_sel(self) -> Distance:
        return Distance(self.distances.AddFromSel())

    def item(self, i_index: cat_variant) -> Distance:
        return Distance(self.distances.Item(i_index))

    def remove(self, i_index: cat_variant) -> None:
        return self.distances.Remove(i_index)

    def __getitem__(self, n: int) -> Distance:
        if (n + 1) > self.count:
            raise StopIteration
        return Distance(self.distances.item(n + 1))

    def __iter__(self) -> Iterator[Distance]:
        for i in range(self.count):
            yield self.child_object(self.com_object.item(i + 1))

    def __repr__(self):
        return f'Distances(name="{self.name}")'
