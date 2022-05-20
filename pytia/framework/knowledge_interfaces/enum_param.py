from pytia.framework.knowledge_interfaces.parameter import Parameter


class EnumParam(Parameter):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.enum_param = com_object

    @property
    def value_enum(self) -> str:
        return self.enum_param.ValueEnum

    @value_enum.setter
    def value_enum(self, value: str):
        self.enum_param.ValueEnum = value

    def __repr__(self):
        return f'EnumParam(name="{ self.name }")'
