from pytia.framework.drafting_interfaces.drawing_text_properties import (
    DrawingTextProperties,
)
from pytia.framework.system_interfaces.cat_base_dispatch import CATBaseDispatch


class DrawingTextRange(CATBaseDispatch):
    def __init__(self, com_object):
        super().__init__()
        self.drawing_text_range = com_object

    @property
    def length(self) -> int:
        return self.drawing_text_range.Length

    @property
    def start(self) -> int:
        return self.drawing_text_range.Start

    @property
    def text(self) -> str:
        return self.drawing_text_range.Text

    @text.setter
    def text(self, value: str):
        self.drawing_text_range.Text = value

    @property
    def text_properties(self) -> DrawingTextProperties:
        return DrawingTextProperties(self.drawing_text_range.TextProperties)

    def get_text_range(self, i_start: int, i_end: int) -> "DrawingTextRange":
        return DrawingTextRange(self.drawing_text_range.GetTextRange(i_start, i_end))

    def insert_after(self, i_string: str) -> None:
        return self.drawing_text_range.InsertAfter(i_string)

    def insert_before(self, i_string: str) -> None:
        return self.drawing_text_range.InsertBefore(i_string)

    def __repr__(self):
        return f"DrawingTextRange()"
