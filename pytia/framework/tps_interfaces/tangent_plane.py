from pytia.framework.system_interfaces.any_object import AnyObject


class TangentPlane(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.tangent_plane = com_object

    @property
    def modifier(self) -> str:
        return self.tangent_plane.Modifier

    @modifier.setter
    def modifier(self, value: str):
        self.tangent_plane.Modifier = value

    def __repr__(self):
        return f'TangentPlane(name="{ self.name }")'
