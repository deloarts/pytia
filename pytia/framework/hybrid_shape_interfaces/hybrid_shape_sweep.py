from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeSweep(HybridShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_sweep = com_object

    @property
    def c0_vertices_mode(self) -> bool:
        return self.hybrid_shape_sweep.C0VerticesMode

    @c0_vertices_mode.setter
    def c0_vertices_mode(self, value: bool):
        self.hybrid_shape_sweep.C0VerticesMode = value

    @property
    def fill_twisted_areas(self) -> int:
        return self.hybrid_shape_sweep.FillTwistedAreas

    @fill_twisted_areas.setter
    def fill_twisted_areas(self, value: int):
        self.hybrid_shape_sweep.FillTwistedAreas = value

    @property
    def setback_value(self) -> float:
        return self.hybrid_shape_sweep.SetbackValue

    @setback_value.setter
    def setback_value(self, value: float):
        self.hybrid_shape_sweep.SetbackValue = value

    def add_cut_points(self, i_element1: Reference, i_element2: Reference) -> None:
        return self.hybrid_shape_sweep.AddCutPoints(
            i_element1.com_object, i_element2.com_object
        )

    def add_fill_points(self, i_element1: Reference, i_element2: Reference) -> None:
        return self.hybrid_shape_sweep.AddFillPoints(
            i_element1.com_object, i_element2.com_object
        )

    def get_cut_point(self, i_rank: int) -> Reference:
        return Reference(self.hybrid_shape_sweep.GetCutPoint(i_rank))

    def get_fill_point(self, i_rank: int) -> Reference:
        return Reference(self.hybrid_shape_sweep.GetFillPoint(i_rank))

    def remove_all_cut_points(self) -> None:
        return self.hybrid_shape_sweep.RemoveAllCutPoints()

    def remove_all_fill_points(self) -> None:
        return self.hybrid_shape_sweep.RemoveAllFillPoints()

    def __repr__(self):
        return f'HybridShapeSweep(name="{ self.name }")'
