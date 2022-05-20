from pytia.framework.knowledge_interfaces.knowledge_activate_object import (
    KnowledgeActivateObject,
)


class Loop(KnowledgeActivateObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.loop = com_object

    def __repr__(self):
        return f'Loop(name="{ self.name }")'
