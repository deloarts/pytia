from pytia.framework.in_interfaces.file_component import FileComponent
from pytia.framework.in_interfaces.text_stream import TextStream


class File(FileComponent):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.file = com_object

    @property
    def size(self) -> int:
        return self.file.Size

    @property
    def type(self) -> str:
        return self.file.Type

    def open_as_text_stream(self, i_mode: str) -> TextStream:
        return TextStream(self.file.OpenAsTextStream(i_mode))

    def __repr__(self):
        return f'File(name="{ self.name }")'
