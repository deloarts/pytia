from typing import TYPE_CHECKING
from pytia.framework.system_interfaces.any_object import AnyObject
from pytia.framework.cat_types.general import cat_variant

if TYPE_CHECKING:
    from pytia.framework.drafting_interfaces.drawing_view import DrawingView
    from pytia.framework.drafting_interfaces.drawing_sheet import DrawingSheet


class DrawingComponent(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.drawing_component = com_object

    @property
    def angle(self) -> float:
        return self.drawing_component.Angle

    @angle.setter
    def angle(self, value: float):
        self.drawing_component.Angle = value

    @property
    def comp_ref(self) -> "DrawingView":
        from pytia.framework.drafting_interfaces.drawing_view import DrawingView

        return DrawingView(self.drawing_component.CompRef)

    @property
    def scale2(self) -> float:
        return self.drawing_component.Scale2

    @scale2.setter
    def scale2(self, value: float):
        self.drawing_component.Scale2 = value

    @property
    def x(self) -> float:
        return self.drawing_component.x

    @x.setter
    def x(self, value: float):
        self.drawing_component.x = value

    @property
    def y(self) -> float:
        return self.drawing_component.y

    @y.setter
    def y(self, value: float):
        self.drawing_component.y = value

    def explode(self) -> None:
        return self.drawing_component.Explode()

    def explode_and_select(self) -> None:
        return self.drawing_component.ExplodeAndSelect()

    def expose_comp_ref(self) -> None:
        return self.drawing_component.ExposeCompRef()

    def expose_comp_ref_in_sheet(self, i_sheet: "DrawingSheet") -> None:
        return self.drawing_component.ExposeCompRefInSheet(i_sheet.com_object)

    def flip(self) -> None:
        return self.drawing_component.Flip()

    def get_flip(self) -> bool:
        return self.drawing_component.GetFlip()

    def get_matrix(self, io_matrix: tuple) -> None:
        return self.drawing_component.GetMatrix(io_matrix)

    def get_modifiable_object(self, i_index: cat_variant) -> AnyObject:
        return AnyObject(self.drawing_component.GetModifiableObject(i_index))

    def get_modifiable_objects_count(self) -> int:
        return self.drawing_component.GetModifiableObjectsCount()

    def set_matrix(self, i_matrix: tuple) -> None:
        return self.drawing_component.SetMatrix(i_matrix)

    def __repr__(self):
        return f'DrawingComponent(name="{self.name}")'
