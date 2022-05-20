from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.knowledge_interfaces.length import Length
from pytia.framework.system_interfaces.any_object import AnyObject


class Limit(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.limit = com_object

    @property
    def dimension(self) -> Length:
        return Length(self.limit.Dimension)

    @property
    def limit_mode(self) -> int:
        return self.limit.LimitMode

    @limit_mode.setter
    def limit_mode(self, value: int):
        self.limit.LimitMode = value

    @property
    def limiting_element(self) -> Reference:
        return Reference(self.limit.LimitingElement)

    @limiting_element.setter
    def limiting_element(self, value: Reference):
        self.limit.LimitingElement = value

    def __repr__(self):
        return f'Limit(name="{ self.name }")'
