from typing import Iterator
from pytia.framework.navigator_interfaces.marker_3D import Marker3D
from pytia.framework.system_interfaces.any_object import AnyObject
from pytia.framework.system_interfaces.collection import Collection
from pytia.framework.cat_types.general import cat_variant


class Marker3Ds(Collection):
    def __init__(self, com_object):
        super().__init__(com_object, child_object=Marker3D)
        self.marker_3ds = com_object

    def add_3d_text(
        self,
        i_text_coordinates: tuple,
        i_text: str,
        i_object_coordinates: tuple,
        i_object: AnyObject,
    ) -> Marker3D:
        return Marker3D(
            self.marker_3ds.Add3DText(
                i_text_coordinates, i_text, i_object_coordinates, i_object.com_object
            )
        )

    def item(self, i_index: cat_variant) -> Marker3D:
        return Marker3D(self.marker_3ds.Item(i_index))

    def remove(self, i_index: cat_variant) -> None:
        return self.marker_3ds.Remove(i_index)

    def __getitem__(self, n: int) -> Marker3D:
        if (n + 1) > self.count:
            raise StopIteration
        return Marker3D(self.marker_3ds.item(n + 1))

    def __iter__(self) -> Iterator[Marker3D]:
        for i in range(self.count):
            yield self.child_object(self.com_object.item(i + 1))

    def __repr__(self):
        return f'Marker3Ds(name="{self.name}")'
