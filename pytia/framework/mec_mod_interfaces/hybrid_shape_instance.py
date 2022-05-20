from pytia.framework.mec_mod_interfaces.hybrid_shape import HybridShape
from pytia.framework.system_interfaces.any_object import AnyObject


class HybridShapeInstance(HybridShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_instance = com_object

    @property
    def inputs_count(self) -> int:
        return self.hybrid_shape_instance.InputsCount

    @property
    def outputs_count(self) -> int:
        return self.hybrid_shape_instance.OutputsCount

    @property
    def parameters_count(self) -> int:
        return self.hybrid_shape_instance.ParametersCount

    def get_input(self, i_index: str) -> AnyObject:
        return AnyObject(self.hybrid_shape_instance.GetInput(i_index))

    def get_input_data(self, i_name: str) -> AnyObject:
        return self.hybrid_shape_instance.GetInputData(i_name)

    def get_input_data_from_position(self, i_position: int) -> AnyObject:
        return self.hybrid_shape_instance.GetInputDataFromPosition(i_position)

    def get_input_from_position(self, i_position: int) -> AnyObject:
        return AnyObject(self.hybrid_shape_instance.GetInputFromPosition(i_position))

    def get_output(self, i_name: str) -> AnyObject:
        return AnyObject(self.hybrid_shape_instance.GetOutput(i_name))

    def get_output_from_position(self, i_position: int) -> AnyObject:
        return AnyObject(self.hybrid_shape_instance.GetOutputFromPosition(i_position))

    def get_parameter(self, i_name: str) -> AnyObject:
        return AnyObject(self.hybrid_shape_instance.GetParameter(i_name))

    def get_parameter_from_position(self, i_position: int) -> AnyObject:
        return AnyObject(
            self.hybrid_shape_instance.GetParameterFromPosition(i_position)
        )

    def put_input(self, i_index: str, i_input: AnyObject) -> None:
        return self.hybrid_shape_instance.PutInput(i_index, i_input.com_object)

    def put_input_data(self, i_name: str, i_input: AnyObject) -> None:
        return self.hybrid_shape_instance.PutInputData(i_name, i_input.com_object)

    def __repr__(self):
        return f'HybridShapeInstance(name="{ self.name }")'
