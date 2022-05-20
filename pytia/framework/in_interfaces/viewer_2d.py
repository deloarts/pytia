from pytia.framework.in_interfaces.viewer import Viewer
from pytia.framework.in_interfaces.viewpoint_2d import Viewpoint2D


class Viewer2D(Viewer):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.viewer_2d = com_object

    @property
    def viewpoint_2d(self) -> Viewpoint2D:
        return Viewpoint2D(self.viewer_2d.Viewpoint2D)

    @viewpoint_2d.setter
    def viewpoint_2d(self, value: Viewpoint2D):
        self.viewer_2d.Viewpoint2D = value

    def __repr__(self):
        return f'Viewer2D(name="{self.name}")'
