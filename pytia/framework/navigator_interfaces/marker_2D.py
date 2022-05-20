from pytia.framework.system_interfaces.any_object import AnyObject


class Marker2D(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.marker_2d = com_object

    @property
    def fill(self) -> int:
        return self.marker_2d.Fill

    @fill.setter
    def fill(self, value: int):
        self.marker_2d.Fill = value

    @property
    def frame(self) -> int:
        return self.marker_2d.Frame

    @frame.setter
    def frame(self, value: int):
        self.marker_2d.Frame = value

    @property
    def picture(self) -> str:
        return self.marker_2d.Picture

    @picture.setter
    def picture(self, value: str):
        self.marker_2d.Picture = value

    @property
    def text(self) -> str:
        return self.marker_2d.Text

    @text.setter
    def text(self, value: str):
        self.marker_2d.Text = value

    @property
    def text_angle(self) -> float:
        return self.marker_2d.TextAngle

    @text_angle.setter
    def text_angle(self, value: float):
        self.marker_2d.TextAngle = value

    @property
    def text_font(self) -> str:
        return self.marker_2d.TextFont

    @text_font.setter
    def text_font(self, value: str):
        self.marker_2d.TextFont = value

    @property
    def text_orientation(self) -> int:
        return self.marker_2d.TextOrientation

    @text_orientation.setter
    def text_orientation(self, value: int):
        self.marker_2d.TextOrientation = value

    @property
    def text_size(self) -> float:
        return self.marker_2d.TextSize

    @text_size.setter
    def text_size(self, value: float):
        self.marker_2d.TextSize = value

    @property
    def type(self) -> int:
        return self.marker_2d.Type

    def get_positions(self, o_coordinates: tuple) -> None:
        return self.marker_2d.GetPositions(o_coordinates)

    def set_positions(self, i_coordinates: tuple) -> None:
        return self.marker_2d.SetPositions(i_coordinates)

    def __repr__(self):
        return f'Marker2D(name="{self.name}")'
