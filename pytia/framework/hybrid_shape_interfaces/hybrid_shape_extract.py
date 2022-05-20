from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeExtract(HybridShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_extract = com_object

    @property
    def angular_threshold(self) -> float:
        return self.hybrid_shape_extract.AngularThreshold

    @angular_threshold.setter
    def angular_threshold(self, value: float):
        self.hybrid_shape_extract.AngularThreshold = value

    @property
    def angular_threshold_activity(self) -> bool:
        return self.hybrid_shape_extract.AngularThresholdActivity

    @angular_threshold_activity.setter
    def angular_threshold_activity(self, value: bool):
        self.hybrid_shape_extract.AngularThresholdActivity = value

    @property
    def complementary_extract(self) -> bool:
        return self.hybrid_shape_extract.ComplementaryExtract

    @complementary_extract.setter
    def complementary_extract(self, value: bool):
        self.hybrid_shape_extract.ComplementaryExtract = value

    @property
    def curvature_threshold(self) -> float:
        return self.hybrid_shape_extract.CurvatureThreshold

    @curvature_threshold.setter
    def curvature_threshold(self, value: float):
        self.hybrid_shape_extract.CurvatureThreshold = value

    @property
    def curvature_threshold_activity(self) -> bool:
        return self.hybrid_shape_extract.CurvatureThresholdActivity

    @curvature_threshold_activity.setter
    def curvature_threshold_activity(self, value: bool):
        self.hybrid_shape_extract.CurvatureThresholdActivity = value

    @property
    def distance_threshold(self) -> float:
        return self.hybrid_shape_extract.DistanceThreshold

    @distance_threshold.setter
    def distance_threshold(self, value: float):
        self.hybrid_shape_extract.DistanceThreshold = value

    @property
    def distance_threshold_activity(self) -> bool:
        return self.hybrid_shape_extract.DistanceThresholdActivity

    @distance_threshold_activity.setter
    def distance_threshold_activity(self, value: bool):
        self.hybrid_shape_extract.DistanceThresholdActivity = value

    @property
    def elem(self) -> Reference:
        return Reference(self.hybrid_shape_extract.Elem)

    @elem.setter
    def elem(self, reference_element: Reference):
        self.hybrid_shape_extract.Elem = reference_element.com_object

    @property
    def is_federated(self) -> bool:
        return self.hybrid_shape_extract.IsFederated

    @is_federated.setter
    def is_federated(self, value: bool):
        self.hybrid_shape_extract.IsFederated = value

    @property
    def propagation_type(self) -> int:
        return self.hybrid_shape_extract.PropagationType

    @propagation_type.setter
    def propagation_type(self, value: int):
        self.hybrid_shape_extract.PropagationType = value

    @property
    def support(self) -> Reference:
        return Reference(self.hybrid_shape_extract.Support)

    @support.setter
    def support(self, reference_support: Reference):
        self.hybrid_shape_extract.Support = reference_support.com_object

    def __repr__(self):
        return f'HybridShapeExtract(name="{ self.name }")'
