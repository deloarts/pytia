from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.knowledge_interfaces.real_param import RealParam
from pytia.framework.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeDirection(HybridShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_direction = com_object

    @property
    def object(self) -> Reference:
        return Reference(self.hybrid_shape_direction.Object)

    @object.setter
    def object(self, reference: Reference):
        self.hybrid_shape_direction.Object = reference.com_object

    @property
    def ref_axis_system(self) -> Reference:
        return Reference(self.hybrid_shape_direction.RefAxisSystem)

    @ref_axis_system.setter
    def ref_axis_system(self, reference_axis: Reference):
        self.hybrid_shape_direction.RefAxisSystem = reference_axis.com_object

    @property
    def type(self) -> int:
        return self.hybrid_shape_direction.Type

    def direction_specification(self) -> int:
        return self.hybrid_shape_direction.DirectionSpecification()

    def get_x(self):
        return RealParam(self.hybrid_shape_direction.GetX())

    def get_x_val(self) -> float:
        return self.hybrid_shape_direction.GetXVal()

    def get_y(self) -> RealParam:
        return RealParam(self.hybrid_shape_direction.GetY())

    def get_y_val(self) -> float:
        return self.hybrid_shape_direction.GetYVal()

    def get_z(self) -> RealParam:
        return RealParam(self.hybrid_shape_direction.GetZ())

    def get_z_val(self) -> float:
        return self.hybrid_shape_direction.GetZVal()

    def __repr__(self):
        return f'HybridShapeDirection(name="{self.name}")'
