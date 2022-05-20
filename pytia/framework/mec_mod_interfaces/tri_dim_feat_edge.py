from pytia.framework.mec_mod_interfaces.edge import Edge


class TriDimFeatEdge(Edge):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.tri_dim_feat_edge = com_object

    def __repr__(self):
        return f'TriDimFeatEdge(name="{self.name}")'
