from typing import Iterator
from pytia.framework.mec_mod_interfaces.fix_together import FixTogether
from pytia.framework.system_interfaces.collection import Collection
from pytia.framework.cat_types.general import cat_variant


class FixTogethers(Collection):
    def __init__(self, com_object):
        super().__init__(com_object, child_object=FixTogether)
        self.fix_togethers = com_object

    def add(self) -> FixTogether:
        return FixTogether(self.fix_togethers.Add())

    def item(self, i_index: cat_variant) -> FixTogether:
        return FixTogether(self.fix_togethers.Item(i_index))

    def remove(self, i_index: cat_variant) -> None:
        return self.fix_togethers.Remove(i_index)

    def __getitem__(self, n: int) -> FixTogether:
        if (n + 1) > self.count:
            raise StopIteration
        return FixTogether(self.fix_togethers.item(n + 1))

    def __iter__(self) -> Iterator[FixTogether]:
        for i in range(self.count):
            yield self.child_object(self.com_object.item(i + 1))

    def __repr__(self):
        return f'FixTogethers(name="{self.name}")'
