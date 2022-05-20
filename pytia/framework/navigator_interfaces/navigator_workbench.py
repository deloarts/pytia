from pytia.framework.in_interfaces.workbench import Workbench
from pytia.framework.navigator_interfaces.annotated_view import AnnotatedView
from pytia.framework.navigator_interfaces.annotated_views import AnnotatedViews
from pytia.framework.navigator_interfaces.dmu_data_flow import DMUDataFlow
from pytia.framework.navigator_interfaces.groups import Groups
from pytia.framework.navigator_interfaces.hyperlinks import Hyperlinks
from pytia.framework.navigator_interfaces.marker_3Ds import Marker3Ds
from pytia.framework.system_interfaces.any_object import AnyObject


class NavigatorWorkbench(Workbench):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.navigator_workbench = com_object

    @property
    def annotated_views(self) -> AnnotatedViews:
        return AnnotatedViews(self.navigator_workbench.AnnotatedViews)

    @property
    def dmu_data_flow(self) -> DMUDataFlow:
        return DMUDataFlow(self.navigator_workbench.DMUDataFlow)

    @property
    def groups(self) -> Groups:
        return Groups(self.navigator_workbench.Groups)

    @property
    def hyperlinks(self) -> Hyperlinks:
        return Hyperlinks(self.navigator_workbench.Hyperlinks)

    @property
    def marker3_ds(self) -> Marker3Ds:
        return Marker3Ds(self.navigator_workbench.Marker3Ds)

    def advanced_view(
        self, i_annotated_view: AnnotatedView, i_view_option: int
    ) -> None:
        return self.navigator_workbench.AdvancedView(
            i_annotated_view.com_object, i_view_option
        )

    def get_order(self, i_object: AnyObject) -> int:
        return self.navigator_workbench.GetOrder(i_object.com_object)

    def set_order(self, i_object: AnyObject, i_new_rank: int) -> None:
        return self.navigator_workbench.SetOrder(i_object.com_object, i_new_rank)

    def view(self, i_annotated_view: AnnotatedView) -> None:
        return self.navigator_workbench.View(i_annotated_view.com_object)

    def __repr__(self):
        return f'NavigatorWorkbench(name="{self.name}")'
