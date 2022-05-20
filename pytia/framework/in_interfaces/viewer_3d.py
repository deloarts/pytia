from pytia.framework.in_interfaces.light_sources import LightSources
from pytia.framework.in_interfaces.viewer import Viewer
from pytia.framework.in_interfaces.viewpoint_3d import Viewpoint3D


class Viewer3D(Viewer):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.viewer_3d = com_object

    @property
    def clipping_mode(self) -> int:
        return self.viewer_3d.ClippingMode

    @clipping_mode.setter
    def clipping_mode(self, value: int):
        self.viewer_3d.ClippingMode = value

    @property
    def far_limit(self) -> float:
        return self.viewer_3d.FarLimit

    @far_limit.setter
    def far_limit(self, value: float):
        self.viewer_3d.FarLimit = value

    @property
    def foggy(self) -> bool:
        return self.viewer_3d.Foggy

    @foggy.setter
    def foggy(self, value: bool):
        self.viewer_3d.Foggy = value

    @property
    def ground(self) -> bool:
        return self.viewer_3d.Ground

    @ground.setter
    def ground(self, value: bool):
        self.viewer_3d.Ground = value

    @property
    def light_sources(self) -> LightSources:
        return LightSources(self.viewer_3d.LightSources)

    @property
    def lighting_intensity(self) -> float:
        return self.viewer_3d.LightingIntensity

    @lighting_intensity.setter
    def lighting_intensity(self, value: float):
        self.viewer_3d.LightingIntensity = value

    @property
    def lighting_mode(self) -> int:
        return self.viewer_3d.LightingMode

    @lighting_mode.setter
    def lighting_mode(self, value: int):
        self.viewer_3d.LightingMode = value

    @property
    def navigation_style(self) -> int:
        return self.viewer_3d.NavigationStyle

    @navigation_style.setter
    def navigation_style(self, value: int):
        self.viewer_3d.NavigationStyle = value

    @property
    def near_limit(self) -> float:
        return self.viewer_3d.NearLimit

    @near_limit.setter
    def near_limit(self, value: float):
        self.viewer_3d.NearLimit = value

    @property
    def rendering_mode(self) -> int:
        return self.viewer_3d.RenderingMode

    @rendering_mode.setter
    def rendering_mode(self, value: int):
        self.viewer_3d.RenderingMode = value

    @property
    def viewpoint_3d(self) -> Viewpoint3D:
        return Viewpoint3D(self.viewer_3d.Viewpoint3D)

    @viewpoint_3d.setter
    def viewpoint_3d(self, value: Viewpoint3D):
        self.viewer_3d.Viewpoint3D = value

    def rotate(self, i_axis: tuple, i_angle: float) -> None:
        return self.viewer_3d.Rotate(i_axis, i_angle)

    def translate(self, i_vector: tuple) -> None:
        return self.viewer_3d.Translate(i_vector)

    def __repr__(self):
        return f'Viewer3D(name="{self.name}")'
