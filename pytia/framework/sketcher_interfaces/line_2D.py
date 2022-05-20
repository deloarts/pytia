from pytia.framework.sketcher_interfaces.curve_2D import Curve2D
from pytia.framework.system_interfaces.system_service import SystemService


class Line2D(Curve2D):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.line_2d = com_object

    def get_direction(self) -> tuple:
        vba_function_name = "get_direction"
        vba_code = """
        Public Function get_direction(line2_d)
            Dim oDirection(2)
            line2_d.GetDirection oDirection
            get_direction = oDirection
        End Function
        """
        system_service = self.application.system_service
        return system_service.evaluate(
            vba_code, 0, vba_function_name, [self.com_object]
        )

    def get_origin(self) -> tuple:
        vba_function_name = "get_origin"
        vba_code = """
        Public Function get_origin(line2_d)
            Dim oOrigin(1)
            line2_d.GetOrigin oOrigin
            get_origin = oOrigin
        End Function
        """
        system_service = self.application.system_service
        return system_service.evaluate(
            vba_code, 0, vba_function_name, [self.com_object]
        )

    def set_data(
        self, i_x: float, i_y: float, i_x_direction: float, i_y_direction: float
    ) -> None:
        return self.line_2d.SetData(i_x, i_y, i_x_direction, i_y_direction)

    def __repr__(self):
        return f'Line2D(name="{self.name}")'
