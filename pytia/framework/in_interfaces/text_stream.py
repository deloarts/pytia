from pytia.framework.system_interfaces.any_object import AnyObject


class TextStream(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.text_stream = com_object

    @property
    def at_end_of_line(self) -> bool:
        return self.text_stream.AtEndOfLine

    @property
    def at_end_of_stream(self) -> bool:
        return self.text_stream.AtEndOfStream

    def close(self) -> None:
        return self.text_stream.Close()

    def read(self, i_num_of_char: int) -> str:
        return self.text_stream.Read(i_num_of_char)

    def read_line(self) -> str:
        return self.text_stream.ReadLine()

    def write(self, i_written_string: str) -> None:
        return self.text_stream.Write(i_written_string)

    def __repr__(self):
        return f'TextStream(name="{ self.name }")'
