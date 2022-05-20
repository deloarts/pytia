from typing import Iterator
from pytia.framework.navigator_interfaces.marker_2D import Marker2D
from pytia.framework.system_interfaces.collection import Collection
from pytia.framework.cat_types.general import cat_variant


class Marker2Ds(Collection):
    def __init__(self, com_object):
        super().__init__(com_object, child_object=Marker2D)
        self.marker_2ds = com_object

    def add2_d_arrow(self, i_coordinates: tuple) -> Marker2D:
        return Marker2D(self.marker_2ds.Add2DArrow(i_coordinates))

    def add2_d_circle(self, i_coordinates: tuple, i_fill_status: int) -> Marker2D:
        return Marker2D(self.marker_2ds.Add2DCircle(i_coordinates, i_fill_status))

    def add2_d_free_hand(self, i_coordinates: tuple) -> Marker2D:
        return Marker2D(self.marker_2ds.Add2DFreeHand(i_coordinates))

    def add2_d_line(self, i_coordinates: tuple) -> Marker2D:
        return Marker2D(self.marker_2ds.Add2DLine(i_coordinates))

    def add2_d_picture(self, i_coordinates: tuple, i_path: str) -> Marker2D:
        return Marker2D(self.marker_2ds.Add2DPicture(i_coordinates, i_path))

    def add2_d_rectangle(self, i_coordinates: tuple, i_fill_status: int) -> Marker2D:
        return Marker2D(self.marker_2ds.Add2DRectangle(i_coordinates, i_fill_status))

    def add2_d_text(self, i_coordinates: tuple, i_text: str) -> Marker2D:
        return Marker2D(self.marker_2ds.Add2DText(i_coordinates, i_text))

    def item(self, i_index: cat_variant) -> Marker2D:
        return Marker2D(self.marker_2ds.Item(i_index))

    def remove(self, i_index: cat_variant) -> None:
        return self.marker_2ds.Remove(i_index)

    def __getitem__(self, n: int) -> Marker2D:
        if (n + 1) > self.count:
            raise StopIteration
        return Marker2D(self.marker_2ds.item(n + 1))

    def __iter__(self) -> Iterator[Marker2D]:
        for i in range(self.count):
            yield self.child_object(self.com_object.item(i + 1))

    def __repr__(self):
        return f'Marker2Ds(name="{self.name}")'
