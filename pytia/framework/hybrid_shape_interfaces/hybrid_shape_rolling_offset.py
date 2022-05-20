from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.knowledge_interfaces.length import Length
from pytia.framework.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeRollingOffset(HybridShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_rolling_offset = com_object

    @property
    def offset(self) -> Length:
        return Length(self.hybrid_shape_rolling_offset.Offset)

    @property
    def support(self) -> Reference:
        return Reference(self.hybrid_shape_rolling_offset.Support)

    @support.setter
    def support(self, reference_support: Reference):
        self.hybrid_shape_rolling_offset.Support = reference_support.com_object

    def get_curve(self, i_pos: int) -> Reference:
        return Reference(self.hybrid_shape_rolling_offset.getCurve(i_pos))

    def get_nb_curve(self) -> int:
        return self.hybrid_shape_rolling_offset.getNbCurve()

    def get_offset(self) -> float:
        return self.hybrid_shape_rolling_offset.getOffset()

    def put_curve(self, i_curve: Reference) -> None:
        return self.hybrid_shape_rolling_offset.putCurve(i_curve.com_object)

    def put_offset(self, i_offset: float) -> None:
        return self.hybrid_shape_rolling_offset.putOffset(i_offset)

    def __repr__(self):
        return f'HybridShapeRollingOffset(name="{self.name}")'
