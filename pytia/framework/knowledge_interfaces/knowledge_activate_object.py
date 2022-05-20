from pytia.framework.knowledge_interfaces.knowledge_object import KnowledgeObject


class KnowledgeActivateObject(KnowledgeObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.knowledge_activate_object = com_object

    @property
    def activated(self) -> bool:
        return self.knowledge_activate_object.Activated

    def activate(self) -> None:
        return self.knowledge_activate_object.Activate()

    def deactivate(self) -> None:
        return self.knowledge_activate_object.Deactivate()

    def __repr__(self):
        return f'KnowledgeActivateObject(name="{ self.name }")'
