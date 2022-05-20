from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.part_interfaces.transformation_shape import TransformationShape
from pytia.framework.system_interfaces.any_object import AnyObject


class Mirror(TransformationShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.mirror = com_object

    @property
    def mirroring_object(self) -> AnyObject:
        return AnyObject(self.mirror.MirroringObject)

    @property
    def mirroring_plane(self) -> Reference:
        return Reference(self.mirror.MirroringPlane)

    @mirroring_plane.setter
    def mirroring_plane(self, value: Reference):
        self.mirror.MirroringPlane = value

    def __repr__(self):
        return f'Mirror(name="{ self.name }")'
