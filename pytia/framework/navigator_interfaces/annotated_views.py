from typing import Iterator
from pytia.framework.in_interfaces.viewpoint_3d import Viewpoint3D
from pytia.framework.navigator_interfaces.annotated_view import AnnotatedView
from pytia.framework.system_interfaces.collection import Collection
from pytia.framework.cat_types.general import cat_variant


class AnnotatedViews(Collection):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.annotated_views = com_object

    def add(self) -> AnnotatedView:
        return AnnotatedView(self.annotated_views.Add())

    def add_from_viewpoint(self, i_viewpoint: Viewpoint3D) -> AnnotatedView:
        return AnnotatedView(
            self.annotated_views.AddFromViewpoint(i_viewpoint.com_object)
        )

    def item(self, i_index: cat_variant) -> AnnotatedView:
        return AnnotatedView(self.annotated_views.Item(i_index))

    def remove(self, i_index: cat_variant) -> None:
        return self.annotated_views.Remove(i_index)

    def __getitem__(self, n: int) -> AnnotatedView:
        if (n + 1) > self.count:
            raise StopIteration
        return AnnotatedView(self.annotated_views.item(n + 1))

    def __iter__(self) -> Iterator[AnnotatedView]:
        for i in range(self.count):
            yield self.child_object(self.com_object.item(i + 1))

    def __repr__(self):
        return f'AnnotatedViews(name="{self.name}")'
