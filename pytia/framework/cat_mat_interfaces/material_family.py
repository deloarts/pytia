from pytia.framework.cat_mat_interfaces.materials import Materials
from pytia.framework.system_interfaces.any_object import AnyObject


class MaterialFamily(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.material_family = com_object

    @property
    def materials(self) -> Materials:
        return Materials(self.material_family.Materials)

    def __repr__(self):
        return f'MaterialFamily(name="{ self.name }")'
