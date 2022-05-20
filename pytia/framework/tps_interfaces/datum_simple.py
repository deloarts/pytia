from typing import TYPE_CHECKING
from pytia.framework.system_interfaces.any_object import AnyObject

if TYPE_CHECKING:
    from pytia.framework.tps_interfaces.annotations import Annotations


class DatumSimple(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.datum_simple = com_object

    @property
    def label(self) -> str:
        return self.datum_simple.Label

    @label.setter
    def label(self, value: str):
        self.datum_simple.Label = value

    @property
    def targets(self) -> "Annotations":
        from pytia.framework.tps_interfaces.annotations import Annotations

        return Annotations(self.datum_simple.Targets)

    def __repr__(self):
        return f'DatumSimple(name="{self.name}")'
