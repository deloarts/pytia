from pytia.framework.system_interfaces.any_object import AnyObject


class NonSemanticDatumTarget(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.non_semantic_datum_target = com_object

    @property
    def low_label(self) -> str:
        return self.non_semantic_datum_target.LowLabel

    @low_label.setter
    def low_label(self, value: str):
        self.non_semantic_datum_target.LowLabel = value

    @property
    def type_specifier(self) -> str:
        return self.non_semantic_datum_target.TypeSpecifier

    @type_specifier.setter
    def type_specifier(self, value: str):
        self.non_semantic_datum_target.TypeSpecifier = value

    @property
    def up_label(self) -> str:
        return self.non_semantic_datum_target.UpLabel

    @up_label.setter
    def up_label(self, value: str):
        self.non_semantic_datum_target.UpLabel = value

    def __repr__(self):
        return f'NonSemanticDatumTarget(name="{ self.name }")'
