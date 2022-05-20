from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.in_interfaces.references import References
from pytia.framework.part_interfaces.dress_up_shape import DressUpShape


class AutoDraft(DressUpShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.auto_draft = com_object

    @property
    def functional_face(self) -> None:
        return None

    @functional_face.setter
    def functional_face(self, reference: Reference):
        self.auto_draft.FunctionalFace = reference

    @property
    def functional_faces(self) -> References:
        return References(self.auto_draft.FunctionalFaces)

    @property
    def main_draft_angle(self) -> Reference:
        return Reference(self.auto_draft.MainDraftAngle)

    @main_draft_angle.setter
    def main_draft_angle(self, value: Reference):
        self.auto_draft.MainDraftAngle = value

    @property
    def mode(self) -> Reference:
        return Reference(self.auto_draft.Mode)

    @mode.setter
    def mode(self, value: Reference):
        self.auto_draft.Mode = value

    @property
    def parting_element(self) -> Reference:
        return Reference(self.auto_draft.PartingElement)

    @parting_element.setter
    def parting_element(self, value: Reference):
        self.auto_draft.PartingElement = value

    @property
    def pulling_direction(self) -> Reference:
        return Reference(self.auto_draft.PullingDirection)

    @pulling_direction.setter
    def pulling_direction(self, value: Reference):
        self.auto_draft.PullingDirection = value

    def __repr__(self):
        return f'AutoDraft(name="{self.name}")'
