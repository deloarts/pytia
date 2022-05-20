from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.in_interfaces.references import References
from pytia.framework.part_interfaces.fillet import Fillet


class EdgeFillet(Fillet):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.edge_fillet = com_object

    @property
    def edge_propagation(self) -> int:
        return self.edge_fillet.EdgePropagation

    @edge_propagation.setter
    def edge_propagation(self, value: int):
        self.edge_fillet.EdgePropagation = value

    @property
    def edges_to_keep(self) -> References:
        return References(self.edge_fillet.EdgesToKeep)

    def add_edge_to_keep(self, i_edge_to_keep: Reference) -> None:
        return self.edge_fillet.AddEdgeToKeep(i_edge_to_keep.com_object)

    def withdraw_edge_to_keep(self, i_edge_to_withdraw: Reference) -> None:
        return self.edge_fillet.WithdrawEdgeToKeep(i_edge_to_withdraw.com_object)

    def __repr__(self):
        return f'EdgeFillet(name="{self.name}")'
