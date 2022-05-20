from pytia.framework.mec_mod_interfaces.boundary import Boundary


class Edge(Boundary):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.edge = com_object

    def __repr__(self):
        return f'Edge(name="{self.name}")'
