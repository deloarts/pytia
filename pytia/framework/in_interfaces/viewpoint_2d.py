from pytia.framework.system_interfaces.any_object import AnyObject


class Viewpoint2D(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.viewpoint_2d = com_object

    @property
    def zoom(self) -> float:
        return self.viewpoint_2d.Zoom

    @zoom.setter
    def zoom(self, value: float):
        self.viewpoint_2d.Zoom = value

    def get_origin(self, o_origin: tuple) -> None:
        return self.viewpoint_2d.GetOrigin(o_origin)

    def put_origin(self, o_origin: tuple) -> None:
        return self.viewpoint_2d.PutOrigin(o_origin)

    def __repr__(self):
        return f'Viewpoint2D(name="{self.name}")'
