from pytia.framework.system_interfaces.any_object import AnyObject
from pytia.framework.cat_types.general import cat_variant


class Marker3D(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.marker_3d = com_object

    @property
    def fill(self) -> int:
        return self.marker_3d.Fill

    @fill.setter
    def fill(self, value: int):
        self.marker_3d.Fill = value

    @property
    def frame(self) -> int:
        return self.marker_3d.Frame

    @frame.setter
    def frame(self, value: int):
        self.marker_3d.Frame = value

    @property
    def text(self) -> str:
        return self.marker_3d.Text

    @text.setter
    def text(self, value: str):
        self.marker_3d.Text = value

    @property
    def text_font(self) -> str:
        return self.marker_3d.TextFont

    @text_font.setter
    def text_font(self, value: str):
        self.marker_3d.TextFont = value

    @property
    def text_orientation(self) -> int:
        return self.marker_3d.TextOrientation

    @text_orientation.setter
    def text_orientation(self, value: int):
        self.marker_3d.TextOrientation = value

    @property
    def text_size(self) -> float:
        return self.marker_3d.TextSize

    @text_size.setter
    def text_size(self, value: float):
        self.marker_3d.TextSize = value

    @property
    def type(self) -> int:
        return self.marker_3d.Type

    def add_object(self, i_object: AnyObject) -> None:
        return self.marker_3d.AddObject(i_object.com_object)

    def count_object(self) -> int:
        return self.marker_3d.CountObject()

    def get_object_positions(self, i_index: cat_variant, o_coordinates: tuple) -> None:
        return self.marker_3d.GetObjectPositions(i_index, o_coordinates)

    def get_text_positions(self, o_coordinates: tuple) -> None:
        return self.marker_3d.GetTextPositions(o_coordinates)

    def item_object(self, i_index: cat_variant) -> AnyObject:
        return self.marker_3d.ItemObject(i_index)

    def remove_object(self, i_index: cat_variant) -> None:
        return self.marker_3d.RemoveObject(i_index)

    def set_object_positions(self, i_index: cat_variant, i_coordinates: tuple) -> None:
        return self.marker_3d.SetObjectPositions(i_index, i_coordinates)

    def set_text_positions(self, i_coordinates: tuple) -> None:
        return self.marker_3d.SetTextPositions(i_coordinates)

    def update(self) -> None:
        return self.marker_3d.Update()

    def __repr__(self):
        return f'Marker3D(name="{self.name}")'
