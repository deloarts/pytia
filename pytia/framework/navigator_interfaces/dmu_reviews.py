from typing import Iterator
from pytia.framework.navigator_interfaces.dmu_review import DMUReview
from pytia.framework.product_structure_interfaces.product import Product
from pytia.framework.system_interfaces.any_object import AnyObject
from pytia.framework.system_interfaces.collection import Collection
from pytia.framework.cat_types.general import cat_variant


class DMUReviews(Collection):
    def __init__(self, com_object):
        super().__init__(com_object, child_object=DMUReview)
        self.dmu_reviews = com_object

    @property
    def current(self) -> AnyObject:
        return AnyObject(self.dmu_reviews.Current)

    def add(self) -> DMUReview:
        return DMUReview(self.dmu_reviews.Add())

    def import_from(self, i_product: Product) -> DMUReview:
        return DMUReview(self.dmu_reviews.ImportFrom(i_product.com_object))

    def item(self, i_index: cat_variant) -> DMUReview:
        return DMUReview(self.dmu_reviews.Item(i_index))

    def remove(self, i_index: cat_variant) -> None:
        return self.dmu_reviews.Remove(i_index)

    def __getitem__(self, n: int) -> DMUReview:
        if (n + 1) > self.count:
            raise StopIteration
        return DMUReview(self.dmu_reviews.item(n + 1))

    def __iter__(self) -> Iterator[DMUReview]:
        for i in range(self.count):
            yield self.child_object(self.com_object.item(i + 1))

    def __repr__(self):
        return f'DmuReviews(name="{self.name}")'
