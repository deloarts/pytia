from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.knowledge_interfaces.length import Length
from pytia.framework.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeOffset(HybridShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_offset = com_object

    @property
    def offset_direction(self) -> bool:
        return self.hybrid_shape_offset.OffsetDirection

    @offset_direction.setter
    def offset_direction(self, value: bool):
        self.hybrid_shape_offset.OffsetDirection = value

    @property
    def offset_value(self) -> Length:
        return Length(self.hybrid_shape_offset.OffsetValue)

    @offset_value.setter
    def offset_value(self, length: Length):
        self.hybrid_shape_offset.OffsetValue = length.com_object

    @property
    def offseted_object(self) -> Reference:
        return Reference(self.hybrid_shape_offset.OffsetedObject)

    @offseted_object.setter
    def offseted_object(self, reference_object: Reference):
        self.hybrid_shape_offset.OffsetedObject = reference_object.com_object

    @property
    def suppress_mode(self) -> bool:
        return self.hybrid_shape_offset.SuppressMode

    @suppress_mode.setter
    def suppress_mode(self, value: bool):
        self.hybrid_shape_offset.SuppressMode = value

    def add_tricky_face(self, i_tricky_face: Reference) -> None:
        return self.hybrid_shape_offset.AddTrickyFace(i_tricky_face.com_object)

    def get_tricky_face(self, i_rank: int) -> Reference:
        return Reference(self.hybrid_shape_offset.GetTrickyFace(i_rank))

    def remove_tricky_face(self, i_rank: int) -> None:
        return self.hybrid_shape_offset.RemoveTrickyFace(i_rank)

    def set_offset_value(self, i_offset: float) -> None:
        return self.hybrid_shape_offset.SetOffsetValue(i_offset)

    def __repr__(self):
        return f'HybridShapeOffset(name="{self.name}")'
