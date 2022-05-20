from typing import Iterator
from pytia.framework.in_interfaces.printer import Printer
from pytia.framework.system_interfaces.collection import Collection
from pytia.framework.cat_types.general import cat_variant


class Printers(Collection):
    def __init__(self, com_object):
        super().__init__(com_object, child_object=Printer)
        self.printers = com_object

    def item(self, i_index: cat_variant) -> Printer:
        return Printer(self.printers.Item(i_index))

    def __getitem__(self, n: int) -> Printer:
        if (n + 1) > self.count:
            raise StopIteration
        return Printer(self.printers.item(n + 1))

    def __iter__(self) -> Iterator[Printer]:
        for i in range(self.count):
            yield self.child_object(self.com_object.item(i + 1))

    def __repr__(self):
        return f'Printers(name="{self.name}")'
