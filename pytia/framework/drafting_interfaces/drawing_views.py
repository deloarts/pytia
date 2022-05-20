from typing import Iterator
from pytia.framework.cat_types.general import cat_variant
from pytia.framework.drafting_interfaces.drawing_view import DrawingView
from pytia.framework.system_interfaces.collection import Collection


class DrawingViews(Collection):
    def __init__(self, com_object):
        super().__init__(com_object, child_object=DrawingView)
        self.drawing_views = com_object

    @property
    def active_view(self) -> DrawingView:
        return DrawingView(self.drawing_views.ActiveView)

    def add(self, i_drawing_view_name: str) -> DrawingView:
        return DrawingView(self.drawing_views.Add(i_drawing_view_name))

    def item(self, i_index: cat_variant) -> DrawingView:
        return DrawingView(self.drawing_views.Item(i_index))

    def remove(self, i_index: cat_variant) -> None:
        return self.drawing_views.Remove(i_index)

    def __getitem__(self, n: int) -> DrawingView:
        if (n + 1) > self.count:
            raise StopIteration
        return DrawingView(self.drawing_views.item(n + 1))

    def __iter__(self) -> Iterator[DrawingView]:
        for i in range(self.count):
            yield self.child_object(self.com_object.item(i + 1))

    def __repr__(self):
        return f'DrawingViews(name="{self.name}")'
