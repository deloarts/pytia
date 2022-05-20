from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.knowledge_interfaces.str_param import StrParam
from pytia.framework.part_interfaces.dress_up_shape import DressUpShape


class Thread(DressUpShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.thread = com_object

    @property
    def depth(self) -> float:
        return self.thread.Depth

    @depth.setter
    def depth(self, value: float):
        self.thread.Depth = value

    @property
    def diameter(self) -> float:
        return self.thread.Diameter

    @diameter.setter
    def diameter(self, value: float):
        self.thread.Diameter = value

    @property
    def lateral_face_element(self) -> Reference:
        return Reference(self.thread.LateralFaceElement)

    @lateral_face_element.setter
    def lateral_face_element(self, value: Reference):
        self.thread.LateralFaceElement = value

    @property
    def limit_face_element(self) -> Reference:
        return Reference(self.thread.LimitFaceElement)

    @limit_face_element.setter
    def limit_face_element(self, value: Reference):
        self.thread.LimitFaceElement = value

    @property
    def pitch(self) -> float:
        return self.thread.Pitch

    @pitch.setter
    def pitch(self, value: float):
        self.thread.Pitch = value

    @property
    def side(self) -> int:
        return self.thread.Side

    @side.setter
    def side(self, value: int):
        self.thread.Side = value

    @property
    def thread_description(self) -> StrParam:
        return StrParam(self.thread.ThreadDescription)

    def create_standard_thread_design_table(self, i_standard_type: int) -> None:
        return self.thread.CreateStandardThreadDesignTable(i_standard_type)

    def create_user_standard_design_table(
        self, i_standard_name: str, i_path: str
    ) -> None:
        return self.thread.CreateUserStandardDesignTable(i_standard_name, i_path)

    def reverse_direction(self) -> None:
        return self.thread.ReverseDirection()

    def set_explicit_polarity(self, i_thread_polarity: int) -> None:
        return self.thread.SetExplicitPolarity(i_thread_polarity)

    def __repr__(self):
        return f'Thread(name="{self.name}")'
