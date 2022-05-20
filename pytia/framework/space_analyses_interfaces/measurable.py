from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.system_interfaces.any_object import AnyObject
from pytia.framework.system_interfaces.system_service import SystemService


class Measurable(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.measurable = com_object

    @property
    def angle(self) -> float:
        return self.measurable.Angle

    @property
    def area(self) -> float:
        return self.measurable.Area

    @property
    def geometry_name(self) -> int:
        return self.measurable.GeometryName

    @property
    def length(self) -> float:
        return self.measurable.Length

    @property
    def perimeter(self) -> float:
        return self.measurable.Perimeter

    @property
    def radius(self) -> float:
        return self.measurable.Radius

    @property
    def volume(self) -> float:
        return self.measurable.Volume

    def get_angle_between(self, i_measured_item: Reference) -> float:
        return self.measurable.GetAngleBetween(i_measured_item.com_object)

    def get_axis(self):
        vba_function_name = "get_axis"
        vba_function = "GetAxis"
        vba_code = f"""   
        Public Function {vba_function_name}(measurable)
            Dim AxisVector (2)
            measurable.{vba_function} AxisVector
            {vba_function_name} = AxisVector
        End Function
        """
        system_service = self.application.system_service
        result = system_service.evaluate(
            vba_code, 0, vba_function_name, [self.measurable]
        )
        return result

    def get_axis_system(self):
        vba_function_name = "get_axis_system"
        vba_function = "GetAxisSystem"
        vba_code = f"""        
            Public Function {vba_function_name}(measurable)
                Dim Components (11)
                measurable.{vba_function} Components
                {vba_function_name} = Components
            End Function
            """
        system_service = self.application.system_service
        result = system_service.evaluate(
            vba_code, 0, vba_function_name, [self.measurable]
        )
        return result

    def get_cog(self):
        vba_function_name = "create_cog"
        vba_function = "GetCOG"
        vba_code = f"""        
        Public Function {vba_function_name}(measurable)
            Dim coord(2)
            measurable.{vba_function} coord
            {vba_function_name} = coord
        End Function
        """
        system_service = self.application.system_service
        result = system_service.evaluate(
            vba_code, 0, vba_function_name, [self.measurable]
        )
        return result

    def get_center(self):
        vba_function_name = "get_center"
        vba_function = "GetCenter"
        vba_code = f"""        
        Public Function {vba_function_name}(measurable)
            Dim Coordinates (2)
            measurable.{vba_function} Coordinates
            {vba_function_name} = Coordinates
        End Function
        """
        system_service = self.application.system_service
        result = system_service.evaluate(
            vba_code, 0, vba_function_name, [self.measurable]
        )
        return result

    def get_direction(self):
        vba_function_name = "get_direction"
        vba_function = "GetDirection"
        vba_code = f"""        
        Public Function {vba_function_name}(measurable)
            Dim direction (2) 
            measurable.{vba_function} direction
            {vba_function_name} = direction
        End Function
        """
        system_service = self.application.system_service
        result = system_service.evaluate(
            vba_code, 0, vba_function_name, [self.measurable]
        )
        return result

    def get_minimum_distance(self, i_measured_item):
        return self.measurable.GetMinimumDistance(i_measured_item.com_object)

    def get_minimum_distance_points(self, i_measured_item):
        vba_function_name = "get_minimum_distance_points"
        vba_function = "GetMinimumDistancePoints"
        vba_code = f"""        
        Public Function {vba_function_name}(measurable, i_measured_item)
            Dim Coordinates (8) 
            measurable.{vba_function} i_measured_item, Coordinates
            {vba_function_name} = Coordinates
        End Function
        """
        system_service = self.application.system_service
        return system_service.evaluate(
            vba_code,
            0,
            vba_function_name,
            [self.measurable, i_measured_item.com_object],
        )

    def get_plane(self):
        vba_function_name = "get_plane"
        vba_function = "GetPlane"
        vba_code = f"""        
        Public Function {vba_function_name}(measurable)
            Dim Components (8)
            measurable.{vba_function} Components
            {vba_function_name} = Components
        End Function
        """
        system_service = self.application.system_service
        return system_service.evaluate(
            vba_code, 0, vba_function_name, [self.measurable]
        )

    def get_point(self):
        vba_function_name = "get_point"
        vba_function = "GetPoint"
        vba_code = f"""        
        Public Function {vba_function_name}(measurable)
            Dim Coordinates (2)
            measurable.{vba_function} Coordinates
            {vba_function_name} = Coordinates
        End Function
        """
        system_service = self.application.system_service
        return system_service.evaluate(
            vba_code, 0, vba_function_name, [self.measurable]
        )

    def get_points_on_axis(self):
        vba_function_name = "get_points_on_axis"
        vba_function = "GetPointsOnAxis"
        vba_code = f"""        
        Public Function {vba_function_name}(measurable)
            Dim Coordinates (8)
            measurable.{vba_function} Coordinates
            {vba_function_name} = Coordinates
        End Function
        """
        system_service = self.application.system_service
        return system_service.evaluate(
            vba_code, 0, vba_function_name, [self.measurable]
        )

    def get_points_on_curve(self):
        vba_function_name = "get_points_on_curve"
        vba_function = "GetPointsOnCurve"
        vba_code = f"""        
        Public Function {vba_function_name}(measurable)
            Dim Coordinates (8)
            measurable.{vba_function} Coordinates
            {vba_function_name} = Coordinates
        End Function
        """
        system_service = self.application.system_service
        return system_service.evaluate(
            vba_code, 0, vba_function_name, [self.measurable]
        )

    def __repr__(self):
        return f"CATIAMeasurable({self.name})"
