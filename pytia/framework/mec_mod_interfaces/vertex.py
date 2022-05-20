from pytia.framework.mec_mod_interfaces.boundary import Boundary


class Vertex(Boundary):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.vertex = com_object

    def __repr__(self):
        return f'Vertex(name="{self.name}")'
