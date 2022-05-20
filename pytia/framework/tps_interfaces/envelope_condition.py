from pytia.framework.system_interfaces.any_object import AnyObject


class EnvelopeCondition(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.envelope_condition = com_object

    @property
    def modifier(self) -> str:
        return self.envelope_condition.Modifier

    def __repr__(self):
        return f'EnvelopCondition(name="{self.name}")'
