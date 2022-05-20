from typing import TYPE_CHECKING, Iterator
from pytia.framework.base import Base
from pytia.framework.system_interfaces.any_object import AnyObject

if TYPE_CHECKING:
    from pytia.framework.in_interfaces.application import Application


class Collection(Base):
    def __init__(self, com_object, child_object=AnyObject):
        super().__init__()
        self.com_object = com_object
        self.child_object = child_object

    @property
    def application(self) -> "Application":
        from pytia.framework.in_interfaces.application import Application

        return Application(self.com_object.Application)

    @property
    def count(self) -> int:
        return self.com_object.Count

    @property
    def name(self) -> str:
        return self.com_object.Name

    @property
    def parent(self) -> AnyObject:
        return AnyObject(self.com_object.Parent)

    def get_item(self, id_name: str) -> AnyObject:
        return self.child_object(self.com_object.GetItem(id_name))

    def get_item_by_index(self, index):
        return self.child_object(self.com_object.Item(index))

    def get_item_names(self):
        names = []
        for i in range(self.com_object.Count):
            name = self.com_object.Item(i + 1).Name
            names.append(name)
        return names

    def get_item_by_name(self, name):
        for i in range(self.com_object.Count):
            if self.com_object.Item(i + 1).Name == name:
                return self.child_object(self.com_object.Item(i + 1))
        return None

    def items(self):
        items_list = []
        for i in range(self.com_object.Count):
            item = self.child_object(self.com_object.Item(i + 1))
            items_list.append(item)
        return items_list

    def __len__(self):
        return self.count

    def __getitem__(self, n: int) -> AnyObject:
        if (n + 1) > self.count:
            raise StopIteration
        return AnyObject(self.com_object.item(n + 1))

    def __iter__(self) -> Iterator[AnyObject]:
        for i in range(self.count):
            yield self.child_object(self.com_object.item(i + 1))

    def __repr__(self):
        return f'Collection(name="{self.name}")'
