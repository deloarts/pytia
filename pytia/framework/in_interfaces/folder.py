from typing import TYPE_CHECKING
from pytia.framework.in_interfaces.file_component import FileComponent
from pytia.framework.in_interfaces.files import Files

if TYPE_CHECKING:
    from pytia.framework.in_interfaces.folders import Folders


class Folder(FileComponent):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.folder = com_object

    @property
    def files(self) -> Files:
        return Files(self.folder.Files)

    @property
    def sub_folders(self) -> "Folders":
        from pytia.framework.in_interfaces.folders import Folders

        return Folders(self.folder.SubFolders)

    def __repr__(self):
        return f'Folder(name="{self.name}")'
