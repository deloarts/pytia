from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.in_interfaces.references import References
from pytia.framework.knowledge_interfaces.length import Length
from pytia.framework.part_interfaces.dress_up_shape import DressUpShape


class Thickness(DressUpShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.thickness = com_object

    @property
    def faces_to_thicken(self) -> References:
        return References(self.thickness.FacesToThicken)

    @property
    def offset(self) -> Length:
        return Length(self.thickness.Offset)

    def add_face_to_thicken(self, i_face_to_thicken: Reference) -> None:
        return self.thickness.AddFaceToThicken(i_face_to_thicken.com_object)

    def add_face_with_different_thickness(self, i_face_to_thicken: Reference) -> None:
        return self.thickness.AddFaceWithDifferentThickness(
            i_face_to_thicken.com_object
        )

    def remove_face_with_different_thickness(self, i_face_to_remove: Reference) -> None:
        return self.thickness.RemoveFaceWithDifferentThickness(
            i_face_to_remove.com_object
        )

    def set_volume_support(self, i_volume_support: Reference) -> None:
        return self.thickness.SetVolumeSupport(i_volume_support.com_object)

    def withdraw_face_to_thicken(self, i_face_to_withdraw: Reference) -> None:
        return self.thickness.WithdrawFaceToThicken(i_face_to_withdraw.com_object)

    def __repr__(self):
        return f'Thickness(name="{self.name}")'
