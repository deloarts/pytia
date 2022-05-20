from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.knowledge_interfaces.real_param import RealParam
from pytia.framework.part_interfaces.dress_up_shape import DressUpShape


class Scaling(DressUpShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.scaling = com_object

    @property
    def factor(self) -> RealParam:
        return RealParam(self.scaling.Factor)

    @property
    def scaling_reference(self) -> Reference:
        return Reference(self.scaling.ScalingReference)

    @scaling_reference.setter
    def scaling_reference(self, value: Reference):
        self.scaling.ScalingReference = value

    def __repr__(self):
        return f'Scaling(name="{ self.name }")'
