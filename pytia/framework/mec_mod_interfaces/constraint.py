from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.knowledge_interfaces.dimension import Dimension
from pytia.framework.system_interfaces.any_object import AnyObject


class Constraint(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.constraint = com_object

    @property
    def angle_sector(self) -> int:
        return self.constraint.AngleSector

    @angle_sector.setter
    def angle_sector(self, value: int):
        self.constraint.AngleSector = value

    @property
    def dimension(self) -> Dimension:
        return Dimension(self.constraint.Dimension)

    @property
    def distance_config(self) -> int:
        return self.constraint.DistanceConfig

    @distance_config.setter
    def distance_config(self, value: int):
        self.constraint.DistanceConfig = value

    @property
    def distance_direction(self) -> int:
        return self.constraint.DistanceDirection

    @distance_direction.setter
    def distance_direction(self, value: int):
        self.constraint.DistanceDirection = value

    @property
    def mode(self) -> int:
        return self.constraint.Mode

    @mode.setter
    def mode(self, value: int):
        self.constraint.Mode = value

    @property
    def orientation(self) -> int:
        return self.constraint.Orientation

    @orientation.setter
    def orientation(self, value: int):
        self.constraint.Orientation = value

    @property
    def reference_axis(self) -> int:
        return self.constraint.ReferenceAxis

    @reference_axis.setter
    def reference_axis(self, value: int):
        self.constraint.ReferenceAxis = value

    @property
    def reference_type(self) -> int:
        return self.constraint.ReferenceType

    @reference_type.setter
    def reference_type(self, value: int):
        self.constraint.ReferenceType = value

    @property
    def side(self) -> int:
        return self.constraint.Side

    @side.setter
    def side(self, value: int):
        self.constraint.Side = value

    @property
    def status(self) -> int:
        return self.constraint.Status

    @property
    def type(self) -> int:
        return self.constraint.Type

    def activate(self) -> None:
        return self.constraint.Activate()

    def deactivate(self) -> None:
        return self.constraint.Deactivate()

    def get_constraint_element(self, i_element_number: int) -> Reference:
        return Reference(self.constraint.GetConstraintElement(i_element_number))

    def get_constraint_visu_location(
        self, o_anchor_point: tuple, o_anchor_vector: tuple
    ) -> None:
        return self.constraint.GetConstraintVisuLocation(
            o_anchor_point, o_anchor_vector
        )

    def is_inactive(self) -> bool:
        return self.constraint.IsInactive()

    def set_constraint_element(
        self, i_element_number: int, i_new_element: Reference
    ) -> None:
        return self.constraint.SetConstraintElement(
            i_element_number, i_new_element.com_object
        )

    def set_constraint_visu_location(
        self, i_new_x: float, i_new_y: float, i_new_z: float
    ) -> None:
        return self.constraint.SetConstraintVisuLocation(i_new_x, i_new_y, i_new_z)

    def __repr__(self):
        return f'Constraint(name="{self.name}")'
