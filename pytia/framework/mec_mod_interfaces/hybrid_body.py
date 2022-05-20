from typing import TYPE_CHECKING
from pytia.framework.mec_mod_interfaces.geometric_elements import GeometricElements
from pytia.framework.mec_mod_interfaces.hybrid_shape import HybridShape
from pytia.framework.mec_mod_interfaces.hybrid_shapes import HybridShapes
from pytia.framework.mec_mod_interfaces.sketches import Sketches
from pytia.framework.system_interfaces.any_object import AnyObject

if TYPE_CHECKING:
    from pytia.framework.mec_mod_interfaces.bodies import Bodies
    from pytia.framework.mec_mod_interfaces.hybrid_bodies import HybridBodies


class HybridBody(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_body = com_object

    @property
    def bodies(self) -> "Bodies":
        from pytia.framework.mec_mod_interfaces.bodies import Bodies

        return Bodies(self.hybrid_body.Bodies)

    @property
    def geometric_elements(self) -> GeometricElements:
        return GeometricElements(self.hybrid_body.GeometricElements)

    @property
    def hybrid_bodies(self) -> "HybridBodies":
        from pytia.framework.mec_mod_interfaces.hybrid_bodies import HybridBodies

        return HybridBodies(self.hybrid_body.HybridBodies)

    @property
    def hybrid_shapes(self) -> HybridShapes:
        return HybridShapes(self.hybrid_body.HybridShapes)

    @property
    def hybrid_sketches(self) -> Sketches:
        return Sketches(self.hybrid_body.HybridSketches)

    def append_hybrid_shape(self, i_hybrid_shape: HybridShape) -> None:
        return self.hybrid_body.AppendHybridShape(i_hybrid_shape.com_object)

    def append_hybrid_shapes(self, shapes):
        for shape in shapes:
            self.append_hybrid_shape(shape)

    def __repr__(self):
        return f'HybridBody(name="{self.name}")'
