from typing import TYPE_CHECKING, Iterator

from pytia.framework.cat_types.general import cat_variant
from pytia.framework.knowledge_interfaces.bool_param import BoolParam
from pytia.framework.knowledge_interfaces.dimension import Dimension
from pytia.framework.knowledge_interfaces.int_param import IntParam
from pytia.framework.knowledge_interfaces.list_parameter import ListParameter
from pytia.framework.knowledge_interfaces.parameter import Parameter
from pytia.framework.knowledge_interfaces.real_param import RealParam
from pytia.framework.knowledge_interfaces.str_param import StrParam
from pytia.framework.knowledge_interfaces.units import Units
from pytia.framework.system_interfaces.any_object import AnyObject
from pytia.framework.system_interfaces.collection import Collection

if TYPE_CHECKING:
    from pytia.framework.knowledge_interfaces.parameter_set import ParameterSet


class Parameters(Collection):
    def __init__(self, com_object):
        super().__init__(com_object, child_object=Parameter)
        self.parameters = com_object

    @property
    def root_parameter_set(self) -> "ParameterSet":
        from pytia.framework.knowledge_interfaces.parameter_set import ParameterSet

        return ParameterSet(self.parameters.RootParameterSet)

    @property
    def units(self) -> Units:
        return Units(self.parameters.Units)

    def create_boolean(self, i_name: str, i_value: bool):
        return BoolParam(self.parameters.CreateBoolean(i_name, i_value))

    def create_dimension(
        self, i_name: str, i_magnitude: str, i_value: float
    ) -> Dimension:
        return Dimension(self.parameters.CreateDimension(i_name, i_magnitude, i_value))

    def create_integer(self, i_name: str, i_value: int) -> IntParam:
        return IntParam(self.parameters.CreateInteger(i_name, i_value))

    def create_list(self, i_name: str) -> ListParameter:
        return ListParameter(self.parameters.CreateList(i_name))

    def create_real(self, i_name: str, i_value: float) -> RealParam:
        return RealParam(self.parameters.CreateReal(i_name, i_value))

    def create_set_of_parameters(self, i_father: AnyObject) -> None:
        return self.parameters.CreateSetOfParameters(i_father.com_object)

    def create_string(self, i_name: str, i_value: str) -> StrParam:
        return StrParam(self.parameters.CreateString(i_name, i_value))

    def get_name_to_use_in_relation(self, i_object: AnyObject) -> str:
        return self.parameters.GetNameToUseInRelation(i_object.com_object)

    def item(self, index: cat_variant) -> Parameter:
        return self.parameters.Item(index)

    def remove(self, i_index: cat_variant) -> None:
        return self.parameters.Remove(i_index)

    def sub_list(self, i_object: AnyObject, i_recursively: bool) -> "Parameters":
        return Parameters(self.parameters.SubList(i_object.com_object, i_recursively))

    def __getitem__(self, n: int) -> Parameter:
        if (n + 1) > self.count:
            raise StopIteration
        return Parameter(self.parameters.item(n + 1))

    def __iter__(self) -> Iterator[Parameter]:
        for i in range(self.count):
            yield self.child_object(self.com_object.item(i + 1))

    def __repr__(self):
        return f'Parameters(name="{self.name}")'
