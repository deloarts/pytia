from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.mec_mod_interfaces.shape import Shape
from pytia.framework.sketcher_interfaces.sketch import Sketch


class SketchBasedShape(Shape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.sketch_based_shape = com_object

    @property
    def sketch(self) -> Sketch:
        return Sketch(self.sketch_based_shape.Sketch)

    def set_profile_element(self, i_profile_element: Reference) -> None:
        return self.sketch_based_shape.SetProfileElement(i_profile_element.com_object)

    def __repr__(self):
        return f'SketchBasedShape(name="{self.name}")'
