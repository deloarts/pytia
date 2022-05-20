from pytia.framework.system_interfaces.any_object import AnyObject


class SystemService(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.system_service = com_object

    def environ(self, i_env_string):
        return str(self.system_service.Environ(i_env_string))

    def evaluate(self, i_script_text, i_language, i_function_name, i_parameters):
        return self.system_service.Evaluate(
            i_script_text, i_language, i_function_name, i_parameters
        )

    def execute_background_processus(self, i_executable_path):
        return int(self.system_service.ExecuteBackgroundProcessus(i_executable_path))

    def execute_processus(self, i_executable_path):
        return int(self.system_service.ExecuteProcessus(i_executable_path))

    def execute_script(
        self, i_library_name, i_type, i_program_name, i_function_name, i_parameters
    ):
        return self.system_service.ExecuteScript(
            i_library_name, i_type, i_program_name, i_function_name, i_parameters
        )

    def print(self, i_string):
        return self.system_service.Print(i_string)

    def __repr__(self):
        return f'SystemService(name="{self.name}")'
