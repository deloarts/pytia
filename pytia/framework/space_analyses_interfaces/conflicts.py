from typing import Iterator
from pytia.framework.space_analyses_interfaces.conflict import Conflict
from pytia.framework.system_interfaces.collection import Collection
from pytia.framework.cat_types.general import cat_variant


class Conflicts(Collection):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.conflicts = com_object

    def item(self, i_index: cat_variant) -> Conflict:
        return Conflict(self.conflicts.Item(i_index))

    def __getitem__(self, n: int) -> Conflict:
        if (n + 1) > self.count:
            raise StopIteration
        return Conflict(self.conflicts.item(n + 1))

    def __iter__(self) -> Iterator[Conflict]:
        for i in range(self.count):
            yield self.child_object(self.com_object.item(i + 1))

    def __repr__(self):
        return f'Conflicts(name="{self.name}")'
