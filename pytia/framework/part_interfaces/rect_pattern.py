from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.knowledge_interfaces.int_param import IntParam
from pytia.framework.part_interfaces.linear_repartition import LinearRepartition
from pytia.framework.part_interfaces.pattern import Pattern


class RectPattern(Pattern):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.rect_pattern = com_object

    @property
    def first_direction_repartition(self) -> LinearRepartition:
        return LinearRepartition(self.rect_pattern.FirstDirectionRepartition)

    @property
    def first_direction_row(self) -> IntParam:
        return IntParam(self.rect_pattern.FirstDirectionRow)

    @property
    def first_orientation(self) -> bool:
        return self.rect_pattern.FirstOrientation

    @first_orientation.setter
    def first_orientation(self, value: bool):
        self.rect_pattern.FirstOrientation = value

    @property
    def first_rectangular_pattern_parameters(self) -> int:
        return self.rect_pattern.FirstRectangularPatternParameters

    @first_rectangular_pattern_parameters.setter
    def first_rectangular_pattern_parameters(self, value: int):
        self.rect_pattern.FirstRectangularPatternParameters = value

    @property
    def second_direction_repartition(self) -> LinearRepartition:
        return LinearRepartition(self.rect_pattern.SecondDirectionRepartition)

    @property
    def second_direction_row(self) -> IntParam:
        return IntParam(self.rect_pattern.SecondDirectionRow)

    @property
    def second_orientation(self) -> bool:
        return self.rect_pattern.SecondOrientation

    @second_orientation.setter
    def second_orientation(self, value: bool):
        self.rect_pattern.SecondOrientation = value

    @property
    def second_rectangular_pattern_parameters(self) -> int:
        return self.rect_pattern.SecondRectangularPatternParameters

    @second_rectangular_pattern_parameters.setter
    def second_rectangular_pattern_parameters(self, value: int):
        self.rect_pattern.SecondRectangularPatternParameters = value

    def get_first_direction(self, io_first_direction: tuple) -> None:
        return self.rect_pattern.GetFirstDirection(io_first_direction)

    def get_second_direction(self, io_second_direction: tuple) -> None:
        return self.rect_pattern.GetSecondDirection(io_second_direction)

    def set_first_direction(self, i_first_direction: Reference) -> None:
        return self.rect_pattern.SetFirstDirection(i_first_direction.com_object)

    def set_instance_spacing(
        self, i_instance_number: int, i_spacing: float, i_direction: int
    ) -> None:
        return self.rect_pattern.SetInstanceSpacing(
            i_instance_number, i_spacing, i_direction
        )

    def set_second_direction(self, i_second_direction: Reference) -> None:
        return self.rect_pattern.SetSecondDirection(i_second_direction.com_object)

    def set_unequal_instance_number(
        self, i_instance_number: int, i_direction: int
    ) -> None:
        return self.rect_pattern.SetUnequalInstanceNumber(
            i_instance_number, i_direction
        )

    def __repr__(self):
        return f'RectPattern(name="{self.name}")'
