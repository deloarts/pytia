from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.knowledge_interfaces.angle import Angle
from pytia.framework.part_interfaces.sketch_based_shape import SketchBasedShape


class Revolution(SketchBasedShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.revolution = com_object

    @property
    def first_angle(self) -> Angle:
        return Angle(self.revolution.FirstAngle)

    @property
    def is_thin(self) -> bool:
        return self.revolution.IsThin

    @is_thin.setter
    def is_thin(self, value: bool):
        self.revolution.IsThin = value

    @property
    def merge_end(self) -> bool:
        return self.revolution.MergeEnd

    @merge_end.setter
    def merge_end(self, value: bool):
        self.revolution.MergeEnd = value

    @property
    def neutral_fiber(self) -> bool:
        return self.revolution.NeutralFiber

    @neutral_fiber.setter
    def neutral_fiber(self, value: bool):
        self.revolution.NeutralFiber = value

    @property
    def revolute_axis(self) -> Reference:
        return Reference(self.revolution.RevoluteAxis)

    @revolute_axis.setter
    def revolute_axis(self, value: Reference):
        self.revolution.RevoluteAxis = value

    @property
    def second_angle(self) -> Angle:
        return Angle(self.revolution.SecondAngle)

    def __repr__(self):
        return f'Revolution(name="{self.name}")'
