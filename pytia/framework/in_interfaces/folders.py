from typing import Iterator
from pytia.framework.in_interfaces.folder import Folder
from pytia.framework.system_interfaces.collection import Collection


class Folders(Collection):
    def __init__(self, com_object):
        super().__init__(com_object, child_object=Folder)
        self.folders = com_object

    def item(self, i_number: int) -> Folder:
        return Folder(self.folders.Item(i_number))

    def __getitem__(self, n: int) -> Folder:
        if (n + 1) > self.count:
            raise StopIteration
        return Folder(self.folders.item(n + 1))

    def __iter__(self) -> Iterator[Folder]:
        for i in range(self.count):
            yield self.child_object(self.com_object.item(i + 1))

    def __repr__(self):
        return f'Folders(name="{self.name}")'
