from pytia.framework.in_interfaces.document import Document
from pytia.framework.mec_mod_interfaces.part import Part
from pytia.framework.product_structure_interfaces.product import Product


class PartDocument(Document):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.part_document = com_object

    @property
    def part(self) -> Part:
        return Part(self.part_document.Part)

    @property
    def product(self) -> Product:
        return Product(self.part_document.Product)

    def __repr__(self):
        return f'PartDocument(name="{ self.name }")'
