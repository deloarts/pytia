from typing import Iterator
from pytia.framework.sketcher_interfaces.geometric_element import GeometricElement
from pytia.framework.system_interfaces.collection import Collection
from pytia.framework.cat_types.general import cat_variant


class GeometricElements(Collection):
    def __init__(self, com_object):
        super().__init__(com_object, child_object=GeometricElement)
        self.geometric_elements = com_object

    def item(self, i_index: cat_variant) -> GeometricElement:
        return GeometricElement(self.geometric_elements.Item(i_index))

    def __getitem__(self, n: int) -> GeometricElement:
        if (n + 1) > self.count:
            raise StopIteration
        return GeometricElement(self.geometric_elements.item(n + 1))

    def __iter__(self) -> Iterator[GeometricElement]:
        for i in range(self.count):
            yield self.child_object(self.com_object.item(i + 1))

    def __repr__(self):
        return f'GeometricElements(name="{self.name}")'
