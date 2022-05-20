from pytia.framework.system_interfaces.any_object import AnyObject


class PrintArea(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.print_area = com_object

    @property
    def activation_state(self) -> bool:
        return self.print_area.ActivationState

    @activation_state.setter
    def activation_state(self, value: bool):
        self.print_area.ActivationState = value

    @property
    def area_height(self) -> float:
        return self.print_area.Area_Height

    @area_height.setter
    def area_height(self, value: float):
        self.print_area.AreaHeigth = value

    @property
    def area_low_x(self) -> float:
        return self.print_area.AreaLowX

    @area_low_x.setter
    def area_low_x(self, value: float):
        self.print_area.AreaLowX = value

    @property
    def area_low_y(self) -> float:
        return self.print_area.AreaLowY

    @area_low_y.setter
    def area_low_y(self, value: float):
        self.print_area.AreaLowY = value

    @property
    def area_width(self) -> float:
        return self.print_area.AreaWidth

    @area_width.setter
    def area_width(self, value: float):
        self.print_area.AreaWidth = float

    def get_area(
        self, o_x: float, o_y: float, o_width: float, o_height: float, o_activated: bool
    ) -> None:
        vba_function_name = "get_area"
        vba_code = """
        Public Function get_area(print_area)
            Dim area (5)
            print_area.GetArea area
            get_area = area
        End Function
        """
        system_service = self.application.system_service
        return system_service.evaluate(
            vba_code, 0, vba_function_name, [self.com_object]
        )

    def set_area(self, i_x: float, i_y: float, i_width: float, i_height: float) -> None:
        return self.print_area.SetArea(i_x, i_y, i_width, i_height)

    def __repr__(self):
        return f'PrintArea(name="{ self.name }")'
