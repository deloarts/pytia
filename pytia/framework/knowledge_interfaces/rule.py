from pytia.framework.knowledge_interfaces.relation import Relation


class Rule(Relation):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.rule = com_object

    def __repr__(self):
        return f'Rule(name="{ self.name }")'
