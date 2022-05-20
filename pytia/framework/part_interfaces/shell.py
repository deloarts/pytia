from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.in_interfaces.references import References
from pytia.framework.knowledge_interfaces.length import Length
from pytia.framework.part_interfaces.dress_up_shape import DressUpShape


class Shell(DressUpShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.shell = com_object

    @property
    def external_thickness(self) -> Length:
        return Length(self.shell.ExternalThickness)

    @property
    def faces_to_remove(self) -> References:
        return References(self.shell.FacesToRemove)

    @property
    def internal_thickness(self) -> Length:
        return Length(self.shell.InternalThickness)

    def add_face_to_remove(self, i_face_to_remove: Reference) -> None:
        return self.shell.AddFaceToRemove(i_face_to_remove.com_object)

    def add_face_with_different_thickness(self, i_face_to_thicken: Reference) -> None:
        return self.shell.AddFaceWithDifferentThickness(i_face_to_thicken.com_object)

    def remove_face_with_different_thickness(self, i_face_to_remove: Reference) -> None:
        return self.shell.RemoveFaceWithDifferentThickness(i_face_to_remove.com_object)

    def set_volume_support(self, i_volume_support: Reference) -> None:
        return self.shell.SetVolumeSupport(i_volume_support.com_object)

    def withdraw_face_to_remove(self, i_face_to_withdraw: Reference) -> None:
        return self.shell.WithdrawFaceToRemove(i_face_to_withdraw.com_object)

    def __repr__(self):
        return f'Shell(name="{self.name}")'
