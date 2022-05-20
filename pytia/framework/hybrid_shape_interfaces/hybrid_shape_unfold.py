from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeUnfold(HybridShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_unfold = com_object

    @property
    def direction_to_unfold(self) -> Reference:
        return Reference(self.hybrid_shape_unfold.DirectionToUnfold)

    @direction_to_unfold.setter
    def direction_to_unfold(self, reference: Reference):
        self.hybrid_shape_unfold.DirectionToUnfold = reference.com_object

    @property
    def edge_to_tear_positioning_orientation(self) -> int:
        return self.hybrid_shape_unfold.EdgeToTearPositioningOrientation

    @edge_to_tear_positioning_orientation.setter
    def edge_to_tear_positioning_orientation(self, value: int):
        self.hybrid_shape_unfold.EdgeToTearPositioningOrientation = value

    @property
    def origin_to_unfold(self) -> Reference:
        return Reference(self.hybrid_shape_unfold.OriginToUnfold)

    @origin_to_unfold.setter
    def origin_to_unfold(self, reference_origin: Reference):
        self.hybrid_shape_unfold.OriginToUnfold = reference_origin.com_object

    @property
    def surface_to_unfold(self) -> Reference:
        return Reference(self.hybrid_shape_unfold.SurfaceToUnfold)

    @surface_to_unfold.setter
    def surface_to_unfold(self, reference_surface: Reference):
        self.hybrid_shape_unfold.SurfaceToUnfold = reference_surface.com_object

    @property
    def surface_type(self) -> int:
        return self.hybrid_shape_unfold.SurfaceType

    @surface_type.setter
    def surface_type(self, value: int):
        self.hybrid_shape_unfold.SurfaceType = value

    @property
    def target_orientation_mode(self) -> int:
        return self.hybrid_shape_unfold.TargetOrientationMode

    @target_orientation_mode.setter
    def target_orientation_mode(self, value: int):
        self.hybrid_shape_unfold.TargetOrientationMode = value

    @property
    def target_plane(self) -> Reference:
        return Reference(self.hybrid_shape_unfold.TargetPlane)

    @target_plane.setter
    def target_plane(self, reference_plane: Reference):
        self.hybrid_shape_unfold.TargetPlane = reference_plane.com_object

    def add_edge_to_tear(self, i_element: Reference) -> None:
        return self.hybrid_shape_unfold.AddEdgeToTear(i_element.com_object)

    def add_element_to_transfer(
        self, i_element: Reference, i_type_of_transfer: int
    ) -> None:
        return self.hybrid_shape_unfold.AddElementToTransfer(
            i_element.com_object, i_type_of_transfer
        )

    def get_edge_to_tear(self, i_rank: int) -> Reference:
        return Reference(self.hybrid_shape_unfold.GetEdgeToTear(i_rank))

    def get_element_to_transfer(
        self, i_rank: int, op_element: Reference, o_type_of_transfer: int
    ) -> None:
        return self.hybrid_shape_unfold.GetElementToTransfer(
            i_rank, op_element.com_object, o_type_of_transfer
        )

    def remove_edge_to_tear(self, i_rank: int) -> None:
        return self.hybrid_shape_unfold.RemoveEdgeToTear(i_rank)

    def remove_element_to_transfer(self, i_rank: int) -> None:
        return self.hybrid_shape_unfold.RemoveElementToTransfer(i_rank)

    def replace_elements_to_transfer(self, i_rank: int, i_element: Reference) -> None:
        return self.hybrid_shape_unfold.ReplaceElementsToTransfer(
            i_rank, i_element.com_object
        )

    def __repr__(self):
        return f'HybridShapeUnfold(name="{self.name}")'
