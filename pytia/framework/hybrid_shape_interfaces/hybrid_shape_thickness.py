from pytia.framework.knowledge_interfaces.length import Length
from pytia.framework.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeThickness(HybridShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_thickness = com_object

    @property
    def orientation(self) -> int:
        return self.hybrid_shape_thickness.Orientation

    @orientation.setter
    def orientation(self, value: int):
        self.hybrid_shape_thickness.Orientation = value

    @property
    def thickness1(self) -> float:
        return self.hybrid_shape_thickness.Thickness1

    @thickness1.setter
    def thickness1(self, value: float):
        self.hybrid_shape_thickness.Thickness1 = value

    @property
    def thickness1_value(self) -> Length:
        return Length(self.hybrid_shape_thickness.Thickness1Value)

    @property
    def thickness2(self) -> float:
        return self.hybrid_shape_thickness.Thickness2

    @thickness2.setter
    def thickness2(self, value: float):
        self.hybrid_shape_thickness.Thickness2 = value

    @property
    def thickness2_value(self) -> Length:
        return Length(self.hybrid_shape_thickness.Thickness2Value)

    def __repr__(self):
        return f'HybridShapeThickness(name="{self.name}")'
