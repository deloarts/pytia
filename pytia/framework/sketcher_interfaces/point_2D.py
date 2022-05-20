from pytia.framework.sketcher_interfaces.geometry_2D import Geometry2D
from pytia.framework.system_interfaces.system_service import SystemService


class Point2D(Geometry2D):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.point_2d = com_object

    def get_coordinates(self) -> tuple:
        vba_function_name = "get_coordinates"
        vba_code = """
        Public Function get_coordinates(point2_d)
            Dim oPoint(1)
            point2_d.GetCoordinates oPoint
            get_coordinates = oPoint
        End Function
        """
        system_service = self.application.system_service
        return system_service.evaluate(
            vba_code, 0, vba_function_name, [self.com_object]
        )

    def set_data(self, i_x: float, i_y: float) -> None:
        return self.point_2d.SetData(i_x, i_y)

    def __repr__(self):
        return f'Point2D(name="{self.name}")'
