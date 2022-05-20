from pytia.framework.system_interfaces.any_object import AnyObject


class FreeState(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.free_state = com_object

    @property
    def modifier(self) -> str:
        return self.free_state.Modifier

    @modifier.setter
    def modifier(self, value: str):
        self.free_state.Modifier = value

    def __repr__(self):
        return f'FreeState(name="{ self.name }")'
