from pytia.framework.knowledge_interfaces.check import Check
from pytia.framework.knowledge_interfaces.real_param import RealParam


class OptimizationConstraint(Check):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.optimization_constraint = com_object

    @property
    def distance_to_satisfaction(self) -> RealParam:
        return RealParam(self.optimization_constraint.DistanceToSatisfaction)

    @property
    def precision(self) -> float:
        return self.optimization_constraint.Precision

    @precision.setter
    def precision(self, value: float):
        self.optimization_constraint.Precision = value

    @property
    def satisfaction(self) -> bool:
        return self.optimization_constraint.Satisfaction

    def __repr__(self):
        return f'OptimizationConstraint(name="{self.name}")'
