from typing import Iterator
from pytia.framework.drafting_interfaces.drawing_picture import DrawingPicture
from pytia.framework.system_interfaces.collection import Collection
from pytia.framework.cat_types.general import cat_variant


class DrawingPictures(Collection):
    def __init__(self, com_object):
        super().__init__(com_object, child_object=DrawingPicture)
        self.drawing_pictures = com_object

    def add(
        self, i_drawing_picture_path: str, i_position_x: float, i_position_y: float
    ) -> DrawingPicture:
        return DrawingPicture(
            self.drawing_pictures.Add(
                i_drawing_picture_path, i_position_x, i_position_y
            )
        )

    def item(self, i_index: cat_variant) -> DrawingPicture:
        return DrawingPicture(self.drawing_pictures.Item(i_index))

    def remove(self, i_index: cat_variant) -> None:
        return self.drawing_pictures.Remove(i_index)

    def __getitem__(self, n: int) -> DrawingPicture:
        if (n + 1) > self.count:
            raise StopIteration
        return DrawingPicture(self.drawing_pictures.item(n + 1))

    def __iter__(self) -> Iterator[DrawingPicture]:
        for i in range(self.count):
            yield self.child_object(self.com_object.item(i + 1))

    def __repr__(self):
        return f'DrawingPictures(name="{self.name}")'
