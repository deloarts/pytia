from pytia.framework.part_interfaces.defeaturing_filter_with_range import (
    DefeaturingFilterWithRange,
)


class DefeaturingFilletFilter(DefeaturingFilterWithRange):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.defeaturing_fillet_filter = com_object

    def __repr__(self):
        return f'DefeaturingFilletFilter(name="{self.name}")'
