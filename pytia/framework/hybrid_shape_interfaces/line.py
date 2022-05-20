from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.mec_mod_interfaces.hybrid_shape import HybridShape


class Line(HybridShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.line = com_object

    @property
    def first_upto_elem(self) -> Reference:
        return Reference(self.line.FirstUptoElem)

    @first_upto_elem.setter
    def first_upto_elem(self, reference_element: Reference):
        self.line.FirstUptoElem = reference_element.com_object

    @property
    def second_upto_elem(self) -> Reference:
        return Reference(self.line.SecondUptoElem)

    @second_upto_elem.setter
    def second_upto_elem(self, reference_element: Reference):
        self.line.SecondUptoElem = reference_element

    def get_direction(self, o_direction: tuple) -> None:
        return self.line.GetDirection(o_direction)

    def get_origin(self, o_origin: tuple) -> None:
        return self.line.GetOrigin(o_origin)

    def put_direction(self, i_direction: tuple) -> None:
        return self.line.PutDirection(i_direction)

    def __repr__(self):
        return f'Line(name="{self.name}")'
