from pytia.framework.knowledge_interfaces.free_parameters import FreeParameters
from pytia.framework.knowledge_interfaces.knowledge_object import KnowledgeObject
from pytia.framework.knowledge_interfaces.optimization_constraints import (
    OptimizationConstraints,
)
from pytia.framework.knowledge_interfaces.real_param import RealParam


class Optimization(KnowledgeObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.optimization = com_object

    @property
    def algorithm_type(self) -> int:
        return self.optimization.AlgorithmType

    @algorithm_type.setter
    def algorithm_type(self, value: int):
        self.optimization.AlgorithmType = value

    @property
    def constraints(self) -> OptimizationConstraints:
        return OptimizationConstraints(self.optimization.Constraints)

    @property
    def conv_speed(self) -> int:
        return self.optimization.ConvSpeed

    @conv_speed.setter
    def conv_speed(self, value: int):
        self.optimization.ConvSpeed = value

    @property
    def free_parameters(self) -> FreeParameters:
        return FreeParameters(self.optimization.FreeParameters)

    @property
    def max_evals_nb(self) -> int:
        return self.optimization.MaxEvalsNb

    @max_evals_nb.setter
    def max_evals_nb(self, value: int):
        self.optimization.MaxEvalsNb = value

    @property
    def max_evals_wo_improvement(self) -> int:
        return self.optimization.MaxEvalsWoImprovement

    @max_evals_wo_improvement.setter
    def max_evals_wo_improvement(self, value: int):
        self.optimization.MaxEvalsWoImprovement = value

    @property
    def max_time(self) -> int:
        return self.optimization.MaxTime

    @max_time.setter
    def max_time(self, value: int):
        self.optimization.MaxTime = value

    @property
    def objective_parameter(self) -> RealParam:
        return RealParam(self.optimization.ObjectiveParameter)

    @objective_parameter.setter
    def objective_parameter(self, value: RealParam):
        self.optimization.ObjectiveParameter = value

    @property
    def optimization_type(self) -> int:
        return self.optimization.OptimizationType

    @optimization_type.setter
    def optimization_type(self, value: int):
        self.optimization.OptimizationType = value

    @property
    def target_value(self) -> RealParam:
        return RealParam(self.optimization.TargetValue)

    @property
    def use_max_evals_wo_improvement(self) -> bool:
        return self.optimization.UseMaxEvalsWoImprovement

    @use_max_evals_wo_improvement.setter
    def use_max_evals_wo_improvement(self, value: bool):
        self.optimization.UseMaxEvalsWoImprovement = value

    @property
    def use_max_time(self) -> bool:
        return self.optimization.UseMaxTime

    @use_max_time.setter
    def use_max_time(self, value: bool):
        self.optimization.UseMaxTime = value

    def run(self, i_with_stop_dialog: bool) -> None:
        return self.optimization.Run(i_with_stop_dialog)

    def __repr__(self):
        return f'Optimization(name="{self.name}")'
