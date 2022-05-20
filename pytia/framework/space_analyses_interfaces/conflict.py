from pytia.framework.product_structure_interfaces.product import Product
from pytia.framework.system_interfaces.any_object import AnyObject
from pytia.framework.system_interfaces.system_service import SystemService


class Conflict(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.conflict = com_object

    @property
    def comment(self) -> str:
        return self.conflict.Comment

    @comment.setter
    def comment(self, value: str):
        self.conflict.Comment = value

    @property
    def comparison_info(self) -> int:
        return self.conflict.ComparisonInfo

    @property
    def first_product(self) -> Product:
        return Product(self.conflict.FirstProduct)

    @property
    def second_product(self) -> Product:
        return Product(self.conflict.SecondProduct)

    @property
    def status(self) -> int:
        return self.conflict.Status

    @status.setter
    def status(self, value: int):
        self.conflict.Status = value

    @property
    def type(self) -> int:
        return self.conflict.Type

    @property
    def value(self) -> float:
        return self.conflict.Value

    def get_first_point_coordinates(self) -> tuple:
        vba_function_name = "get_first_point_coordinates"
        vba_code = """
        Public Function get_first_point_coordinates(conflict)
            Dim oCoordinates(2)
            conflict.GetFirstPointCoordinates oCoordinates
            get_first_point_coordinates = oCoordinates
        End Function
        """
        system_service = self.application.system_service
        return system_service.evaluate(
            vba_code, 0, vba_function_name, [self.com_object]
        )

    def get_second_point_coordinates(self) -> tuple:
        vba_function_name = "get_second_point_coordinates"
        vba_code = """
        Public Function get_second_point_coordinates(conflict)
            Dim oCoordinates (2)
            conflict.GetSecondPointCoordinates oCoordinates
            get_second_point_coordinates = oCoordinates
        End Function
        """
        system_service = self.application.system_service
        return system_service.evaluate(
            vba_code, 0, vba_function_name, [self.com_object]
        )

    def __repr__(self):
        return f'Conflict(name="{ self.name }")'
