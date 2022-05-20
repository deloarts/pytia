from pytia.framework.part_interfaces.boolean_shape import BooleanShape


class Intersect(BooleanShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.intersect = com_object

    def __repr__(self):
        return f'Intersect(name="{self.name}")'
