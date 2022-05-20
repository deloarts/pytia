from typing import Iterator
from pytia.framework.mec_mod_interfaces.boundary import Boundary
from pytia.framework.mec_mod_interfaces.shape import Shape
from pytia.framework.system_interfaces.collection import Collection
from pytia.framework.cat_types.general import cat_variant


class Shapes(Collection):
    def __init__(self, com_object):
        super().__init__(com_object, child_object=Shape)
        self.shapes = com_object

    def get_boundary(self, i_label: str) -> Boundary:
        return Boundary(self.shapes.GetBoundary(i_label))

    def item(self, i_index: cat_variant) -> Shape:
        return Shape(self.shapes.Item(i_index))

    def __getitem__(self, n: int) -> Shape:
        if (n + 1) > self.count:
            raise StopIteration
        return Shape(self.shapes.item(n + 1))

    def __iter__(self) -> Iterator[Shape]:
        for i in range(self.count):
            yield self.child_object(self.com_object.item(i + 1))

    def __repr__(self):
        return f'Shapes(name="{self.name}")'
