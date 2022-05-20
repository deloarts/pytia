from typing import Iterator
from pytia.framework.system_interfaces.any_object import AnyObject
from pytia.framework.system_interfaces.collection import Collection
from pytia.framework.tps_interfaces.annotation_set import AnnotationSet
from pytia.framework.cat_types.general import cat_variant


class AssemblyAnnotationSets(Collection):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.assembly_annotation_sets = com_object

    def item(self, i_index: cat_variant) -> AnyObject:
        return AnyObject(self.assembly_annotation_sets.Item(i_index))

    def load_annotation_sets_list(self) -> None:
        return self.assembly_annotation_sets.LoadAnnotationSetsList()

    def __getitem__(self, n: int) -> AnnotationSet:
        if (n + 1) > self.count:
            raise StopIteration
        return AnnotationSet(self.assembly_annotation_sets.item(n + 1))

    def __iter__(self) -> Iterator[AnnotationSet]:
        for i in range(self.count):
            yield self.child_object(self.com_object.item(i + 1))

    def __repr__(self):
        return f'AssemblyAnnotationSets(name="{self.name}")'
