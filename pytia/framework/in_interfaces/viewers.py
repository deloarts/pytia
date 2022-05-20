from typing import Iterator
from pytia.framework.in_interfaces.viewer import Viewer
from pytia.framework.system_interfaces.collection import Collection


class Viewers(Collection):
    def __init__(self, com_object):
        super().__init__(com_object, child_object=Viewer)
        self.viewers = com_object

    def item(self, i_index: int) -> Viewer:
        return Viewer(self.viewers.Item(i_index))

    def __getitem__(self, n: int) -> Viewer:
        if (n + 1) > self.count:
            raise StopIteration
        return Viewer(self.viewers.item(n + 1))

    def __iter__(self) -> Iterator[Viewer]:
        for i in range(self.count):
            yield self.child_object(self.com_object.item(i + 1))

    def __repr__(self):
        return f'Viewers(name="{self.name}")'
