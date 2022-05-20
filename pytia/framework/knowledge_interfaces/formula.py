from pytia.framework.knowledge_interfaces.relation import Relation


class Formula(Relation):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.formula = com_object

    def __repr__(self):
        return f'Formula(name="{ self.name }")'
