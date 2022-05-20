from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeLawDistProj(HybridShape):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_law_dist_proj = com_object

    @property
    def applied_unit_symbol(self) -> str:
        return self.hybrid_shape_law_dist_proj.AppliedUnitSymbol

    @applied_unit_symbol.setter
    def applied_unit_symbol(self, value: str):
        self.hybrid_shape_law_dist_proj.AppliedUnitSymbol = value

    @property
    def definition(self) -> Reference:
        return Reference(self.hybrid_shape_law_dist_proj.Definition)

    @definition.setter
    def definition(self, reference_definition: Reference):
        self.hybrid_shape_law_dist_proj.Definition = reference_definition.com_object

    @property
    def measure_unit_symbol(self) -> str:
        return self.hybrid_shape_law_dist_proj.MeasureUnitSymbol()

    @measure_unit_symbol.setter
    def measure_unit_symbol(self, value: str):
        self.hybrid_shape_law_dist_proj.MeasureUnitSymbol = value

    @property
    def parameter_on_definition(self) -> bool:
        return self.hybrid_shape_law_dist_proj.ParameterOnDefinition

    @parameter_on_definition.setter
    def parameter_on_definition(self, value: bool):
        self.hybrid_shape_law_dist_proj.ParameterOnDefinition = value

    @property
    def positive_direction_orientation(self) -> int:
        return self.hybrid_shape_law_dist_proj.PositiveDirectionOrientation

    @positive_direction_orientation.setter
    def positive_direction_orientation(self, value: int):
        self.hybrid_shape_law_dist_proj.PositiveDirectionOrientation = value

    @property
    def reference(self) -> Reference:
        return Reference(self.hybrid_shape_law_dist_proj.Reference)

    @reference.setter
    def reference(self, reference: Reference):
        self.hybrid_shape_law_dist_proj.Reference = reference.com_object

    @property
    def scaling(self) -> float:
        return self.hybrid_shape_law_dist_proj.Scaling

    @scaling.setter
    def scaling(self, value: float):
        self.hybrid_shape_law_dist_proj.Scaling = value

    def get_applied_unit_symbol(self, o_symbol: str) -> None:
        return self.hybrid_shape_law_dist_proj.GetAppliedUnitSymbol(o_symbol)

    def get_measure_unit_symbol(self, o_symbol: str) -> None:
        return self.hybrid_shape_law_dist_proj.GetMeasureUnitSymbol(o_symbol)

    def get_plane_normal(self, o_normal: tuple) -> None:
        return self.hybrid_shape_law_dist_proj.GetPlaneNormal(o_normal)

    def is_heterogeneous_law(self) -> bool:
        return self.hybrid_shape_law_dist_proj.IsHeterogeneousLaw()

    def put_plane_normal(self, i_normal: tuple) -> None:
        return self.hybrid_shape_law_dist_proj.PutPlaneNormal(i_normal)

    def __repr__(self):
        return f'HybridShapeLawDistProj(name="{self.name}")'
