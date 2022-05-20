from typing import Iterator
from pytia.framework.exception_handling.exceptions import CATIAApplicationException
from pytia.framework.mec_mod_interfaces.hybrid_body import HybridBody
from pytia.framework.system_interfaces.collection import Collection
from pytia.framework.cat_types.general import cat_variant


class HybridBodies(Collection):
    def __init__(self, com_object, child_object=HybridBody):
        super().__init__(com_object, child_object=HybridBody)
        self.hybrid_bodies = com_object
        self.child_object = child_object

    def add(self) -> HybridBody:
        return HybridBody(self.hybrid_bodies.Add())

    def item(self, i_index: cat_variant) -> HybridBody:
        try:
            return HybridBody(self.hybrid_bodies.Item(i_index))
        except Exception as e:
            raise CATIAApplicationException(f'Could not find hybrid_body "i_index"')

    def __getitem__(self, n: int) -> HybridBody:
        if (n + 1) > self.count:
            raise StopIteration
        return HybridBody(self.hybrid_bodies.item(n + 1))

    def __iter__(self) -> Iterator[HybridBody]:
        for i in range(self.count):
            yield self.child_object(self.com_object.item(i + 1))

    def __repr__(self):
        return f'HybridBodies(name="{self.name}")'
