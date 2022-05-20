from typing import TYPE_CHECKING
from pytia.framework.in_interfaces.camera_3d import Camera3D
from pytia.framework.system_interfaces.any_object import AnyObject
from pytia.framework.tps_interfaces.tps_view import TPSView
from pytia.framework.tps_interfaces.tps_views import TPSViews
from pytia.framework.tps_interfaces.tps_parallel_on_screen import TPSParallelOnScreen

if TYPE_CHECKING:
    from pytia.framework.tps_interfaces.annotations import Annotations
    from pytia.framework.tps_interfaces.annotation_set import AnnotationSet


class Capture(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.capture = com_object

    @property
    def active_view(self) -> TPSView:
        return TPSView(self.capture.ActiveView)

    @active_view.setter
    def active_view(self, value: TPSView):
        self.capture.ActiveView = value

    @property
    def active_view_state(self) -> bool:
        return self.capture.ActiveViewState

    @active_view_state.setter
    def active_view_state(self, value: bool):
        self.capture.ActiveViewState = value

    @property
    def annotations(self) -> "Annotations":
        from pytia.framework.tps_interfaces.annotations import Annotations

        return Annotations(self.capture.Annotations)

    @annotations.setter
    def annotations(self, value: "Annotations"):
        self.capture.Annotations = value

    @property
    def camera(self) -> Camera3D:
        return Camera3D(self.capture.Camera)

    @camera.setter
    def camera(self, value: Camera3D):
        self.capture.Camera = value

    @property
    def clipping_plane(self) -> bool:
        return self.capture.ClippingPlane

    @clipping_plane.setter
    def clipping_plane(self, value: bool):
        self.capture.ClippingPlane = value

    @property
    def current(self) -> bool:
        return self.capture.Current

    @current.setter
    def current(self, value: bool):
        self.capture.Current = value

    @property
    def manage_hide_show_body(self) -> bool:
        return self.capture.ManageHideShowBody

    @manage_hide_show_body.setter
    def manage_hide_show_body(self, value: bool):
        self.capture.ManageHideShowBody = value

    @property
    def set(self) -> "AnnotationSet":
        from pytia.framework.tps_interfaces.annotation_set import AnnotationSet

        return AnnotationSet(self.capture.Set)

    @property
    def tps_views(self) -> TPSViews:
        return TPSViews(self.capture.TPSViews)

    @tps_views.setter
    def tps_views(self, value: TPSViews):
        self.capture.TPSViews = value

    @property
    def view_point(self) -> bool:
        return self.capture.ViewPoint

    @view_point.setter
    def view_point(self, value: bool):
        self.capture.ViewPoint = value

    def display_capture(self) -> None:
        return self.capture.DisplayCapture()

    def display_capture_2(self, ib_apply_mirror: bool) -> None:
        return self.capture.DisplayCapture2(ib_apply_mirror)

    def tps_parallel_on_screen(self) -> TPSParallelOnScreen:
        return TPSParallelOnScreen(self.capture.TPSParallelOnScreen())

    def __repr__(self):
        return f'Capture(name="{self.name}")'
