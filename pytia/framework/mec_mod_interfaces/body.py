from pytia.framework.mec_mod_interfaces.hybrid_bodies import HybridBodies
from pytia.framework.mec_mod_interfaces.hybrid_shape import HybridShape
from pytia.framework.mec_mod_interfaces.hybrid_shapes import HybridShapes
from pytia.framework.mec_mod_interfaces.ordered_geometrical_sets import (
    OrderedGeometricalSets,
)
from pytia.framework.mec_mod_interfaces.shapes import Shapes
from pytia.framework.mec_mod_interfaces.sketches import Sketches
from pytia.framework.system_interfaces.any_object import AnyObject


class Body(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.body = com_object

    @property
    def hybrid_bodies(self) -> HybridBodies:
        return HybridBodies(self.body.HybridBodies)

    @property
    def hybrid_shapes(self) -> HybridShapes:
        return HybridShapes(self.body.HybridShapes)

    @property
    def in_boolean_operation(self) -> bool:
        return self.body.InBooleanOperation

    @property
    def ordered_geometrical_sets(self) -> OrderedGeometricalSets:
        return OrderedGeometricalSets(self.body.OrderedGeometricalSets)

    @property
    def shapes(self) -> Shapes:
        return Shapes(self.body.Shapes)

    @property
    def sketches(self) -> Sketches:
        return Sketches(self.body.Sketches)

    def insert_hybrid_shape(self, i_hybrid_shape: HybridShape) -> None:
        return self.body.InsertHybridShape(i_hybrid_shape.com_object)

    def __repr__(self):
        return f'Body(name="{self.name}")'
