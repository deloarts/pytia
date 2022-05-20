from typing import TYPE_CHECKING
from pytia.framework.system_interfaces.any_object import AnyObject

if TYPE_CHECKING:
    from pytia.framework.drafting_interfaces.drawing_leaders import DrawingLeaders


class DrawingLeader(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.drawing_leader = com_object

    @property
    def all_around(self) -> bool:
        return self.drawing_leader.AllAround

    @all_around.setter
    def all_around(self, value: bool):
        self.drawing_leader.AllAround = value

    @property
    def anchor_point(self) -> int:
        return self.drawing_leader.AnchorPoint

    @anchor_point.setter
    def anchor_point(self, value: int):
        self.drawing_leader.AnchorPoint = value

    @property
    def head_symbol(self) -> int:
        return self.drawing_leader.HeadSymbol

    @head_symbol.setter
    def head_symbol(self, value: int):
        self.drawing_leader.HeadSymbol = value

    @property
    def head_target(self) -> AnyObject:
        return AnyObject(self.drawing_leader.HeadTarget)

    @head_target.setter
    def head_target(self, value: AnyObject):
        self.drawing_leader.HeadTarget = value

    @property
    def leaders(self) -> "DrawingLeaders":
        from pytia.framework.drafting_interfaces.drawing_leaders import DrawingLeaders

        return DrawingLeaders(self.drawing_leader.Leaders)

    @property
    def nb_interruption(self) -> int:
        return self.drawing_leader.NbInterruption

    @property
    def nb_point(self) -> int:
        return self.drawing_leader.NbPoint

    def add_interruption(
        self,
        i_first_point_x: float,
        i_first_point_y: float,
        i_second_point_x: float,
        i_second_point_y: float,
    ) -> None:
        return self.drawing_leader.AddInterruption(
            i_first_point_x, i_first_point_y, i_second_point_x, i_second_point_y
        )

    def add_point(self, i_num: int, i_x: float, i_y: float) -> None:
        return self.drawing_leader.AddPoint(i_num, i_x, i_y)

    def get_interruptions(self, o_interruptions: tuple) -> int:
        return self.drawing_leader.GetInterruptions(o_interruptions)

    def get_point(self, i_num: int, o_x: float, o_y: float) -> None:
        return self.drawing_leader.GetPoint(i_num, o_x, o_y)

    def get_points(self, o_points: tuple) -> int:
        return self.drawing_leader.GetPoints(o_points)

    def modify_point(self, i_num: int, i_x: float, i_y: float) -> None:
        return self.drawing_leader.ModifyPoint(i_num, i_x, i_y)

    def remove_interruption(self, i_num: int) -> None:
        return self.drawing_leader.RemoveInterruption(i_num)

    def remove_point(self, i_num: int) -> None:
        return self.drawing_leader.RemovePoint(i_num)

    def __repr__(self):
        return f'DrawingLeader(name="{self.name}")'
