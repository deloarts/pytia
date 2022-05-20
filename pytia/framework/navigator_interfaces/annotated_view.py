from pytia.framework.navigator_interfaces.marker_2Ds import Marker2Ds
from pytia.framework.system_interfaces.any_object import AnyObject


class AnnotatedView(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.annotated_view = com_object

    @property
    def behavior_mode(self) -> int:
        return self.annotated_view.BehaviorMode

    @behavior_mode.setter
    def behavior_mode(self, value: int):
        self.annotated_view.BehaviorMode = value

    @property
    def comment(self) -> str:
        return self.annotated_view.Comment

    @comment.setter
    def comment(self, value: str):
        self.annotated_view.Comment = value

    @property
    def field_of_view(self) -> float:
        return self.annotated_view.FieldOfView

    @property
    def marker2_ds(self) -> Marker2Ds:
        return Marker2Ds(self.annotated_view.Marker2Ds)

    @property
    def projection_mode(self) -> int:
        return self.annotated_view.ProjectionMode

    @property
    def sound(self) -> str:
        return self.annotated_view.Sound

    @sound.setter
    def sound(self, value: str):
        self.annotated_view.Sound = value

    @property
    def zoom(self) -> float:
        return self.annotated_view.Zoom

    def get_origin(self, o_origin: tuple) -> None:
        return self.annotated_view.GetOrigin(o_origin)

    def get_sight_direction(self, o_sight: tuple) -> None:
        return self.annotated_view.GetSightDirection(o_sight)

    def get_up_direction(self, o_up: tuple) -> None:
        return self.annotated_view.GetUpDirection(o_up)

    def update(self) -> None:
        return self.annotated_view.Update()

    def __repr__(self):
        return f'AnnotatedView(name="{self.name}")'
