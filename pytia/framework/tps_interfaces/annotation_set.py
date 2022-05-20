from typing import TYPE_CHECKING
from pytia.framework.system_interfaces.any_object import AnyObject
from pytia.framework.tps_interfaces.annotation_factory import AnnotationFactory
from pytia.framework.tps_interfaces.annotation_factory_2 import AnnotationFactory2
from pytia.framework.tps_interfaces.capture_factory import CaptureFactory
from pytia.framework.tps_interfaces.captures import Captures
from pytia.framework.tps_interfaces.tps_view import TPSView
from pytia.framework.tps_interfaces.tps_view_factory import TPSViewFactory
from pytia.framework.tps_interfaces.annotations import Annotations
from pytia.framework.tps_interfaces.tps_views import TPSViews

if TYPE_CHECKING:
    from pytia.framework.mec_mod_interfaces.part import Part


class AnnotationSet(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.annotation_set = com_object

    @property
    def active_view(self) -> TPSView:
        return TPSView(self.annotation_set.ActiveView)

    @active_view.setter
    def active_view(self, value: TPSView):
        self.annotation_set.ActiveView = value

    @property
    def an_empty_annotations_list(self) -> Annotations:
        return Annotations(self.annotation_set.AnEmptyAnnotationsList)

    @property
    def annotation_factory(self) -> AnnotationFactory:
        import pytia.framework.tps_interfaces.annotation_factory

        return pytia.framework.tps_interfaces.annotation_factory.AnnotationFactory(
            self.annotation_set.AnnotationFactory
        )

    @property
    def annotation_factory_2(self) -> AnnotationFactory2:
        return AnnotationFactory2(self.annotation_set.AnnotationFactory2)

    @property
    def annotation_set_type(self) -> int:
        return self.annotation_set.AnnotationSetType

    @property
    def annotations(self) -> Annotations:
        return Annotations(self.annotation_set.Annotations)

    @property
    def capture_factory(self) -> CaptureFactory:
        return CaptureFactory(self.annotation_set.CaptureFactory)

    @property
    def captures(self) -> Captures:
        return Captures(self.annotation_set.Captures)

    @property
    def kind_of_set(self) -> str:
        return self.annotation_set.KindOfSet

    @property
    def standard(self) -> str:
        return self.annotation_set.Standard

    @property
    def switch_on(self) -> bool:
        return self.annotation_set.SwitchOn

    @switch_on.setter
    def switch_on(self, value: bool):
        self.annotation_set.SwitchOn = value

    @property
    def tps_view_factory(self) -> TPSViewFactory:
        return TPSViewFactory(self.annotation_set.TPSViewFactory)

    @property
    def tps_views(self) -> TPSViews:
        return TPSViews(self.annotation_set.TPSViews)

    def apply_view_re_use_when_copy_set_to(self) -> None:
        return self.annotation_set.ApplyViewReUseWhenCopySetTo()

    def global_copy_set_to(self, i_destination_part: "Part") -> str:
        from pytia.framework.mec_mod_interfaces.part import Part

        return self.annotation_set.GlobalCopySetTo(i_destination_part.com_object)

    def global_copy_set_to_with_transformation(
        self, i_destination_part: "Part", i_transfo: tuple
    ) -> str:
        return self.annotation_set.GlobalCopySetToWithTransformation(
            i_destination_part.com_object, i_transfo
        )

    def __repr__(self):
        return f'AnnotationSet(name="{self.name}")'
