from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeTransfer(HybridShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_transfer = com_object

    @property
    def element_to_transfer(self) -> Reference:
        return Reference(self.hybrid_shape_transfer.ElementToTransfer)

    @element_to_transfer.setter
    def element_to_transfer(self, reference_element: Reference):
        self.hybrid_shape_transfer.ElementToTransfer = reference_element.com_object

    @property
    def surface_to_unfold(self) -> Reference:
        return Reference(self.hybrid_shape_transfer.SurfaceToUnfold)

    @surface_to_unfold.setter
    def surface_to_unfold(self, reference_surface: Reference):
        self.hybrid_shape_transfer.SurfaceToUnfold = reference_surface.com_object

    @property
    def type_of_transfer(self) -> int:
        return self.hybrid_shape_transfer.TypeOfTransfer

    @type_of_transfer.setter
    def type_of_transfer(self, value: int):
        self.hybrid_shape_transfer.TypeOfTransfer = value

    @property
    def unfold_type(self) -> int:
        return self.hybrid_shape_transfer.UnfoldType

    @unfold_type.setter
    def unfold_type(self, value: int):
        self.hybrid_shape_transfer.UnfoldType = value

    @property
    def unfolded_surface(self) -> Reference:
        return Reference(self.hybrid_shape_transfer.UnfoldedSurface)

    @unfolded_surface.setter
    def unfolded_surface(self, reference_surface: Reference):
        self.hybrid_shape_transfer.UnfoldedSurface = reference_surface.com_object

    def __repr__(self):
        return f'HybridShapeTransfer(name="{self.name}")'
