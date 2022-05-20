from typing import Iterator
from pytia.framework.system_interfaces.any_object import AnyObject
from pytia.framework.system_interfaces.collection import Collection
from pytia.framework.tps_interfaces.annotation import Annotation
from pytia.framework.cat_types.general import cat_variant


class Annotations(Collection):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.annotations = com_object
        self.child_object = Annotation

    def add(self, i_annot: Annotation) -> None:
        return self.annotations.Add(i_annot.com_object)

    def item(self, i_index: cat_variant) -> Annotation:
        return Annotation(self.annotations.Item(i_index))

    def item2(self, i_index: cat_variant) -> AnyObject:
        return AnyObject(self.annotations.Item2(i_index))

    def __getitem__(self, n: int) -> Annotation:
        if (n + 1) > self.count:
            raise StopIteration
        return Annotation(self.annotations.item(n + 1))

    def __iter__(self) -> Iterator[Annotation]:
        for i in range(self.count):
            yield self.child_object(self.com_object.item(i + 1))

    def __repr__(self):
        return f'Annotations(name="{self.name}")'
