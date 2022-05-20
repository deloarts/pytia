from pytia.framework.mec_mod_interfaces.shape import Shape
from pytia.framework.system_interfaces.any_object import AnyObject


class ShapeInstance(Shape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.shape_instance = com_object

    @property
    def inputs_count(self) -> int:
        return self.shape_instance.InputsCount

    @property
    def outputs_count(self) -> int:
        return self.shape_instance.OutputsCount

    @property
    def parameters_count(self) -> int:
        return self.shape_instance.ParametersCount

    def get_input(self, i_name: str) -> AnyObject:
        return AnyObject(self.shape_instance.GetInput(i_name))

    def get_input_data(self, i_name: str) -> AnyObject:
        return self.shape_instance.GetInputData(i_name)

    def get_input_data_from_position(self, i_position: int) -> AnyObject:
        return self.shape_instance.GetInputDataFromPosition(i_position)

    def get_input_from_position(self, i_position: int) -> AnyObject:
        return AnyObject(self.shape_instance.GetInputFromPosition(i_position))

    def get_output(self, i_name: str) -> AnyObject:
        return AnyObject(self.shape_instance.GetOutput(i_name))

    def get_output_from_position(self, i_position: int) -> AnyObject:
        return AnyObject(self.shape_instance.GetOutputFromPosition(i_position))

    def get_parameter(self, i_name: str) -> AnyObject:
        return AnyObject(self.shape_instance.GetParameter(i_name))

    def get_parameter_from_position(self, i_position: int) -> AnyObject:
        return AnyObject(self.shape_instance.GetParameterFromPosition(i_position))

    def put_input(self, i_name: str, i_input: AnyObject) -> None:
        return self.shape_instance.PutInput(i_name, i_input.com_object)

    def put_input_data(self, i_name: str, i_input: AnyObject) -> None:
        return self.shape_instance.PutInputData(i_name, i_input.com_object)

    def __repr__(self):
        return f'ShapeInstance(name="{ self.name }")'
