from typing import Iterator
from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.mec_mod_interfaces.boundary import Boundary
from pytia.framework.sketcher_interfaces.sketch import Sketch
from pytia.framework.system_interfaces.collection import Collection
from pytia.framework.cat_types.general import cat_variant


class Sketches(Collection):
    def __init__(self, com_object):
        super().__init__(com_object, child_object=Sketch)
        self.sketches = com_object

    def add(self, i_plane: Reference) -> Sketch:
        return Sketch(self.sketches.Add(i_plane.com_object))

    def get_boundary(self, i_label: str) -> Boundary:
        return Boundary(self.sketches.GetBoundary(i_label))

    def item(self, i_index: cat_variant) -> Sketch:
        return Sketch(self.sketches.Item(i_index))

    def __getitem__(self, n: int) -> Sketch:
        if (n + 1) > self.count:
            raise StopIteration
        return Sketch(self.sketches.item(n + 1))

    def __iter__(self) -> Iterator[Sketch]:
        for i in range(self.count):
            yield self.child_object(self.com_object.item(i + 1))

    def __repr__(self):
        return f'Sketches(name="{self.name}")'
