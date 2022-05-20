from pytia.framework.hybrid_shape_interfaces.hybrid_shape_direction import (
    HybridShapeDirection,
)
from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.knowledge_interfaces.length import Length
from pytia.framework.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeTranslate(HybridShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_translate = com_object

    @property
    def coord_x_value(self) -> float:
        return self.hybrid_shape_translate.CoordXValue

    @coord_x_value.setter
    def coord_x_value(self, value: float):
        self.hybrid_shape_translate.CoordXValue = value

    @property
    def coord_y_value(self) -> float:
        return self.hybrid_shape_translate.CoordYValue

    @coord_y_value.setter
    def coord_y_value(self, value: float):
        self.hybrid_shape_translate.CoordYValue = value

    @property
    def coord_z_value(self) -> float:
        return self.hybrid_shape_translate.CoordZValue

    @coord_z_value.setter
    def coord_z_value(self, value: float):
        self.hybrid_shape_translate.CoordZValue = value

    @property
    def direction(self) -> HybridShapeDirection:
        return HybridShapeDirection(self.hybrid_shape_translate.Direction)

    @direction.setter
    def direction(self, direction: HybridShapeDirection):
        self.hybrid_shape_translate.Direction = direction.com_object

    @property
    def distance(self) -> Length:
        return Length(self.hybrid_shape_translate.Distance)

    @property
    def distance_value(self) -> float:
        return self.hybrid_shape_translate.DistanceValue

    @distance_value.setter
    def distance_value(self, value: float):
        self.hybrid_shape_translate.DistanceValue = value

    @property
    def elem_to_translate(self) -> Reference:
        return Reference(self.hybrid_shape_translate.ElemToTranslate)

    @elem_to_translate.setter
    def elem_to_translate(self, reference_element: Reference):
        self.hybrid_shape_translate.ElemToTranslate = reference_element.com_object

    @property
    def first_point(self) -> Reference:
        return Reference(self.hybrid_shape_translate.FirstPoint)

    @first_point.setter
    def first_point(self, reference_point: Reference):
        self.hybrid_shape_translate.FirstPoint = reference_point.com_object

    @property
    def ref_axis_system(self) -> Reference:
        return Reference(self.hybrid_shape_translate.RefAxisSystem)

    @ref_axis_system.setter
    def ref_axis_system(self, reference_axis: Reference):
        self.hybrid_shape_translate.RefAxisSystem = reference_axis.com_object

    @property
    def second_point(self) -> Reference:
        return Reference(self.hybrid_shape_translate.SecondPoint)

    @second_point.setter
    def second_point(self, reference_point: Reference):
        self.hybrid_shape_translate.SecondPoint = reference_point.com_object

    @property
    def vector_type(self) -> int:
        return self.hybrid_shape_translate.VectorType

    @vector_type.setter
    def vector_type(self, value: int):
        self.hybrid_shape_translate.VectorType = value

    @property
    def volume_result(self) -> bool:
        return self.hybrid_shape_translate.VolumeResult

    @volume_result.setter
    def volume_result(self, value: bool):
        self.hybrid_shape_translate.VolumeResult = value

    def get_creation_mode(self) -> int:
        return self.hybrid_shape_translate.GetCreationMode()

    def set_creation_mode(self, i_creation: bool) -> None:
        return self.hybrid_shape_translate.SetCreationMode(i_creation)

    def __repr__(self):
        return f'HybridShapeTranslate(name="{self.name}")'
