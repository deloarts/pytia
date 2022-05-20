from pytia.framework.product_structure_interfaces.product import Product
from pytia.framework.system_interfaces.any_object import AnyObject
from pytia.framework.cat_types.general import cat_variant


class FixTogether(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.fix_together = com_object

    @property
    def fix_togethers_count(self) -> int:
        return self.fix_together.FixTogethersCount

    @property
    def products_count(self) -> int:
        return self.fix_together.ProductsCount

    def add_fix_together(self, i_fix_together: "FixTogether") -> None:
        return self.fix_together.AddFixTogether(i_fix_together.com_object)

    def add_product(self, i_product: Product) -> None:
        return self.fix_together.AddProduct(i_product.com_object)

    def get_fix_together(self, i_index: cat_variant) -> "FixTogether":
        return FixTogether(self.fix_together.GetFixTogether(i_index))

    def get_product(self, i_index: cat_variant) -> Product:
        return Product(self.fix_together.GetProduct(i_index))

    def remove_fix_together(self, i_index: cat_variant) -> None:
        return self.fix_together.RemoveFixTogether(i_index)

    def remove_product(self, i_index: cat_variant) -> None:
        return self.fix_together.RemoveProduct(i_index)

    def __repr__(self):
        return f'FixTogether(name="{self.name}")'
