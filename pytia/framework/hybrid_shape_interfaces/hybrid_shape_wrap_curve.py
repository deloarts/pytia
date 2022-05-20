from pytia.framework.hybrid_shape_interfaces.hybrid_shape_direction import (
    HybridShapeDirection,
)
from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeWrapCurve(HybridShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_wrap_curve = com_object

    @property
    def first_curves_constraint(self) -> int:
        return self.hybrid_shape_wrap_curve.FirstCurvesConstraint

    @first_curves_constraint.setter
    def first_curves_constraint(self, value: int):
        self.hybrid_shape_wrap_curve.FirstCurvesConstraint = value

    @property
    def last_curves_constraint(self) -> int:
        return self.hybrid_shape_wrap_curve.LastCurvesConstraint

    @last_curves_constraint.setter
    def last_curves_constraint(self, value: int):
        self.hybrid_shape_wrap_curve.LastCurvesConstraint = value

    @property
    def surface(self) -> Reference:
        return Reference(self.hybrid_shape_wrap_curve.Surface)

    @surface.setter
    def surface(self, reference_surface: Reference):
        self.hybrid_shape_wrap_curve.Surface = reference_surface.com_object

    def get_curves(
        self, i_position: int, o_reference_curve: Reference, o_target_curve: Reference
    ) -> None:
        return self.hybrid_shape_wrap_curve.GetCurves(
            i_position, o_reference_curve.com_object, o_target_curve.com_object
        )

    def get_number_of_curves(self) -> int:
        return self.hybrid_shape_wrap_curve.GetNumberOfCurves()

    def get_reference_direction(
        self, o_direction_type: int, o_direction: HybridShapeDirection
    ) -> None:
        return self.hybrid_shape_wrap_curve.GetReferenceDirection(
            o_direction_type, o_direction.com_object
        )

    def get_reference_spine(self, o_spine_type: int, o_spine: Reference) -> None:
        return self.hybrid_shape_wrap_curve.GetReferenceSpine(
            o_spine_type, o_spine.com_object
        )

    def insert_curves(
        self, i_position: int, i_reference_curve: Reference, i_target_curve: Reference
    ) -> None:
        return self.hybrid_shape_wrap_curve.InsertCurves(
            i_position, i_reference_curve.com_object, i_target_curve.com_object
        )

    def insert_reference_curve(
        self, i_position: int, i_reference_curve: Reference
    ) -> None:
        return self.hybrid_shape_wrap_curve.InsertReferenceCurve(
            i_position, i_reference_curve.com_object
        )

    def remove_curves(self, i_position: int) -> None:
        return self.hybrid_shape_wrap_curve.RemoveCurves(i_position)

    def set_reference_direction(self, i_direction: HybridShapeDirection) -> None:
        return self.hybrid_shape_wrap_curve.SetReferenceDirection(
            i_direction.com_object
        )

    def set_reference_spine(self, i_spine: Reference) -> None:
        return self.hybrid_shape_wrap_curve.SetReferenceSpine(i_spine.com_object)

    def __repr__(self):
        return f'HybridShapeWrapCurve(name="{self.name}")'
