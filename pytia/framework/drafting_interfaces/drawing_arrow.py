from pytia.framework.system_interfaces.any_object import AnyObject


class DrawingArrow(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.drawing_arrow = com_object

    @property
    def head_symbol(self) -> int:
        return self.drawing_arrow.HeadSymbol

    @head_symbol.setter
    def head_symbol(self, value: int):
        self.drawing_arrow.HeadSymbol = value

    @property
    def head_target(self) -> AnyObject:
        return AnyObject(self.drawing_arrow.HeadTarget)

    @head_target.setter
    def head_target(self, value: AnyObject):
        self.drawing_arrow.HeadTarget = value

    @property
    def nb_interruption(self) -> int:
        return self.drawing_arrow.NbInterruption

    @property
    def nb_point(self) -> int:
        return self.drawing_arrow.NbPoint

    @property
    def tail_symbol(self) -> int:
        return self.drawing_arrow.TailSymbol

    @tail_symbol.setter
    def tail_symbol(self, value: int):
        self.drawing_arrow.TailSymbol = value

    @property
    def tail_target(self) -> AnyObject:
        return AnyObject(self.drawing_arrow.TailTarget)

    @tail_target.setter
    def tail_target(self, value: AnyObject):
        self.drawing_arrow.TailTarget = value

    def add_interruption(
        self,
        i_first_point_x: float,
        i_first_point_y: float,
        i_second_point_x: float,
        i_second_point_y: float,
    ) -> None:
        return self.drawing_arrow.AddInterruption(
            i_first_point_x, i_first_point_y, i_second_point_x, i_second_point_y
        )

    def add_point(self, i_num: int, i_x: float, i_y: float) -> None:
        return self.drawing_arrow.AddPoint(i_num, i_x, i_y)

    def get_interruptions(self, o_interruptions: tuple) -> int:
        return self.drawing_arrow.GetInterruptions(o_interruptions)

    def get_point(self, i_num: int, o_x: float, o_y: float) -> None:
        return self.drawing_arrow.GetPoint(i_num, o_x, o_y)

    def get_points(self, o_points: tuple) -> int:
        return self.drawing_arrow.GetPoints(o_points)

    def modify_point(self, i_num: int, i_x: float, i_y: float) -> None:
        return self.drawing_arrow.ModifyPoint(i_num, i_x, i_y)

    def remove_interruption(self, i_num: int) -> None:
        return self.drawing_arrow.RemoveInterruption(i_num)

    def remove_point(self, i_num: int) -> None:
        return self.drawing_arrow.RemovePoint(i_num)

    def __repr__(self):
        return f'DrawingArrow(name="{self.name}")'
