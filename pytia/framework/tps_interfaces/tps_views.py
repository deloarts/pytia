from typing import Iterator
from pytia.framework.system_interfaces.any_object import AnyObject
from pytia.framework.system_interfaces.collection import Collection
from pytia.framework.cat_types.general import cat_variant
from pytia.framework.tps_interfaces.tps_view import TPSView


class TPSViews(Collection):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.tps_views = com_object
        child_object = TPSView

    def item(self, i_index: cat_variant) -> TPSView:
        return TPSView(self.tps_views.Item(i_index))

    def __getitem__(self, n: int) -> TPSView:
        if (n + 1) > self.count:
            raise StopIteration
        return TPSView(self.tps_views.item(n + 1))

    def __iter__(self) -> Iterator[TPSView]:
        for i in range(self.count):
            yield self.child_object(self.com_object.item(i + 1))

    def __repr__(self):
        return f'TpsViews(name="{self.name}")'
