from pytia.framework.part_interfaces.boolean_shape import BooleanShape


class Add(BooleanShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.add = com_object

    def __repr__(self):
        return f'Add(name="{self.name}")'
