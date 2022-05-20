from typing import Iterator
from pytia.framework.drafting_interfaces.drawing_text import DrawingText
from pytia.framework.system_interfaces.collection import Collection


class DrawingTexts(Collection):
    def __init__(self, com_object):
        super().__init__(com_object, child_object=DrawingText)
        self.drawing_texts = com_object
        self.child_object = DrawingText

    def add(
        self, i_drawing_text: str, i_position_x: float, i_position_y: float
    ) -> DrawingText:
        return DrawingText(
            self.drawing_texts.Add(i_drawing_text, i_position_x, i_position_y)
        )

    def item(self, i_index: int) -> DrawingText:
        return DrawingText(self.drawing_texts.Item(i_index))

    def remove(self, i_index: int) -> None:
        return self.drawing_texts.Remove(i_index)

    def __getitem__(self, n: int) -> DrawingText:
        if (n + 1) > self.count:
            raise StopIteration
        return DrawingText(self.drawing_texts.item(n + 1))

    def __iter__(self) -> Iterator[DrawingText]:
        for i in range(self.count):
            yield self.child_object(self.com_object.item(i + 1))

    def __repr__(self):
        return f'DrawingTexts(name="{self.name}")'
