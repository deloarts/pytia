from pytia.framework.system_interfaces.any_object import AnyObject


class CompositeTolerance(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.composite_tolerance = com_object

    @property
    def box_count(self) -> float:
        return self.composite_tolerance.BoxCount

    @property
    def value(self) -> float:
        return self.composite_tolerance.Value

    def __repr__(self):
        return f'CompositeTolerance(name="{ self.name }")'
