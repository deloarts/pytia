from pytia.framework.hybrid_shape_interfaces.hybrid_shape_direction import (
    HybridShapeDirection,
)
from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.knowledge_interfaces.angle import Angle
from pytia.framework.knowledge_interfaces.length import Length
from pytia.framework.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapePositionTransfo(HybridShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_position_transfo = com_object

    @property
    def initial_direction_computation_mode(self) -> int:
        return self.hybrid_shape_position_transfo.InitialDirectionComputationMode

    @initial_direction_computation_mode.setter
    def initial_direction_computation_mode(self, value: int):
        self.hybrid_shape_position_transfo.InitialDirectionComputationMode = value

    @property
    def mode(self) -> int:
        return self.hybrid_shape_position_transfo.Mode

    @mode.setter
    def mode(self, value: int):
        self.hybrid_shape_position_transfo.Mode = value

    @property
    def profile(self) -> Reference:
        return Reference(self.hybrid_shape_position_transfo.Profile)

    @profile.setter
    def profile(self, reference_profile: Reference):
        self.hybrid_shape_position_transfo.Profile = reference_profile.com_object

    def get_nb_pos_angle(self) -> int:
        return self.hybrid_shape_position_transfo.GetNbPosAngle()

    def get_nb_pos_coord(self) -> int:
        return self.hybrid_shape_position_transfo.GetNbPosCoord()

    def get_pos_angle(self, i_i: int) -> Angle:
        return Angle(self.hybrid_shape_position_transfo.GetPosAngle(i_i))

    def get_pos_coord(self, ii: int) -> Length:
        return Length(self.hybrid_shape_position_transfo.GetPosCoord(ii))

    def get_pos_point(self, ii: int) -> Reference:
        return Reference(self.hybrid_shape_position_transfo.GetPosPoint(ii))

    def get_pos_swap_axes(self, ii: int) -> int:
        return self.hybrid_shape_position_transfo.GetPosSwapAxes(ii)

    def get_position_direction(self, i_i: int) -> HybridShapeDirection:
        return HybridShapeDirection(
            self.hybrid_shape_position_transfo.GetPositionDirection(i_i)
        )

    def remove_all_pos_angle(self) -> None:
        return self.hybrid_shape_position_transfo.RemoveAllPosAngle()

    def remove_all_pos_coord(self) -> None:
        return self.hybrid_shape_position_transfo.RemoveAllPosCoord()

    def set_pos_angle(self, i_i: int, i_angle: Angle) -> None:
        return self.hybrid_shape_position_transfo.SetPosAngle(i_i, i_angle.com_object)

    def set_pos_coord(self, i_i: int, i_coordinate: Length) -> None:
        return self.hybrid_shape_position_transfo.SetPosCoord(
            i_i, i_coordinate.com_object
        )

    def set_pos_point(self, i_i: int, i_elem: Reference) -> None:
        return self.hybrid_shape_position_transfo.SetPosPoint(i_i, i_elem.com_object)

    def set_pos_swap_axes(self, ii: int, i_inversion: int) -> None:
        return self.hybrid_shape_position_transfo.SetPosSwapAxes(ii, i_inversion)

    def set_position_direction(self, i_i: int, i_elem: HybridShapeDirection) -> None:
        return self.hybrid_shape_position_transfo.SetPositionDirection(
            i_i, i_elem.com_object
        )

    def __repr__(self):
        return f'HybridShapePositionTransfo(name="{self.name}")'
