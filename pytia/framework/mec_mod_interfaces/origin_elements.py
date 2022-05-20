from pytia.framework.system_interfaces.any_object import AnyObject


class OriginElements(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.origin_elements = com_object

    @property
    def plane_xy(self) -> AnyObject:
        return AnyObject(self.origin_elements.PlaneXY)

    @property
    def plane_yz(self) -> AnyObject:
        return AnyObject(self.origin_elements.PlaneYZ)

    @property
    def plane_zx(self) -> AnyObject:
        return AnyObject(self.origin_elements.PlaneZX)

    def __repr__(self):
        return f'OriginElements(name="{ self.name }")'
