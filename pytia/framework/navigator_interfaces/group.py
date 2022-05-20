from pytia.framework.product_structure_interfaces.product import Product
from pytia.framework.system_interfaces.any_object import AnyObject
from pytia.framework.cat_types.general import cat_variant


class Group(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.group = com_object

    @property
    def extract_mode(self) -> int:
        return self.group.ExtractMode

    @extract_mode.setter
    def extract_mode(self, value: int):
        self.group.ExtractMode = value

    def add_explicit(self, i_product: AnyObject) -> None:
        return self.group.AddExplicit(i_product.com_object)

    def count_explicit(self) -> int:
        return self.group.CountExplicit()

    def count_extract(self) -> int:
        return self.group.CountExtract()

    def count_invert(self) -> int:
        return self.group.CountInvert()

    def fill_sel_with_extract(self) -> None:
        return self.group.FillSelWithExtract()

    def fill_sel_with_invert(self) -> None:
        return self.group.FillSelWithInvert()

    def item_explicit(self, i_index: cat_variant) -> AnyObject:
        return self.group.ItemExplicit(i_index)

    def item_extract(self, i_index: cat_variant) -> Product:
        return Product(self.group.ItemExtract(i_index))

    def item_invert(self, i_index: cat_variant) -> Product:
        return Product(self.group.ItemInvert(i_index))

    def remove_explicit(self, i_index: cat_variant) -> None:
        return self.group.RemoveExplicit(i_index)

    def __repr__(self):
        return f'Group(name="{self.name}")'
