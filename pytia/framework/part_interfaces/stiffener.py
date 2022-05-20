from pytia.framework.knowledge_interfaces.length import Length
from pytia.framework.part_interfaces.sketch_based_shape import SketchBasedShape


class Stiffener(SketchBasedShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.stiffener = com_object

    @property
    def is_from_top(self) -> bool:
        return self.stiffener.IsFromTop

    @is_from_top.setter
    def is_from_top(self, value: bool):
        self.stiffener.IsFromTop = value

    @property
    def is_symmetric(self) -> bool:
        return self.stiffener.IsSymmetric

    @is_symmetric.setter
    def is_symmetric(self, value: bool):
        self.stiffener.IsSymmetric = value

    @property
    def thickness(self) -> Length:
        return Length(self.stiffener.Thickness)

    @property
    def thickness_from_top(self) -> Length:
        return Length(self.stiffener.ThicknessFromTop)

    def reverse_depth(self) -> None:
        return self.stiffener.ReverseDepth()

    def reverse_thickness(self) -> None:
        return self.stiffener.ReverseThickness()

    def __repr__(self):
        return f'Stiffener(name="{ self.name }")'
