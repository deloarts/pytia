from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.in_interfaces.references import References
from pytia.framework.knowledge_interfaces.angle import Angle
from pytia.framework.knowledge_interfaces.length import Length
from pytia.framework.part_interfaces.dress_up_shape import DressUpShape


class Chamfer(DressUpShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.chamfer = com_object

    @property
    def angle(self) -> Angle:
        return Angle(self.chamfer.Angle)

    @property
    def elements_to_chamfer(self) -> References:
        return References(self.chamfer.ElementsToChamfer)

    @property
    def length1(self) -> Length:
        return Length(self.chamfer.Length1)

    @property
    def length2(self) -> Length:
        return Length(self.chamfer.Length2)

    @property
    def mode(self) -> int:
        return self.chamfer.Mode

    @mode.setter
    def mode(self, value: int):
        self.chamfer.Mode = value

    @property
    def orientation(self) -> int:
        return self.chamfer.Orientation

    @orientation.setter
    def orientation(self, value: int):
        self.chamfer.Orientation = value

    @property
    def propagation(self) -> int:
        return self.chamfer.Propagation

    @propagation.setter
    def propagation(self, value: int):
        self.chamfer.Propagation = value

    def add_element_to_chamfer(self, i_element_to_chamfer: Reference) -> None:
        return self.chamfer.AddElementToChamfer(i_element_to_chamfer.com_object)

    def withdraw_element_to_chamfer(self, i_element_to_withdraw: Reference) -> None:
        return self.chamfer.WithdrawElementToChamfer(i_element_to_withdraw.com_object)

    def __repr__(self):
        return f'Chamfer(name="{self.name}")'
