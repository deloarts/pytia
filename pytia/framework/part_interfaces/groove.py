from pytia.framework.part_interfaces.revolution import Revolution


class Groove(Revolution):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.groove = com_object

    def __repr__(self):
        return f'Groove(name="{self.name}")'
