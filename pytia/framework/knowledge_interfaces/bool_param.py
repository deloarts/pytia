from pytia.framework.knowledge_interfaces.enum_param import EnumParam


class BoolParam(EnumParam):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.bool_param = com_object

    @property
    def value(self) -> bool:
        return self.bool_param.Value

    @value.setter
    def value(self, value: bool):
        self.bool_param.Value = value

    def __repr__(self):
        return f'BoolParam(name="{self.name}")'
