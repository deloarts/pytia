from pytia.framework.part_interfaces.defeaturing_filters import DefeaturingFilters
from pytia.framework.part_interfaces.dress_up_shape import DressUpShape


class Defeaturing(DressUpShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.defeaturing = com_object

    @property
    def filters(self) -> DefeaturingFilters:
        return DefeaturingFilters(self.defeaturing.Filters)

    def __repr__(self):
        return f'Defeaturing(name="{ self.name }")'
