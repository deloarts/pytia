from pytia.framework.in_interfaces.page_setup import PageSetup
from pytia.framework.in_interfaces.viewer import Viewer
from pytia.framework.in_interfaces.viewers import Viewers
from pytia.framework.system_interfaces.any_object import AnyObject


class Window(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.window = com_object

    @property
    def active_viewer(self) -> Viewer:
        return Viewer(self.window.ActiveViewer)

    @property
    def caption(self) -> str:
        return self.window.Caption

    @caption.setter
    def caption(self, value: str):
        self.window.Caption = value

    @property
    def height(self) -> int:
        return self.window.Height

    @height.setter
    def height(self, value: int):
        self.window.Height = value

    @property
    def left(self) -> int:
        return self.window.Left

    @left.setter
    def left(self, value: int):
        self.window.Left = value

    @property
    def page_setup(self) -> PageSetup:
        return PageSetup(self.window.PageSetup)

    @page_setup.setter
    def page_setup(self, value: PageSetup):
        self.window.PageSetup = value

    @property
    def top(self) -> int:
        return self.window.Top

    @top.setter
    def top(self, value: int):
        self.window.Top = value

    @property
    def viewers(self) -> Viewers:
        return Viewers(self.window.Viewers)

    @property
    def width(self) -> int:
        return self.window.Width

    @width.setter
    def width(self, value: int):
        self.window.Width = value

    @property
    def window_state(self) -> int:
        return self.window.WindowState

    @window_state.setter
    def window_state(self, value: int):
        self.window.WindowState = value

    def activate(self) -> None:
        return self.window.Activate()

    def activate_next(self) -> None:
        return self.window.ActivateNext()

    def activate_previous(self) -> None:
        return self.window.ActivatePrevious()

    def close(self) -> None:
        return self.window.Close()

    def new_window(self) -> "Window":
        return Window(self.window.NewWindow())

    def print_out(self) -> None:
        return self.window.PrintOut()

    def print_to_file(self, file_name: str) -> None:
        return self.window.PrintToFile(file_name)

    def __repr__(self):
        return f'Window(name="{self.name}")'
