from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.knowledge_interfaces.angle import Angle
from pytia.framework.system_interfaces.any_object import AnyObject


class AxisSystem(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.axis_system = com_object

    @property
    def axis_rotation_angle(self) -> Angle:
        return Angle(self.axis_system.AxisRotationAngle)

    @property
    def axis_rotation_reference(self) -> Reference:
        return Reference(self.axis_system.AxisRotationReference)

    @axis_rotation_reference.setter
    def axis_rotation_reference(self, value: Reference):
        self.axis_system.AxisRotationReference = value

    @property
    def is_current(self) -> bool:
        return self.axis_system.IsCurrent

    @is_current.setter
    def is_current(self, value: bool):
        self.axis_system.IsCurrent = value

    @property
    def origin_point(self) -> Reference:
        return Reference(self.axis_system.OriginPoint)

    @origin_point.setter
    def origin_point(self, value: Reference):
        self.axis_system.OriginPoint = value

    @property
    def origin_type(self) -> int:
        return self.axis_system.OriginType

    @origin_type.setter
    def origin_type(self, value: int):
        self.axis_system.OriginType = value

    @property
    def type(self) -> int:
        return self.axis_system.Type

    @type.setter
    def type(self, value: int):
        self.axis_system.Type = value

    @property
    def x_axis_direction(self) -> Reference:
        return Reference(self.axis_system.XAxisDirection)

    @x_axis_direction.setter
    def x_axis_direction(self, value: Reference):
        self.axis_system.XAxisDirection = value

    @property
    def x_axis_type(self) -> int:
        return self.axis_system.XAxisType

    @x_axis_type.setter
    def x_axis_type(self, value: int):
        self.axis_system.XAxisType = value

    @property
    def y_axis_direction(self) -> Reference:
        return Reference(self.axis_system.YAxisDirection)

    @y_axis_direction.setter
    def y_axis_direction(self, value: Reference):
        self.axis_system.YAxisDirection = value

    @property
    def y_axis_type(self) -> int:
        return self.axis_system.YAxisType

    @y_axis_type.setter
    def y_axis_type(self, value: int):
        self.axis_system.YAxisType = value

    @property
    def z_axis_direction(self) -> Reference:
        return Reference(self.axis_system.ZAxisDirection)

    @z_axis_direction.setter
    def z_axis_direction(self, value: Reference):
        self.axis_system.ZAxisDirection = value

    @property
    def z_axis_type(self) -> int:
        return self.axis_system.ZAxisType

    @z_axis_type.setter
    def z_axis_type(self, value: int):
        self.axis_system.ZAxisType = value

    def get_euler_angles(self) -> tuple:
        vba_function_name = "get_euler_angles"
        vba_code = """
        Public Function get_euler_angles(axis_system)
            Dim oFirstAngle (2)
            axis_system.GetEulerAngles oFirstAngle
            get_euler_angles = oFirstAngle
        End Function
        """
        system_service = self.application.system_service
        return system_service.evaluate(
            vba_code, 0, vba_function_name, [self.com_object]
        )

    def get_origin(self) -> tuple:
        vba_function_name = "get_origin"
        vba_code = """
        Public Function get_origin(axis_system)
            Dim oOrigin (2)
            axis_system.GetOrigin oOrigin
            get_origin = oOrigin
        End Function
        """
        system_service = self.application.system_service
        return system_service.evaluate(
            vba_code, 0, vba_function_name, [self.com_object]
        )

    def get_vectors(self) -> tuple:
        vba_function_name = "get_vectors"
        vba_code = """
        Public Function get_vectors(axis_system)
            Dim oVectorX (2)
            axis_system.GetVectors oVectorX
            get_vectors = oVectorX
        End Function
        """
        system_service = self.application.system_service
        return system_service.evaluate(
            vba_code, 0, vba_function_name, [self.com_object]
        )

    def get_x_axis(self) -> tuple:
        vba_function_name = "get_x_axis"
        vba_code = """
        Public Function get_x_axis(axis_system)
            Dim oXAxis (2)
            axis_system.GetXAxis oXAxis
            get_x_axis = oXAxis
        End Function
        """
        system_service = self.application.system_service
        return system_service.evaluate(
            vba_code, 0, vba_function_name, [self.com_object]
        )

    def get_y_axis(self) -> tuple:
        vba_function_name = "get_y_axis"
        vba_code = """
        Public Function get_y_axis(axis_system)
            Dim oYAxis (2)
            axis_system.GetYAxis oYAxis
            get_y_axis = oYAxis
        End Function
        """
        system_service = self.application.system_service
        return system_service.evaluate(
            vba_code, 0, vba_function_name, [self.com_object]
        )

    def get_z_axis(self) -> tuple:
        vba_function_name = "get_z_axis"
        vba_code = """
        Public Function get_z_axis(axis_system)
            Dim oZAxis (2)
            axis_system.GetZAxis oZAxis
            get_z_axis = oZAxis
        End Function
        """
        system_service = self.application.system_service
        return system_service.evaluate(
            vba_code, 0, vba_function_name, [self.com_object]
        )

    def put_origin(self, i_origin: tuple) -> None:
        return self.axis_system.PutOrigin(i_origin)

    def put_vectors(self, i_vector_x: tuple, i_vector_y: tuple) -> None:
        return self.axis_system.PutVectors(i_vector_x, i_vector_y)

    def put_x_axis(self, i_x_axis: tuple) -> None:
        return self.axis_system.PutXAxis(i_x_axis)

    def put_y_axis(self, i_y_axis: tuple) -> None:
        return self.axis_system.PutYAxis(i_y_axis)

    def put_z_axis(self, i_z_axis: tuple) -> None:
        return self.axis_system.PutZAxis(i_z_axis)

    def __repr__(self):
        return f'AxisSystem(name="{self.name}")'
