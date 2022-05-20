from pytia.framework.system_interfaces.any_object import AnyObject


class GeometricElement(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.geometric_element = com_object

    @property
    def geometric_type(self) -> int:
        return self.geometric_element.GeometricType

    def __repr__(self):
        return f'GeometricElement(name="{ self.name }")'
