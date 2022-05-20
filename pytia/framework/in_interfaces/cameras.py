from typing import Iterator
from pytia.framework.in_interfaces.camera import Camera
from pytia.framework.system_interfaces.collection import Collection
from pytia.framework.cat_types.general import cat_variant


class Cameras(Collection):
    def __init__(self, com_object):
        super().__init__(com_object, child_object=Camera)
        self.cameras = com_object

    def item(self, i_index: cat_variant) -> Camera:
        return Camera(self.cameras.Item(i_index))

    def remove(self, i_index: cat_variant) -> None:
        return self.cameras.Remove(i_index)

    def __getitem__(self, n: int) -> Camera:
        if (n + 1) > self.count:
            raise StopIteration
        return Camera(self.cameras.item(n + 1))

    def __iter__(self) -> Iterator[Camera]:
        for i in range(self.count):
            yield self.child_object(self.com_object.item(i + 1))

    def __repr__(self):
        return f'Cameras(name="{self.name}")'
