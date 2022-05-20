from pytia.framework.cat_mat_interfaces.material_family import MaterialFamily
from pytia.framework.system_interfaces.collection import Collection
from pytia.framework.cat_types.general import cat_variant


class MaterialFamilies(Collection):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.material_families = com_object

    def add(self) -> MaterialFamily:
        return MaterialFamily(self.material_families.Add())

    def item(self, i_index: cat_variant) -> MaterialFamily:
        return MaterialFamily(self.material_families.Item(i_index))

    def remove(self, i_index: cat_variant) -> None:
        self.material_families.Remove(i_index)

    def __repr__(self):
        return f'MaterialFamilies(name="{ self.name }")'
