from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.knowledge_interfaces.angle import Angle
from pytia.framework.knowledge_interfaces.length import Length
from pytia.framework.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeCurveSmooth(HybridShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_curve_smooth = com_object

    @property
    def correction_mode(self) -> int:
        return self.hybrid_shape_curve_smooth.CorrectionMode

    @correction_mode.setter
    def correction_mode(self, value: int):
        self.hybrid_shape_curve_smooth.CorrectionMode = value

    @property
    def curvature_threshold(self) -> float:
        return self.hybrid_shape_curve_smooth.CurvatureThreshold

    @curvature_threshold.setter
    def curvature_threshold(self, value: float):
        self.hybrid_shape_curve_smooth.CurvatureThreshold = value

    @property
    def curvature_threshold_activity(self) -> bool:
        return self.hybrid_shape_curve_smooth.CurvatureThresholdActivity

    @curvature_threshold_activity.setter
    def curvature_threshold_activity(self, value: bool):
        self.hybrid_shape_curve_smooth.CurvatureThresholdActivity = value

    @property
    def curve_to_smooth(self) -> Reference:
        return Reference(self.hybrid_shape_curve_smooth.CurveToSmooth)

    @curve_to_smooth.setter
    def curve_to_smooth(self, reference_curve: Reference):
        self.hybrid_shape_curve_smooth.CurveToSmooth = reference_curve.com_object

    @property
    def end_extremity_continuity(self) -> int:
        return self.hybrid_shape_curve_smooth.EndExtremityContinuity

    @end_extremity_continuity.setter
    def end_extremity_continuity(self, value: int):
        self.hybrid_shape_curve_smooth.EndExtremityContinuity = value

    @property
    def maximum_deviation(self) -> Length:
        return Length(self.hybrid_shape_curve_smooth.MaximumDeviation)

    @property
    def maximum_deviation_activity(self) -> bool:
        return self.hybrid_shape_curve_smooth.MaximumDeviationActivity

    @maximum_deviation_activity.setter
    def maximum_deviation_activity(self, value: bool):
        self.hybrid_shape_curve_smooth.MaximumDeviationActivity = value

    @property
    def start_extremity_continuity(self) -> int:
        return self.hybrid_shape_curve_smooth.StartExtremityContinuity

    @start_extremity_continuity.setter
    def start_extremity_continuity(self, value: int):
        self.hybrid_shape_curve_smooth.StartExtremityContinuity = value

    @property
    def support(self) -> Reference:
        return Reference(self.hybrid_shape_curve_smooth.Support)

    @support.setter
    def support(self, reference_support: Reference):
        self.hybrid_shape_curve_smooth.Support = reference_support.com_object

    @property
    def tangency_threshold(self) -> Angle:
        return Angle(self.hybrid_shape_curve_smooth.TangencyThreshold)

    @property
    def topology_simplification_activity(self) -> bool:
        return self.hybrid_shape_curve_smooth.TopologySimplificationActivity

    @topology_simplification_activity.setter
    def topology_simplification_activity(self, value: bool):
        self.hybrid_shape_curve_smooth.TopologySimplificationActivity = value

    def add_frozen_curve_segment(self, i_curve: Reference) -> None:
        return self.hybrid_shape_curve_smooth.AddFrozenCurveSegment(i_curve.com_object)

    def add_frozen_point(self, i_point: Reference) -> None:
        return self.hybrid_shape_curve_smooth.AddFrozenPoint(i_point.com_object)

    def get_frozen_curve_segment(self, i_pos: int) -> Reference:
        return Reference(self.hybrid_shape_curve_smooth.GetFrozenCurveSegment(i_pos))

    def get_frozen_curve_segments_size(self) -> int:
        return self.hybrid_shape_curve_smooth.GetFrozenCurveSegmentsSize()

    def get_frozen_point(self, i_pos: int) -> Reference:
        return Reference(self.hybrid_shape_curve_smooth.GetFrozenPoint(i_pos))

    def get_frozen_points_size(self) -> int:
        return self.hybrid_shape_curve_smooth.GetFrozenPointsSize()

    def remove_all_frozen_curve_segments(self) -> None:
        return self.hybrid_shape_curve_smooth.RemoveAllFrozenCurveSegments()

    def remove_all_frozen_points(self) -> None:
        return self.hybrid_shape_curve_smooth.RemoveAllFrozenPoints()

    def remove_frozen_curve_segment(self, i_curve: Reference) -> None:
        return self.hybrid_shape_curve_smooth.RemoveFrozenCurveSegment(
            i_curve.com_object
        )

    def remove_frozen_point(self, i_point: Reference) -> None:
        return self.hybrid_shape_curve_smooth.RemoveFrozenPoint(i_point.com_object)

    def set_maximum_deviation(self, i_max_deviation: float) -> None:
        return self.hybrid_shape_curve_smooth.SetMaximumDeviation(i_max_deviation)

    def set_tangency_threshold(self, i_tangency_threshold: float) -> None:
        return self.hybrid_shape_curve_smooth.SetTangencyThreshold(i_tangency_threshold)

    def __repr__(self):
        return f'HybridShapeCurveSmooth(name="{self.name}")'
