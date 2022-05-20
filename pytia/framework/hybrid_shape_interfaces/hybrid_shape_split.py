from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeSplit(HybridShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_split = com_object

    @property
    def automatic_extrapolation_mode(self) -> bool:
        return self.hybrid_shape_split.AutomaticExtrapolationMode

    @automatic_extrapolation_mode.setter
    def automatic_extrapolation_mode(self, value: bool):
        self.hybrid_shape_split.AutomaticExtrapolationMode = value

    @property
    def both_sides_mode(self) -> bool:
        return self.hybrid_shape_split.BothSidesMode

    @both_sides_mode.setter
    def both_sides_mode(self, value: bool):
        self.hybrid_shape_split.BothSidesMode = value

    @property
    def cutting_elem(self) -> Reference:
        return Reference(self.hybrid_shape_split.CuttingElem)

    @cutting_elem.setter
    def cutting_elem(self, reference_element: Reference):
        self.hybrid_shape_split.CuttingElem = reference_element.com_object

    @property
    def elem_to_cut(self) -> Reference:
        return Reference(self.hybrid_shape_split.ElemToCut)

    @elem_to_cut.setter
    def elem_to_cut(self, reference_element: Reference):
        self.hybrid_shape_split.ElemToCut = reference_element.com_object

    @property
    def extrapolation_type(self) -> int:
        return self.hybrid_shape_split.ExtrapolationType

    @extrapolation_type.setter
    def extrapolation_type(self, value: int):
        self.hybrid_shape_split.ExtrapolationType = value

    @property
    def intersection_computation(self) -> bool:
        return self.hybrid_shape_split.IntersectionComputation

    @intersection_computation.setter
    def intersection_computation(self, value: bool):
        self.hybrid_shape_split.IntersectionComputation = value

    @property
    def orientation(self) -> int:
        return self.hybrid_shape_split.Orientation

    @orientation.setter
    def orientation(self, value: int):
        self.hybrid_shape_split.Orientation = value

    @property
    def support(self) -> Reference:
        return Reference(self.hybrid_shape_split.Support)

    @support.setter
    def support(self, reference_support: Reference):
        self.hybrid_shape_split.Support = reference_support.com_object

    @property
    def volume_result(self) -> int:
        return self.hybrid_shape_split.VolumeResult

    @volume_result.setter
    def volume_result(self, value: int):
        self.hybrid_shape_split.VolumeResult = value

    def add_cutting_elem(self, i_elem: Reference, i_orientation: int) -> None:
        return self.hybrid_shape_split.AddCuttingElem(i_elem.com_object, i_orientation)

    def add_element_to_keep(self, i_element: Reference) -> None:
        return self.hybrid_shape_split.AddElementToKeep(i_element.com_object)

    def add_element_to_remove(self, i_element: Reference) -> None:
        return self.hybrid_shape_split.AddElementToRemove(i_element.com_object)

    def get_cutting_elem(self, i_rank: int) -> Reference:
        return Reference(self.hybrid_shape_split.GetCuttingElem(i_rank))

    def get_intersection(self, i_rank: int) -> Reference:
        return Reference(self.hybrid_shape_split.GetIntersection(i_rank))

    def get_kept_elem(self, i_rank: int) -> Reference:
        return Reference(self.hybrid_shape_split.GetKeptElem(i_rank))

    def get_nb_cutting_elem(self) -> int:
        return self.hybrid_shape_split.GetNbCuttingElem()

    def get_nb_elements_to_keep(self) -> int:
        return self.hybrid_shape_split.GetNbElementsToKeep()

    def get_nb_elements_to_remove(self) -> int:
        return self.hybrid_shape_split.GetNbElementsToRemove()

    def get_orientation(self, i_rank: int) -> int:
        return self.hybrid_shape_split.GetOrientation(i_rank)

    def get_other_side(self) -> Reference:
        return Reference(self.hybrid_shape_split.GetOtherSide())

    def get_removed_elem(self, i_rank: int) -> Reference:
        return Reference(self.hybrid_shape_split.GetRemovedElem(i_rank))

    def invert_orientation(self) -> None:
        return self.hybrid_shape_split.InvertOrientation()

    def remove_cutting_elem(self, i_elem: Reference) -> None:
        return self.hybrid_shape_split.RemoveCuttingElem(i_elem.com_object)

    def remove_element_to_keep(self, i_rank: int) -> None:
        return self.hybrid_shape_split.RemoveElementToKeep(i_rank)

    def remove_element_to_remove(self, i_rank: int) -> None:
        return self.hybrid_shape_split.RemoveElementToRemove(i_rank)

    def set_orientation(self, i_rank: int, i_orientation: int) -> None:
        return self.hybrid_shape_split.SetOrientation(i_rank, i_orientation)

    def __repr__(self):
        return f'HybridShapeSplit(name="{self.name}")'
