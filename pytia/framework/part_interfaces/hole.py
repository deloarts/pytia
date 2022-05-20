from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.knowledge_interfaces.angle import Angle
from pytia.framework.knowledge_interfaces.length import Length
from pytia.framework.knowledge_interfaces.str_param import StrParam
from pytia.framework.part_interfaces.limit import Limit
from pytia.framework.part_interfaces.sketch_based_shape import SketchBasedShape


class Hole(SketchBasedShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hole = com_object

    @property
    def anchor_mode(self) -> int:
        return self.hole.AnchorMode

    @anchor_mode.setter
    def anchor_mode(self, value: int):
        self.hole.AnchorMode = value

    @property
    def bottom_angle(self) -> Angle:
        return Angle(self.hole.BottomAngle)

    @property
    def bottom_limit(self) -> Limit:
        return Limit(self.hole.BottomLimit)

    @property
    def bottom_type(self) -> int:
        return self.hole.BottomType

    @bottom_type.setter
    def bottom_type(self, value: int):
        self.hole.BottomType = value

    @property
    def counter_sunk_mode(self) -> int:
        return self.hole.CounterSunkMode

    @counter_sunk_mode.setter
    def counter_sunk_mode(self, value: int):
        self.hole.CounterSunkMode = value

    @property
    def diameter(self) -> Length:
        return Length(self.hole.Diameter)

    @property
    def head_angle(self) -> Angle:
        return Angle(self.hole.HeadAngle)

    @property
    def head_depth(self) -> Length:
        return Length(self.hole.HeadDepth)

    @property
    def head_diameter(self) -> Length:
        return Length(self.hole.HeadDiameter)

    @property
    def hole_thread_description(self) -> StrParam:
        return StrParam(self.hole.HoleThreadDescription)

    @property
    def thread_depth(self) -> Length:
        return Length(self.hole.ThreadDepth)

    @property
    def thread_diameter(self) -> Length:
        return Length(self.hole.ThreadDiameter)

    @property
    def thread_pitch(self) -> Length:
        return Length(self.hole.ThreadPitch)

    @property
    def thread_side(self) -> int:
        return self.hole.ThreadSide

    @thread_side.setter
    def thread_side(self, value: int):
        self.hole.ThreadSide = value

    @property
    def threading_mode(self) -> int:
        return self.hole.ThreadingMode

    @threading_mode.setter
    def threading_mode(self, value: int):
        self.hole.ThreadingMode = value

    @property
    def type(self) -> int:
        return self.hole.Type

    @type.setter
    def type(self, value: int):
        self.hole.Type = value

    def create_standard_thread_design_table(self, i_standard_type: int) -> None:
        return self.hole.CreateStandardThreadDesignTable(i_standard_type)

    def create_user_standard_design_table(
        self, i_standard_name: str, i_path: str
    ) -> None:
        return self.hole.CreateUserStandardDesignTable(i_standard_name, i_path)

    def get_direction(self, io_direction: tuple) -> None:
        return self.hole.GetDirection(io_direction)

    def get_origin(self, io_origin: tuple) -> None:
        return self.hole.GetOrigin(io_origin)

    def reverse(self) -> None:
        return self.hole.Reverse()

    def set_direction(self, i_direction: Reference) -> None:
        return self.hole.SetDirection(i_direction.com_object)

    def set_origin(self, i_x: float, i_y: float, i_z: float) -> None:
        return self.hole.SetOrigin(i_x, i_y, i_z)

    def __repr__(self):
        return f'Hole(name="{self.name}")'
