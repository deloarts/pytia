from pytia.framework.in_interfaces.viewer_2d import Viewer2D


class SpecsViewer(Viewer2D):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.specs_viewer = com_object

    @property
    def layout(self) -> int:
        return self.specs_viewer.Layout

    @layout.setter
    def layout(self, value: int):
        self.specs_viewer.Layout = value

    def __repr__(self):
        return f'SpecsViewer(name="{ self.name }")'
