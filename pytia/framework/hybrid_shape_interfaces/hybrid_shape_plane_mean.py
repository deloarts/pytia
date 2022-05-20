from pytia.framework.hybrid_shape_interfaces.plane import Plane
from pytia.framework.in_interfaces.reference import Reference


class HybridShapePlaneMean(Plane):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_plane_mean = com_object

    def add_point(self, i_passing_point: Reference) -> None:
        return self.hybrid_shape_plane_mean.AddPoint(i_passing_point.com_object)

    def get_point(self, i_rank: int, o_passing_point: Reference) -> None:
        return self.hybrid_shape_plane_mean.GetPoint(i_rank, o_passing_point.com_object)

    def get_pos(self, i_point: Reference) -> int:
        return self.hybrid_shape_plane_mean.GetPos(i_point.com_object)

    def get_size(self) -> int:
        return self.hybrid_shape_plane_mean.GetSize()

    def remove_all(self) -> None:
        return self.hybrid_shape_plane_mean.RemoveAll()

    def remove_element(self, i_rank: int) -> None:
        return self.hybrid_shape_plane_mean.RemoveElement(i_rank)

    def replace_point_at_position(self, i_point: Reference, i_pos: int) -> None:
        return self.hybrid_shape_plane_mean.ReplacePointAtPosition(
            i_point.com_object, i_pos
        )

    def __repr__(self):
        return f'HybridShapePlaneMean(name="{self.name}")'
