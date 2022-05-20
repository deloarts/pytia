from pytia.framework.knowledge_interfaces.int_param import IntParam
from pytia.framework.system_interfaces.any_object import AnyObject


class Repartition(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.repartition = com_object

    @property
    def instances_count(self) -> IntParam:
        return IntParam(self.repartition.InstancesCount)

    def __repr__(self):
        return f'Repartition(name="{ self.name }")'
