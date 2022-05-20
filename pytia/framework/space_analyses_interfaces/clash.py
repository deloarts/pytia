from pytia.framework.navigator_interfaces.annotated_views import AnnotatedViews
from pytia.framework.navigator_interfaces.group import Group
from pytia.framework.navigator_interfaces.marker_3Ds import Marker3Ds
from pytia.framework.space_analyses_interfaces.conflicts import Conflicts
from pytia.framework.system_interfaces.any_object import AnyObject


class Clash(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.clash = com_object

    @property
    def annotated_views(self) -> AnnotatedViews:
        return AnnotatedViews(self.clash.AnnotatedViews)

    @property
    def clearance(self) -> float:
        return self.clash.Clearance

    @clearance.setter
    def clearance(self, value: float):
        self.clash.Clearance = value

    @property
    def computation_type(self) -> int:
        return self.clash.ComputationType

    @computation_type.setter
    def computation_type(self, value: int):
        self.clash.ComputationType = value

    @property
    def conflicts(self) -> Conflicts:
        return Conflicts(self.clash.Conflicts)

    @property
    def first_group(self) -> Group:
        return Group(self.clash.FirstGroup)

    @first_group.setter
    def first_group(self, value: Group):
        self.clash.FirstGroup = value

    @property
    def interference_type(self) -> int:
        return self.clash.InterferenceType

    @interference_type.setter
    def interference_type(self, value: int):
        self.clash.InterferenceType = value

    @property
    def marker_3ds(self) -> Marker3Ds:
        return Marker3Ds(self.clash.Marker3Ds)

    @property
    def second_group(self) -> Group:
        return Group(self.clash.SecondGroup)

    @second_group.setter
    def second_group(self, group: Group):
        self.clash.SecondGroup = group.com_object

    def compute(self) -> None:
        return self.clash.Compute()

    def export(self, i_type: int, i_path: str) -> None:
        return self.clash.Export(i_type, i_path)

    def __repr__(self):
        return f'Clash(name="{self.name}")'
