from typing import Iterator
from pytia.framework.space_analyses_interfaces.clash_result import ClashResult
from pytia.framework.system_interfaces.collection import Collection
from pytia.framework.cat_types.general import cat_variant


class ClashResults(Collection):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.clash_results = com_object

    def add_from_xml(self, i_path: str, i_type: int) -> ClashResult:
        return ClashResult(self.clash_results.AddFromXML(i_path, i_type))

    def item(self, i_index: cat_variant) -> ClashResult:
        return ClashResult(self.clash_results.Item(i_index))

    def remove(self, i_index: cat_variant) -> None:
        return self.clash_results.Remove(i_index)

    def __getitem__(self, n: int) -> ClashResult:
        if (n + 1) > self.count:
            raise StopIteration
        return ClashResult(self.clash_results.item(n + 1))

    def __iter__(self) -> Iterator[ClashResult]:
        for i in range(self.count):
            yield self.child_object(self.com_object.item(i + 1))

    def __repr__(self):
        return f'ClashResults(name="{self.name}")'
