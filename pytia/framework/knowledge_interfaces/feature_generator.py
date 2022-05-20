from pytia.framework.system_interfaces.any_object import AnyObject


class FeatureGenerator(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.feature_generator = com_object

    @property
    def nb_generated_features(self) -> int:
        return self.feature_generator.NbGeneratedFeatures

    @property
    def script(self) -> str:
        return self.feature_generator.Script

    @script.setter
    def script(self, value: str):
        self.feature_generator.Script = value

    def generate(self, i_context: AnyObject) -> None:
        return self.feature_generator.Generate(i_context.com_object)

    def generate_in_context(self, i_inputs_array: tuple) -> None:
        return self.feature_generator.GenerateInContext(i_inputs_array)

    def load_script_from_file_path(self, i_file_path: str) -> None:
        return self.feature_generator.LoadScriptFromFilePath(i_file_path)

    def __repr__(self):
        return f'FeatureGenerator(name="{ self.name }")'
