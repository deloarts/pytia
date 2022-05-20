from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.part_interfaces.sketch_based_shape import SketchBasedShape


class SolidCombine(SketchBasedShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.solid_combine = com_object

    @property
    def first_component_direction(self) -> Reference:
        return Reference(self.solid_combine.FirstComponentDirection)

    @first_component_direction.setter
    def first_component_direction(self, value: Reference):
        self.solid_combine.FirstComponentDirection = value

    @property
    def first_component_profile(self) -> Reference:
        return Reference(self.solid_combine.FirstComponentProfile)

    @first_component_profile.setter
    def first_component_profile(self, value: Reference):
        self.solid_combine.FirstComponentProfile = value

    @property
    def second_component_direction(self) -> Reference:
        return Reference(self.solid_combine.SecondComponentDirection)

    @second_component_direction.setter
    def second_component_direction(self, value: Reference):
        self.solid_combine.SecondComponentDirection = value

    @property
    def second_component_profile(self) -> Reference:
        return Reference(self.solid_combine.SecondComponentProfile)

    @second_component_profile.setter
    def second_component_profile(self, value: Reference):
        self.solid_combine.SecondComponentProfile = value

    def __repr__(self):
        return f'SolidCombine(name="{ self.name }")'
