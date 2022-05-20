from pytia.framework.mec_mod_interfaces.hybrid_shape import HybridShape


class Plane(HybridShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.plane = com_object

    def get_first_axis(self, o_first_axis: tuple) -> None:
        return self.plane.GetFirstAxis(o_first_axis)

    def get_origin(self, o_origin: tuple) -> None:
        return self.plane.GetOrigin(o_origin)

    def get_position(self, o_x: float, o_y: float, o_z: float) -> None:
        return self.plane.GetPosition(o_x, o_y, o_z)

    def get_second_axis(self, o_second_axis: tuple) -> None:
        return self.plane.GetSecondAxis(o_second_axis)

    def is_a_ref_plane(self) -> int:
        return self.plane.IsARefPlane()

    def put_first_axis(self, i_first_axis: tuple) -> None:
        return self.plane.PutFirstAxis(i_first_axis)

    def put_origin(self, i_origin: tuple) -> None:
        return self.plane.PutOrigin(i_origin)

    def put_second_axis(self, i_second_axis: tuple) -> None:
        return self.plane.PutSecondAxis(i_second_axis)

    def remove_position(self) -> None:
        return self.plane.RemovePosition()

    def set_position(self, i_x: float, i_y: float, i_z: float) -> None:
        return self.plane.SetPosition(i_x, i_y, i_z)

    def __repr__(self):
        return f'Plane(name="{ self.name }")'
