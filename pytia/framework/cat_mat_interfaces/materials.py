from pytia.framework.cat_mat_interfaces.material import Material
from pytia.framework.system_interfaces.collection import Collection
from pytia.framework.cat_types.general import cat_variant


class Materials(Collection):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.materials = com_object

    def add(self) -> Material:
        return Material(self.materials.Add())

    def item(self, i_index: cat_variant) -> Material:
        return Material(self.materials.Item(i_index))

    def remove(self, i_index: cat_variant) -> None:
        self.materials.Remove(i_index)

    def sorted_item(self, i_index: cat_variant, i_mode: int) -> Material:
        return Material(self.materials.SortedItem(i_index, i_mode))

    def __repr__(self):
        return f'Materials(name="{ self.name }")'
