from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.part_interfaces.limit import Limit
from pytia.framework.part_interfaces.sketch_based_shape import SketchBasedShape


class Prism(SketchBasedShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.prism = com_object

    @property
    def direction_orientation(self) -> int:
        return self.prism.DirectionOrientation

    @direction_orientation.setter
    def direction_orientation(self, value: int):
        self.prism.DirectionOrientation = value

    @property
    def direction_type(self) -> int:
        return self.prism.DirectionType

    @direction_type.setter
    def direction_type(self, value: int):
        self.prism.DirectionType = value

    @property
    def first_limit(self) -> Limit:
        return Limit(self.prism.FirstLimit)

    @property
    def is_symmetric(self) -> bool:
        return self.prism.IsSymmetric

    @is_symmetric.setter
    def is_symmetric(self, value: bool):
        self.prism.IsSymmetric = value

    @property
    def is_thin(self) -> bool:
        return self.prism.IsThin

    @is_thin.setter
    def is_thin(self, value: bool):
        self.prism.IsThin = value

    @property
    def merge_end(self) -> bool:
        return self.prism.MergeEnd

    @merge_end.setter
    def merge_end(self, value: bool):
        self.prism.MergeEnd = value

    @property
    def neutral_fiber(self) -> bool:
        return self.prism.NeutralFiber

    @neutral_fiber.setter
    def neutral_fiber(self, value: bool):
        self.prism.NeutralFiber = value

    @property
    def second_limit(self) -> Limit:
        return Limit(self.prism.SecondLimit)

    def get_direction(self, io_direction: tuple) -> None:
        return self.prism.GetDirection(io_direction)

    def reverse_inner_side(self) -> None:
        return self.prism.ReverseInnerSide()

    def set_direction(self, i_line: Reference) -> None:
        return self.prism.SetDirection(i_line.com_object)

    def __repr__(self):
        return f'Prism(name="{self.name}")'
