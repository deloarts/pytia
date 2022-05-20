from pytia.framework.knowledge_interfaces.length import Length
from pytia.framework.part_interfaces.repartition import Repartition


class LinearRepartition(Repartition):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.linear_repartition = com_object

    @property
    def spacing(self) -> Length:
        return Length(self.linear_repartition.Spacing)

    def __repr__(self):
        return f'LinearRepartition(name="{ self.name }")'
