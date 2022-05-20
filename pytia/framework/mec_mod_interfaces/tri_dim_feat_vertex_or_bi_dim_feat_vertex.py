from pytia.framework.mec_mod_interfaces.vertex import Vertex


class TriDimFeatVertexOrBiDimFeatVertex(Vertex):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.tri_dim_feat_vertex_or_bi_dim_feat_vertex = com_object

    def __repr__(self):
        return f'TriDimFeatVertexOrBiDimFeatVertex(name="{self.name}")'
