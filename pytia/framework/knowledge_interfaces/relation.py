from typing import TYPE_CHECKING
from pytia.framework.knowledge_interfaces.knowledge_activate_object import (
    KnowledgeActivateObject,
)
from pytia.framework.system_interfaces.any_object import AnyObject

if TYPE_CHECKING:
    from pytia.framework.knowledge_interfaces.parameter import Parameter


class Relation(KnowledgeActivateObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.relation = com_object

    @property
    def comment(self) -> str:
        return self.relation.Comment

    @comment.setter
    def comment(self, value: str):
        self.relation.Comment = value

    @property
    def context(self) -> AnyObject:
        return AnyObject(self.relation.Context)

    @property
    def nb_in_parameters(self) -> int:
        return self.relation.NbInParameters

    @property
    def nb_out_parameters(self) -> int:
        return self.relation.NbOutParameters

    @property
    def value(self) -> str:
        return self.relation.Value

    def get_in_parameter(self, i_index: int) -> AnyObject:
        return AnyObject(self.relation.GetInParameter(i_index))

    def get_out_parameter(self, i_index: int) -> "Parameter":
        from pytia.framework.knowledge_interfaces.parameter import Parameter

        return Parameter(self.relation.GetOutParameter(i_index))

    def modify(self, i_value: str) -> None:
        return self.relation.Modify(i_value)

    def rename(self, i_name: str) -> None:
        return self.relation.Rename(i_name)

    def __repr__(self):
        return f'Relation(name="{self.name}")'
