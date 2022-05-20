from typing import Iterator
from pytia.framework.product_structure_interfaces.product import Product
from pytia.framework.system_interfaces.any_object import AnyObject
from pytia.framework.system_interfaces.collection import Collection
from pytia.framework.tps_interfaces.annotation_set import AnnotationSet
from pytia.framework.cat_types.general import cat_variant


class AnnotationSets(Collection):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.annotation_sets = com_object
        self.child_object = AnnotationSet

    def add_in_a_product(self, i_product: Product, i_standard: str) -> AnnotationSet:
        return AnnotationSet(
            self.annotation_sets.AddInAProduct(i_product.com_object, i_standard)
        )

    def item(self, i_index: cat_variant) -> AnnotationSet:
        return AnnotationSet(self.annotation_sets.Item(i_index))

    def load_annotation_sets_list(self) -> None:
        return self.annotation_sets.LoadAnnotationSetsList()

    def __getitem__(self, n: int) -> AnnotationSet:
        if (n + 1) > self.count:
            raise StopIteration
        return AnnotationSet(self.annotation_sets.item(n + 1))

    def __iter__(self) -> Iterator[AnnotationSet]:
        for i in range(self.count):
            yield self.child_object(self.com_object.item(i + 1))

    def __repr__(self):
        return f'AnnotationSets(name="{self.name}")'
