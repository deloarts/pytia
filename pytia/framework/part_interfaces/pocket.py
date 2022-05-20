from pytia.framework.part_interfaces.prism import Prism


class Pocket(Prism):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.pocket = com_object

    def __repr__(self):
        return f'Pocket(name="{self.name}")'
