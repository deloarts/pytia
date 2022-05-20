from pytia.framework.sketcher_interfaces.curve_2D import Curve2D
from pytia.framework.sketcher_interfaces.point_2D import Point2D
from pytia.framework.system_interfaces.system_service import SystemService


class Circle2D(Curve2D):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.circle_2d = com_object

    @property
    def center_point(self) -> Point2D:
        return Point2D(self.circle_2d.CenterPoint)

    @center_point.setter
    def center_point(self, value: Point2D):
        self.circle_2d.CenterPoint = value

    @property
    def radius(self) -> float:
        return self.circle_2d.Radius

    def get_center(self) -> tuple:
        vba_function_name = "get_center"
        vba_code = """
        Public Function get_center(circle2_d)
            Dim oData (2)
            circle2_d.GetCenter oData
            get_center = oData
        End Function
        """
        system_service = self.application.system_service
        return system_service.evaluate(
            vba_code, 0, vba_function_name, [self.com_object]
        )

    def set_data(self, i_center_x: float, i_center_y: float, i_radius: float) -> None:
        return self.circle_2d.SetData(i_center_x, i_center_y, i_radius)

    def __repr__(self):
        return f'Circle2D(name="{self.name}")'
