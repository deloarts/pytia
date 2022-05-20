from pytia.framework.sketcher_interfaces.curve_2D import Curve2D
from pytia.framework.sketcher_interfaces.point_2D import Point2D
from pytia.framework.system_interfaces.system_service import SystemService


class Spline2D(Curve2D):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.spline_2d = com_object

    def get_control_points(self) -> tuple:
        vba_function_name = "get_control_points"
        vba_code = """
        Public Function get_control_points(spline2_d)
            Dim oCtrlPoints (1)
            spline2_d.GetControlPoints oCtrlPoints
            get_control_points = oCtrlPoints
        End Function
        """
        system_service = self.application.system_service
        return system_service.evaluate(
            vba_code, 0, vba_function_name, [self.com_object]
        )

    def get_number_of_control_points(self) -> float:
        return self.spline_2d.GetNumberOfControlPoints()

    def insert_control_point_after(
        self, i_ctrl_point: Point2D, i_position: int
    ) -> None:
        return self.spline_2d.InsertControlPointAfter(
            i_ctrl_point.com_object, i_position
        )

    def __repr__(self):
        return f'Spline2D(name="{self.name}")'
