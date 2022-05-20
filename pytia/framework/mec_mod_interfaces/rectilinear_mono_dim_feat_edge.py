from pytia.framework.mec_mod_interfaces.mono_dim_feat_edge import MonoDimFeatEdge


class RectilinearMonoDimFeatEdge(MonoDimFeatEdge):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.rectilinear_mono_dim_feat_edge = com_object

    def get_direction(self, o_direction: tuple) -> None:
        return self.rectilinear_mono_dim_feat_edge.GetDirection(o_direction)

    def get_origin(self, o_origin: tuple) -> None:
        return self.rectilinear_mono_dim_feat_edge.GetOrigin(o_origin)

    def __repr__(self):
        return f'RectilinearMonoDimFeatEdge(name="{self.name}")'
