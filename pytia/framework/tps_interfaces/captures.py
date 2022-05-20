from typing import Iterator
from pytia.framework.system_interfaces.any_object import AnyObject
from pytia.framework.system_interfaces.collection import Collection
from pytia.framework.tps_interfaces.capture import Capture
from pytia.framework.cat_types.general import cat_variant


class Captures(Collection):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.captures = com_object

    def item(self, i_index: cat_variant) -> AnyObject:
        return AnyObject(self.captures.Item(i_index))

    def __getitem__(self, n: int) -> Capture:
        if (n + 1) > self.count:
            raise StopIteration
        return Capture(self.captures.item(n + 1))

    def __iter__(self) -> Iterator[Capture]:
        for i in range(self.count):
            yield self.child_object(self.com_object.item(i + 1))

    def __repr__(self):
        return f'Captures(name="{self.name}")'
