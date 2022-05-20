from pytia.framework.in_interfaces.camera import Camera
from pytia.framework.in_interfaces.viewpoint_2d import Viewpoint2D


class Camera2D(Camera):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.camera_2d = com_object

    @property
    def viewpoint2_d(self) -> Viewpoint2D:
        return Viewpoint2D(self.camera_2d.Viewpoint2D)

    @viewpoint2_d.setter
    def viewpoint2_d(self, value: Viewpoint2D):
        self.camera_2d.Viewpoint2D = value

    def __repr__(self):
        return f'Camera2D(name="{self.name}")'
