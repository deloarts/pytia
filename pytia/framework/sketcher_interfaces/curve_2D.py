from pytia.framework.sketcher_interfaces.geometry_2D import Geometry2D
from pytia.framework.sketcher_interfaces.point_2D import Point2D
from pytia.framework.system_interfaces.system_service import SystemService


class Curve2D(Geometry2D):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.curve_2d = com_object

    @property
    def continuity(self) -> int:
        return self.curve_2d.Continuity

    @property
    def end_point(self) -> Point2D:
        return Point2D(self.curve_2d.EndPoint)

    @end_point.setter
    def end_point(self, end_point: Point2D):
        self.curve_2d.EndPoint = end_point.com_object

    @property
    def period(self) -> float:
        return self.curve_2d.Period

    @property
    def start_point(self) -> Point2D:
        return Point2D(self.curve_2d.StartPoint)

    @start_point.setter
    def start_point(self, start_point: Point2D):
        self.curve_2d.StartPoint = start_point.com_object

    def get_curvature(self, i_param: float) -> tuple:
        vba_function_name = "get_curvature"
        vba_code = """
        Public Function get_curvature(curve2_d, i_param)
            Dim oCurvature (2)
            curve2_d.GetCurvature i_param, oCurvature
            get_curvature = oCurvature
        End Function
        """
        system_service = self.application.system_service
        return system_service.evaluate(
            vba_code, 0, vba_function_name, [self.com_object, i_param]
        )

    def get_derivatives(self, i_param: float) -> tuple:
        vba_function_name = "get_derivatives"
        vba_code = """
        Public Function get_derivatives(curve2_d, i_param)
            Dim oDerivative(2)
            curve2_d.GetDerivatives iParam, oDerivative
            get_derivatives = oDerivative
        End Function
        """
        system_service = self.application.system_service
        return system_service.evaluate(
            vba_code, 0, vba_function_name, [self.com_object, i_param]
        )

    def get_end_points(self) -> tuple:
        vba_function_name = "get_end_points"
        vba_code = """
        Public Function get_end_points(curve2_d)
            Dim oEndPoints (3)
            curve2_d.GetEndPoints oEndPoints
            get_end_points = oEndPoints
        End Function
        """
        system_service = self.application.system_service
        return system_service.evaluate(
            vba_code, 0, vba_function_name, [self.com_object]
        )

    def get_length_at_param(self, i_from_param: float, i_to_param: float) -> float:
        return self.curve_2d.GetLengthAtParam(i_from_param, i_to_param)

    def get_param_at_length(self, i_from_param: float, i_length: float) -> float:
        return self.curve_2d.GetParamAtLength(i_from_param, i_length)

    def get_param_extents(self) -> tuple:
        vba_function_name = "get_param_extents"
        vba_code = """
        Public Function get_param_extents(curve2_d)
            Dim oParams(1)
            curve2_d.GetParamExtents oParams
            get_param_extents = oParams
        End Function
        """
        system_service = self.application.system_service
        return system_service.evaluate(
            vba_code, 0, vba_function_name, [self.com_object]
        )

    def get_point_at_param(self, i_param: float) -> tuple:
        vba_function_name = "get_point_at_param"
        vba_code = """
        Public Function get_point_at_param(curve2_d, i_param)
            Dim oPoint (1)
            curve2_d.GetPointAtParam i_param, oPoint
            get_point_at_param = oPoint
        End Function
        """
        system_service = self.application.system_service
        return system_service.evaluate(
            vba_code, 0, vba_function_name, [self.com_object, i_param]
        )

    def get_range_box(self) -> tuple:
        vba_function_name = "get_range_box"
        vba_code = """
        Public Function get_range_box(curve2_d)
            Dim oBoundPoint(3)
            curve2_d.GetRangeBox oBoundPoint
            get_range_box = oBoundPoint
        End Function
        """
        system_service = self.application.system_service
        return system_service.evaluate(
            vba_code, 0, vba_function_name, [self.com_object]
        )

    def get_tangent(self, i_param: float) -> tuple:
        vba_function_name = "get_tangent"
        vba_code = """
        Public Function get_tangent(curve2_d, i_param)
            Dim oTangency(1)
            curve2_d.GetTangent i_param, oTangency
            get_tangent = oTangency
        End Function
        """
        system_service = self.application.system_service
        return system_service.evaluate(
            vba_code, 0, vba_function_name, [self.com_object, i_param]
        )

    def is_periodic(self) -> bool:
        return self.curve_2d.IsPeriodic()

    def __repr__(self):
        return f'Curve2D(name="{self.name}")'
