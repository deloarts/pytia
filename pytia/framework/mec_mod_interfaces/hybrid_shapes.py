from typing import Iterator
from pytia.framework.mec_mod_interfaces.boundary import Boundary
from pytia.framework.mec_mod_interfaces.hybrid_shape import HybridShape
from pytia.framework.system_interfaces.collection import Collection
from pytia.framework.cat_types.general import cat_variant


class HybridShapes(Collection):
    def __init__(self, com_object):
        super().__init__(com_object, child_object=HybridShape)
        self.hybrid_shapes = com_object

    def get_boundary(self, i_label: str) -> Boundary:
        return Boundary(self.hybrid_shapes.GetBoundary(i_label))

    def item(self, i_index: cat_variant) -> HybridShape:
        return HybridShape(self.hybrid_shapes.Item(i_index))

    def __getitem__(self, n: int) -> HybridShape:
        if (n + 1) > self.count:
            raise StopIteration
        return HybridShape(self.hybrid_shapes.item(n + 1))

    def __iter__(self) -> Iterator[HybridShape]:
        for i in range(self.count):
            yield self.child_object(self.com_object.item(i + 1))

    def __repr__(self):
        return f'HybridShapes(name="{self.name}")'
