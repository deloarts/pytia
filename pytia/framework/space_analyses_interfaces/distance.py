from pytia.framework.navigator_interfaces.annotated_views import AnnotatedViews
from pytia.framework.navigator_interfaces.group import Group
from pytia.framework.navigator_interfaces.marker_3Ds import Marker3Ds
from pytia.framework.product_structure_interfaces.product import Product
from pytia.framework.system_interfaces.any_object import AnyObject
from pytia.framework.system_interfaces.system_service import SystemService


class Distance(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.distance = com_object

    @property
    def accuracy(self) -> float:
        return self.distance.Accuracy

    @accuracy.setter
    def accuracy(self, value: float):
        self.distance.Accuracy = value

    @property
    def annotated_views(self) -> AnnotatedViews:
        return AnnotatedViews(self.distance.AnnotatedViews)

    @property
    def computation_type(self) -> int:
        return self.distance.ComputationType

    @computation_type.setter
    def computation_type(self, value: int):
        self.distance.ComputationType = value

    @property
    def first_group(self) -> Group:
        return Group(self.distance.FirstGroup)

    @first_group.setter
    def first_group(self, value: Group):
        self.distance.FirstGroup = value

    @property
    def first_product(self) -> Product:
        return Product(self.distance.FirstProduct)

    @property
    def is_defined(self) -> int:
        return self.distance.IsDefined

    @property
    def marker_3ds(self) -> Marker3Ds:
        return Marker3Ds(self.distance.Marker3Ds)

    @property
    def maximum_distance(self) -> float:
        return self.distance.MaximumDistance

    @maximum_distance.setter
    def maximum_distance(self, value: float):
        self.distance.MaximumDistance = value

    @property
    def measure_type(self) -> int:
        return self.distance.MeasureType

    @measure_type.setter
    def measure_type(self, value: int):
        self.distance.MeasureType = value

    @property
    def minimum_distance(self) -> float:
        return self.distance.MinimumDistance

    @minimum_distance.setter
    def minimum_distance(self, value: float):
        self.distance.MinimumDistance = value

    @property
    def second_group(self) -> Group:
        return Group(self.distance.SecondGroup)

    @second_group.setter
    def second_group(self, value: Group):
        self.distance.SecondGroup = value

    @property
    def second_product(self) -> Product:
        return Product(self.distance.SecondProduct)

    @property
    def value(self) -> float:
        return self.distance.Value

    def compute(self) -> None:
        return self.distance.Compute()

    def get_first_point_coordinates(self) -> tuple:
        vba_function_name = "get_first_point_coordinates"
        vba_code = """
        Public Function get_first_point_coordinates(distance)
            Dim oCoordinates (2)
            distance.GetFirstPointCoordinates oCoordinates
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
        Public Function get_second_point_coordinates(distance)
            Dim oCoordinates (2)
            distance.GetSecondPointCoordinates oCoordinates
            get_second_point_coordinates = oCoordinates
        End Function
        """
        system_service = self.application.system_service
        return system_service.evaluate(
            vba_code, 0, vba_function_name, [self.com_object]
        )

    def __repr__(self):
        return f'Distance(name="{self.name}")'
