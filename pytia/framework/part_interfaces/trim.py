from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.part_interfaces.boolean_shape import BooleanShape


class Trim(BooleanShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.trim = com_object

    def add_face_to_keep(self, i_face_to_keep: Reference) -> None:
        return self.trim.AddFaceToKeep(i_face_to_keep.com_object)

    def add_face_to_keep2(
        self, i_face_to_keep: Reference, i_face_adjacent_for_keep: Reference
    ) -> None:
        return self.trim.AddFaceToKeep2(
            i_face_to_keep.com_object, i_face_adjacent_for_keep.com_object
        )

    def add_face_to_remove(self, i_face_to_remove: Reference) -> None:
        return self.trim.AddFaceToRemove(i_face_to_remove.com_object)

    def add_face_to_remove2(
        self, i_face_to_remove: Reference, i_face_adjacent_for_remove: Reference
    ) -> None:
        return self.trim.AddFaceToRemove2(
            i_face_to_remove.com_object, i_face_adjacent_for_remove.com_object
        )

    def withdraw_face_to_keep(self, i_face_to_withdraw: Reference) -> None:
        return self.trim.WithdrawFaceToKeep(i_face_to_withdraw.com_object)

    def withdraw_face_to_keep2(
        self, i_face_to_withdraw: Reference, i_face_adjacent_for_keep: Reference
    ) -> None:
        return self.trim.WithdrawFaceToKeep2(
            i_face_to_withdraw.com_object, i_face_adjacent_for_keep.com_object
        )

    def withdraw_face_to_remove(self, i_face_to_withdraw: Reference) -> None:
        return self.trim.WithdrawFaceToRemove(i_face_to_withdraw.com_object)

    def withdraw_face_to_remove2(
        self, i_face_to_withdraw: Reference, i_face_adjacent_for_remove: Reference
    ) -> None:
        return self.trim.WithdrawFaceToRemove2(
            i_face_to_withdraw.com_object, i_face_adjacent_for_remove.com_object
        )

    def __repr__(self):
        return f'Trim(name="{self.name}")'
