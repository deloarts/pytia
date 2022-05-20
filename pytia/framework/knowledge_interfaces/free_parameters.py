from typing import Iterator
from typing import TYPE_CHECKING
from pytia.framework.knowledge_interfaces.free_parameter import FreeParameter
from pytia.framework.system_interfaces.collection import Collection
from pytia.framework.cat_types.general import cat_variant

if TYPE_CHECKING:
    from pytia.framework.knowledge_interfaces.real_param import RealParam


class FreeParameters(Collection):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.free_parameters = com_object

    def add_free_parameter(self, parameter: "RealParam") -> FreeParameter:
        return FreeParameter(
            self.free_parameters.AddFreeParameter(parameter.com_object)
        )

    def item(self, i_index: cat_variant) -> FreeParameter:
        return FreeParameter(self.free_parameters.Item(i_index))

    def remove_free_parameter(self, i_index: cat_variant) -> None:
        return self.free_parameters.RemoveFreeParameter(i_index)

    def __getitem__(self, n: int) -> FreeParameter:
        if (n + 1) > self.count:
            raise StopIteration
        return FreeParameter(self.free_parameters.item(n + 1))

    def __iter__(self) -> Iterator[FreeParameter]:
        for i in range(self.count):
            yield self.child_object(self.com_object.item(i + 1))

    def __repr__(self):
        return f'FreeParameters(name="{self.name}")'
