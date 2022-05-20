from typing import Iterator
from pytia.framework.drafting_interfaces.drawing_welding import DrawingWelding
from pytia.framework.system_interfaces.collection import Collection


class DrawingWeldings(Collection):
    def __init__(self, com_object):
        super().__init__(com_object, child_object=DrawingWelding)
        self.drawing_weldings = com_object

    def add(
        self, i_symbol: int, i_position_x: float, i_position_y: float
    ) -> DrawingWelding:
        return DrawingWelding(
            self.drawing_weldings.Add(i_symbol, i_position_x, i_position_y)
        )

    def item(self, i_index: int) -> DrawingWelding:
        return DrawingWelding(self.drawing_weldings.Item(i_index))

    def remove(self, i_index: int) -> None:
        return self.drawing_weldings.Remove(i_index)

    def __getitem__(self, n: int) -> DrawingWelding:
        if (n + 1) > self.count:
            raise StopIteration
        return DrawingWelding(self.drawing_weldings.item(n + 1))

    def __iter__(self) -> Iterator[DrawingWelding]:
        for i in range(self.count):
            yield self.child_object(self.com_object.item(i + 1))

    def __repr__(self):
        return f'DrawingWeldings(name="{self.name}")'
