from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.in_interfaces.references import References
from pytia.framework.knowledge_interfaces.length import Length
from pytia.framework.part_interfaces.edge_fillet import EdgeFillet


class VarRadEdgeFillet(EdgeFillet):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.var_rad_edge_fillet = com_object

    @property
    def bitangency_type(self) -> int:
        return self.var_rad_edge_fillet.BitangencyType

    @bitangency_type.setter
    def bitangency_type(self, value: int):
        self.var_rad_edge_fillet.BitangencyType = value

    @property
    def edges_to_fillet(self) -> References:
        return References(self.var_rad_edge_fillet.EdgesToFillet)

    @property
    def fillet_spine(self) -> Reference:
        return Reference(self.var_rad_edge_fillet.FilletSpine)

    @fillet_spine.setter
    def fillet_spine(self, value: Reference):
        self.var_rad_edge_fillet.FilletSpine = value

    @property
    def fillet_variation(self) -> int:
        return self.var_rad_edge_fillet.FilletVariation

    @fillet_variation.setter
    def fillet_variation(self, value: int):
        self.var_rad_edge_fillet.FilletVariation = value

    @property
    def imposed_vertices(self) -> References:
        return References(self.var_rad_edge_fillet.ImposedVertices)

    def add_edge_to_fillet(self, i_edge: Reference, i_radius: float) -> None:
        return self.var_rad_edge_fillet.AddEdgeToFillet(i_edge.com_object, i_radius)

    def add_imposed_vertex(self, i_vertex: Reference, i_radius: float) -> None:
        return self.var_rad_edge_fillet.AddImposedVertex(i_vertex.com_object, i_radius)

    def imposed_vertex_radius(self, i_imposed_vertex: Reference) -> Length:
        return Length(
            self.var_rad_edge_fillet.ImposedVertexRadius(i_imposed_vertex.com_object)
        )

    def withdraw_edge_to_fillet(self, i_edge: Reference) -> None:
        return self.var_rad_edge_fillet.WithdrawEdgeToFillet(i_edge.com_object)

    def withdraw_imposed_vertex(self, i_vertex: Reference) -> None:
        return self.var_rad_edge_fillet.WithdrawImposedVertex(i_vertex.com_object)

    def __repr__(self):
        return f'VarRadEdgeFillet(name="{ self.name }")'
