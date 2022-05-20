from pytia.framework.system_interfaces.any_object import AnyObject


class SendToService(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.send_to_service = com_object

    def add_file(self, i_path: str) -> None:
        return self.send_to_service.AddFile(i_path)

    def get_last_send_to_method_error(
        self, o_error_param: str, o_error_code: int
    ) -> None:
        return self.send_to_service.GetLastSendToMethodError(
            o_error_param, o_error_code
        )

    def get_list_of_dependant_file(self, o_dependant: tuple) -> None:
        return self.send_to_service.GetListOfDependantFile(o_dependant)

    def get_list_of_to_be_copied_files(self, o_will_be_copied: tuple) -> None:
        return self.send_to_service.GetListOfToBeCopiedFiles(o_will_be_copied)

    def keep_directory(self, i_keep: bool) -> None:
        return self.send_to_service.KeepDirectory(i_keep)

    def remove_file(self, i_file: str) -> None:
        return self.send_to_service.RemoveFile(i_file)

    def run(self) -> None:
        return self.send_to_service.Run()

    def set_directory_file(self, i_directory: str) -> None:
        return self.send_to_service.SetDirectoryFile(i_directory)

    def set_directory_one_file(self, i_file: str, i_directory: str) -> None:
        return self.send_to_service.SetDirectoryOneFile(i_file, i_directory)

    def set_initial_file(self, i_path: str) -> None:
        return self.send_to_service.SetInitialFile(i_path)

    def set_rename_file(self, i_oldname: str, i_new_name: str) -> None:
        return self.send_to_service.SetRenameFile(i_oldname, i_new_name)

    def __repr__(self):
        return f'SendToService(name="{self.name}")'
