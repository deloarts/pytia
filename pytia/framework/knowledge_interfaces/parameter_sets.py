from typing import Iterator
from pytia.framework.knowledge_interfaces.parameter_set import ParameterSet
from pytia.framework.system_interfaces.collection import Collection
from pytia.framework.cat_types.general import cat_variant


class ParameterSets(Collection):
    def __init__(self, com_object):
        super().__init__(com_object, child_object=ParameterSet)
        self.parameter_sets = com_object

    def create_set(self, i_name: str) -> ParameterSet:
        return ParameterSet(self.parameter_sets.CreateSet(i_name))

    def item(self, i_index: cat_variant) -> ParameterSet:
        return ParameterSet(self.parameter_sets.Item(i_index))

    def __getitem__(self, n: int) -> ParameterSet:
        if (n + 1) > self.count:
            raise StopIteration
        return ParameterSet(self.parameter_sets.item(n + 1))

    def __iter__(self) -> Iterator[ParameterSet]:
        for i in range(self.count):
            yield self.child_object(self.com_object.item(i + 1))

    def __repr__(self):
        return f'ParameterSets(name="{self.name}")'
