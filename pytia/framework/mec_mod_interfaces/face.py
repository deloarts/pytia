from pytia.framework.mec_mod_interfaces.boundary import Boundary


class Face(Boundary):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.face = com_object

    def __repr__(self):
        return f'Face(name="{self.name}")'
