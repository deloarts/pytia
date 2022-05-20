from typing import Iterator
from typing import TYPE_CHECKING
from pytia.framework.product_structure_interfaces.product import Product
from pytia.framework.system_interfaces.collection import Collection
from pytia.framework.cat_types.general import cat_variant

if TYPE_CHECKING:
    from pytia.framework.in_interfaces.document import Document


class Products(Collection):
    def __init__(self, com_object):
        super().__init__(com_object, child_object=Product)
        self.products = com_object

    def add_component(self, i_reference_product: Product) -> Product:
        return Product(self.products.AddComponent(i_reference_product.com_object))

    def add_components_from_files(self, i_files_list: tuple, i_method: str) -> None:
        return self.products.AddComponentsFromFiles(i_files_list, i_method)

    def add_external_component(self, i_product_document: "Document") -> Product:
        return Product(
            self.products.AddExternalComponent(i_product_document.com_object)
        )

    def add_new_component(self, i_documen_type: str, i_part_number: str) -> Product:
        return Product(self.products.AddNewComponent(i_documen_type, i_part_number))

    def add_new_product(self, i_part_number: str) -> Product:
        return Product(self.products.AddNewProduct(i_part_number))

    def item(self, i_index: cat_variant) -> Product:
        return Product(self.products.Item(i_index))

    def remove(self, i_index: cat_variant) -> None:
        return self.products.Remove(i_index)

    def replace_component(
        self, i_old_component: Product, i_file_path: str, i_multi_instances: bool
    ) -> Product:
        return Product(
            self.products.ReplaceComponent(
                i_old_component.com_object, i_file_path, i_multi_instances
            )
        )

    def replace_product(
        self,
        i_old_component: Product,
        i_new_reference: Product,
        i_multi_instances: bool,
    ) -> Product:
        return Product(
            self.products.ReplaceProduct(
                i_old_component.com_object,
                i_new_reference.com_object,
                i_multi_instances,
            )
        )

    def __len__(self):
        return self.count

    def __getitem__(self, n: int) -> Product:
        if (n + 1) > self.count:
            raise StopIteration
        return Product(self.products.item(n + 1))

    def __iter__(self) -> Iterator[Product]:
        for i in range(self.count):
            yield self.child_object(self.com_object.item(i + 1))

    def __repr__(self):
        return f'Products(name="{self.name}")'
