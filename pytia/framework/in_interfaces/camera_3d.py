from pytia.framework.in_interfaces.camera import Camera
from pytia.framework.in_interfaces.viewpoint_3d import Viewpoint3D


class Camera3D(Camera):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.camera_3d = com_object

    @property
    def viewpoint3_d(self) -> Viewpoint3D:
        return Viewpoint3D(self.camera_3d.Viewpoint3D)

    @viewpoint3_d.setter
    def viewpoint3_d(self, value: Viewpoint3D):
        self.camera_3d.Viewpoint3D = value

    def __repr__(self):
        return f'Camera3D(name="{self.name}")'
