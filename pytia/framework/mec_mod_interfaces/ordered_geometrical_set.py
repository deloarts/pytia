from typing import TYPE_CHECKING
from pytia.framework.mec_mod_interfaces.hybrid_shapes import HybridShapes
from pytia.framework.mec_mod_interfaces.sketches import Sketches
from pytia.framework.system_interfaces.any_object import AnyObject

if TYPE_CHECKING:
    from pytia.framework.mec_mod_interfaces.bodies import Bodies
    from pytia.framework.mec_mod_interfaces.ordered_geometrical_sets import (
        OrderedGeometricalSets,
    )
    from pytia.framework.mec_mod_interfaces.hybrid_shape import HybridShape


class OrderedGeometricalSet(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.ordered_geometrical_set = com_object

    @property
    def bodies(self) -> "Bodies":
        from pytia.framework.mec_mod_interfaces.bodies import Bodies

        return Bodies(self.ordered_geometrical_set.Bodies)

    @property
    def hybrid_shapes(self) -> HybridShapes:
        return HybridShapes(self.ordered_geometrical_set.HybridShapes)

    @property
    def ordered_geometrical_sets(self) -> "OrderedGeometricalSets":
        from pytia.framework.mec_mod_interfaces.ordered_geometrical_sets import (
            OrderedGeometricalSets,
        )

        return OrderedGeometricalSets(
            self.ordered_geometrical_set.OrderedGeometricalSets
        )

    @property
    def ordered_sketches(self) -> Sketches:
        return Sketches(self.ordered_geometrical_set.OrderedSketches)

    def insert_hybrid_shape(self, i_hybrid_shape: "HybridShape") -> None:
        return self.ordered_geometrical_set.InsertHybridShape(i_hybrid_shape.com_object)

    def __repr__(self):
        return f'OrderedGeometricalSet(name="{self.name}")'
