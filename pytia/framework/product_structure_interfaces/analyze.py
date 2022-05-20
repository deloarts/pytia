from pytia.framework.system_interfaces.any_object import AnyObject
from pytia.framework.system_interfaces.system_service import SystemService


class Analyze(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.analyze = com_object

    @property
    def mass(self) -> float:
        return self.analyze.Mass

    @property
    def volume(self) -> float:
        return self.analyze.Volume

    @property
    def wet_area(self) -> float:
        return self.analyze.WetArea

    def get_gravity_center(self):
        vba_function_name = "get_gravity_center"
        vba_code = """
        Public Function get_gravity_center(analyze)
            Dim oGravityCenterCoordinatesArray (2)
            analyze.GetGravityCenter oGravityCenterCoordinatesArray
            get_gravity_center = oGravityCenterCoordinatesArray
        End Function
        """
        system_service = self.application.system_service
        return system_service.evaluate(
            vba_code, 0, vba_function_name, [self.com_object]
        )

    def get_inertia(self):
        vba_function_name = "get_inertia"
        vba_code = """
        Public Function get_inertia(analyze)
            Dim oInertiaMatrixArray (8)
            analyze.GetInertia oInertiaMatrixArray
            get_inertia = oInertiaMatrixArray
        End Function
        """
        system_service = self.application.system_service
        return system_service.evaluate(
            vba_code, 0, vba_function_name, [self.com_object]
        )

    def __repr__(self):
        return f'Analyze(name="{self.name}")'
