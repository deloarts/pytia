from pytia.framework.drafting_interfaces.drawing_component import DrawingComponent
from pytia.framework.system_interfaces.any_object import AnyObject
from pytia.framework.tps_interfaces.tps_parallel_on_screen import TPSParallelOnScreen
from pytia.framework.cat_types.general import cat_variant


class Noa(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.noa = com_object

    @property
    def flag_text(self) -> str:
        return self.noa.FlagText

    @flag_text.setter
    def flag_text(self, value: str):
        self.noa.FlagText = value

    @property
    def text(self) -> str:
        return self.noa.Text

    @text.setter
    def text(self, value: str):
        self.noa.Text = value

    def add_url(self, i_url: str) -> None:
        return self.noa.AddURL(i_url)

    def get_ditto(self) -> DrawingComponent:
        return DrawingComponent(self.noa.GetDitto())

    def get_modifiable_text(self, i_index: cat_variant) -> AnyObject:
        return AnyObject(self.noa.GetModifiableText(i_index))

    def get_modifiable_texts_count(self) -> int:
        return self.noa.GetModifiableTextsCount()

    def get_nbr_url(self, o_number_of_url: cat_variant) -> None:
        return self.noa.GetNbrURL(o_number_of_url)

    def get_nbr_url_2(self) -> int:
        return self.noa.GetNbrURL2()

    def modify_url(self, i_url: str, i_index: cat_variant) -> None:
        return self.noa.ModifyURL(i_url, i_index)

    def remove_url(self, i_index: cat_variant) -> None:
        return self.noa.RemoveURL(i_index)

    def tps_parallel_on_screen(self) -> TPSParallelOnScreen:
        return TPSParallelOnScreen(self.noa.TPSParallelOnScreen())

    def url(self, i_index: cat_variant) -> str:
        return self.noa.URL(i_index)

    def __repr__(self):
        return f'Noa(name="{self.name}")'
