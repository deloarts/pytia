from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.part_interfaces.fillet import Fillet


class TritangentFillet(Fillet):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.tritangent_fillet = com_object

    @property
    def face_to_remove(self) -> Reference:
        return Reference(self.tritangent_fillet.FaceToRemove)

    @face_to_remove.setter
    def face_to_remove(self, value: Reference):
        self.tritangent_fillet.FaceToRemove = value

    @property
    def first_face(self) -> Reference:
        return Reference(self.tritangent_fillet.FirstFace)

    @first_face.setter
    def first_face(self, value: Reference):
        self.tritangent_fillet.FirstFace = value

    @property
    def second_face(self) -> Reference:
        return Reference(self.tritangent_fillet.SecondFace)

    @second_face.setter
    def second_face(self, value: Reference):
        self.tritangent_fillet.SecondFace = value

    def __repr__(self):
        return f'TritangentFillet(name="{ self.name }")'
