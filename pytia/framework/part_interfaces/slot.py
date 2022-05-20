from pytia.framework.part_interfaces.sweep import Sweep


class Slot(Sweep):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.slot = com_object

    def __repr__(self):
        return f'Slot(name="{self.name}")'
