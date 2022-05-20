from typing import Iterator
from pytia.framework.drafting_interfaces.drawing_dimension import DrawingDimension
from pytia.framework.system_interfaces.collection import Collection
from pytia.framework.cat_types.general import cat_variant


class DrawingDimensions(Collection):
    def __init__(self, com_object):
        super().__init__(com_object, child_object=DrawingDimension)
        self.drawing_dimensions = com_object

    def add(
        self,
        i_type_dim: int,
        i_geom_elem: tuple,
        i_pt_coord_elem: tuple,
        i_line_rep: int,
    ) -> DrawingDimension:
        return DrawingDimension(
            self.drawing_dimensions.Add(
                i_type_dim, i_geom_elem, i_pt_coord_elem, i_line_rep
            )
        )

    def add2(
        self,
        i_type_dim: int,
        i_geom_elem: tuple,
        i_pt_coord_elem: tuple,
        i_ldc_ref_elem: cat_variant,
        i_ldc_ref_angle: int,
    ) -> DrawingDimension:
        return DrawingDimension(
            self.drawing_dimensions.Add2(
                i_type_dim,
                i_geom_elem,
                i_pt_coord_elem,
                i_ldc_ref_elem,
                i_ldc_ref_angle,
            )
        )

    def item(self, i_index: cat_variant) -> DrawingDimension:
        return DrawingDimension(self.drawing_dimensions.Item(i_index))

    def remove(self, i_index: cat_variant) -> None:
        return self.drawing_dimensions.Remove(i_index)

    def __getitem__(self, n: int) -> DrawingDimension:
        if (n + 1) > self.count:
            raise StopIteration
        return DrawingDimension(self.drawing_dimensions.item(n + 1))

    def __iter__(self) -> Iterator[DrawingDimension]:
        for i in range(self.count):
            yield self.child_object(self.com_object.item(i + 1))

    def __repr__(self):
        return f'DrawingDimensions(name="{self.name}")'
