from pytia.framework.mec_mod_interfaces.vertex import Vertex


class ZeroDimFeatVertexOrWireBoundaryMonoDimFeatVertex(Vertex):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.zero_dim_feat_vertex_or_wire_boundary_mono_dim_feat_vertex = com_object

    def __repr__(self):
        return f'ZeroDimFeatVertexOrWireBoundaryMonoDimFeatVertex(name="{self.name}")'
