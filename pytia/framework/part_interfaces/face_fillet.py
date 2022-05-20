from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.knowledge_interfaces.length import Length
from pytia.framework.part_interfaces.fillet import Fillet


class FaceFillet(Fillet):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.face_fillet = com_object

    @property
    def first_face(self) -> Reference:
        return Reference(self.face_fillet.FirstFace)

    @first_face.setter
    def first_face(self, value: Reference):
        self.face_fillet.FirstFace = value

    @property
    def radius(self) -> Length:
        return Length(self.face_fillet.Radius)

    @property
    def second_face(self) -> Reference:
        return Reference(self.face_fillet.SecondFace)

    @second_face.setter
    def second_face(self, value: Reference):
        self.face_fillet.SecondFace = value

    def __repr__(self):
        return f'FaceFillet(name="{ self.name }")'
