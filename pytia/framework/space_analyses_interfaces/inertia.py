from pytia.framework.system_interfaces.any_object import AnyObject
from pytia.framework.system_interfaces.system_service import SystemService


class Inertia(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.inertia = com_object

    @property
    def density(self) -> float:
        return self.inertia.Density

    @density.setter
    def density(self, value: float):
        self.inertia.Density = value

    @property
    def granularity_mode(self) -> int:
        return self.inertia.GranularityMode

    @granularity_mode.setter
    def granularity_mode(self, value: int):
        self.inertia.GranularityMode = value

    @property
    def mass(self) -> float:
        return self.inertia.Mass

    def get_cog_position(self) -> tuple:
        vba_function_name = "get_cog_position"
        vba_code = """
        Public Function get_cog_position(inertia)
            Dim oCoordinates (2)
            inertia.GetCOGPosition oCoordinates
            get_cog_position = oCoordinates
        End Function
        """
        system_service = self.application.system_service
        return system_service.evaluate(
            vba_code, 0, vba_function_name, [self.com_object]
        )

    def get_inertia_matrix(self) -> tuple:
        vba_function_name = "get_inertia_matrix"
        vba_code = """
        Public Function get_inertia_matrix(inertia)
            Dim oMatrix (8)
            inertia.GetInertiaMatrix oMatrix
            get_inertia_matrix = oMatrix
        End Function
        """
        system_service = self.application.system_service
        return system_service.evaluate(
            vba_code, 0, vba_function_name, [self.com_object]
        )

    def get_principal_axes(self) -> tuple:
        vba_function_name = "get_principal_axes"
        vba_code = """
        Public Function get_principal_axes(inertia)
            Dim oComponents(8)
            inertia.GetPrincipalAxes oComponents
            get_principal_axes = oComponents
        End Function
        """
        system_service = self.application.system_service
        return system_service.evaluate(
            vba_code, 0, vba_function_name, [self.com_object]
        )

    def get_principal_moments(self) -> tuple:
        vba_function_name = "get_principal_moments"
        vba_code = """
        Public Function get_principal_moments(inertia)
            Dim oValues (2)
            inertia.GetPrincipalMoments oValues
            get_principal_moments = oValues
        End Function
        """
        system_service = self.application.system_service
        return system_service.evaluate(
            vba_code, 0, vba_function_name, [self.com_object]
        )

    def __repr__(self):
        return f'Inertia(name="{ self.name }")'
