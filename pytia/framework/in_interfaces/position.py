from pytia.framework.in_interfaces.move import Move
from pytia.framework.system_interfaces.system_service import SystemService


class Position(Move):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.position = com_object

    def get_components(self) -> tuple:
        vba_function_name = "get_components"
        vba_code = """
        Public Function get_components(position)
            Dim oAxisComponentsArray(11)
            position.GetComponents oAxisComponentsArray
            get_components = oAxisComponentsArray
        End Function
        """
        system_service = self.application.system_service
        return system_service.evaluate(
            vba_code, 0, vba_function_name, [self.com_object]
        )

    def set_components(self, i_axis_components_array: tuple) -> None:
        return self.position.SetComponents(i_axis_components_array)

    def __repr__(self):
        return f'Position(name="{self.name}")'
