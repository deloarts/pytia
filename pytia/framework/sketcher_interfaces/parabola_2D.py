from pytia.framework.sketcher_interfaces.curve_2D import Curve2D
from pytia.framework.system_interfaces.system_service import SystemService


class Parabola2D(Curve2D):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.parabola_2d = com_object

    @property
    def focal_distance(self) -> float:
        return self.parabola_2d.FocalDistance

    def get_axis(self) -> tuple:
        vba_function_name = "get_axis"
        vba_code = """
        Public Function get_axis(parabola2_d)
            Dim oAxis (1)
            parabola2_d.GetAxis oAxis
            get_axis = oAxis
        End Function
        """
        system_service = self.application.system_service
        return system_service.evaluate(
            vba_code, 0, vba_function_name, [self.com_object]
        )

    def get_center(self) -> tuple:
        vba_function_name = "get_center"
        vba_code = """
        Public Function get_center(parabola2_d)
            Dim oCenter(1)
            parabola2_d.GetCenter oCenter
            get_center = oCenter
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
        i_axis_x: float,
        i_axis_y: float,
        i_focal_distance: float,
    ) -> None:
        return self.parabola_2d.SetData(
            i_center_x, i_center_y, i_axis_x, i_axis_y, i_focal_distance
        )

    def __repr__(self):
        return f'Parabola2D(name="{self.name}")'
