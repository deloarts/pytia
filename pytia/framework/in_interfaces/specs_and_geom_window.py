from pytia.framework.in_interfaces.specs_viewer import SpecsViewer
from pytia.framework.in_interfaces.window import Window


class SpecsAndGeomWindow(Window):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.specs_and_geom_window = com_object

    @property
    def layout(self) -> int:
        return self.specs_and_geom_window.Layout

    @layout.setter
    def layout(self, value: int):
        self.specs_and_geom_window.Layout = value

    @property
    def specs_viewer(self) -> SpecsViewer:
        return SpecsViewer(self.specs_and_geom_window.SpecsViewer)

    def __repr__(self):
        return f'SpecsAndGeomWindow(name="{ self.name }")'
