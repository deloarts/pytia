from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.knowledge_interfaces.angle import Angle
from pytia.framework.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeRevol(HybridShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_revol = com_object

    @property
    def axis(self) -> Reference:
        return Reference(self.hybrid_shape_revol.Axis)

    @axis.setter
    def axis(self, reference_axis: Reference):
        self.hybrid_shape_revol.Axis = reference_axis.com_object

    @property
    def begin_angle(self) -> Angle:
        return Angle(self.hybrid_shape_revol.BeginAngle)

    @property
    def context(self) -> int:
        return self.hybrid_shape_revol.Context

    @context.setter
    def context(self, value: int):
        self.hybrid_shape_revol.Context = value

    @property
    def end_angle(self) -> Angle:
        return Angle(self.hybrid_shape_revol.EndAngle)

    @property
    def first_limit_type(self) -> int:
        return self.hybrid_shape_revol.FirstLimitType

    @first_limit_type.setter
    def first_limit_type(self, value: int):
        self.hybrid_shape_revol.FirstLimitType = value

    @property
    def first_upto_element(self) -> Reference:
        return Reference(self.hybrid_shape_revol.FirstUptoElement)

    @first_upto_element.setter
    def first_upto_element(self, reference_element: Reference):
        self.hybrid_shape_revol.FirstUptoElement = reference_element.com_object

    @property
    def orientation(self) -> bool:
        return self.hybrid_shape_revol.Orientation

    @orientation.setter
    def orientation(self, value: bool):
        self.hybrid_shape_revol.Orientation = value

    @property
    def profile(self) -> Reference:
        return Reference(self.hybrid_shape_revol.Profil)

    @profile.setter
    def profile(self, reference_profile: Reference):
        self.hybrid_shape_revol.Profil = reference_profile.com_object

    @property
    def second_limit_type(self) -> int:
        return self.hybrid_shape_revol.SecondLimitType

    @second_limit_type.setter
    def second_limit_type(self, value: int):
        self.hybrid_shape_revol.SecondLimitType = value

    @property
    def second_upto_element(self) -> Reference:
        return Reference(self.hybrid_shape_revol.SecondUptoElement)

    @second_upto_element.setter
    def second_upto_element(self, reference_element: Reference):
        self.hybrid_shape_revol.SecondUptoElement = reference_element.com_object

    def __repr__(self):
        return f'HybridShapeRevol(name="{self.name}")'
