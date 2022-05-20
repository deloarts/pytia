from pytia.framework.part_interfaces.surface_based_shape import SurfaceBasedShape


class Split(SurfaceBasedShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.split = com_object

    @property
    def splitting_side(self) -> int:
        return self.split.SplittingSide

    @splitting_side.setter
    def splitting_side(self, value: int):
        self.split.SplittingSide = value

    def __repr__(self):
        return f'Split(name="{ self.name }")'
