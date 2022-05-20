from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.in_interfaces.references import References
from pytia.framework.part_interfaces.dress_up_shape import DressUpShape


class RemoveFace(DressUpShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.remove_face = com_object

    @property
    def keep_face(self):
        return self.remove_face.KeepFace

    @keep_face.setter
    def keep_face(self, reference_face: Reference):
        self.remove_face.KeepFace = reference_face.com_object

    @property
    def keep_faces(self) -> References:
        return References(self.remove_face.KeepFaces)

    @property
    def propagation(self) -> References:
        return References(self.remove_face.Propagation)

    @property
    def remove_face(self):
        return self.remove_face.RemoveFace

    @remove_face.setter
    def remove_face(self, reference_face: Reference):
        self.remove_face.RemoveFace = reference_face.com_object

    @property
    def remove_faces(self) -> References:
        return References(self.remove_face.RemoveFaces)

    def remove_keep_face(self, i_keep_face: Reference) -> None:
        return self.remove_face.remove_KeepFace(i_keep_face.com_object)

    def remove_remove_face(self, i_remove_face: Reference) -> None:
        return self.remove_face.remove_RemoveFace(i_remove_face.com_object)

    def __repr__(self):
        return f'RemoveFace(name="{self.name}")'
