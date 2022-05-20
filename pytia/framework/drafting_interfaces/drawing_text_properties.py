from pytia.framework.system_interfaces.cat_base_dispatch import CATBaseDispatch


class DrawingTextProperties(CATBaseDispatch):
    def __init__(self, com_object):
        super().__init__()
        self.drawing_text_properties = com_object

    @property
    def anchor_point(self) -> int:
        return self.drawing_text_properties.AnchorPoint

    @anchor_point.setter
    def anchor_point(self, value: int):
        self.drawing_text_properties.AnchorPoint = value

    @property
    def blanking(self) -> int:
        return self.drawing_text_properties.Blanking

    @blanking.setter
    def blanking(self, value: int):
        self.drawing_text_properties.Blanking = value

    @property
    def bold(self) -> int:
        return self.drawing_text_properties.Bold

    @bold.setter
    def bold(self, value: int):
        self.drawing_text_properties.Bold = value

    @property
    def color(self) -> int:
        return self.drawing_text_properties.Color

    @color.setter
    def color(self, value: int):
        self.drawing_text_properties.Color = value

    @property
    def font_name(self) -> str:
        return self.drawing_text_properties.FontName

    @font_name.setter
    def font_name(self, value: str):
        self.drawing_text_properties.FontName = value

    @property
    def font_size(self) -> float:
        return self.drawing_text_properties.FontSize

    @font_size.setter
    def font_size(self, value: float):
        self.drawing_text_properties.FontSize = value

    @property
    def frame_type(self) -> int:
        return self.drawing_text_properties.FrameType

    @frame_type.setter
    def frame_type(self, value: int):
        self.drawing_text_properties.FrameType = value

    @property
    def italic(self) -> int:
        return self.drawing_text_properties.Italic

    @italic.setter
    def italic(self, value: int):
        self.drawing_text_properties.Italic = value

    @property
    def justification(self) -> int:
        return self.drawing_text_properties.Justification

    @justification.setter
    def justification(self, value: int):
        self.drawing_text_properties.Justification = value

    @property
    def kerning(self) -> int:
        return self.drawing_text_properties.Kerning

    @kerning.setter
    def kerning(self, value: int):
        self.drawing_text_properties.Kerning = value

    @property
    def mirror(self) -> int:
        return self.drawing_text_properties.Mirror

    @mirror.setter
    def mirror(self, value: int):
        self.drawing_text_properties.Mirror = value

    @property
    def overline(self) -> int:
        return self.drawing_text_properties.Overline

    @overline.setter
    def overline(self, value: int):
        self.drawing_text_properties.Overline = value

    @property
    def strike_thru(self) -> int:
        return self.drawing_text_properties.StrikeThru

    @strike_thru.setter
    def strike_thru(self, value: int):
        self.drawing_text_properties.StrikeThru = value

    @property
    def subscript(self) -> int:
        return self.drawing_text_properties.Subscript

    @subscript.setter
    def subscript(self, value: int):
        self.drawing_text_properties.Subscript = value

    @property
    def superscript(self) -> int:
        return self.drawing_text_properties.Superscript

    @superscript.setter
    def superscript(self, value: int):
        self.drawing_text_properties.Superscript = value

    @property
    def underline(self) -> int:
        return self.drawing_text_properties.Underline

    @underline.setter
    def underline(self, value: int):
        self.drawing_text_properties.Underline = value

    def activate_frame(self, i_type: int) -> None:
        return self.drawing_text_properties.ActivateFrame(i_type)

    def update(self) -> None:
        return self.drawing_text_properties.Update()

    def __repr__(self):
        return f"DrawingTextProperties()"
