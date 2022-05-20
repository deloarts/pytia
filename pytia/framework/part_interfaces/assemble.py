from pytia.framework.part_interfaces.boolean_shape import BooleanShape


class Assemble(BooleanShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.assemble = com_object

    def __repr__(self):
        return f'Assemble(name="{self.name}")'
