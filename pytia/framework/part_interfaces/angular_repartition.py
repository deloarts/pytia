from pytia.framework.knowledge_interfaces.angle import Angle
from pytia.framework.part_interfaces.repartition import Repartition


class AngularRepartition(Repartition):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.angular_repartition = com_object

    @property
    def angular_spacing(self) -> Angle:
        return Angle(self.angular_repartition.AngularSpacing)

    @property
    def instance_spacing(self) -> Angle:
        return Angle(self.angular_repartition.InstanceSpacing)

    def __repr__(self):
        return f'AngularRepartition(name="{ self.name }")'
