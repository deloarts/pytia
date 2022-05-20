from typing import Iterator
from pytia.framework.drafting_interfaces.drawing_arrow import DrawingArrow
from pytia.framework.system_interfaces.collection import Collection


class DrawingArrows(Collection):
    def __init__(self, com_object):
        super().__init__(com_object, child_object=DrawingArrow)
        self.drawing_arrows = com_object

    def add(
        self,
        i_head_point_x: float,
        i_head_point_y: float,
        i_tail_point_x: float,
        i_tail_point_y: float,
    ) -> DrawingArrow:
        return DrawingArrow(
            self.drawing_arrows.Add(
                i_head_point_x, i_head_point_y, i_tail_point_x, i_tail_point_y
            )
        )

    def item(self, i_index: int) -> DrawingArrow:
        return DrawingArrow(self.drawing_arrows.Item(i_index))

    def remove(self, i_index: int) -> None:
        return self.drawing_arrows.Remove(i_index)

    def __getitem__(self, n: int) -> DrawingArrow:
        if (n + 1) > self.count:
            raise StopIteration
        return DrawingArrow(self.drawing_arrows.item(n + 1))

    def __iter__(self) -> Iterator[DrawingArrow]:
        for i in range(self.count):
            yield self.child_object(self.com_object.item(i + 1))

    def __repr__(self):
        return f'DrawingArrows(name="{self.name}")'
