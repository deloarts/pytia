from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeTrim(HybridShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_trim = com_object

    @property
    def automatic_extrapolation_mode(self) -> bool:
        return self.hybrid_shape_trim.AutomaticExtrapolationMode

    @automatic_extrapolation_mode.setter
    def automatic_extrapolation_mode(self, value: bool):
        self.hybrid_shape_trim.AutomaticExtrapolationMode = value

    @property
    def connex(self) -> bool:
        return self.hybrid_shape_trim.Connex

    @connex.setter
    def connex(self, value: bool):
        self.hybrid_shape_trim.Connex = value

    @property
    def first_elem(self) -> Reference:
        return Reference(self.hybrid_shape_trim.FirstElem)

    @first_elem.setter
    def first_elem(self, reference_element: Reference):
        self.hybrid_shape_trim.FirstElem = reference_element.com_object

    @property
    def first_orientation(self) -> int:
        return self.hybrid_shape_trim.FirstOrientation

    @first_orientation.setter
    def first_orientation(self, value: int):
        self.hybrid_shape_trim.FirstOrientation = value

    @property
    def intersection_computation(self) -> bool:
        return self.hybrid_shape_trim.IntersectionComputation

    @intersection_computation.setter
    def intersection_computation(self, value: bool):
        self.hybrid_shape_trim.IntersectionComputation = value

    @property
    def keep_all_pieces(self) -> bool:
        return self.hybrid_shape_trim.KeepAllPieces

    @keep_all_pieces.setter
    def keep_all_pieces(self, value: bool):
        self.hybrid_shape_trim.KeepAllPieces = value

    @property
    def manifold(self) -> bool:
        return self.hybrid_shape_trim.Manifold

    @manifold.setter
    def manifold(self, value: bool):
        self.hybrid_shape_trim.Manifold = value

    @property
    def mode(self) -> int:
        return self.hybrid_shape_trim.Mode

    @mode.setter
    def mode(self, value: int):
        self.hybrid_shape_trim.Mode = value

    @property
    def second_elem(self) -> Reference:
        return Reference(self.hybrid_shape_trim.SecondElem)

    @second_elem.setter
    def second_elem(self, reference_element: Reference):
        self.hybrid_shape_trim.SecondElem = reference_element.com_object

    @property
    def second_orientation(self) -> int:
        return self.hybrid_shape_trim.SecondOrientation

    @second_orientation.setter
    def second_orientation(self, value: int):
        self.hybrid_shape_trim.SecondOrientation = value

    @property
    def simplify(self) -> bool:
        return self.hybrid_shape_trim.Simplify

    @simplify.setter
    def simplify(self, value: bool):
        self.hybrid_shape_trim.Simplify = value

    @property
    def support(self) -> Reference:
        return Reference(self.hybrid_shape_trim.Support)

    @support.setter
    def support(self, reference_support: Reference):
        self.hybrid_shape_trim.Support = reference_support.com_object

    def add_element_to_keep(self, i_element: Reference) -> None:
        return self.hybrid_shape_trim.AddElementToKeep(i_element.com_object)

    def add_element_to_remove(self, i_element: Reference) -> None:
        return self.hybrid_shape_trim.AddElementToRemove(i_element.com_object)

    def add_piece_cutter(
        self, i_rank: int, i_cutter_elem: int, i_orientation: int
    ) -> None:
        return self.hybrid_shape_trim.AddPieceCutter(
            i_rank, i_cutter_elem, i_orientation
        )

    def get_elem(self, i_rank: int) -> Reference:
        return Reference(self.hybrid_shape_trim.GetElem(i_rank))

    def get_kept_elem(self, i_rank: int) -> Reference:
        return Reference(self.hybrid_shape_trim.GetKeptElem(i_rank))

    def get_nb_elem(self) -> int:
        return self.hybrid_shape_trim.GetNbElem()

    def get_nb_elements_to_keep(self) -> int:
        return self.hybrid_shape_trim.GetNbElementsToKeep()

    def get_nb_elements_to_remove(self) -> int:
        return self.hybrid_shape_trim.GetNbElementsToRemove()

    def get_next_orientation(self, i_rank: int) -> int:
        return self.hybrid_shape_trim.GetNextOrientation(i_rank)

    def get_piece_cutter(
        self,
        i_rank: int,
        i_cutter_index: int,
        o_cutter_elem_idx: int,
        o_orientation: int,
    ) -> None:
        return self.hybrid_shape_trim.GetPieceCutter(
            i_rank, i_cutter_index, o_cutter_elem_idx, o_orientation
        )

    def get_piece_discrimination_index(self, i_rank: int, o_index: int) -> None:
        return self.hybrid_shape_trim.GetPieceDiscriminationIndex(i_rank, o_index)

    def get_piece_nb_cutters(self, i_rank: int) -> int:
        return self.hybrid_shape_trim.GetPieceNbCutters(i_rank)

    def get_portion_to_keep(self, i_rank: int) -> int:
        return self.hybrid_shape_trim.GetPortionToKeep(i_rank)

    def get_previous_orientation(self, i_rank: int) -> int:
        return self.hybrid_shape_trim.GetPreviousOrientation(i_rank)

    def get_removed_elem(self, i_rank: int) -> Reference:
        return Reference(self.hybrid_shape_trim.GetRemovedElem(i_rank))

    def invert_first_orientation(self) -> None:
        return self.hybrid_shape_trim.InvertFirstOrientation()

    def invert_second_orientation(self) -> None:
        return self.hybrid_shape_trim.InvertSecondOrientation()

    def remove_element_to_keep(self, i_rank: int) -> None:
        return self.hybrid_shape_trim.RemoveElementToKeep(i_rank)

    def remove_element_to_remove(self, i_rank: int) -> None:
        return self.hybrid_shape_trim.RemoveElementToRemove(i_rank)

    def remove_piece_cutter(self, i_rank: int, i_cutter_index: int) -> None:
        return self.hybrid_shape_trim.RemovePieceCutter(i_rank, i_cutter_index)

    def set_elem(self, i_rank: int, i_elem: Reference) -> None:
        return self.hybrid_shape_trim.SetElem(i_rank, i_elem.com_object)

    def set_next_orientation(self, i_rank: int, i_orientation: int) -> None:
        return self.hybrid_shape_trim.SetNextOrientation(i_rank, i_orientation)

    def set_piece_discrimination_index(self, i_rank: int, i_index: int) -> None:
        return self.hybrid_shape_trim.SetPieceDiscriminationIndex(i_rank, i_index)

    def set_portion_to_keep(self, i_rank: int, i_portion_number: int) -> None:
        return self.hybrid_shape_trim.SetPortionToKeep(i_rank, i_portion_number)

    def set_previous_orientation(self, i_rank: int, i_orientation: int) -> None:
        return self.hybrid_shape_trim.SetPreviousOrientation(i_rank, i_orientation)

    def __repr__(self):
        return f'HybridShapeTrim(name="{self.name}")'
