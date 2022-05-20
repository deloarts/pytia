from pytia.framework.part_interfaces.sweep import Sweep


class Rib(Sweep):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.rib = com_object

    def __repr__(self):
        return f'Rib(name="{self.name}")'
