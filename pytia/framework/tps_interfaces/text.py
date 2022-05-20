from pytia.framework.drafting_interfaces.drawing_text import DrawingText
from pytia.framework.system_interfaces.any_object import AnyObject
from pytia.framework.tps_interfaces.tps_parallel_on_screen import TPSParallelOnScreen


class Text(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.text_com = com_object

    @property
    def text(self) -> str:
        return self.text_com.Text

    @text.setter
    def text(self, value: str):
        self.text_com.Text = value

    def get_2d_annot(self) -> DrawingText:
        return DrawingText(self.text_com.Get2dAnnot())

    def tps_parallel_on_screen(self) -> TPSParallelOnScreen:
        return TPSParallelOnScreen(self.text_com.TPSParallelOnScreen())

    def __repr__(self):
        return f'Text(name="{self.name}")'
