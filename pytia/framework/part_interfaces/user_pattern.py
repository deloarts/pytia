from pytia.framework.part_interfaces.pattern import Pattern
from pytia.framework.system_interfaces.any_object import AnyObject


class UserPattern(Pattern):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.user_pattern = com_object

    @property
    def anchor_point(self) -> AnyObject:
        return AnyObject(self.user_pattern.AnchorPoint)

    @anchor_point.setter
    def anchor_point(self, value: AnyObject):
        self.user_pattern.AnchorPoint = value

    @property
    def feature_to_locate_positions(self) -> AnyObject:
        return AnyObject(self.user_pattern.FeatureToLocatePositions)

    def add_feature_to_locate_positions(
        self, i_feature_to_locate_positions: AnyObject
    ) -> None:
        return self.user_pattern.AddFeatureToLocatePositions(
            i_feature_to_locate_positions.com_object
        )

    def __repr__(self):
        return f'UserPattern(name="{ self.name }")'
