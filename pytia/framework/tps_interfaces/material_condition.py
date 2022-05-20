from pytia.framework.system_interfaces.any_object import AnyObject


class MaterialCondition(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.material_condition = com_object

    @property
    def modifier(self) -> str:
        return self.material_condition.Modifier

    def __repr__(self):
        return f'MaterialCondition(name="{ self.name }")'
