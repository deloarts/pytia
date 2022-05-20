from pytia.framework.knowledge_interfaces.real_param import RealParam
from pytia.framework.system_interfaces.any_object import AnyObject


class FreeParameter(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.free_parameter = com_object

    @property
    def inf_range(self) -> float:
        return self.free_parameter.InfRange

    @inf_range.setter
    def inf_range(self, value: float):
        self.free_parameter.InfRange = value

    @property
    def parameter(self) -> RealParam:
        return RealParam(self.free_parameter.Parameter)

    @parameter.setter
    def parameter(self, value: RealParam):
        self.free_parameter.Parameter = value

    @property
    def step(self) -> float:
        return self.free_parameter.Step

    @step.setter
    def step(self, value: float):
        self.free_parameter.Step = value

    @property
    def sup_range(self) -> float:
        return self.free_parameter.SupRange

    @sup_range.setter
    def sup_range(self, value: float):
        self.free_parameter.SupRange = value

    def __repr__(self):
        return f'FreeParameter(name="{ self.name }")'
