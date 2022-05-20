from typing import Iterator
from pytia.framework.drafting_interfaces.drawing_thread import DrawingThread
from pytia.framework.system_interfaces.collection import Collection


class DrawingThreads(Collection):
    def __init__(self, com_object):
        super().__init__(com_object, child_object=DrawingThread)
        self.drawing_threads = com_object

    def add(self, i_geom_elem) -> DrawingThread:
        return DrawingThread(self.drawing_threads.Add(i_geom_elem.com_object))

    def item(self, i_index: int) -> DrawingThread:
        return DrawingThread(self.drawing_threads.Item(i_index))

    def remove(self, i_index: int) -> None:
        return self.drawing_threads.Remove(i_index)

    def __getitem__(self, n: int) -> DrawingThread:
        if (n + 1) > self.count:
            raise StopIteration
        return DrawingThread(self.drawing_threads.item(n + 1))

    def __iter__(self) -> Iterator[DrawingThread]:
        for i in range(self.count):
            yield self.child_object(self.com_object.item(i + 1))

    def __repr__(self):
        return f'DrawingThreads(name="{self.name}")'
