from pytia.framework.hybrid_shape_interfaces.hybrid_shape_direction import (
    HybridShapeDirection,
)
from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.knowledge_interfaces.length import Length
from pytia.framework.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeConic(HybridShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_conic = com_object

    @property
    def conic_parameter(self) -> float:
        return self.hybrid_shape_conic.ConicParameter

    @conic_parameter.setter
    def conic_parameter(self, value: float):
        self.hybrid_shape_conic.ConicParameter = value

    @property
    def conic_user_tol(self) -> Length:
        return Length(self.hybrid_shape_conic.ConicUserTol)

    @property
    def end_point(self) -> Reference:
        return Reference(self.hybrid_shape_conic.EndPoint)

    @end_point.setter
    def end_point(self, reference_point: Reference):
        self.hybrid_shape_conic.EndPoint = reference_point.com_object

    @property
    def end_tangent(self) -> HybridShapeDirection:
        return HybridShapeDirection(self.hybrid_shape_conic.EndTangent)

    @end_tangent.setter
    def end_tangent(self, direction: HybridShapeDirection):
        self.hybrid_shape_conic.EndTangent = direction.com_object

    @property
    def start_point(self) -> Reference:
        return Reference(self.hybrid_shape_conic.StartPoint)

    @start_point.setter
    def start_point(self, reference_point: Reference):
        self.hybrid_shape_conic.StartPoint = reference_point

    @property
    def start_tangent(self) -> HybridShapeDirection:
        return HybridShapeDirection(self.hybrid_shape_conic.StartTangent)

    @start_tangent.setter
    def start_tangent(self, direction: HybridShapeDirection):
        self.hybrid_shape_conic.StartTangent = direction

    @property
    def support_plane(self) -> Reference:
        return Reference(self.hybrid_shape_conic.SupportPlane)

    @support_plane.setter
    def support_plane(self, reference_plane: Reference):
        self.hybrid_shape_conic.SupportPlane = reference_plane.com_object

    @property
    def tangent_int_point(self) -> Reference:
        return Reference(self.hybrid_shape_conic.TangentIntPoint)

    @tangent_int_point.setter
    def tangent_int_point(self, reference_tangent_point: Reference):
        self.hybrid_shape_conic.TangentIntPoint = reference_tangent_point

    def get_end_tangent_direction_flag(self, o_orientation: int) -> None:
        return self.hybrid_shape_conic.GetEndTangentDirectionFlag(o_orientation)

    def get_intermed_tangent(self, i_index_point: int) -> HybridShapeDirection:
        return HybridShapeDirection(
            self.hybrid_shape_conic.GetIntermedTangent(i_index_point)
        )

    def get_intermediate_point(
        self, i_index_point: int, o_end_point: Reference
    ) -> None:
        return self.hybrid_shape_conic.GetIntermediatePoint(
            i_index_point, o_end_point.com_object
        )

    def get_intermediate_tangent_direction_flag(
        self, i_index_point: int, o_orientation: int
    ) -> None:
        return self.hybrid_shape_conic.GetIntermediateTangentDirectionFlag(
            i_index_point, o_orientation
        )

    def get_start_tangent_direction_flag(self, o_orientation: int) -> None:
        return self.hybrid_shape_conic.GetStartTangentDirectionFlag(o_orientation)

    def set_end_tangent_direction_flag(self, i_orientation: int) -> None:
        return self.hybrid_shape_conic.SetEndTangentDirectionFlag(i_orientation)

    def set_intermediate_point(
        self, i_index_point: int, i_end_point: Reference
    ) -> None:
        return self.hybrid_shape_conic.SetIntermediatePoint(
            i_index_point, i_end_point.com_object
        )

    def set_intermediate_tangent(
        self, i_index_point: int, i_tgt_dir: HybridShapeDirection
    ) -> None:
        return self.hybrid_shape_conic.SetIntermediateTangent(
            i_index_point, i_tgt_dir.com_object
        )

    def set_intermediate_tangent_direction_flag(
        self, i_index_point: int, i_orientation: int
    ) -> None:
        return self.hybrid_shape_conic.SetIntermediateTangentDirectionFlag(
            i_index_point, i_orientation
        )

    def set_start_and_end_tangents_plus_conic_parameter(
        self,
        i_start_tgt: HybridShapeDirection,
        i_end_tgt: HybridShapeDirection,
        i_conic_param: float,
    ) -> None:
        return self.hybrid_shape_conic.SetStartAndEndTangentsPlusConicParameter(
            i_start_tgt.com_object, i_end_tgt.com_object, i_conic_param
        )

    def set_start_and_end_tangents_plus_passing_point(
        self,
        i_start_tgt: HybridShapeDirection,
        i_end_tgt: HybridShapeDirection,
        i_passing_pt: Reference,
    ) -> None:
        return self.hybrid_shape_conic.SetStartAndEndTangentsPlusPassingPoint(
            i_start_tgt.com_object, i_end_tgt.com_object, i_passing_pt.com_object
        )

    def set_start_tangent_direction_flag(self, i_orientation: int) -> None:
        return self.hybrid_shape_conic.SetStartTangentDirectionFlag(i_orientation)

    def set_tangent_intersect_point_plus_conic_parm(
        self, i_tgt_int: Reference, i_conic_param: float
    ) -> None:
        return self.hybrid_shape_conic.SetTangentIntersectPointPlusConicParm(
            i_tgt_int.com_object, i_conic_param
        )

    def set_tangent_intersect_point_plus_passing_point(
        self, i_tgt_int: Reference, i_passing_pt: Reference
    ) -> None:
        return self.hybrid_shape_conic.SetTangentIntersectPointPlusPassingPoint(
            i_tgt_int.com_object, i_passing_pt.com_object
        )

    def set_three_intermediate_passing_points(
        self, i_pass_pt1: Reference, i_pass_pt2: Reference, i_pass_pt3: Reference
    ) -> None:
        return self.hybrid_shape_conic.SetThreeIntermediatePassingPoints(
            i_pass_pt1.com_object, i_pass_pt2.com_object, i_pass_pt3.com_object
        )

    def set_two_intermediate_passing_points_plus_one_tangent(
        self,
        i_pass_pt1: Reference,
        i_pass_pt2: Reference,
        i_tgt_dir: HybridShapeDirection,
        i_index_point: int,
    ) -> None:
        return self.hybrid_shape_conic.SetTwoIntermediatePassingPointsPlusOneTangent(
            i_pass_pt1.com_object,
            i_pass_pt2.com_object,
            i_tgt_dir.com_object,
            i_index_point,
        )

    def switch_end_tangent_direction(self) -> None:
        return self.hybrid_shape_conic.SwitchEndTangentDirection()

    def switch_intermediate_tangent_direction(self, i_index_point: int) -> None:
        return self.hybrid_shape_conic.SwitchIntermediateTangentDirection(i_index_point)

    def switch_start_tangent_direction(self) -> None:
        return self.hybrid_shape_conic.SwitchStartTangentDirection()

    def __repr__(self):
        return f'HybridShapeConic(name="{self.name}")'
