from pytia.framework.mec_mod_interfaces.edge import Edge


class MonoDimFeatEdge(Edge):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.mono_dim_feat_edge = com_object

    def __repr__(self):
        return f'MonoDimFeatEdge(name="{self.name}")'
