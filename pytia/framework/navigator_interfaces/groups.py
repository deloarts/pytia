from typing import Iterator
from pytia.framework.navigator_interfaces.group import Group
from pytia.framework.system_interfaces.collection import Collection
from pytia.framework.cat_types.general import cat_variant


class Groups(Collection):
    def __init__(self, com_object):
        super().__init__(com_object, child_object=Group)
        self.groups = com_object

    def add(self) -> Group:
        return Group(self.groups.Add())

    def add_from_sel(self) -> Group:
        return Group(self.groups.AddFromSel())

    def all_leaves(self) -> Group:
        return Group(self.groups.AllLeaves())

    def item(self, i_index: cat_variant) -> Group:
        return Group(self.groups.Item(i_index))

    def remove(self, i_index: cat_variant) -> None:
        return self.groups.Remove(i_index)

    def __getitem__(self, n: int) -> Group:
        if (n + 1) > self.count:
            raise StopIteration
        return Group(self.groups.item(n + 1))

    def __iter__(self) -> Iterator[Group]:
        for i in range(self.count):
            yield self.child_object(self.com_object.item(i + 1))

    def __repr__(self):
        return f'Groups(name="{self.name}")'
