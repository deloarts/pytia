from pytia.framework.knowledge_interfaces.angle import Angle
from pytia.framework.knowledge_interfaces.length import Length
from pytia.framework.part_interfaces.defeaturing_filter import DefeaturingFilter


class DefeaturingFilterWithRange(DefeaturingFilter):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.defeaturing_filter_with_range = com_object

    def get_maximum_activity(self, i_range_id: str) -> bool:
        return self.defeaturing_filter_with_range.getMaximumActivity(i_range_id)

    def get_maximum_angle(self, i_range_id: str) -> Angle:
        return Angle(self.defeaturing_filter_with_range.getMaximumAngle(i_range_id))

    def get_maximum_length(self, i_range_id: str) -> Length:
        return Length(self.defeaturing_filter_with_range.getMaximumLength(i_range_id))

    def get_maximum_value(self, i_range_id: str) -> float:
        return self.defeaturing_filter_with_range.getMaximumValue(i_range_id)

    def get_minimum_activity(self, i_range_id: str) -> bool:
        return self.defeaturing_filter_with_range.getMinimumActivity(i_range_id)

    def get_minimum_angle(self, i_range_id: str) -> Angle:
        return Angle(self.defeaturing_filter_with_range.getMinimumAngle(i_range_id))

    def get_minimum_length(self, i_range_id: str) -> Length:
        return Length(self.defeaturing_filter_with_range.getMinimumLength(i_range_id))

    def get_minimum_value(self, i_range_id: str) -> float:
        return self.defeaturing_filter_with_range.getMinimumValue(i_range_id)

    def set_maximum_activity(self, i_range_id: str, i_value: bool) -> None:
        return self.defeaturing_filter_with_range.setMaximumActivity(
            i_range_id, i_value
        )

    def set_maximum_value(self, i_range_id: str, i_value: float) -> None:
        return self.defeaturing_filter_with_range.setMaximumValue(i_range_id, i_value)

    def set_minimum_activity(self, i_range_id: str, i_value: bool) -> None:
        return self.defeaturing_filter_with_range.setMinimumActivity(
            i_range_id, i_value
        )

    def set_minimum_value(self, i_range_id: str, i_value: float) -> None:
        return self.defeaturing_filter_with_range.setMinimumValue(i_range_id, i_value)

    def __repr__(self):
        return f'DefeaturingFilterWithRange(name="{ self.name }")'
