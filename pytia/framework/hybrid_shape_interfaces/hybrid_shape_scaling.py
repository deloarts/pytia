from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.knowledge_interfaces.real_param import RealParam
from pytia.framework.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeScaling(HybridShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_scaling = com_object

    @property
    def center(self) -> Reference:
        return Reference(self.hybrid_shape_scaling.Center)

    @center.setter
    def center(self, reference_center: Reference):
        self.hybrid_shape_scaling.Center = reference_center.com_object

    @property
    def creation_mode(self) -> bool:
        return self.hybrid_shape_scaling.CreationMode

    @creation_mode.setter
    def creation_mode(self, value: bool):
        self.hybrid_shape_scaling.CreationMode = value

    @property
    def elem_to_scale(self) -> Reference:
        return Reference(self.hybrid_shape_scaling.ElemToScale)

    @elem_to_scale.setter
    def elem_to_scale(self, reference_element: Reference):
        self.hybrid_shape_scaling.ElemToScale = reference_element.com_object

    @property
    def ratio(self) -> RealParam:
        return RealParam(self.hybrid_shape_scaling.Ratio)

    @property
    def ratio_value(self) -> float:
        return self.hybrid_shape_scaling.RatioValue

    @ratio_value.setter
    def ratio_value(self, value: float):
        self.hybrid_shape_scaling.RatioValue = value

    @property
    def volume_result(self) -> bool:
        return self.hybrid_shape_scaling.VolumeResult

    @volume_result.setter
    def volume_result(self, value: bool):
        self.hybrid_shape_scaling.VolumeResult = value

    def __repr__(self):
        return f'HybridShapeScaling(name="{self.name}")'
