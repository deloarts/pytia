from pytia.framework.part_interfaces.boolean_shape import BooleanShape


class Remove(BooleanShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.remove = com_object

    def __repr__(self):
        return f'Remove(name="{self.name}")'
