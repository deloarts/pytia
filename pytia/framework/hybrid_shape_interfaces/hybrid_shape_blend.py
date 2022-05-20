from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.knowledge_interfaces.angle import Angle
from pytia.framework.knowledge_interfaces.length import Length
from pytia.framework.knowledge_interfaces.real_param import RealParam
from pytia.framework.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeBlend(HybridShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_blend = com_object

    @property
    def coupling(self) -> int:
        return self.hybrid_shape_blend.Coupling

    @coupling.setter
    def coupling(self, value: int):
        self.hybrid_shape_blend.Coupling = value

    @property
    def ruled_developable_surface(self) -> bool:
        return self.hybrid_shape_blend.RuledDevelopableSurface

    @ruled_developable_surface.setter
    def ruled_developable_surface(self, value: bool):
        self.hybrid_shape_blend.RuledDevelopableSurface = value

    @property
    def smooth_angle_threshold(self) -> Angle:
        return Angle(self.hybrid_shape_blend.SmoothAngleThreshold)

    @property
    def smooth_angle_threshold_activity(self) -> bool:
        return self.hybrid_shape_blend.SmoothAngleThresholdActivity

    @smooth_angle_threshold_activity.setter
    def smooth_angle_threshold_activity(self, value: bool):
        self.hybrid_shape_blend.SmoothAngleThresholdActivity = value

    @property
    def smooth_deviation(self) -> Length:
        return Length(self.hybrid_shape_blend.SmoothDeviation)

    @property
    def smooth_deviation_activity(self) -> bool:
        return self.hybrid_shape_blend.SmoothDeviationActivity

    @smooth_deviation_activity.setter
    def smooth_deviation_activity(self, value: bool):
        self.hybrid_shape_blend.SmoothDeviationActivity = value

    @property
    def spine(self) -> Reference:
        return Reference(self.hybrid_shape_blend.Spine)

    @spine.setter
    def spine(self, reference_spine: Reference):
        self.hybrid_shape_blend.Spine = reference_spine.com_object

    def get_border_mode(self, i_blend_limit: int) -> int:
        return self.hybrid_shape_blend.GetBorderMode(i_blend_limit)

    def get_closing_point(self, i_blend_limit: int) -> Reference:
        return Reference(self.hybrid_shape_blend.GetClosingPoint(i_blend_limit))

    def get_continuity(self, i_blend_limit: int) -> int:
        return self.hybrid_shape_blend.GetContinuity(i_blend_limit)

    def get_curve(self, i_blend_limit: int) -> Reference:
        return Reference(self.hybrid_shape_blend.GetCurve(i_blend_limit))

    def get_orientation(self, i_blend_limit: int) -> int:
        return self.hybrid_shape_blend.GetOrientation(i_blend_limit)

    def get_ruled_developable_surface_connection(self, i_blend_limit: int) -> int:
        return self.hybrid_shape_blend.GetRuledDevelopableSurfaceConnection(
            i_blend_limit
        )

    def get_support(self, i_blend_limit: int) -> Reference:
        return Reference(self.hybrid_shape_blend.GetSupport(i_blend_limit))

    def get_tension_in_double(self, i_blend_limit: int, i_rank: int) -> RealParam:
        return RealParam(
            self.hybrid_shape_blend.GetTensionInDouble(i_blend_limit, i_rank)
        )

    def get_tension_type(self, i_blend_limit: int) -> int:
        return self.hybrid_shape_blend.GetTensionType(i_blend_limit)

    def get_transition(self, i_blend_limit: int) -> int:
        return self.hybrid_shape_blend.GetTransition(i_blend_limit)

    def get_trim_support(self, i_blend_limit: int) -> int:
        return self.hybrid_shape_blend.GetTrimSupport(i_blend_limit)

    def insert_coupling(self, i_position: int) -> None:
        return self.hybrid_shape_blend.InsertCoupling(i_position)

    def insert_coupling_point(
        self, i_coupling_index: int, i_position: int, i_point: Reference
    ) -> None:
        return self.hybrid_shape_blend.InsertCouplingPoint(
            i_coupling_index, i_position, i_point.com_object
        )

    def set_border_mode(self, i_blend_limit: int, i_border: int) -> None:
        return self.hybrid_shape_blend.SetBorderMode(i_blend_limit, i_border)

    def set_closing_point(self, i_blend_limit: int, i_closing_point: Reference) -> None:
        return self.hybrid_shape_blend.SetClosingPoint(
            i_blend_limit, i_closing_point.com_object
        )

    def set_continuity(self, i_blend_limit: int, i_continuity: int) -> None:
        return self.hybrid_shape_blend.SetContinuity(i_blend_limit, i_continuity)

    def set_curve(self, i_blend_limit: int, i_curve: Reference) -> None:
        return self.hybrid_shape_blend.SetCurve(i_blend_limit, i_curve.com_object)

    def set_orientation(self, i_blend_limit: int, i_orientation: int) -> None:
        return self.hybrid_shape_blend.SetOrientation(i_blend_limit, i_orientation)

    def set_ruled_developable_surface_connection(
        self, i_blend_limit: int, i_blend_connection: int
    ) -> None:
        return self.hybrid_shape_blend.SetRuledDevelopableSurfaceConnection(
            i_blend_limit, i_blend_connection
        )

    def set_smooth_angle_threshold(self, i_angle: float) -> None:
        return self.hybrid_shape_blend.SetSmoothAngleThreshold(i_angle)

    def set_smooth_deviation(self, i_length: float) -> None:
        return self.hybrid_shape_blend.SetSmoothDeviation(i_length)

    def set_support(self, i_blend_limit: int, i_support: Reference) -> None:
        return self.hybrid_shape_blend.SetSupport(i_blend_limit, i_support.com_object)

    def set_tension_in_double(
        self,
        i_blend_limit: int,
        i_tension_type: int,
        i_first_tension: float,
        i_second_tension: float,
    ) -> None:
        return self.hybrid_shape_blend.SetTensionInDouble(
            i_blend_limit, i_tension_type, i_first_tension, i_second_tension
        )

    def set_tension_type(self, i_blend_limit: int, i_tension_type: int) -> None:
        return self.hybrid_shape_blend.SetTensionType(i_blend_limit, i_tension_type)

    def set_transition(self, i_blend_limit: int, i_transition: int) -> None:
        return self.hybrid_shape_blend.SetTransition(i_blend_limit, i_transition)

    def set_trim_support(self, i_blend_limit: int, i_trim_support: int) -> None:
        return self.hybrid_shape_blend.SetTrimSupport(i_blend_limit, i_trim_support)

    def unset_closing_point(self, i_blend_limit: int) -> None:
        return self.hybrid_shape_blend.UnsetClosingPoint(i_blend_limit)

    def unset_support(self, i_blend_limit: int) -> None:
        return self.hybrid_shape_blend.UnsetSupport(i_blend_limit)

    def __repr__(self):
        return f'HybridShapeBlend(name="{self.name}")'
