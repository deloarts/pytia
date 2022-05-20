from pytia.framework.system_interfaces.any_object import AnyObject


class DimensionPattern(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.dimension_pattern = com_object

    @property
    def instance_count(self) -> float:
        return self.dimension_pattern.InstanceCount

    def __repr__(self):
        return f'DimensionPattern(name="{ self.name }")'
