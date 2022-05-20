from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.in_interfaces.references import References
from pytia.framework.part_interfaces.surface_based_shape import SurfaceBasedShape


class ReplaceFace(SurfaceBasedShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.replace_face = com_object

    @property
    def remove_face(self) -> References:
        return References(self.replace_face.RemoveFace)

    @property
    def splitting_side(self) -> int:
        return self.replace_face.SplittingSide

    @splitting_side.setter
    def splitting_side(self, value: int):
        self.replace_face.SplittingSide = value

    def add_remove_face(self, i_remove_face: Reference) -> None:
        return self.replace_face.AddRemoveFace(i_remove_face.com_object)

    def add_split_plane(self, i_split_plane: Reference) -> None:
        return self.replace_face.AddSplitPlane(i_split_plane.com_object)

    def delete_remove_face(self, i_remove_face: Reference) -> None:
        return self.replace_face.DeleteRemoveFace(i_remove_face.com_object)

    def __repr__(self):
        return f'ReplaceFace(name="{self.name}")'
