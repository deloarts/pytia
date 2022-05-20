from pytia.framework.in_interfaces.file import File
from pytia.framework.in_interfaces.folder import Folder
from pytia.framework.system_interfaces.any_object import AnyObject


class FileSystem(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.file_system = com_object

    @property
    def file_separator(self) -> str:
        return self.file_system.FileSeparator

    @property
    def path_separator(self) -> str:
        return self.file_system.PathSeparator

    @property
    def temporary_directory(self) -> Folder:
        return Folder(self.file_system.TemporaryDirectory)

    def concatenate_paths(self, i_path_chunk1: str, i_path_chunk2: str) -> str:
        return self.file_system.ConcatenatePaths(i_path_chunk1, i_path_chunk2)

    def copy_file(
        self, i_path_source: str, i_path_destination: str, i_overwrite: bool
    ) -> None:
        return self.file_system.CopyFile(i_path_source, i_path_destination, i_overwrite)

    def copy_folder(self, i_source_path: str, i_destination_path: str) -> None:
        return self.file_system.CopyFolder(i_source_path, i_destination_path)

    def create_file(self, i_path: str, i_overwrite: bool) -> File:
        return File(self.file_system.CreateFile(i_path, i_overwrite))

    def create_folder(self, i_path: str) -> Folder:
        return Folder(self.file_system.CreateFolder(i_path))

    def delete_file(self, i_path: str) -> None:
        return self.file_system.DeleteFile(i_path)

    def delete_folder(self, i_path: str) -> None:
        return self.file_system.DeleteFolder(i_path)

    def file_exists(self, i_path: str) -> bool:
        return self.file_system.FileExists(i_path)

    def folder_exists(self, i_path: str) -> bool:
        return self.file_system.FolderExists(i_path)

    def get_file(self, i_path: str) -> File:
        return File(self.file_system.GetFile(i_path))

    def get_folder(self, i_path: str) -> Folder:
        return Folder(self.file_system.GetFolder(i_path))

    def __repr__(self):
        return f'FileSystem(name="{self.name}")'
