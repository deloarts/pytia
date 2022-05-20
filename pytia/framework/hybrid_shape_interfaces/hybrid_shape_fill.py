from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeFill(HybridShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_fill = com_object

    @property
    def advanced_tolerant_mode(self) -> int:
        return self.hybrid_shape_fill.AdvancedTolerantMode

    @advanced_tolerant_mode.setter
    def advanced_tolerant_mode(self, value: int):
        self.hybrid_shape_fill.AdvancedTolerantMode = value

    @property
    def constraint(self) -> Reference:
        return Reference(self.hybrid_shape_fill.Constraint)

    @constraint.setter
    def constraint(self, reference: Reference):
        self.hybrid_shape_fill.Constraint = reference.com_object

    @property
    def continuity(self) -> int:
        return self.hybrid_shape_fill.Continuity

    @continuity.setter
    def continuity(self, value: int):
        self.hybrid_shape_fill.Continuity = value

    @property
    def detection(self) -> int:
        return self.hybrid_shape_fill.Detection

    @detection.setter
    def detection(self, value: int):
        self.hybrid_shape_fill.Detection = value

    @property
    def maximum_deviation_value(self) -> float:
        return self.hybrid_shape_fill.MaximumDeviationValue

    @maximum_deviation_value.setter
    def maximum_deviation_value(self, value: float):
        self.hybrid_shape_fill.MaximumDeviationValue = value

    @property
    def plane_only_mode(self) -> bool:
        return self.hybrid_shape_fill.PlaneOnlyMode

    @plane_only_mode.setter
    def plane_only_mode(self, value: bool):
        self.hybrid_shape_fill.PlaneOnlyMode = value

    @property
    def tolerant_mode(self) -> bool:
        return self.hybrid_shape_fill.TolerantMode

    @tolerant_mode.setter
    def tolerant_mode(self, value: bool):
        self.hybrid_shape_fill.TolerantMode = value

    def add_bound(self, i_boundary: Reference) -> None:
        return self.hybrid_shape_fill.AddBound(i_boundary.com_object)

    def add_support_at_bound(self, i_boundary: Reference, i_support: Reference) -> None:
        return self.hybrid_shape_fill.AddSupportAtBound(
            i_boundary.com_object, i_support.com_object
        )

    def append_constraint(self, i_constraint: Reference) -> None:
        return self.hybrid_shape_fill.AppendConstraint(i_constraint.com_object)

    def get_bound_at_position(self, i_pos: int) -> Reference:
        return Reference(self.hybrid_shape_fill.GetBoundAtPosition(i_pos))

    def get_bound_position(self, i_boundary: Reference) -> int:
        return self.hybrid_shape_fill.GetBoundPosition(i_boundary.com_object)

    def get_bound_size(self) -> int:
        return self.hybrid_shape_fill.GetBoundSize()

    def get_boundary_continuity(self, i_pos: int) -> int:
        return self.hybrid_shape_fill.GetBoundaryContinuity(i_pos)

    def get_constraint_at_position(self, i_pos: int) -> Reference:
        return Reference(self.hybrid_shape_fill.GetConstraintAtPosition(i_pos))

    def get_constraints_size(self) -> int:
        return self.hybrid_shape_fill.GetConstraintsSize()

    def get_support_at_position(self, i_pos: int) -> Reference:
        return Reference(self.hybrid_shape_fill.GetSupportAtPosition(i_pos))

    def insert_bound_after_position(self, i_boundary: Reference, i_pos: int) -> None:
        return self.hybrid_shape_fill.InsertBoundAfterPosition(
            i_boundary.com_object, i_pos
        )

    def remove_all_bound(self) -> None:
        return self.hybrid_shape_fill.RemoveAllBound()

    def remove_all_constraints(self) -> None:
        return self.hybrid_shape_fill.RemoveAllConstraints()

    def remove_bound_at_position(self, i_pos: int) -> None:
        return self.hybrid_shape_fill.RemoveBoundAtPosition(i_pos)

    def remove_constraint(self, i_pos: int) -> None:
        return self.hybrid_shape_fill.RemoveConstraint(i_pos)

    def remove_support_at_position(self, i_pos: int) -> None:
        return self.hybrid_shape_fill.RemoveSupportAtPosition(i_pos)

    def replace_bound_at_position(self, i_boundary: Reference, i_pos: int) -> None:
        return self.hybrid_shape_fill.ReplaceBoundAtPosition(
            i_boundary.com_object, i_pos
        )

    def replace_constraint(self, i_pos: int, i_constraint: Reference) -> None:
        return self.hybrid_shape_fill.ReplaceConstraint(i_pos, i_constraint.com_object)

    def replace_support_at_position(self, i_support: Reference, i_pos: int) -> None:
        return self.hybrid_shape_fill.ReplaceSupportAtPosition(
            i_support.com_object, i_pos
        )

    def set_boundary_continuity(self, i_continuity: int, i_pos: int) -> None:
        return self.hybrid_shape_fill.SetBoundaryContinuity(i_continuity, i_pos)

    def __repr__(self):
        return f'HybridShapeFill(name="{self.name}")'
