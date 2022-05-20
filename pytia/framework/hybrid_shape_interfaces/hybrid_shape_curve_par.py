from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.knowledge_interfaces.length import Length
from pytia.framework.mec_mod_interfaces.hybrid_shape import HybridShape
from pytia.framework.system_interfaces.system_service import SystemService


class HybridShapeCurvePar(HybridShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_curve_par = com_object

    @property
    def curve_offseted(self) -> Reference:
        return Reference(self.hybrid_shape_curve_par.CurveOffseted)

    @curve_offseted.setter
    def curve_offseted(self, reference_curve: Reference):
        self.hybrid_shape_curve_par.CurveOffseted = reference_curve.com_object

    @property
    def curve_par_law(self) -> Reference:
        return Reference(self.hybrid_shape_curve_par.CurveParLaw)

    @curve_par_law.setter
    def curve_par_law(self, value: Reference):
        self.hybrid_shape_curve_par.CurveParLaw = value.com_object

    @property
    def curve_par_type(self) -> int:
        return self.hybrid_shape_curve_par.CurveParType

    @curve_par_type.setter
    def curve_par_type(self, value: int):
        self.hybrid_shape_curve_par.CurveParType = value

    @property
    def geodesic(self) -> bool:
        return self.hybrid_shape_curve_par.Geodesic

    @geodesic.setter
    def geodesic(self, value: bool):
        self.hybrid_shape_curve_par.Geodesic = value

    @property
    def invert_direction(self) -> bool:
        return self.hybrid_shape_curve_par.InvertDirection

    @invert_direction.setter
    def invert_direction(self, value: bool):
        self.hybrid_shape_curve_par.InvertDirection = value

    @property
    def invert_mapping_law(self) -> bool:
        return self.hybrid_shape_curve_par.InvertMappingLaw

    @invert_mapping_law.setter
    def invert_mapping_law(self, value: bool):
        self.hybrid_shape_curve_par.InvertMappingLaw = value

    @property
    def keep_both_sides(self) -> bool:
        return self.hybrid_shape_curve_par.KeepBothSides

    @keep_both_sides.setter
    def keep_both_sides(self, value: bool):
        self.hybrid_shape_curve_par.KeepBothSides = value

    @property
    def law_type(self) -> int:
        return self.hybrid_shape_curve_par.LawType

    @law_type.setter
    def law_type(self, value: int):
        self.hybrid_shape_curve_par.LawType = value

    @property
    def maximum_deviation_value(self) -> float:
        return self.hybrid_shape_curve_par.MaximumDeviationValue

    @maximum_deviation_value.setter
    def maximum_deviation_value(self, value: float):
        self.hybrid_shape_curve_par.MaximumDeviationValue = value

    @property
    def offset(self) -> Length:
        return Length(self.hybrid_shape_curve_par.Offset)

    @property
    def offset2(self) -> Length:
        return Length(self.hybrid_shape_curve_par.Offset2)

    @property
    def other_side(self) -> Reference:
        return Reference(self.hybrid_shape_curve_par.OtherSide)

    @property
    def passing_point(self) -> Reference:
        return Reference(self.hybrid_shape_curve_par.PassingPoint)

    @passing_point.setter
    def passing_point(self, reference_point: Reference):
        self.hybrid_shape_curve_par.PassingPoint = reference_point.com_object

    @property
    def smoothing_type(self) -> int:
        return self.hybrid_shape_curve_par.SmoothingType

    @smoothing_type.setter
    def smoothing_type(self, value: int):
        self.hybrid_shape_curve_par.SmoothingType = value

    @property
    def support(self) -> Reference:
        return Reference(self.hybrid_shape_curve_par.Support)

    @support.setter
    def support(self, reference_support: Reference):
        self.hybrid_shape_curve_par.Support = reference_support.com_object

    @property
    def p_3d_smoothing(self) -> bool:
        return self.hybrid_shape_curve_par.p3DSmoothing

    @p_3d_smoothing.setter
    def p_3d_smoothing(self, value: bool):
        self.hybrid_shape_curve_par.p3DSmoothing = value

    def get_plane_normal(self) -> tuple:
        vba_function_name = "get_plane_normal"
        vba_code = """
        Public Function get_plane_normal(hybrid_shape_curve_par)
            Dim oNormal (2)
            hybrid_shape_curve_par.GetPlaneNormal oNormal
            get_plane_normal = oNormal
        End Function
        """
        system_service = self.application.system_service
        return system_service.evaluate(
            vba_code, 0, vba_function_name, [self.com_object]
        )

    def put_plane_normal(self, i_normal: tuple) -> None:
        return self.hybrid_shape_curve_par.PutPlaneNormal(i_normal)

    def __repr__(self):
        return f'HybridShapeCurvePar(name="{self.name}")'
