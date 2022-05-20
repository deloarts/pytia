from typing import Iterator
from typing import TYPE_CHECKING
from pytia.framework.drafting_interfaces.drawing_component import DrawingComponent
from pytia.framework.system_interfaces.collection import Collection
from pytia.framework.cat_types.general import cat_variant

if TYPE_CHECKING:
    from pytia.framework.drafting_interfaces.drawing_view import DrawingView


class DrawingComponents(Collection):
    def __init__(self, com_object):
        super().__init__(com_object, child_object=DrawingComponent)
        self.drawing_components = com_object

    def add(
        self,
        i_drawing_component_ref: "DrawingView",
        i_position_x: float,
        i_position_y: float,
    ) -> DrawingComponent:
        return DrawingComponent(
            self.drawing_components.Add(
                i_drawing_component_ref.com_object, i_position_x, i_position_y
            )
        )

    def item(self, i_index: cat_variant) -> DrawingComponent:
        return DrawingComponent(self.drawing_components.Item(i_index))

    def remove(self, i_index: cat_variant) -> None:
        return self.drawing_components.Remove(i_index)

    def __getitem__(self, n: int) -> DrawingComponent:
        if (n + 1) > self.count:
            raise StopIteration
        return DrawingComponent(self.drawing_components.item(n + 1))

    def __iter__(self) -> Iterator[DrawingComponent]:
        for i in range(self.count):
            yield self.child_object(self.com_object.item(i + 1))

    def __repr__(self):
        return f"DrawingComponents()"
