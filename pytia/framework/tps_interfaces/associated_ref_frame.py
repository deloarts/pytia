from typing import TYPE_CHECKING
from pytia.framework.system_interfaces.any_object import AnyObject

if TYPE_CHECKING:
    from pytia.framework.tps_interfaces.annotation import Annotation
    from pytia.framework.tps_interfaces.annotation_2 import Annotation2


class AssociatedRefFrame(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.associated_ref_frame = com_object

    @property
    def reference_frame(self) -> "Annotation":
        from pytia.framework.tps_interfaces.annotation import Annotation

        return Annotation(self.associated_ref_frame.ReferenceFrame)

    @property
    def reference_frame_2(self) -> "Annotation2":
        from pytia.framework.tps_interfaces.annotation_2 import Annotation2

        return Annotation2(self.associated_ref_frame.ReferenceFrame2)

    def __repr__(self):
        return f'AssociatedRefFrame(name="{self.name}")'
