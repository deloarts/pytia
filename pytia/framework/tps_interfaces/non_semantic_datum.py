from pytia.framework.system_interfaces.any_object import AnyObject


class NonSemanticDatum(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.non_semantic_datum = com_object

    @property
    def label(self) -> str:
        return self.non_semantic_datum.Label

    @label.setter
    def label(self, value: str):
        self.non_semantic_datum.Label = value

    def __repr__(self):
        return f'NonSemanticDatum(name="{ self.name }")'
