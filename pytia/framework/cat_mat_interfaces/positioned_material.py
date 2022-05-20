from pytia.framework.cat_mat_interfaces.material import Material
from pytia.framework.system_interfaces.any_object import AnyObject


class PositionedMaterial(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.positioned_material = com_object

    @property
    def application_mode(self) -> int:
        return self.positioned_material.ApplicationMode

    @property
    def inheritance_mode(self) -> int:
        return self.positioned_material.InheritanceMode

    @inheritance_mode.setter
    def inheritance_mode(self, value: int):
        self.positioned_material.InheritanceMode = value

    @property
    def material(self) -> Material:
        return Material(self.positioned_material.Material)

    def __repr__(self):
        return f'PositionedMaterial(name="{ self.name }")'
