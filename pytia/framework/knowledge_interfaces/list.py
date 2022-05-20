from typing import Iterator
from pytia.framework.system_interfaces.any_object import AnyObject
from pytia.framework.system_interfaces.collection import Collection
from pytia.framework.cat_types.general import cat_variant


class List(Collection):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.list = com_object

    def add(self, i_item_value: AnyObject) -> None:
        return self.list.Add(i_item_value.com_object)

    def item(self, i_index: cat_variant) -> AnyObject:
        return AnyObject(self.list.Item(i_index))

    def remove(self, i_index: cat_variant) -> None:
        return self.list.Remove(i_index)

    def reorder(
        self, i_index_current: cat_variant, i_index_target: cat_variant
    ) -> None:
        return self.list.Reorder(i_index_current, i_index_target)

    def replace(self, i_index: cat_variant, i_item_value: AnyObject) -> None:
        return self.list.Replace(i_index, i_item_value.com_object)

    def __getitem__(self, n: int) -> AnyObject:
        if (n + 1) > self.count:
            raise StopIteration
        return AnyObject(self.list.item(n + 1))

    def __iter__(self) -> Iterator[AnyObject]:
        for i in range(self.count):
            yield self.child_object(self.com_object.item(i + 1))

    def __repr__(self):
        return f'List(name="{self.name}")'
