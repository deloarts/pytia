from typing import Iterator
from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.system_interfaces.collection import Collection
from pytia.framework.cat_types.general import cat_variant


class References(Collection):
    def __init__(self, com_object):
        super().__init__(com_object, child_object=Reference)
        self.references = com_object

    def item(self, i_index: cat_variant) -> Reference:
        return Reference(self.references.Item(i_index))

    def __getitem__(self, n: int) -> Reference:
        if (n + 1) > self.count:
            raise StopIteration
        return Reference(self.references.item(n + 1))

    def __iter__(self) -> Iterator[Reference]:
        for i in range(self.count):
            yield self.child_object(self.com_object.item(i + 1))

    def __repr__(self):
        return f'References(name="{self.name}")'
