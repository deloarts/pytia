from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.in_interfaces.references import References
from pytia.framework.knowledge_interfaces.length import Length
from pytia.framework.part_interfaces.edge_fillet import EdgeFillet


class ConstRadEdgeFillet(EdgeFillet):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.const_rad_edge_fillet = com_object

    @property
    def objects_to_fillet(self) -> References:
        return References(self.const_rad_edge_fillet.ObjectsToFillet)

    @property
    def radius(self) -> Length:
        return Length(self.const_rad_edge_fillet.Radius)

    def add_object_to_fillet(self, i_object_to_fillet: Reference) -> None:
        return self.const_rad_edge_fillet.AddObjectToFillet(
            i_object_to_fillet.com_object
        )

    def withdraw_object_to_fillet(self, i_object_to_withdraw: Reference) -> None:
        return self.const_rad_edge_fillet.WithdrawObjectToFillet(
            i_object_to_withdraw.com_object
        )

    def __repr__(self):
        return f'ConstRadEdgeFillet(name="{self.name}")'
