from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.knowledge_interfaces.length import Length
from pytia.framework.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapePolyline(HybridShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_polyline = com_object

    @property
    def closure(self) -> bool:
        return self.hybrid_shape_polyline.Closure

    @closure.setter
    def closure(self, value: bool):
        self.hybrid_shape_polyline.Closure = value

    @property
    def number_of_elements(self) -> int:
        return self.hybrid_shape_polyline.NumberOfElements

    def get_element(
        self, i_position: int, o_element: Reference, o_radius: Length
    ) -> None:
        return self.hybrid_shape_polyline.GetElement(
            i_position, o_element.com_object, o_radius.com_object
        )

    def insert_element(self, i_point: Reference, i_position: int) -> None:
        return self.hybrid_shape_polyline.InsertElement(i_point.com_object, i_position)

    def remove_element(self, i_position: int) -> None:
        return self.hybrid_shape_polyline.RemoveElement(i_position)

    def replace_element(self, i_point: Reference, i_position: int) -> None:
        return self.hybrid_shape_polyline.ReplaceElement(i_point.com_object, i_position)

    def set_radius(self, i_position: int, i_radius: float) -> None:
        return self.hybrid_shape_polyline.SetRadius(i_position, i_radius)

    def __repr__(self):
        return f'HybridShapePolyline(name="{self.name}")'
