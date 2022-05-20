from pytia.framework.part_interfaces.defeaturing_filter_with_range import (
    DefeaturingFilterWithRange,
)


class DefeaturingHoleFilter(DefeaturingFilterWithRange):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.defeaturing_hole_filter = com_object

    def __repr__(self):
        return f'DefeaturingHoleFilter(name="{self.name}")'
