from pytia.framework.mec_mod_interfaces.tri_dim_feat_edge import TriDimFeatEdge


class RectilinearTriDimFeatEdge(TriDimFeatEdge):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.rectilinear_tri_dim_feat_edge = com_object

    def get_direction(self, o_direction: tuple) -> None:
        return self.rectilinear_tri_dim_feat_edge.GetDirection(o_direction)

    def get_origin(self, o_origin: tuple) -> None:
        return self.rectilinear_tri_dim_feat_edge.GetOrigin(o_origin)

    def __repr__(self):
        return f'RectilinearTriDimFeatEdge(name="{self.name}")'
