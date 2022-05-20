from pytia.framework.drafting_interfaces.drawing_leaders import DrawingLeaders
from pytia.framework.drafting_interfaces.drawing_text_properties import (
    DrawingTextProperties,
)
from pytia.framework.system_interfaces.any_object import AnyObject


class DrawingText(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.drawing_text = com_object

    @property
    def anchor_position(self) -> int:
        return self.drawing_text.AnchorPosition

    @anchor_position.setter
    def anchor_position(self, value: int):
        self.drawing_text.AnchorPosition = value

    @property
    def angle(self) -> float:
        return self.drawing_text.Angle

    @angle.setter
    def angle(self, value: float):
        self.drawing_text.Angle = value

    @property
    def associative_element(self) -> AnyObject:
        return AnyObject(self.drawing_text.AssociativeElement)

    @associative_element.setter
    def associative_element(self, value: AnyObject):
        self.drawing_text.AssociativeElement = value

    @property
    def frame_type(self) -> int:
        return self.drawing_text.FrameType

    @frame_type.setter
    def frame_type(self, value: int):
        self.drawing_text.FrameType = value

    @property
    def leaders(self):
        return DrawingLeaders(self.drawing_text.Leaders)

    @property
    def text(self) -> str:
        return self.drawing_text.Text

    @text.setter
    def text(self, value: str):
        self.drawing_text.Text = value

    @property
    def text_properties(self) -> DrawingTextProperties:
        return DrawingTextProperties(self.drawing_text.TextProperties)

    @property
    def wrapping_width(self) -> float:
        return self.drawing_text.WrappingWidth

    @wrapping_width.setter
    def wrapping_width(self, value: float):
        self.drawing_text.WrappingWidth = value

    @property
    def x(self) -> float:
        return self.drawing_text.x

    @x.setter
    def x(self, value: float):
        self.drawing_text.x = value

    @property
    def y(self) -> float:
        return self.drawing_text.y

    @y.setter
    def y(self, value: float):
        self.drawing_text.y = value

    def activate_frame(self, itype: int) -> None:
        return self.drawing_text.ActivateFrame(itype)

    def get_font_name(self, i_first, inb_character):
        return self.drawing_text.GetFontName(i_first, inb_character)

    def get_font_size(self, i_first: int, inb_character: int) -> float:
        return self.drawing_text.GetFontSize(i_first, inb_character)

    def get_modifiable_in_2d_component_instances(self) -> bool:
        return self.drawing_text.GetModifiableIn2DComponentInstances()

    def get_parameter_on_sub_string(
        self, i_param: int, i_first: int, inb_character: int
    ) -> int:
        return self.drawing_text.GetParameterOnSubString(
            i_param, i_first, inb_character
        )

    def insert_variable(
        self, i_first: int, inb_character: int, ibase: AnyObject
    ) -> None:
        return self.drawing_text.InsertVariable(
            i_first, inb_character, ibase.com_object
        )

    def set_font_name(self, i_first: int, inb_character: int, i_font_name: str) -> None:
        return self.drawing_text.SetFontName(i_first, inb_character, i_font_name)

    def set_font_size(
        self, i_first: int, inb_character: int, i_font_size: float
    ) -> None:
        return self.drawing_text.SetFontSize(i_first, inb_character, i_font_size)

    def set_modifiable_in_2d_component_instances(self) -> None:
        return self.drawing_text.SetModifiableIn2DComponentInstances()

    def set_parameter_on_sub_string(
        self, i_param: int, i_first: int, inb_character: int, i_val: int
    ) -> None:
        return self.drawing_text.SetParameterOnSubString(
            i_param, i_first, inb_character, i_val
        )

    def __repr__(self):
        return f'DrawingText(name="{self.name}")'
