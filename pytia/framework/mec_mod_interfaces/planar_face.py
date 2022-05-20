from pytia.framework.mec_mod_interfaces.face import Face


class PlanarFace(Face):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.planar_face = com_object

    def get_first_axis(self, o_first_axis: tuple) -> None:
        return self.planar_face.GetFirstAxis(o_first_axis)

    def get_origin(self, o_origin: tuple) -> None:
        return self.planar_face.GetOrigin(o_origin)

    def get_second_axis(self, o_second_axis: tuple) -> None:
        return self.planar_face.GetSecondAxis(o_second_axis)

    def __repr__(self):
        return f'PlanarFace(name="{self.name}")'
