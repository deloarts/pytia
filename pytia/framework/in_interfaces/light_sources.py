from typing import Iterator
from pytia.framework.in_interfaces.light_source import LightSource
from pytia.framework.system_interfaces.collection import Collection


class LightSources(Collection):
    def __init__(self, com_object):
        super().__init__(com_object, child_object=LightSource)
        self.light_sources = com_object

    def add(self) -> LightSource:
        return LightSource(self.light_sources.Add())

    def item(self, i_index: int) -> LightSource:
        return LightSource(self.light_sources.Item(i_index))

    def remove(self, i_index: int) -> None:
        return self.light_sources.Remove(i_index)

    def __getitem__(self, n: int) -> LightSource:
        if (n + 1) > self.count:
            raise StopIteration
        return LightSource(self.light_sources.item(n + 1))

    def __iter__(self) -> Iterator[LightSource]:
        for i in range(self.count):
            yield self.child_object(self.com_object.item(i + 1))

    def __repr__(self):
        return f'LightSources(name="{self.name}")'
