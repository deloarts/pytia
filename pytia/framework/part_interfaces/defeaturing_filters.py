from typing import Iterator
from pytia.framework.part_interfaces.defeaturing_filter import DefeaturingFilter
from pytia.framework.system_interfaces.collection import Collection
from pytia.framework.cat_types.general import cat_variant


class DefeaturingFilters(Collection):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.defeaturing_filters = com_object

    def add(self, i_filter_type_to_add: str) -> int:
        return self.defeaturing_filters.Add(i_filter_type_to_add)

    def item(self, i_filter_id: cat_variant) -> DefeaturingFilter:
        return DefeaturingFilter(self.defeaturing_filters.Item(i_filter_id))

    def remove(self, i_filter_id: cat_variant) -> None:
        return self.defeaturing_filters.Remove(i_filter_id)

    def __getitem__(self, n: int) -> DefeaturingFilter:
        if (n + 1) > self.count:
            raise StopIteration
        return DefeaturingFilter(self.defeaturing_filters.item(n + 1))

    def __iter__(self) -> Iterator[DefeaturingFilter]:
        for i in range(self.count):
            yield self.child_object(self.com_object.item(i + 1))

    def __repr__(self):
        return f'DefeaturingFilters(name="{self.name}")'
