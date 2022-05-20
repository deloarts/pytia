from typing import TYPE_CHECKING
from pytia.framework.in_interfaces.camera import Camera
from pytia.framework.system_interfaces.any_object import AnyObject

if TYPE_CHECKING:
    from pytia.framework.in_interfaces.viewer_2d import Viewer2D
    from pytia.framework.in_interfaces.viewer_3d import Viewer3D


class Viewer(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.viewer = com_object

    @property
    def full_screen(self) -> bool:
        return self.viewer.FullScreen

    @full_screen.setter
    def full_screen(self, value: bool):
        self.viewer.FullScreen = value

    @property
    def height(self) -> int:
        return self.viewer.Height

    @property
    def width(self) -> int:
        return self.viewer.Width

    def activate(self) -> None:
        return self.viewer.Activate()

    def capture_to_file(self, i_format: int, i_file: str) -> None:
        return self.viewer.CaptureToFile(i_format, i_file)

    def get_background_color(self) -> None:
        vba_function_name = "get_background_color"
        vba_code = """
        Public Function get_background_color(viewer)
            Dim color (2)
            viewer.GetBackgroundColor color
            get_background_color = color
        End Function
        """
        system_service = self.application.system_service
        return system_service.evaluate(
            vba_code, 0, vba_function_name, [self.com_object]
        )

    def create_viewer_2d(self) -> "Viewer2D":
        from pytia.framework.in_interfaces.viewer_2d import Viewer2D

        return Viewer2D(self.viewer)

    def create_viewer_3d(self) -> "Viewer3D":
        from pytia.framework.in_interfaces.viewer_3d import Viewer3D

        return Viewer3D(self.viewer)

    def new_camera(self) -> Camera:
        return Camera(self.viewer.NewCamera())

    def put_background_color(self, color: tuple) -> None:
        return self.viewer.PutBackgroundColor(color)

    def reframe(self) -> None:
        return self.viewer.Reframe()

    def update(self) -> None:
        return self.viewer.Update()

    def zoom_in(self) -> None:
        return self.viewer.ZoomIn()

    def zoom_out(self) -> None:
        return self.viewer.ZoomOut()

    def __repr__(self):
        return f'Viewer(name="{self.name}")'
