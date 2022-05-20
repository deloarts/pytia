from pytia.framework.system_interfaces.any_object import AnyObject


class Move(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.move = com_object

    @property
    def movable_object(self) -> "Move":
        return Move(self.move.MovableObject)

    def apply(self, i_transformation_array: tuple) -> None:
        return self.move.Apply(i_transformation_array)

    def __repr__(self):
        return f'Move(name="{self.name}")'
