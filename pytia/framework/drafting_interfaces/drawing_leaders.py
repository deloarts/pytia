from typing import Iterator
from pytia.framework.drafting_interfaces.drawing_leader import DrawingLeader
from pytia.framework.system_interfaces.collection import Collection


class DrawingLeaders(Collection):
    def __init__(self, com_object):
        super().__init__(com_object, child_object=DrawingLeader)
        self.drawing_leaders = com_object

    def add(self, i_head_point_x: float, i_head_point_y: float) -> DrawingLeader:
        return DrawingLeader(self.drawing_leaders.Add(i_head_point_x, i_head_point_y))

    def item(self, i_index: int) -> DrawingLeader:
        return DrawingLeader(self.drawing_leaders.Item(i_index))

    def remove(self, i_index: int) -> None:
        return self.drawing_leaders.Remove(i_index)

    def __getitem__(self, n: int) -> DrawingLeader:
        if (n + 1) > self.count:
            raise StopIteration
        return DrawingLeader(self.drawing_leaders.item(n + 1))

    def __iter__(self) -> Iterator[DrawingLeader]:
        for i in range(self.count):
            yield self.child_object(self.com_object.item(i + 1))

    def __repr__(self):
        return f'DrawingLeaders(name="{self.name}")'
