from pytia.framework.part_interfaces.repartition import Repartition
from pytia.framework.system_interfaces.any_object import AnyObject


class UserRepartition(Repartition):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.user_repartition = com_object

    @property
    def feature_to_locate_positions(self) -> AnyObject:
        return AnyObject(self.user_repartition.FeatureToLocatePositions)

    def add_feature_to_locate_positions(
        self, i_feature_to_locate_positions: AnyObject
    ) -> None:
        return self.user_repartition.AddFeatureToLocatePositions(
            i_feature_to_locate_positions.com_object
        )

    def __repr__(self):
        return f'UserRepartition(name="{ self.name }")'
