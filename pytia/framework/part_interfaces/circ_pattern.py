from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.knowledge_interfaces.int_param import IntParam
from pytia.framework.part_interfaces.angular_repartition import AngularRepartition
from pytia.framework.part_interfaces.linear_repartition import LinearRepartition
from pytia.framework.part_interfaces.pattern import Pattern


class CircPattern(Pattern):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.circ_pattern = com_object

    @property
    def angular_direction_row(self) -> IntParam:
        return IntParam(self.circ_pattern.AngularDirectionRow)

    @property
    def angular_repartition(self) -> AngularRepartition:
        return AngularRepartition(self.circ_pattern.AngularRepartition)

    @property
    def circular_pattern_parameters(self) -> int:
        return self.circ_pattern.CircularPatternParameters

    @circular_pattern_parameters.setter
    def circular_pattern_parameters(self, value: int):
        self.circ_pattern.CircularPatternParameters = value

    @property
    def radial_alignment(self) -> bool:
        return self.circ_pattern.RadialAlignment

    @radial_alignment.setter
    def radial_alignment(self, value: bool):
        self.circ_pattern.RadialAlignment = value

    @property
    def radial_direction_row(self) -> IntParam:
        return IntParam(self.circ_pattern.RadialDirectionRow)

    @property
    def radial_repartition(self) -> LinearRepartition:
        return LinearRepartition(self.circ_pattern.RadialRepartition)

    @property
    def rotation_orientation(self) -> bool:
        return self.circ_pattern.RotationOrientation

    @rotation_orientation.setter
    def rotation_orientation(self, value: bool):
        self.circ_pattern.RotationOrientation = value

    def get_rotation_axis(self, io_rotation_axis: tuple) -> None:
        return self.circ_pattern.GetRotationAxis(io_rotation_axis)

    def get_rotation_center(self, io_rotation_center: tuple) -> None:
        return self.circ_pattern.GetRotationCenter(io_rotation_center)

    def set_instance_angular_spacing(
        self, i_instance_number: int, i_angular_spacing: float
    ) -> None:
        return self.circ_pattern.SetInstanceAngularSpacing(
            i_instance_number, i_angular_spacing
        )

    def set_rotation_axis(self, i_rotation_axis: Reference) -> None:
        return self.circ_pattern.SetRotationAxis(i_rotation_axis.com_object)

    def set_rotation_center(self, i_rotation_center: Reference) -> None:
        return self.circ_pattern.SetRotationCenter(i_rotation_center.com_object)

    def set_unequal_instance_number(self, i_instance_number: int) -> None:
        return self.circ_pattern.SetUnequalInstanceNumber(i_instance_number)

    def set_unequal_step(self, i_instance_number: int) -> None:
        return self.circ_pattern.SetUnequalStep(i_instance_number)

    def __repr__(self):
        return f'CircPattern(name="{self.name}")'
