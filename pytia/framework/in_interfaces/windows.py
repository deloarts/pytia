from typing import Iterator
from pytia.framework.in_interfaces.window import Window
from pytia.framework.system_interfaces.collection import Collection
from pytia.framework.cat_types.general import cat_variant


class Windows(Collection):
    def __init__(self, com_object):
        super().__init__(com_object, child_object=Window)
        self.windows = com_object

    def arrange(self, i_style: int) -> None:
        return self.windows.Arrange(i_style)

    def item(self, i_index: cat_variant) -> Window:
        return Window(self.windows.Item(i_index))

    def __getitem__(self, n: int) -> Window:
        if (n + 1) > self.count:
            raise StopIteration
        return Window(self.windows.item(n + 1))

    def __iter__(self) -> Iterator[Window]:
        for i in range(self.count):
            yield self.child_object(self.com_object.item(i + 1))

    def __repr__(self):
        return f'Windows(name="{self.name}")'
