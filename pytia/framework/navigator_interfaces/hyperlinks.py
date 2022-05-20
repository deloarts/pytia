from typing import Iterator
from pytia.framework.navigator_interfaces.hyperlink import Hyperlink
from pytia.framework.system_interfaces.any_object import AnyObject
from pytia.framework.system_interfaces.collection import Collection
from pytia.framework.cat_types.general import cat_variant


class Hyperlinks(Collection):
    def __init__(self, com_object):
        super().__init__(com_object, child_object=Hyperlink)
        self.hyperlinks = com_object

    def add(self, i_object: AnyObject) -> Hyperlink:
        return Hyperlink(self.hyperlinks.Add(i_object.com_object))

    def get_hyperlink(self, i_object: AnyObject) -> Hyperlink:
        return Hyperlink(self.hyperlinks.GetHyperlink(i_object.com_object))

    def item(self, i_index: cat_variant) -> Hyperlink:
        return Hyperlink(self.hyperlinks.Item(i_index))

    def remove(self, i_index: cat_variant) -> None:
        return self.hyperlinks.Remove(i_index)

    def __getitem__(self, n: int) -> Hyperlink:
        if (n + 1) > self.count:
            raise StopIteration
        return Hyperlink(self.hyperlinks.item(n + 1))

    def __iter__(self) -> Iterator[Hyperlink]:
        for i in range(self.count):
            yield self.child_object(self.com_object.item(i + 1))

    def __repr__(self):
        return f'Hyperlinks(name="{self.name}")'
