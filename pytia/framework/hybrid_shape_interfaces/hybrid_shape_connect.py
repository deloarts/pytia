from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.knowledge_interfaces.real_param import RealParam
from pytia.framework.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeConnect(HybridShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_connect = com_object

    @property
    def base_curve(self) -> Reference:
        return Reference(self.hybrid_shape_connect.BaseCurve)

    @base_curve.setter
    def base_curve(self, refernce_curve: Reference):
        self.hybrid_shape_connect.BaseCurve = refernce_curve.com_object

    @property
    def connect_type(self) -> int:
        return self.hybrid_shape_connect.ConnectType

    @connect_type.setter
    def connect_type(self, value: int):
        self.hybrid_shape_connect.ConnectType = value

    @property
    def first_continuity(self) -> int:
        return self.hybrid_shape_connect.FirstContinuity

    @first_continuity.setter
    def first_continuity(self, value: int):
        self.hybrid_shape_connect.FirstContinuity = value

    @property
    def first_curve(self) -> Reference:
        return Reference(self.hybrid_shape_connect.FirstCurve)

    @first_curve.setter
    def first_curve(self, refernce_curve: Reference):
        self.hybrid_shape_connect.FirstCurve = refernce_curve.com_object

    @property
    def first_orientation(self) -> int:
        return self.hybrid_shape_connect.FirstOrientation

    @first_orientation.setter
    def first_orientation(self, value: int):
        self.hybrid_shape_connect.FirstOrientation = value

    @property
    def first_point(self) -> Reference:
        return Reference(self.hybrid_shape_connect.FirstPoint)

    @first_point.setter
    def first_point(self, refernce_curve: Reference):
        self.hybrid_shape_connect.FirstPoint = refernce_curve.com_object

    @property
    def first_tension(self) -> RealParam:
        return RealParam(self.hybrid_shape_connect.FirstTension)

    @property
    def second_continuity(self) -> int:
        return self.hybrid_shape_connect.SecondContinuity

    @second_continuity.setter
    def second_continuity(self, value: int):
        self.hybrid_shape_connect.SecondContinuity = value

    @property
    def second_curve(self) -> Reference:
        return Reference(self.hybrid_shape_connect.SecondCurve)

    @second_curve.setter
    def second_curve(self, refernce_curve: Reference):
        self.hybrid_shape_connect.SecondCurve = refernce_curve.com_object

    @property
    def second_orientation(self) -> int:
        return self.hybrid_shape_connect.SecondOrientation

    @second_orientation.setter
    def second_orientation(self, value: int):
        self.hybrid_shape_connect.SecondOrientation = value

    @property
    def second_point(self) -> Reference:
        return Reference(self.hybrid_shape_connect.SecondPoint)

    @second_point.setter
    def second_point(self, reference_point: Reference):
        self.hybrid_shape_connect.SecondPoint = reference_point.com_object

    @property
    def second_tension(self) -> RealParam:
        return RealParam(self.hybrid_shape_connect.SecondTension)

    @property
    def trim(self) -> bool:
        return self.hybrid_shape_connect.Trim

    @trim.setter
    def trim(self, value: bool):
        self.hybrid_shape_connect.Trim = value

    def __repr__(self):
        return f'HybridShapeConnect(name="{self.name}")'
