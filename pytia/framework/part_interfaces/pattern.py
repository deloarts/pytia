from pytia.framework.knowledge_interfaces.angle import Angle
from pytia.framework.part_interfaces.transformation_shape import TransformationShape
from pytia.framework.system_interfaces.any_object import AnyObject


class Pattern(TransformationShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.pattern = com_object

    @property
    def item_to_copy(self) -> AnyObject:
        return AnyObject(self.pattern.ItemToCopy)

    @item_to_copy.setter
    def item_to_copy(self, value: AnyObject):
        self.pattern.ItemToCopy = value

    @property
    def rotation_angle(self) -> Angle:
        return Angle(self.pattern.RotationAngle)

    def activate_position(self, i_pos_u: int, i_pos_v: int) -> None:
        return self.pattern.ActivatePosition(i_pos_u, i_pos_v)

    def desactivate_position(self, i_pos_u: int, i_pos_v: int) -> None:
        return self.pattern.DesactivatePosition(i_pos_u, i_pos_v)

    def __repr__(self):
        return f'Pattern(name="{ self.name }")'
