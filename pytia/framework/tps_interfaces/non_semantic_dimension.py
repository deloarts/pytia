from pytia.framework.drafting_interfaces.drawing_dimension import DrawingDimension
from pytia.framework.system_interfaces.any_object import AnyObject
from pytia.framework.tps_interfaces.dimension_limit import DimensionLimit


class NonSemanticDimension(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.non_semantic_dimension = com_object

    def dimension_limit(self) -> DimensionLimit:
        return DimensionLimit(self.non_semantic_dimension.DimensionLimit())

    def get_2d_annot(self) -> DrawingDimension:
        return DrawingDimension(self.non_semantic_dimension.Get2dAnnot())

    def has_dimension_limit(self) -> bool:
        return self.non_semantic_dimension.HasDimensionLimit()

    def __repr__(self):
        return f'NonSemanticDimension(name="{self.name}")'
