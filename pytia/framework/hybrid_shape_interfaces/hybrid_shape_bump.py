from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.knowledge_interfaces.length import Length
from pytia.framework.knowledge_interfaces.real_param import RealParam
from pytia.framework.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeBump(HybridShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_bump = com_object

    @property
    def body_to_bump(self) -> Reference:
        return Reference(self.hybrid_shape_bump.BodyToBump)

    @body_to_bump.setter
    def body_to_bump(self, value: Reference):
        self.hybrid_shape_bump.BodyToBump = value.com_object

    @property
    def center_tension(self) -> RealParam:
        return RealParam(self.hybrid_shape_bump.CenterTension)

    @center_tension.setter
    def center_tension(self, real_param: RealParam):
        self.hybrid_shape_bump.CenterTension = real_param.com_object

    @property
    def continuity_type(self) -> int:
        return self.hybrid_shape_bump.ContinuityType

    @continuity_type.setter
    def continuity_type(self, value: int):
        self.hybrid_shape_bump.ContinuityType = value

    @property
    def deformation_center(self) -> Reference:
        return Reference(self.hybrid_shape_bump.DeformationCenter)

    @deformation_center.setter
    def deformation_center(self, reference_center: Reference):
        self.hybrid_shape_bump.DeformationCenter = reference_center.com_object

    @property
    def deformation_dir(self) -> Reference:
        return Reference(self.hybrid_shape_bump.DeformationDir)

    @deformation_dir.setter
    def deformation_dir(self, reference_direction: Reference):
        self.hybrid_shape_bump.DeformationDir = reference_direction.com_object

    @property
    def deformation_dist(self) -> Length:
        return Length(self.hybrid_shape_bump.DeformationDist)

    @deformation_dist.setter
    def deformation_dist(self, length: Length):
        self.hybrid_shape_bump.DeformationDist = length.com_object

    @property
    def deformation_dist_value(self) -> float:
        return self.hybrid_shape_bump.DeformationDistValue

    @deformation_dist_value.setter
    def deformation_dist_value(self, value: float):
        self.hybrid_shape_bump.DeformationDistValue = value

    @property
    def limit_curve(self) -> Reference:
        return Reference(self.hybrid_shape_bump.LimitCurve)

    @limit_curve.setter
    def limit_curve(self, reference_curve: Reference):
        self.hybrid_shape_bump.LimitCurve = reference_curve.com_object

    @property
    def projection_dir(self) -> Reference:
        return Reference(self.hybrid_shape_bump.ProjectionDir)

    @projection_dir.setter
    def projection_dir(self, reference_projection_direction: Reference):
        self.hybrid_shape_bump.ProjectionDir = reference_projection_direction.com_object

    def __repr__(self):
        return f'HybridShapeBump(name="{self.name}")'
