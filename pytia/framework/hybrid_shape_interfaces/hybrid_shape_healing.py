from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.knowledge_interfaces.angle import Angle
from pytia.framework.knowledge_interfaces.length import Length
from pytia.framework.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeHealing(HybridShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_healing = com_object

    @property
    def canonic_free_mode(self) -> int:
        return self.hybrid_shape_healing.CononicFreeMode

    @canonic_free_mode.setter
    def canonic_free_mode(self, mode: int):
        self.hybrid_shape_healing.CanonicFreeMode = mode

    @property
    def continuity(self) -> int:
        return self.hybrid_shape_healing.Continuity

    @continuity.setter
    def continuity(self, value: int):
        self.hybrid_shape_healing.Continuity = value

    @property
    def distance_objective(self) -> Length:
        return Length(self.hybrid_shape_healing.DistanceObjective)

    @property
    def merging_distance(self) -> Length:
        return Length(self.hybrid_shape_healing.MergingDistance)

    @property
    def no_of_bodies_to_heal(self) -> int:
        return self.hybrid_shape_healing.NoOfBodiesToHeal

    @property
    def no_of_edges_to_keep_sharp(self) -> int:
        return self.hybrid_shape_healing.NoOfEdgesToKeepSharp

    @property
    def no_of_elements_to_freeze(self) -> int:
        return self.hybrid_shape_healing.NoOfElementsToFreeze

    @property
    def sharpness_angle(self) -> Angle:
        return Angle(self.hybrid_shape_healing.SharpnessAngle)

    @property
    def tangency_angle(self) -> Angle:
        return Angle(self.hybrid_shape_healing.TangencyAngle)

    @property
    def tangency_objective(self) -> Length:
        return Length(self.hybrid_shape_healing.TangencyObjective)

    def add_body_to_heal(self, i_body: Reference) -> None:
        return self.hybrid_shape_healing.AddBodyToHeal(i_body.com_object)

    def add_edge_to_keep_sharp(self, i_edge: Reference) -> None:
        return self.hybrid_shape_healing.AddEdgeToKeepSharp(i_edge.com_object)

    def add_elements_to_freeze(self, i_element: Reference) -> None:
        return self.hybrid_shape_healing.AddElementsToFreeze(i_element.com_object)

    def get_body_to_heal(self, i_position: int) -> Reference:
        return Reference(self.hybrid_shape_healing.GetBodyToHeal(i_position))

    def get_edge_to_keep_sharp(self, i_position: int) -> Reference:
        return Reference(self.hybrid_shape_healing.GetEdgeToKeepSharp(i_position))

    def get_element_to_freeze(self, i_position: int) -> Reference:
        return Reference(self.hybrid_shape_healing.GetElementToFreeze(i_position))

    def remove_body_to_heal(self, i_position: int) -> None:
        return self.hybrid_shape_healing.RemoveBodyToHeal(i_position)

    def remove_edge_to_keep_sharp(self, i_position: int) -> None:
        return self.hybrid_shape_healing.RemoveEdgeToKeepSharp(i_position)

    def remove_element_to_freeze(self, i_position: int) -> None:
        return self.hybrid_shape_healing.RemoveElementToFreeze(i_position)

    def replace_to_heal_element(self, i_index: int, i_new_heal: Reference) -> None:
        return self.hybrid_shape_healing.ReplaceToHealElement(
            i_index, i_new_heal.com_object
        )

    def set_distance_objective(self, i_distance_objective: float) -> None:
        return self.hybrid_shape_healing.SetDistanceObjective(i_distance_objective)

    def set_merging_distance(self, i_merging_distance: float) -> None:
        return self.hybrid_shape_healing.SetMergingDistance(i_merging_distance)

    def set_sharpness_angle(self, i_sharpness_angle: float) -> None:
        return self.hybrid_shape_healing.SetSharpnessAngle(i_sharpness_angle)

    def set_tangency_angle(self, i_tangency_angle: float) -> None:
        return self.hybrid_shape_healing.SetTangencyAngle(i_tangency_angle)

    def set_tangency_objective(self, i_tangency_objective: float) -> None:
        return self.hybrid_shape_healing.SetTangencyObjective(i_tangency_objective)

    def __repr__(self):
        return f'HybridShapeHealing(name="{ self.name }")'
