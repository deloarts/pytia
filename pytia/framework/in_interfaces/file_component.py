from typing import TYPE_CHECKING
from pytia.framework.system_interfaces.any_object import AnyObject

if TYPE_CHECKING:
    from pytia.framework.in_interfaces.folder import Folder


class FileComponent(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.file_component = com_object

    @property
    def parent_folder(self) -> "Folder":
        from pytia.framework.in_interfaces.folder import Folder

        return Folder(self.file_component.ParentFolder)

    @parent_folder.setter
    def parent_folder(self, value: "Folder"):
        self.file_component.ParentFolder = value

    @property
    def path(self) -> str:
        return self.file_component.Path

    def __repr__(self):
        return f'FileComponent(name="{self.name}")'
