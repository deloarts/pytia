from pytia.framework.sketcher_interfaces.point_2D import Point2D
from pytia.framework.system_interfaces.system_service import SystemService


class ControlPoint2D(Point2D):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.control_point_2d = com_object

    @property
    def curvature(self) -> float:
        return self.control_point_2d.Curvature

    @curvature.setter
    def curvature(self, value: float):
        self.control_point_2d.Curvature = value

    def get_tangent(self) -> tuple:
        vba_function_name = "get_tangent"
        vba_code = """
        Public Function get_tangent(control_point2_d)
            Dim oTangent (1)
            control_point2_d.GetTangent oTangent
            get_tangent = oTangent
        End Function
        """
        system_service = self.application.system_service
        return system_service.evaluate(
            vba_code, 0, vba_function_name, [self.com_object]
        )

    def set_tangent(self, i_tangent_x: float, i_tangent_y: float) -> None:
        return self.control_point_2d.SetTangent(i_tangent_x, i_tangent_y)

    def unset_curvature(self) -> None:
        return self.control_point_2d.UnsetCurvature()

    def unset_tangent(self) -> None:
        return self.control_point_2d.UnsetTangent()

    def __repr__(self):
        return f'ControlPoint2D(name="{self.name}")'
