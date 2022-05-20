from typing import Iterator
from pytia.framework.space_analyses_interfaces.section import Section
from pytia.framework.system_interfaces.collection import Collection
from pytia.framework.cat_types.general import cat_variant


class Sections(Collection):
    def __init__(self, com_object):
        super().__init__(com_object, child_object=Section)
        self.sections = com_object

    def add(self) -> Section:
        return Section(self.sections.Add())

    def add_from_sel(self) -> Section:
        return Section(self.sections.AddFromSel())

    def item(self, i_index: cat_variant) -> Section:
        return Section(self.sections.Item(i_index))

    def remove(self, i_index: cat_variant) -> None:
        return self.sections.Remove(i_index)

    def __getitem__(self, n: int) -> Section:
        if (n + 1) > self.count:
            raise StopIteration
        return Section(self.sections.item(n + 1))

    def __iter__(self) -> Iterator[Section]:
        for i in range(self.count):
            yield self.child_object(self.com_object.item(i + 1))

    def __repr__(self):
        return f'Sections(name="{self.name}")'
