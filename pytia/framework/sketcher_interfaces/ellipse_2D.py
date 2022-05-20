from pytia.framework.sketcher_interfaces.curve_2D import Curve2D
from pytia.framework.sketcher_interfaces.point_2D import Point2D
from pytia.framework.system_interfaces.system_service import SystemService


class Ellipse2D(Curve2D):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.ellipse_2d = com_object

    @property
    def center_point(self) -> Point2D:
        return Point2D(self.ellipse_2d.CenterPoint)

    @center_point.setter
    def center_point(self, value: Point2D):
        self.ellipse_2d.CenterPoint = value

    @property
    def major_radius(self) -> float:
        return self.ellipse_2d.MajorRadius

    @property
    def minor_radius(self) -> float:
        return self.ellipse_2d.MinorRadius

    def get_center(self) -> tuple:
        vba_function_name = "get_center"
        vba_code = """
        Public Function get_center(ellipse2_d)
            Dim oCenter (1)
            ellipse2_d.GetCenter oCenter
            get_center = oCenter
        End Function
        """
        system_service = self.application.system_service
        return system_service.evaluate(
            vba_code, 0, vba_function_name, [self.com_object]
        )

    def get_major_axis(self) -> tuple:
        vba_function_name = "get_major_axis"
        vba_code = """
        Public Function get_major_axis(ellipse2_d)
            Dim oMajorAxis (1)
            ellipse2_d.GetMajorAxis oMajorAxis
            get_major_axis = oMajorAxis
        End Function
        """
        system_service = self.application.system_service
        return system_service.evaluate(
            vba_code, 0, vba_function_name, [self.com_object]
        )

    def get_minor_axis(self) -> tuple:
        vba_function_name = "get_minor_axis"
        vba_code = """
        Public Function get_minor_axis(ellipse2_d)
            Dim oMajorAxis (1)
            ellipse2_d.GetMinorAxis oMajorAxis
            get_minor_axis = oMajorAxis
        End Function
        """
        system_service = self.application.system_service
        return system_service.evaluate(
            vba_code, 0, vba_function_name, [self.com_object]
        )

    def set_data(
        self,
        i_center_x: float,
        i_center_y: float,
        i_major_x: float,
        i_major_y: float,
        i_major_radius: float,
        i_minor_radius: float,
    ) -> None:
        return self.ellipse_2d.SetData(
            i_center_x, i_center_y, i_major_x, i_major_y, i_major_radius, i_minor_radius
        )

    def __repr__(self):
        return f'Ellipse2D(name="{self.name}")'
