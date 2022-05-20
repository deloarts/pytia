from typing import Iterator
from pytia.framework.space_analyses_interfaces.inertia import Inertia
from pytia.framework.system_interfaces.any_object import AnyObject
from pytia.framework.system_interfaces.collection import Collection
from pytia.framework.cat_types.general import cat_variant


class Inertias(Collection):
    def __init__(self, com_object):
        super().__init__(com_object, child_object=Inertia)
        self.inertias = com_object

    def add(self, i_object: AnyObject) -> Inertia:
        return Inertia(self.inertias.Add(i_object.com_object))

    def item(self, i_index: cat_variant) -> Inertia:
        return Inertia(self.inertias.Item(i_index))

    def remove(self, i_index: cat_variant) -> None:
        return self.inertias.Remove(i_index)

    def __getitem__(self, n: int) -> Inertia:
        if (n + 1) > self.count:
            raise StopIteration
        return Inertia(self.inertias.item(n + 1))

    def __iter__(self) -> Iterator[Inertia]:
        for i in range(self.count):
            yield self.child_object(self.com_object.item(i + 1))

    def __repr__(self):
        return f'Inertias(name="{self.name}")'
