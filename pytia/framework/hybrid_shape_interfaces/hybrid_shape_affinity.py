from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.knowledge_interfaces.real_param import RealParam
from pytia.framework.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeAffinity(HybridShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_affinity = com_object

    @property
    def axis_first_direction(self) -> Reference:
        return Reference(self.hybrid_shape_affinity.AxisFirstDirection)

    @axis_first_direction.setter
    def axis_first_direction(self, value: Reference):
        self.hybrid_shape_affinity.AxisFirstDirection = value.com_object

    @property
    def axis_origin(self) -> Reference:
        return Reference(self.hybrid_shape_affinity.AxisOrigin)

    @axis_origin.setter
    def axis_origin(self, value: Reference):
        self.hybrid_shape_affinity.AxisOrigin = value.com_object

    @property
    def axis_plane(self) -> Reference:
        return Reference(self.hybrid_shape_affinity.AxisPlane)

    @axis_plane.setter
    def axis_plane(self, value: Reference):
        self.hybrid_shape_affinity.AxisPlane = value.com_object

    @property
    def creation_mode(self) -> bool:
        return self.hybrid_shape_affinity.CreationMode

    @creation_mode.setter
    def creation_mode(self, value: bool):
        self.hybrid_shape_affinity.CreationMode = value

    @property
    def elem_to_transform(self) -> Reference:
        return Reference(self.hybrid_shape_affinity.ElemToTransform)

    @elem_to_transform.setter
    def elem_to_transform(self, value: Reference):
        self.hybrid_shape_affinity.ElemToTransform = value.com_object

    @property
    def volume_result(self) -> bool:
        return self.hybrid_shape_affinity.VolumeResult

    @volume_result.setter
    def volume_result(self, value: bool):
        self.hybrid_shape_affinity.VolumeResult = value

    @property
    def x_ratios(self) -> RealParam:
        return RealParam(self.hybrid_shape_affinity.XRatios)

    @property
    def y_ratios(self) -> RealParam:
        return RealParam(self.hybrid_shape_affinity.YRatios)

    @property
    def z_ratios(self) -> RealParam:
        return RealParam(self.hybrid_shape_affinity.ZRatios)

    def __repr__(self):
        return f'HybridShapeAffinity(name="{self.name}")'
