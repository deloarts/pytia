from typing import TYPE_CHECKING
from pytia.framework.system_interfaces.any_object import AnyObject

if TYPE_CHECKING:
    from pytia.framework.navigator_interfaces.dmu_reviews import DMUReviews


class DMUReview(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.dmu_review = com_object

    @property
    def activation(self) -> int:
        return self.dmu_review.Activation

    @activation.setter
    def activation(self, value: int):
        self.dmu_review.Activation = value

    @property
    def dmu_reviews(self) -> "DMUReviews":
        from pytia.framework.navigator_interfaces.dmu_reviews import DMUReviews

        return DMUReviews(self.dmu_review.DMUReviews)

    def __repr__(self):
        return f'DmuReview(name="{self.name}")'
