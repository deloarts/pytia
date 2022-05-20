from pytia.framework.system_interfaces.any_object import AnyObject
from pytia.framework.tps_interfaces.tps_parallel_on_screen import TPSParallelOnScreen
from pytia.framework.cat_types.general import cat_variant


class FlagNote(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.flag_note = com_object

    @property
    def flag_note_text(self) -> str:
        return self.flag_note.FlagNoteText

    @flag_note_text.setter
    def flag_note_text(self, value: str):
        self.flag_note.FlagNoteText = value

    @property
    def text(self) -> str:
        return self.flag_note.Text

    @text.setter
    def text(self, value: str):
        self.flag_note.Text = value

    def add_url(self, i_url: str) -> None:
        return self.flag_note.AddURL(i_url)

    def get_nbr_url(self, o_number_of_url: cat_variant) -> None:
        return self.flag_note.GetNbrURL(o_number_of_url)

    def get_nbr_url2(self) -> int:
        return self.flag_note.GetNbrURL2()

    def modify_url(self, i_url: str, i_index: cat_variant) -> None:
        return self.flag_note.ModifyURL(i_url, i_index)

    def remove_url(self, i_index: cat_variant) -> None:
        return self.flag_note.RemoveURL(i_index)

    def tps_parallel_on_screen(self) -> TPSParallelOnScreen:
        return TPSParallelOnScreen(self.flag_note.TPSParallelOnScreen())

    def url(self, i_index: cat_variant) -> str:
        return self.flag_note.URL(i_index)

    def __repr__(self):
        return f'FlagNote(name="{self.name}")'
