import warnings
from pathlib import Path
from typing import Iterator

from pytia.framework.cat_types.general import cat_variant, list_str
from pytia.framework.exception_handling import CATIAApplicationException
from pytia.framework.in_interfaces.document import Document
from pytia.framework.system_interfaces.collection import Collection


class Documents(Collection):
    def __init__(self, com_object):
        super().__init__(com_object, child_object=Document)
        self.documents = com_object
        self.child_object = Document

    def add(self, document_type) -> Document:
        return Document(self.documents.Add(document_type))

    def count_types(self, file_type_list: list_str) -> int:
        items = self.get_item_names()
        if isinstance(file_type_list, str):
            type_list = [elem.lower() for elem in [file_type_list]]
        elif isinstance(file_type_list, list):
            type_list = [elem.lower() for elem in file_type_list]
        else:
            raise CATIAApplicationException(
                f"File type list {file_type_list} not valid type."
            )
        return len(
            [True for name in items for typ in type_list if name.lower().find(typ) > 0]
        )

    def new_from(self, full_name: Path) -> Document:
        return Document(self.documents.NewFrom(str(full_name)))

    def item(self, index: cat_variant) -> Document:
        try:
            return Document(self.documents.Item(index))
        except Exception as e:
            raise CATIAApplicationException(f'Could not get item "{index}".')

    def num_open(self) -> int:
        warning_string = (
            "The COM object can return the incorrect number of documents open. //n"
            "For example, after a CATPart document is closed CATIA can keep"
            "the linked document `ABQMaterialPropertiesCatalog.CATfct` loaded in the session."
        )
        warnings.warn(warning_string)
        return self.documents.Count

    def open(self, file_name: Path) -> Document:
        return Document(self.documents.Open(str(file_name)))

    def read(self, file_name: Path) -> Document:
        return Document(self.documents.Read(str(file_name)))

    def __getitem__(self, n: int) -> Document:
        if (n + 1) > self.count:
            raise StopIteration
        return Document(self.documents.item(n + 1))

    def __iter__(self) -> Iterator[Document]:
        for i in range(self.count):
            yield self.child_object(self.com_object.item(i + 1))

    def __repr__(self):
        return f'Documents(name="{self.name}")'
