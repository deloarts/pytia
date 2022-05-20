from typing import Iterator
from pytia.framework.mec_mod_interfaces.body import Body
from pytia.framework.system_interfaces.collection import Collection
from pytia.framework.cat_types.general import cat_variant


class Bodies(Collection):
    def __init__(self, collection_com_object):
        super().__init__(collection_com_object, child_object=Body)
        self.bodies = collection_com_object

    def add(self) -> Body:
        return Body(self.bodies.Add())

    def item(self, i_index: cat_variant) -> Body:
        return Body(self.bodies.Item(i_index))

    def __getitem__(self, n: int) -> Body:
        if (n + 1) > self.count:
            raise StopIteration
        return Body(self.bodies.item(n + 1))

    def __iter__(self) -> Iterator[Body]:
        for i in range(self.count):
            yield self.child_object(self.com_object.item(i + 1))

    def __repr__(self):
        return f'Bodies(name="{self.name}")'
