from typing import TYPE_CHECKING
from pytia.framework.navigator_interfaces.annotated_views import AnnotatedViews
from pytia.framework.navigator_interfaces.group import Group
from pytia.framework.navigator_interfaces.marker_3Ds import Marker3Ds
from pytia.framework.system_interfaces.any_object import AnyObject
from pytia.framework.system_interfaces.system_service import SystemService

if TYPE_CHECKING:
    from pytia.framework.in_interfaces.document import Document


class Section(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.section = com_object

    @property
    def annotated_views(self) -> AnnotatedViews:
        return AnnotatedViews(self.section.AnnotatedViews)

    @property
    def behavior(self) -> int:
        return self.section.Behavior

    @behavior.setter
    def behavior(self, value: int):
        self.section.Behavior = value

    @property
    def cut_mode(self) -> int:
        return self.section.CutMode

    @cut_mode.setter
    def cut_mode(self, value: int):
        self.section.CutMode = value

    @property
    def group(self) -> Group:
        return Group(self.section.Group)

    @group.setter
    def group(self, value: Group):
        self.section.Group = value

    @property
    def height(self) -> float:
        return self.section.Height

    @height.setter
    def height(self, value: float):
        self.section.Height = value

    @property
    def marker_3ds(self) -> Marker3Ds:
        return Marker3Ds(self.section.Marker3Ds)

    @property
    def thickness(self) -> float:
        return self.section.Thickness

    @thickness.setter
    def thickness(self, value: float):
        self.section.Thickness = value

    @property
    def type(self) -> int:
        return self.section.Type

    @type.setter
    def type(self, value: int):
        self.section.Type = value

    @property
    def width(self) -> float:
        return self.section.Width

    @width.setter
    def width(self, value: float):
        self.section.Width = value

    def export(self) -> "Document":
        from pytia.framework.in_interfaces.document import Document

        return Document(self.section.Export())

    def get_position(self) -> tuple:
        vba_function_name = "get_position"
        vba_code = """
        Public Function get_position(section)
            Dim oComponents(11)
            section.GetPosition oComponents
            get_position = oComponents
        End Function
        """
        system_service = self.application.system_service
        return system_service.evaluate(
            vba_code, 0, vba_function_name, [self.com_object]
        )

    def is_empty(self) -> int:
        return self.section.IsEmpty()

    def set_position(self, i_components: tuple):
        return self.section.SetPosition(i_components)

    def __repr__(self):
        return f'Section(name="{self.name}")'
