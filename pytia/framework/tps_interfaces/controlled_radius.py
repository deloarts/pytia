from pytia.framework.system_interfaces.any_object import AnyObject


class ControlledRadius(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.controlled_radius = com_object

    @property
    def modifier(self) -> str:
        return self.controlled_radius.Modifier

    def __repr__(self):
        return f'ControlledRadius(name="{self.name}")'
