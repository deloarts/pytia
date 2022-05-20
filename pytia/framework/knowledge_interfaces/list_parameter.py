from pytia.framework.knowledge_interfaces.list import List
from pytia.framework.knowledge_interfaces.parameter import Parameter


class ListParameter(Parameter):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.list_parameter = com_object

    @property
    def value_list(self) -> List:
        return List(self.list_parameter.ValueList)

    def __repr__(self):
        return f'ListParameter(name="{ self.name }")'
