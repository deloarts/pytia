from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.mec_mod_interfaces.body import Body
from pytia.framework.mec_mod_interfaces.shape import Shape


class BooleanShape(Shape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.boolean_shape = com_object

    @property
    def body(self) -> Body:
        return Body(self.boolean_shape.Body)

    def set_operated_object(self, i_reference_object: Reference) -> None:
        return self.boolean_shape.SetOperatedObject(i_reference_object.com_object)

    def set_operating_volume(self, i_reference_object: Reference) -> None:
        return self.boolean_shape.SetOperatingVolume(i_reference_object.com_object)

    def __repr__(self):
        return f'BooleanShape(name="{self.name}")'
