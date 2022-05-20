from pytia.framework.knowledge_interfaces.relation import Relation


class Check(Relation):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.check = com_object

    @property
    def diagnosis(self) -> bool:
        return self.check.Diagnosis

    @property
    def severity(self) -> int:
        return self.check.Severity

    @severity.setter
    def severity(self, value: int):
        self.check.Severity = value

    def __repr__(self):
        return f'Check(name="{ self.name }")'
