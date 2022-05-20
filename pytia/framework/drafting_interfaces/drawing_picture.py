from pytia.framework.system_interfaces.any_object import AnyObject


class DrawingPicture(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.drawing_picture = com_object

    @property
    def crop_bottom(self) -> float:
        return self.drawing_picture.cropBottom

    @crop_bottom.setter
    def crop_bottom(self, value: float):
        self.drawing_picture.cropBottom = value

    @property
    def crop_left(self) -> float:
        return self.drawing_picture.cropLeft

    @crop_left.setter
    def crop_left(self, value: float):
        self.drawing_picture.cropLeft = value

    @property
    def crop_right(self) -> float:
        return self.drawing_picture.cropRight

    @crop_right.setter
    def crop_right(self, value: float):
        self.drawing_picture.cropRight = value

    @property
    def crop_top(self) -> float:
        return self.drawing_picture.cropTop

    @crop_top.setter
    def crop_top(self, value: float):
        self.drawing_picture.cropTop = value

    @property
    def format(self) -> int:
        return self.drawing_picture.format

    @format.setter
    def format(self, value: int):
        self.drawing_picture.format = value

    @property
    def height(self) -> float:
        return self.drawing_picture.height

    @height.setter
    def height(self, value: float):
        self.drawing_picture.height = value

    @property
    def ratio_lock(self) -> bool:
        return self.drawing_picture.ratioLock

    @ratio_lock.setter
    def ratio_lock(self, value: bool):
        self.drawing_picture.ratioLock = value

    @property
    def width(self) -> float:
        return self.drawing_picture.width

    @width.setter
    def width(self, value: float):
        self.drawing_picture.width = value

    @property
    def x(self) -> float:
        return self.drawing_picture.x

    @x.setter
    def x(self, value: float):
        self.drawing_picture.x = value

    @property
    def y(self) -> float:
        return self.drawing_picture.y

    @y.setter
    def y(self, value: float):
        self.drawing_picture.y = value

    def get_original_height(self) -> float:
        return self.drawing_picture.GetOriginalHeight()

    def get_original_width(self) -> float:
        return self.drawing_picture.GetOriginalWidth()

    def __repr__(self):
        return f'DrawingPicture(name="{self.name}")'
