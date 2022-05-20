from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeAxisToAxis(HybridShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_axis_to_axis = com_object

    @property
    def creation_mode(self) -> bool:
        return self.hybrid_shape_axis_to_axis.CreationMode

    @creation_mode.setter
    def creation_mode(self, value: bool):
        self.hybrid_shape_axis_to_axis.CreationMode = value

    @property
    def elem_to_transform(self) -> Reference:
        return Reference(self.hybrid_shape_axis_to_axis.ElemToTransform)

    @elem_to_transform.setter
    def elem_to_transform(self, value: Reference):
        self.hybrid_shape_axis_to_axis.ElemToTransform = value.com_object

    @property
    def reference_axis(self) -> Reference:
        return Reference(self.hybrid_shape_axis_to_axis.ReferenceAxis)

    @reference_axis.setter
    def reference_axis(self, value: Reference):
        self.hybrid_shape_axis_to_axis.ReferenceAxis = value.com_object

    @property
    def target_axis(self) -> Reference:
        return Reference(self.hybrid_shape_axis_to_axis.TargetAxis)

    @target_axis.setter
    def target_axis(self, value: Reference):
        self.hybrid_shape_axis_to_axis.TargetAxis = value.com_object

    @property
    def volume_result(self) -> bool:
        return self.hybrid_shape_axis_to_axis.VolumeResult

    @volume_result.setter
    def volume_result(self, value: bool):
        self.hybrid_shape_axis_to_axis.VolumeResult = value

    def __repr__(self):
        return f'HybridShapeAxisToAxis(name="{self.name}")'
