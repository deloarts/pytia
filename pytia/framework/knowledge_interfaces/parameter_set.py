from typing import TYPE_CHECKING
from pytia.framework.knowledge_interfaces.parameters import Parameters
from pytia.framework.system_interfaces.any_object import AnyObject

if TYPE_CHECKING:
    from pytia.framework.knowledge_interfaces.parameter_sets import ParameterSets


class ParameterSet(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.parameter_set = com_object

    @property
    def all_parameters(self) -> list:
        from .parameter import Parameter

        items = []
        for i in range(0, self.parameter_set.AllParameters.Count):
            items.append(Parameter(self.parameter_set.AllParameters.Item(i + 1)))
        return items

    @property
    def direct_parameters(self) -> Parameters:
        return Parameters(self.parameter_set.DirectParameters)

    @property
    def parameter_sets(self) -> "ParameterSets":
        from pytia.framework.knowledge_interfaces.parameter_sets import ParameterSets

        return ParameterSets(self.parameter_set.ParameterSets)

    def __repr__(self):
        return f'ParameterSet(name="{self.name}")'
