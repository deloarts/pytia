from pytia.framework.part_interfaces.revolution import Revolution


class Shaft(Revolution):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.shaft = com_object

    def __repr__(self):
        return f'Shaft(name="{self.name}")'
