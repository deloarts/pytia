from pytia.framework.knowledge_interfaces.relation import Relation
from pytia.framework.system_interfaces.any_object import AnyObject


class Parameter(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.parameter = com_object

    @property
    def comment(self) -> str:
        return self.parameter.Comment

    @comment.setter
    def comment(self, value: str):
        self.parameter.Comment = value

    @property
    def context(self) -> AnyObject:
        return AnyObject(self.parameter.Context)

    @property
    def hidden(self) -> bool:
        return self.parameter.Hidden

    @hidden.setter
    def hidden(self, value: bool):
        self.parameter.Hidden = value

    @property
    def is_true_parameter(self) -> bool:
        return self.parameter.IsTrueParameter

    @property
    def optional_relation(self) -> Relation:
        return Relation(self.parameter.OptionalRelation)

    @property
    def read_only(self) -> bool:
        return self.parameter.ReadOnly

    @property
    def renamed(self) -> bool:
        return self.parameter.Renamed

    @property
    def user_access_mode(self) -> int:
        return self.parameter.UserAccessMode

    def rename(self, i_name: str) -> None:
        return self.parameter.Rename(i_name)

    def valuate_from_string(self, i_value: str) -> None:
        return self.parameter.ValuateFromString(i_value)

    def value_as_string(self) -> str:
        return self.parameter.ValueAsString()

    def __repr__(self):
        return f'Parameter(name="{self.name}")'
