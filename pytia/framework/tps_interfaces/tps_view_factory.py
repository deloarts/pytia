from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.system_interfaces.any_object import AnyObject
from pytia.framework.tps_interfaces.tps_view import TPSView
from pytia.framework.cat_types.general import cat_variant


class TPSViewFactory(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.tps_view_factory = com_object

    def create_view(self, i_plane: Reference, i_view_type: cat_variant) -> TPSView:
        return TPSView(
            self.tps_view_factory.CreateView(i_plane.com_object, i_view_type)
        )

    def __repr__(self):
        return f'TpsViewFactory(name="{self.name}")'
