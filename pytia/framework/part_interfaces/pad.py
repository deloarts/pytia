from pytia.framework.part_interfaces.prism import Prism


class Pad(Prism):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.pad = com_object

    def __repr__(self):
        return f'Pad(name="{self.name}")'
