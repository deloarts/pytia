from pytia.framework.hybrid_shape_interfaces.hybrid_shape_direction import (
    HybridShapeDirection,
)
from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.knowledge_interfaces.length import Length
from pytia.framework.knowledge_interfaces.real_param import RealParam
from pytia.framework.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeSpline(HybridShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_spline = com_object

    def add_point(self, ip_ia_point: Reference) -> None:
        return self.hybrid_shape_spline.AddPoint(ip_ia_point.com_object)

    def add_point_with_constraint_explicit(
        self,
        ip_ia_point: Reference,
        ip_ia_dir_tangency: HybridShapeDirection,
        i_tangency_norm: float,
        i_inverse_tangency: int,
        ip_ia_dir_curvature: HybridShapeDirection,
        i_curvature_radius: float,
    ) -> None:
        return self.hybrid_shape_spline.AddPointWithConstraintExplicit(
            ip_ia_point.com_object,
            ip_ia_dir_tangency.com_object,
            i_tangency_norm,
            i_inverse_tangency,
            ip_ia_dir_curvature.com_object,
            i_curvature_radius,
        )

    def add_point_with_constraint_from_curve(
        self,
        ip_ia_point: Reference,
        ip_ia_curve_cst: Reference,
        i_tangency_norm: float,
        i_invert_value: int,
        i_crv_cst_type: int,
    ) -> None:
        return self.hybrid_shape_spline.AddPointWithConstraintFromCurve(
            ip_ia_point.com_object,
            ip_ia_curve_cst.com_object,
            i_tangency_norm,
            i_invert_value,
            i_crv_cst_type,
        )

    def get_closure(self) -> int:
        return self.hybrid_shape_spline.GetClosure()

    def get_constraint_type(self, i_pos: int) -> int:
        return self.hybrid_shape_spline.GetConstraintType(i_pos)

    def get_curvature_radius(self, i_pos: int) -> Length:
        return Length(self.hybrid_shape_spline.GetCurvatureRadius(i_pos))

    def get_direction_inversion(self, i_pos: int) -> int:
        return self.hybrid_shape_spline.GetDirectionInversion(i_pos)

    def get_nb_control_point(self) -> int:
        return self.hybrid_shape_spline.GetNbControlPoint()

    def get_point(self, i_pos: int) -> Reference:
        return Reference(self.hybrid_shape_spline.GetPoint(i_pos))

    def get_point_constraint_explicit(
        self,
        i_pos: int,
        op_ia_dir_tangency: HybridShapeDirection,
        o_tangency_norm: float,
        o_inverse_tangency: int,
        op_ia_dir_curvature: HybridShapeDirection,
        o_curvature_radius: float,
    ) -> None:
        return self.hybrid_shape_spline.GetPointConstraintExplicit(
            i_pos,
            op_ia_dir_tangency.com_object,
            o_tangency_norm,
            o_inverse_tangency,
            op_ia_dir_curvature.com_object,
            o_curvature_radius,
        )

    def get_point_constraint_from_curve(
        self,
        i_pos: int,
        op_ia_curve_cst: Reference,
        o_tangency_norm: float,
        o_invert_value: int,
        o_crv_cst_type: int,
    ) -> None:
        return self.hybrid_shape_spline.GetPointConstraintFromCurve(
            i_pos,
            op_ia_curve_cst.com_object,
            o_tangency_norm,
            o_invert_value,
            o_crv_cst_type,
        )

    def get_point_position(self, ip_ia_point: Reference) -> int:
        return self.hybrid_shape_spline.GetPointPosition(ip_ia_point.com_object)

    def get_spline_type(self) -> int:
        return self.hybrid_shape_spline.GetSplineType()

    def get_support(self) -> Reference:
        return Reference(self.hybrid_shape_spline.GetSupport())

    def get_tangent_norm(self, i_pos: int) -> RealParam:
        return RealParam(self.hybrid_shape_spline.GetTangentNorm(i_pos))

    def invert_direction(self, i_pos: int) -> None:
        return self.hybrid_shape_spline.InvertDirection(i_pos)

    def remove_all(self) -> None:
        return self.hybrid_shape_spline.RemoveAll()

    def remove_control_point(self, i_pos: int) -> None:
        return self.hybrid_shape_spline.RemoveControlPoint(i_pos)

    def remove_curvature_radius_direction(self, i_pos: int) -> None:
        return self.hybrid_shape_spline.RemoveCurvatureRadiusDirection(i_pos)

    def remove_curvature_radius_value(self, i_pos: int) -> None:
        return self.hybrid_shape_spline.RemoveCurvatureRadiusValue(i_pos)

    def remove_support(self) -> None:
        return self.hybrid_shape_spline.RemoveSupport()

    def remove_tangent_direction(self, i_pos: int) -> None:
        return self.hybrid_shape_spline.RemoveTangentDirection(i_pos)

    def remove_tension(self, i_pos: int) -> None:
        return self.hybrid_shape_spline.RemoveTension(i_pos)

    def replace_point_at_position(self, i_pos: int, i_point: Reference) -> None:
        return self.hybrid_shape_spline.ReplacePointAtPosition(
            i_pos, i_point.com_object
        )

    def set_closing(self, i_closing_type: int) -> None:
        return self.hybrid_shape_spline.SetClosing(i_closing_type)

    def set_point_after(self, i_pos: int, ip_ia_point: Reference) -> None:
        return self.hybrid_shape_spline.SetPointAfter(i_pos, ip_ia_point.com_object)

    def set_point_before(self, i_pos: int, ip_ia_point: Reference) -> None:
        return self.hybrid_shape_spline.SetPointBefore(i_pos, ip_ia_point.com_object)

    def set_point_constraint_explicit(
        self,
        i_pos: int,
        ip_ia_dir_tangency: HybridShapeDirection,
        i_tangency_norm: float,
        i_inverse_tangency: int,
        ip_ia_dir_curvature: HybridShapeDirection,
        i_curvature_radius: float,
    ) -> None:
        return self.hybrid_shape_spline.SetPointConstraintExplicit(
            i_pos,
            ip_ia_dir_tangency.com_object,
            i_tangency_norm,
            i_inverse_tangency,
            ip_ia_dir_curvature.com_object,
            i_curvature_radius,
        )

    def set_point_constraint_from_curve(
        self,
        i_pos: int,
        ip_ia_curve_cst: Reference,
        i_tangency_norm: float,
        i_invert_value: int,
        i_crv_cst_type: int,
    ) -> None:
        return self.hybrid_shape_spline.SetPointConstraintFromCurve(
            i_pos,
            ip_ia_curve_cst.com_object,
            i_tangency_norm,
            i_invert_value,
            i_crv_cst_type,
        )

    def set_spline_type(self, i_spline_type: int) -> None:
        return self.hybrid_shape_spline.SetSplineType(i_spline_type)

    def set_support(self, i_support: Reference) -> None:
        return self.hybrid_shape_spline.SetSupport(i_support.com_object)

    def __repr__(self):
        return f'HybridShapeSpline(name="{self.name}")'
