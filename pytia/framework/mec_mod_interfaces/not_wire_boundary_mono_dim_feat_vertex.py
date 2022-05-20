from pytia.framework.mec_mod_interfaces.vertex import Vertex


class NotWireBoundaryMonoDimFeatVertex(Vertex):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.not_wire_boundary_mono_dim_feat_vertex = com_object

    def __repr__(self):
        return f'NotWireBoundaryMonoDimFeatVertex(name="{self.name}")'
