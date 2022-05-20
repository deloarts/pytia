from pytia.framework.mec_mod_interfaces.hybrid_shape import HybridShape
from pytia.framework.system_interfaces.system_service import SystemService


class Point(HybridShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.point_ = com_object

    def get_coordinates(self) -> tuple:
        vba_function_name = "get_coordinates"
        vba_code = """
        Public Function get_coordinates(point)
            Dim oCoordinates (2)
            point.GetCoordinates oCoordinates
            get_coordinates = oCoordinates
        End Function
        """
        system_service = self.application.system_service
        return system_service.evaluate(
            vba_code, 0, vba_function_name, [self.com_object]
        )

    def set_coordinates(self, o_coordinates: tuple) -> None:
        return self.point_.SetCoordinates(o_coordinates)

    def __repr__(self):
        return f'Point(name="{self.name}")'
