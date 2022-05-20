from typing import Iterator
from pytia.framework.in_interfaces.file import File
from pytia.framework.system_interfaces.collection import Collection


class Files(Collection):
    def __init__(self, com_object):
        super().__init__(com_object, child_object=File)
        self.files = com_object

    def item(self, i_number: int) -> File:
        return File(self.files.Item(i_number))

    def __getitem__(self, n: int) -> File:
        if (n + 1) > self.count:
            raise StopIteration
        return File(self.files.item(n + 1))

    def __iter__(self) -> Iterator[File]:
        for i in range(self.count):
            yield self.child_object(self.com_object.item(i + 1))

    def __repr__(self):
        return f'Files(name="{self.name}")'
