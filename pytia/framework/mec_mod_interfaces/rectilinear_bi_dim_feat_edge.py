from pytia.framework.mec_mod_interfaces.bi_dim_feat_edge import BiDimFeatEdge


class RectilinearBiDimFeatEdge(BiDimFeatEdge):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.rectilinear_bi_dim_feat_edge = com_object

    def get_direction(self, o_direction: tuple) -> None:
        return self.rectilinear_bi_dim_feat_edge.GetDirection(o_direction)

    def get_origin(self, o_origin: tuple) -> None:
        return self.rectilinear_bi_dim_feat_edge.GetOrigin(o_origin)

    def __repr__(self):
        return f'RectilinearBiDimFeatEdge(name="{ self.name }")'
