from pytia.framework.cat_mat_interfaces.material_families import MaterialFamilies
from pytia.framework.in_interfaces.document import Document


class MaterialDocument(Document):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.material_document = com_object

    @property
    def families(self) -> MaterialFamilies:
        return MaterialFamilies(self.material_document.Families)

    def __repr__(self):
        return f'MaterialDocument(name="{ self.name }")'
