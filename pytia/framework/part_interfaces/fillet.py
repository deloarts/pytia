from pytia.framework.part_interfaces.dress_up_shape import DressUpShape


class Fillet(DressUpShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.fillet = com_object

    @property
    def fillet_boundary_relimitation(self) -> int:
        return self.fillet.FilletBoundaryRelimitation

    @fillet_boundary_relimitation.setter
    def fillet_boundary_relimitation(self, value: int):
        self.fillet.FilletBoundaryRelimitation = value

    @property
    def fillet_trim_support(self) -> int:
        return self.fillet.FilletTrimSupport

    @fillet_trim_support.setter
    def fillet_trim_support(self, value: int):
        self.fillet.FilletTrimSupport = value

    def __repr__(self):
        return f'Fillet(name="{ self.name }")'
