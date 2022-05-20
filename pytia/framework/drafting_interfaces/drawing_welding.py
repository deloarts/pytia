from pytia.framework.drafting_interfaces.drawing_leaders import DrawingLeaders
from pytia.framework.drafting_interfaces.drawing_text_properties import (
    DrawingTextProperties,
)
from pytia.framework.drafting_interfaces.drawing_text_range import DrawingTextRange
from pytia.framework.system_interfaces.any_object import AnyObject


class DrawingWelding(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.drawing_welding = com_object

    @property
    def angle(self) -> float:
        return self.drawing_welding.Angle

    @angle.setter
    def angle(self, value: float):
        self.drawing_welding.Angle = value

    @property
    def identification_line_side(self) -> int:
        return self.drawing_welding.IdentificationLineSide

    @identification_line_side.setter
    def identification_line_side(self, value: int):
        self.drawing_welding.IdentificationLineSide = value

    @property
    def leaders(self) -> DrawingLeaders:
        return DrawingLeaders(self.drawing_welding.Leaders)

    @property
    def text_properties(self) -> DrawingTextProperties:
        return DrawingTextProperties(self.drawing_welding.TextProperties)

    @property
    def welding_side(self) -> int:
        return self.drawing_welding.WeldingSide

    @welding_side.setter
    def welding_side(self, value: int):
        self.drawing_welding.WeldingSide = value

    @property
    def welding_tail(self) -> int:
        return self.drawing_welding.WeldingTail

    @welding_tail.setter
    def welding_tail(self, value: int):
        self.drawing_welding.WeldingTail = value

    @property
    def x(self) -> float:
        return self.drawing_welding.x

    @x.setter
    def x(self, value: float):
        self.drawing_welding.x = value

    @property
    def y(self) -> float:
        return self.drawing_welding.y

    @y.setter
    def y(self, value: float):
        self.drawing_welding.y = value

    def get_additional_symbol(self, i_weld: int) -> int:
        return self.drawing_welding.GetAdditionalSymbol(i_weld)

    def get_finish_symbol(self, i_weld: int) -> int:
        return self.drawing_welding.GetFinishSymbol(i_weld)

    def get_symbol(self, i_weld: int) -> int:
        return self.drawing_welding.GetSymbol(i_weld)

    def get_text_range(self, i_field: int) -> DrawingTextRange:
        return DrawingTextRange(self.drawing_welding.GetTextRange(i_field))

    def set_additional_symbol(self, i_symbol: int, i_weld: int) -> None:
        return self.drawing_welding.SetAdditionalSymbol(i_symbol, i_weld)

    def set_finish_symbol(self, i_finish_symbol: int, i_weld: int) -> None:
        return self.drawing_welding.SetFinishSymbol(i_finish_symbol, i_weld)

    def set_symbol(self, i_symbol: int, i_weld: int) -> None:
        return self.drawing_welding.SetSymbol(i_symbol, i_weld)

    def __repr__(self):
        return f'DrawingWelding(name="{self.name}")'
