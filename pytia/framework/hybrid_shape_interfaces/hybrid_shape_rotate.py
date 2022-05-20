from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.knowledge_interfaces.angle import Angle
from pytia.framework.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeRotate(HybridShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_rotate = com_object

    @property
    def angle(self) -> Angle:
        return Angle(self.hybrid_shape_rotate.Angle)

    @property
    def angle_value(self) -> float:
        return self.hybrid_shape_rotate.AngleValue

    @angle_value.setter
    def angle_value(self, value: float):
        self.hybrid_shape_rotate.AngleValue = value

    @property
    def axis(self) -> Reference:
        return Reference(self.hybrid_shape_rotate.Axis)

    @axis.setter
    def axis(self, reference_axis: Reference):
        self.hybrid_shape_rotate.Axis = reference_axis.com_object

    @property
    def elem_to_rotate(self) -> Reference:
        return Reference(self.hybrid_shape_rotate.ElemToRotate)

    @elem_to_rotate.setter
    def elem_to_rotate(self, reference_element: Reference):
        self.hybrid_shape_rotate.ElemToRotate = reference_element.com_object

    @property
    def first_element(self) -> Reference:
        return Reference(self.hybrid_shape_rotate.FirstElement)

    @first_element.setter
    def first_element(self, reference_element: Reference):
        self.hybrid_shape_rotate.FirstElement = reference_element.com_object

    @property
    def first_point(self) -> Reference:
        return Reference(self.hybrid_shape_rotate.FirstPoint)

    @first_point.setter
    def first_point(self, reference_point: Reference):
        self.hybrid_shape_rotate.FirstPoint = reference_point.com_object

    @property
    def orientation_of_first_element(self) -> bool:
        return self.hybrid_shape_rotate.OrientationOfFirstElement

    @orientation_of_first_element.setter
    def orientation_of_first_element(self, value: bool):
        self.hybrid_shape_rotate.OrientationOfFirstElement = value

    @property
    def orientation_of_second_element(self) -> bool:
        return self.hybrid_shape_rotate.OrientationOfSecondElement

    @orientation_of_second_element.setter
    def orientation_of_second_element(self, value: bool):
        self.hybrid_shape_rotate.OrientationOfSecondElement = value

    @property
    def rotation_type(self) -> int:
        return self.hybrid_shape_rotate.RotationType

    @rotation_type.setter
    def rotation_type(self, value: int):
        self.hybrid_shape_rotate.RotationType = value

    @property
    def second_element(self) -> Reference:
        return Reference(self.hybrid_shape_rotate.SecondElement)

    @second_element.setter
    def second_element(self, reference_element: Reference):
        self.hybrid_shape_rotate.SecondElement = reference_element.com_object

    @property
    def second_point(self) -> Reference:
        return Reference(self.hybrid_shape_rotate.SecondPoint)

    @second_point.setter
    def second_point(self, reference_point: Reference):
        self.hybrid_shape_rotate.SecondPoint = reference_point.com_object

    @property
    def third_point(self) -> Reference:
        return Reference(self.hybrid_shape_rotate.ThirdPoint)

    @third_point.setter
    def third_point(self, reference_point: Reference):
        self.hybrid_shape_rotate.ThirdPoint = reference_point.com_object

    @property
    def volume_result(self) -> bool:
        return self.hybrid_shape_rotate.VolumeResult

    @volume_result.setter
    def volume_result(self, value: bool):
        self.hybrid_shape_rotate.VolumeResult = value

    def get_creation_mode(self) -> int:
        return self.hybrid_shape_rotate.GetCreationMode()

    def set_creation_mode(self, i_creation: bool) -> None:
        return self.hybrid_shape_rotate.SetCreationMode(i_creation)

    def __repr__(self):
        return f'HybridShapeRotate(name="{self.name}")'
