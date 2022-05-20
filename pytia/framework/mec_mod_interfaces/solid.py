from pytia.framework.in_interfaces.move import Move
from pytia.framework.mec_mod_interfaces.shape import Shape
from pytia.framework.system_interfaces.any_object import AnyObject


class Solid(Shape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.solid = com_object

    @property
    def move(self) -> Move:
        return Move(self.solid.Move)

    @property
    def source_element(self) -> AnyObject:
        return AnyObject(self.solid.SourceElement)

    @property
    def source_product(self) -> AnyObject:
        return AnyObject(self.solid.SourceProduct)

    def __repr__(self):
        return f'Solid(name="{ self.name }")'
