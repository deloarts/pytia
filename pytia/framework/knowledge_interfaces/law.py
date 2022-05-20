from pytia.framework.knowledge_interfaces.relation import Relation


class Law(Relation):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.law = com_object

    def add_formal_parameter(self, i_name: str, i_magnitude: str) -> None:
        return self.law.AddFormalParameter(i_name, i_magnitude)

    def remove_formal_parameter(self, i_name: str) -> None:
        return self.law.RemoveFormalParameter(i_name)

    def __repr__(self):
        return f'Law(name="{ self.name }")'
