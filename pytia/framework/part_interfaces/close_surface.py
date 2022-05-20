from pytia.framework.knowledge_interfaces.int_param import IntParam
from pytia.framework.part_interfaces.angular_repartition import AngularRepartition
from pytia.framework.part_interfaces.linear_repartition import LinearRepartition
from pytia.framework.part_interfaces.pattern import Pattern


class CloseSurface(Pattern):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.close_surface = com_object

    @property
    def angular_direction_row(self):
        return IntParam(self.close_surface.AngularDirectionRow)

    @property
    def angular_repartition(self):
        return AngularRepartition(self.close_surface.AngularRepartition)

    @property
    def circular_pattern_parameters(self):
        return self.close_surface.CircularPatternParameters

    @circular_pattern_parameters.setter
    def circular_pattern_parameters(self, value):
        self.close_surface.CircularPatternParameters = value

    @property
    def radial_alignment(self):
        return self.close_surface.RadialAlignment

    @radial_alignment.setter
    def radial_alignment(self, value):
        self.close_surface.RadialAlignment = value

    @property
    def radial_direction_row(self):
        return IntParam(self.close_surface.RadialDirectionRow)

    @property
    def radial_repartition(self):
        return LinearRepartition(self.close_surface.RadialRepartition)

    @property
    def rotation_orientation(self):
        return self.close_surface.RotationOrientation

    @rotation_orientation.setter
    def rotation_orientation(self, value):
        self.close_surface.RotationOrientation = value

    def get_rotation_axis(self, io_rotation_axis):
        return self.close_surface.GetRotationAxis(io_rotation_axis)

    def get_rotation_center(self, io_rotation_center):
        return self.close_surface.GetRotationCenter(io_rotation_center)

    def set_instance_angular_spacing(self, i_instance_number, i_angular_spacing):
        return self.close_surface.SetInstanceAngularSpacing(
            i_instance_number, i_angular_spacing
        )

    def set_rotation_axis(self, i_rotation_axis):
        return self.close_surface.SetRotationAxis(i_rotation_axis.com_object)

    def set_rotation_center(self, i_rotation_center):
        return self.close_surface.SetRotationCenter(i_rotation_center.com_object)

    def set_unequal_instance_number(self, i_instance_number):
        return self.close_surface.SetUnequalInstanceNumber(i_instance_number)

    def set_unequal_step(self, i_instance_number):
        return self.close_surface.SetUnequalStep(i_instance_number)

    def __repr__(self):
        return f'CloseSurface(name="{ self.name }")'
