from pytia.framework.hybrid_shape_interfaces.hybrid_shape_direction import (
    HybridShapeDirection,
)
from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.knowledge_interfaces.angle import Angle
from pytia.framework.mec_mod_interfaces.hybrid_shape import HybridShape
from pytia.framework.system_interfaces.system_service import SystemService


class HybridShapeCircle(HybridShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_circle = com_object

    @property
    def axis_computation(self) -> bool:
        return self.hybrid_shape_circle.AxisComputation

    @axis_computation.setter
    def axis_computation(self, value: bool):
        self.hybrid_shape_circle.AxisComputation = value

    @property
    def axis_direction(self) -> HybridShapeDirection:
        return HybridShapeDirection(self.hybrid_shape_circle.AxisDirection)

    @axis_direction.setter
    def axis_direction(self, direction: HybridShapeDirection):
        self.hybrid_shape_circle.AxisDirection = direction.com_object

    @property
    def end_angle(self) -> Angle:
        return Angle(self.hybrid_shape_circle.EndAngle)

    @property
    def start_angle(self) -> Angle:
        return Angle(self.hybrid_shape_circle.StartAngle)

    def get_axis(self, i_position: int, o_axis: Reference) -> None:
        return self.hybrid_shape_circle.GetAxis(i_position, o_axis.com_object)

    def get_center(
        self, o_center_x: float, o_center_y: float, o_center_z: float
    ) -> None:
        return self.hybrid_shape_circle.GetCenter(o_center_x, o_center_y, o_center_z)

    def get_free_center(self) -> tuple:
        vba_function_name = "get_free_center"
        vba_code = """
        Public Function get_free_center(hybrid_shape_circle)
            Dim ioCenter (2)
            hybrid_shape_circle.GetFreeCenter ioCenter
            get_free_center = ioCenter
        End Function
        """
        system_service = self.application.system_service
        return system_service.evaluate(
            vba_code, 0, vba_function_name, [self.com_object]
        )

    def get_free_radius(self) -> float:
        return self.hybrid_shape_circle.GetFreeRadius()

    def get_limitation(self) -> int:
        return self.hybrid_shape_circle.GetLimitation()

    def set_limitation(self, i_limitation: int) -> None:
        return self.hybrid_shape_circle.SetLimitation(i_limitation)

    def __repr__(self):
        return f'HybridShapeCircle(name="{self.name}")'
