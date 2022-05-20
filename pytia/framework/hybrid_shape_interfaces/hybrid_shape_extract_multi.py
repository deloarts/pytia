from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeExtractMulti(HybridShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_extract_multi = com_object

    def add_constraint(
        self,
        i_constraint: Reference,
        i_type: int,
        i_complementaire: bool,
        i_is_federated: bool,
        i_crvtre_thsld: float,
        i_pos: int,
    ) -> None:
        return self.hybrid_shape_extract_multi.AddConstraint(
            i_constraint.com_object,
            i_type,
            i_complementaire,
            i_is_federated,
            i_crvtre_thsld,
            i_pos,
        )

    def add_constraint_tolerant(
        self,
        i_constraint: Reference,
        i_type: int,
        i_complementaire: bool,
        i_is_federated: bool,
        i_distre_thsld: float,
        i_angtre_thsld: float,
        i_crvtre_thsld: float,
        i_pos: int,
    ) -> None:
        return self.hybrid_shape_extract_multi.AddConstraintTolerant(
            i_constraint.com_object,
            i_type,
            i_complementaire,
            i_is_federated,
            i_distre_thsld,
            i_angtre_thsld,
            i_crvtre_thsld,
            i_pos,
        )

    def get_angular_threshold(self, i_pos: int) -> float:
        return self.hybrid_shape_extract_multi.GetAngularThreshold(i_pos)

    def get_angular_threshold_activity(self, i_pos: int) -> bool:
        return self.hybrid_shape_extract_multi.GetAngularThresholdActivity(i_pos)

    def get_complementary_extract_multi(self, i_pos: int) -> bool:
        return self.hybrid_shape_extract_multi.GetComplementaryExtractMulti(i_pos)

    def get_curvature_threshold(self, i_pos: int) -> float:
        return self.hybrid_shape_extract_multi.GetCurvatureThreshold(i_pos)

    def get_curvature_threshold_activity(self, i_pos: int) -> bool:
        return self.hybrid_shape_extract_multi.GetCurvatureThresholdActivity(i_pos)

    def get_distance_threshold(self, i_pos: int) -> float:
        return self.hybrid_shape_extract_multi.GetDistanceThreshold(i_pos)

    def get_distance_threshold_activity(self, i_pos: int) -> bool:
        return self.hybrid_shape_extract_multi.GetDistanceThresholdActivity(i_pos)

    def get_element(self, i_pos: int) -> Reference:
        return Reference(self.hybrid_shape_extract_multi.GetElement(i_pos))

    def get_is_federated(self, i_pos: int) -> bool:
        return self.hybrid_shape_extract_multi.GetIsFederated(i_pos)

    def get_list_of_constraints(self, o_list_of_extracted_constraints: tuple) -> None:
        return self.hybrid_shape_extract_multi.GetListOfConstraints(
            o_list_of_extracted_constraints
        )

    def get_nb_constraints(self, o_nb_constraints: int) -> None:
        return self.hybrid_shape_extract_multi.GetNbConstraints(o_nb_constraints)

    def get_propagation_type(self, i_pos: int) -> int:
        return self.hybrid_shape_extract_multi.GetPropagationType(i_pos)

    def get_support(self, i_pos: int) -> Reference:
        return Reference(self.hybrid_shape_extract_multi.GetSupport(i_pos))

    def remove_element(self, i_position: int) -> None:
        return self.hybrid_shape_extract_multi.RemoveElement(i_position)

    def replace_element(
        self, i_extract_to_replace: Reference, i_new_extract: Reference, i_pos: int
    ) -> None:
        return self.hybrid_shape_extract_multi.ReplaceElement(
            i_extract_to_replace.com_object, i_new_extract.com_object, i_pos
        )

    def set_angular_threshold(self, i_pos: int, i_angtre_thsld: float) -> None:
        return self.hybrid_shape_extract_multi.SetAngularThreshold(
            i_pos, i_angtre_thsld
        )

    def set_angular_threshold_activity(
        self, i_pos: int, i_angtre_thsld_activity: bool
    ) -> None:
        return self.hybrid_shape_extract_multi.SetAngularThresholdActivity(
            i_pos, i_angtre_thsld_activity
        )

    def set_complementary_extract_multi(
        self, i_pos: int, i_complementaire: bool
    ) -> None:
        return self.hybrid_shape_extract_multi.SetComplementaryExtractMulti(
            i_pos, i_complementaire
        )

    def set_curvature_threshold(self, i_pos: int, i_crvtre_thsld: float) -> None:
        return self.hybrid_shape_extract_multi.SetCurvatureThreshold(
            i_pos, i_crvtre_thsld
        )

    def set_curvature_threshold_activity(
        self, i_pos: int, i_crvtre_thsld_activity: bool
    ) -> None:
        return self.hybrid_shape_extract_multi.SetCurvatureThresholdActivity(
            i_pos, i_crvtre_thsld_activity
        )

    def set_distance_threshold(self, i_pos: int, i_distre_thsld: float) -> None:
        return self.hybrid_shape_extract_multi.SetDistanceThreshold(
            i_pos, i_distre_thsld
        )

    def set_distance_threshold_activity(
        self, i_pos: int, i_distre_thsld_activity: bool
    ) -> None:
        return self.hybrid_shape_extract_multi.SetDistanceThresholdActivity(
            i_pos, i_distre_thsld_activity
        )

    def set_element(self, i_pos: int, i_elem: Reference) -> None:
        return self.hybrid_shape_extract_multi.SetElement(i_pos, i_elem.com_object)

    def set_is_federated(self, i_pos: int, i_is_federated: bool) -> None:
        return self.hybrid_shape_extract_multi.SetIsFederated(i_pos, i_is_federated)

    def set_propagation_type(self, i_pos: int, i_type_propag: int) -> None:
        return self.hybrid_shape_extract_multi.SetPropagationType(i_pos, i_type_propag)

    def set_support(self, i_pos: int, i_support: Reference) -> None:
        return self.hybrid_shape_extract_multi.SetSupport(i_pos, i_support.com_object)

    def __repr__(self):
        return f'HybridShapeExtractMulti(name="{self.name}")'
