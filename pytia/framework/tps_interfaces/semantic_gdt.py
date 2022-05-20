from pytia.framework.system_interfaces.any_object import AnyObject
from pytia.framework.tps_interfaces.associated_ref_frame import AssociatedRefFrame
from pytia.framework.tps_interfaces.composite_tolerance import CompositeTolerance
from pytia.framework.tps_interfaces.free_state import FreeState
from pytia.framework.tps_interfaces.material_condition import MaterialCondition
from pytia.framework.tps_interfaces.particular_tol_elem import ParticularTolElem
from pytia.framework.tps_interfaces.projected_tolerance_zone import (
    ProjectedToleranceZone,
)
from pytia.framework.tps_interfaces.shifted_profile_tolerance import (
    ShiftedProfileTolerance,
)
from pytia.framework.tps_interfaces.tps_parallel_on_screen import TPSParallelOnScreen
from pytia.framework.tps_interfaces.tangent_plane import TangentPlane
from pytia.framework.tps_interfaces.tolerance_per_unit_basis_restrictive_value import (
    TolerancePerUnitBasisRestrictiveValue,
)
from pytia.framework.tps_interfaces.tolerance_unit_basis_value import (
    ToleranceUnitBasisValue,
)
from pytia.framework.tps_interfaces.tolerance_zone import ToleranceZone


class SemanticGDT(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.semantic_gdt = com_object

    def associated_ref_frame(self) -> AssociatedRefFrame:
        return AssociatedRefFrame(self.semantic_gdt.AssociatedRefFrame())

    def composite_tolerance(self) -> CompositeTolerance:
        return CompositeTolerance(self.semantic_gdt.CompositeTolerance())

    def free_state(self) -> FreeState:
        return FreeState(self.semantic_gdt.FreeState())

    def has_a_free_state(self) -> bool:
        return self.semantic_gdt.HasAFreeState()

    def has_a_material_condition(self) -> bool:
        return self.semantic_gdt.HasAMaterialCondition()

    def has_a_particular_tol_elem(self) -> bool:
        return self.semantic_gdt.HasAParticularTolElem()

    def has_a_tangent_plane(self) -> bool:
        return self.semantic_gdt.HasATangentPlane()

    def has_a_tolerance_per_unit_basis_restrictive_value(self) -> bool:
        return self.semantic_gdt.HasATolerancePerUnitBasisRestrictiveValue()

    def is_a_composite_tolerance(self) -> bool:
        return self.semantic_gdt.IsACompositeTolerance()

    def is_a_projected_tolerance_zone(self) -> bool:
        return self.semantic_gdt.IsAProjectedToleranceZone()

    def is_a_shifted_profile_tolerance(self) -> bool:
        return self.semantic_gdt.IsAShiftedProfileTolerance()

    def is_a_tolerance_unit_basis_value(self) -> bool:
        return self.semantic_gdt.IsAToleranceUnitBasisValue()

    def is_a_tolerance_zone(self) -> bool:
        return self.semantic_gdt.IsAToleranceZone()

    def is_an_associated_ref_frame(self) -> bool:
        return self.semantic_gdt.IsAnAssociatedRefFrame()

    def material_condition(self) -> MaterialCondition:
        return MaterialCondition(self.semantic_gdt.MaterialCondition())

    def particular_tol_elem(self) -> ParticularTolElem:
        return ParticularTolElem(self.semantic_gdt.ParticularTolElem())

    def projected_tolerance_zone(self) -> ProjectedToleranceZone:
        return ProjectedToleranceZone(self.semantic_gdt.ProjectedToleranceZone())

    def shifted_profile_tolerance(self) -> ShiftedProfileTolerance:
        return ShiftedProfileTolerance(self.semantic_gdt.ShiftedProfileTolerance())

    def tps_parallel_on_screen(self) -> TPSParallelOnScreen:
        return TPSParallelOnScreen(self.semantic_gdt.TPSParallelOnScreen())

    def tangent_plane(self) -> TangentPlane:
        return TangentPlane(self.semantic_gdt.TangentPlane())

    def tolerance_per_unit_basis_restrictive_value(
        self,
    ) -> TolerancePerUnitBasisRestrictiveValue:
        return TolerancePerUnitBasisRestrictiveValue(
            self.semantic_gdt.TolerancePerUnitBasisRestrictiveValue()
        )

    def tolerance_unit_basis_value(self) -> ToleranceUnitBasisValue:
        return ToleranceUnitBasisValue(self.semantic_gdt.ToleranceUnitBasisValue())

    def tolerance_zone(self) -> ToleranceZone:
        return ToleranceZone(self.semantic_gdt.ToleranceZone())

    def __repr__(self):
        return f'SemanticGdt(name="{self.name}")'
