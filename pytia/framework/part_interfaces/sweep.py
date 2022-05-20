from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.part_interfaces.sketch_based_shape import SketchBasedShape
from pytia.framework.sketcher_interfaces.sketch import Sketch


class Sweep(SketchBasedShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.sweep = com_object

    @property
    def anchor_dir_reverse(self) -> bool:
        return self.sweep.AnchorDirReverse

    @anchor_dir_reverse.setter
    def anchor_dir_reverse(self, value: bool):
        self.sweep.AnchorDirReverse = value

    @property
    def center_curve(self) -> Sketch:
        return Sketch(self.sweep.CenterCurve)

    @property
    def center_curve_element(self) -> Reference:
        return Reference(self.sweep.CenterCurveElement)

    @center_curve_element.setter
    def center_curve_element(self, value: Reference):
        self.sweep.CenterCurveElement = value

    @property
    def is_thin(self) -> bool:
        return self.sweep.IsThin

    @is_thin.setter
    def is_thin(self, value: bool):
        self.sweep.IsThin = value

    @property
    def merge_end(self) -> bool:
        return self.sweep.MergeEnd

    @merge_end.setter
    def merge_end(self, value: bool):
        self.sweep.MergeEnd = value

    @property
    def merge_mode(self) -> int:
        return self.sweep.MergeMode

    @merge_mode.setter
    def merge_mode(self, value: int):
        self.sweep.MergeMode = value

    @property
    def move_profile_to_path(self) -> bool:
        return self.sweep.MoveProfileToPath

    @move_profile_to_path.setter
    def move_profile_to_path(self, value: bool):
        self.sweep.MoveProfileToPath = value

    @property
    def neutral_fiber(self) -> bool:
        return self.sweep.NeutralFiber

    @neutral_fiber.setter
    def neutral_fiber(self, value: bool):
        self.sweep.NeutralFiber = value

    @property
    def normal_axis_dir_reverse(self) -> bool:
        return self.sweep.NormalAxisDirReverse

    @normal_axis_dir_reverse.setter
    def normal_axis_dir_reverse(self, value: bool):
        self.sweep.NormalAxisDirReverse = value

    @property
    def pulling_dir_element(self) -> Reference:
        return Reference(self.sweep.PullingDirElement)

    @pulling_dir_element.setter
    def pulling_dir_element(self, value: Reference):
        self.sweep.PullingDirElement = value

    @property
    def reference_surface_element(self) -> Reference:
        return Reference(self.sweep.ReferenceSurfaceElement)

    @reference_surface_element.setter
    def reference_surface_element(self, value: Reference):
        self.sweep.ReferenceSurfaceElement = value

    def set_keep_angle_option(self) -> None:
        return self.sweep.SetKeepAngleOption()

    def __repr__(self):
        return f'Sweep(name="{ self.name }")'
