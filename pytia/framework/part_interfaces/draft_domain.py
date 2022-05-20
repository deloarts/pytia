from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.in_interfaces.references import References
from pytia.framework.knowledge_interfaces.angle import Angle
from pytia.framework.system_interfaces.any_object import AnyObject


class DraftDomain(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.draft_domain = com_object

    @property
    def draft_angle(self) -> Angle:
        return Angle(self.draft_domain.DraftAngle)

    @property
    def faces_to_draft(self) -> References:
        return References(self.draft_domain.FacesToDraft)

    @property
    def multiselection_mode(self) -> int:
        return self.draft_domain.MultiselectionMode

    @multiselection_mode.setter
    def multiselection_mode(self, value: int):
        self.draft_domain.MultiselectionMode = value

    @property
    def neutral_element(self) -> Reference:
        return Reference(self.draft_domain.NeutralElement)

    @neutral_element.setter
    def neutral_element(self, value: Reference):
        self.draft_domain.NeutralElement = value

    @property
    def neutral_propagation_mode(self) -> int:
        return self.draft_domain.NeutralPropagationMode

    @neutral_propagation_mode.setter
    def neutral_propagation_mode(self, value: int):
        self.draft_domain.NeutralPropagationMode = value

    @property
    def pulling_direction_element(self) -> Reference:
        return Reference(self.draft_domain.PullingDirectionElement)

    @pulling_direction_element.setter
    def pulling_direction_element(self, value: Reference):
        self.draft_domain.PullingDirectionElement = value

    def add_face_to_draft(self, i_face: Reference) -> None:
        return self.draft_domain.AddFaceToDraft(i_face.com_object)

    def get_pulling_direction(self, io_pulling_direction: tuple) -> None:
        return self.draft_domain.GetPullingDirection(io_pulling_direction)

    def remove_face_to_draft(self, i_face: Reference) -> None:
        return self.draft_domain.RemoveFaceToDraft(i_face.com_object)

    def set_pulling_direction(self, i_x: float, i_y: float, i_z: float) -> None:
        return self.draft_domain.SetPullingDirection(i_x, i_y, i_z)

    def set_volume_support(self, i_volume_support: Reference) -> None:
        return self.draft_domain.SetVolumeSupport(i_volume_support.com_object)

    def __repr__(self):
        return f'DraftDomain(name="{ self.name }")'
