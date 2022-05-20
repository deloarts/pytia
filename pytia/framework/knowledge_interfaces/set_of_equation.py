from typing import TYPE_CHECKING
from pytia.framework.knowledge_interfaces.relation import Relation

if TYPE_CHECKING:
    from pytia.framework.knowledge_interfaces.parameter import Parameter


class SetOfEquation(Relation):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.set_of_equation = com_object

    def get_max_calculation_time(self) -> int:
        return self.set_of_equation.GetMaxCalculationTime()

    def get_precision(self) -> float:
        return self.set_of_equation.GetPrecision()

    def get_symbolc_transformations(self) -> bool:
        return self.set_of_equation.GetSymbolcTransformations()

    def is_stop_dialog(self) -> bool:
        return self.set_of_equation.IsStopDialog()

    def set_max_calculation_time(self, i_max_time: int) -> None:
        return self.set_of_equation.SetMaxCalculationTime(i_max_time)

    def set_parameter_as_input(self, i_parameter: "Parameter") -> None:
        return self.set_of_equation.SetParameterAsInput(i_parameter.com_object)

    def set_parameter_as_output(self, i_parameter: "Parameter") -> None:
        return self.set_of_equation.SetParameterAsOutput(i_parameter.com_object)

    def set_precision(self, i_eps: float) -> None:
        return self.set_of_equation.SetPrecision(i_eps)

    def use_stop_dialog(self, i_used: bool) -> None:
        return self.set_of_equation.UseStopDialog(i_used)

    def use_symbolc_transformations(self, i_gauss: bool) -> None:
        return self.set_of_equation.UseSymbolcTransformations(i_gauss)

    def __repr__(self):
        return f'SetOfEquation(name="{self.name}")'
