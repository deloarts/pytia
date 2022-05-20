from pytia.framework.system_interfaces.any_object import AnyObject


class KnowledgeObject(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.knowledge_object = com_object

    @property
    def hidden(self) -> bool:
        return self.knowledge_object.Hidden

    @hidden.setter
    def hidden(self, value: bool):
        self.knowledge_object.Hidden = value

    @property
    def is_const(self) -> bool:
        return self.knowledge_object.IsConst

    @is_const.setter
    def is_const(self, value: bool):
        self.knowledge_object.IsConst = value

    def __repr__(self):
        return f'KnowledgeObject(name="{ self.name }")'
