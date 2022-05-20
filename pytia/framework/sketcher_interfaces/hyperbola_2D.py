from pytia.framework.sketcher_interfaces.curve_2D import Curve2D
from pytia.framework.system_interfaces.system_service import SystemService


class Hyperbola2D(Curve2D):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hyperbola_2d = com_object

    @property
    def imaginary_radius(self) -> float:
        return self.hyperbola_2d.ImaginaryRadius

    @property
    def radius(self) -> float:
        return self.hyperbola_2d.Radius

    def get_axis(self) -> tuple:
        vba_function_name = "get_axis"
        vba_code = """
        Public Function get_axis(hyperbola_2d)
            Dim oAxis (1)
            hyperbola_2d.GetAxis oAxis
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
        Public Function get_center(hyperbola_2d)
            Dim oCenter (1)
            hyperbola_2d.GetCenter oCenter
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
        i_major_radius: float,
        i_minor_radius: float,
    ) -> None:
        return self.hyperbola_2d.SetData(
            i_center_x, i_center_y, i_axis_x, i_axis_y, i_major_radius, i_minor_radius
        )

    def __repr__(self):
        return f'Hyperbola2D(name="{self.name}")'
