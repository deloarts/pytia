from pytia.framework.in_interfaces.document import Document
from pytia.framework.product_structure_interfaces.product import Product


class ProductDocument(Document):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.product_document = com_object

    @property
    def product(self) -> Product:
        return Product(self.product_document.Product)

    def __repr__(self):
        return f'ProductDocument(name="{ self.name }")'
