from pytia.framework.system_interfaces.any_object import AnyObject
from pytia.framework.tps_interfaces.associated_ref_frame import AssociatedRefFrame
from pytia.framework.tps_interfaces.composite_tolerance import CompositeTolerance
from pytia.framework.tps_interfaces.controlled_radius import ControlledRadius
from pytia.framework.tps_interfaces.datum_simple import DatumSimple
from pytia.framework.tps_interfaces.datum_target import DatumTarget
from pytia.framework.tps_interfaces.default_annotation import DefaultAnnotation
from pytia.framework.tps_interfaces.dimension_3d import Dimension3D
from pytia.framework.tps_interfaces.dimension_limit import DimensionLimit
from pytia.framework.tps_interfaces.dimension_pattern import DimensionPattern
from pytia.framework.tps_interfaces.envelope_condition import EnvelopeCondition
from pytia.framework.tps_interfaces.flag_note import FlagNote
from pytia.framework.tps_interfaces.free_state import FreeState
from pytia.framework.tps_interfaces.material_condition import MaterialCondition
from pytia.framework.tps_interfaces.noa import Noa
from pytia.framework.tps_interfaces.particular_tol_elem import ParticularTolElem
from pytia.framework.tps_interfaces.projected_tolerance_zone import (
    ProjectedToleranceZone,
)
from pytia.framework.tps_interfaces.reference_frame import ReferenceFrame
from pytia.framework.tps_interfaces.roughness import Roughness
from pytia.framework.tps_interfaces.shifted_profile_tolerance import (
    ShiftedProfileTolerance,
)
from pytia.framework.tps_interfaces.tangent_plane import TangentPlane
from pytia.framework.tps_interfaces.text import Text
from pytia.framework.tps_interfaces.tolerance_per_unit_basis_restrictive_value import (
    TolerancePerUnitBasisRestrictiveValue,
)
from pytia.framework.tps_interfaces.tolerance_unit_basis_value import (
    ToleranceUnitBasisValue,
)
from pytia.framework.tps_interfaces.tolerance_zone import ToleranceZone
from pytia.framework.tps_interfaces.tps_view import TPSView


class Annotation(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.annotation = com_object

    @property
    def super_type(self) -> str:
        return self.annotation.SuperType

    @property
    def tps_status(self) -> str:
        return self.annotation.TPSStatus

    @property
    def type(self) -> str:
        return self.annotation.Type

    @property
    def z(self) -> float:
        return self.annotation.Z

    @z.setter
    def z(self, value: float):
        self.annotation.Z = value

    def add_leader(self) -> None:
        return self.annotation.AddLeader()

    def apply_referenced_geom_colour(
        self, i_releated_r: int, i_releated_g: int, i_releated_b: int
    ) -> None:
        return self.annotation.ApplyReferencedGeomColor(
            i_releated_r, i_releated_g, i_releated_b
        )

    def apply_referenced_init_colour(self) -> None:
        return self.annotation.ApplyReferencedInitColor()

    def associated_ref_frame(self) -> AssociatedRefFrame:
        return AssociatedRefFrame(self.annotation.AssociatedRefFrame())

    def composite_tolerance(self) -> CompositeTolerance:
        return CompositeTolerance(self.annotation.CompositeTolerance())

    def controlled_radius(self) -> ControlledRadius:
        return ControlledRadius(self.annotation.ControlledRadius())

    def datum_simple(self) -> DatumSimple:
        return DatumSimple(self.annotation.DatumSimple())

    def datum_target(self) -> DatumTarget:
        return DatumTarget(self.annotation.DatumTarget())

    def default_annotation(self) -> DefaultAnnotation:
        return DefaultAnnotation(self.annotation.DefaultAnnotation())

    def dimension_3d(self) -> Dimension3D:
        return Dimension3D(self.annotation.Dimension3D())

    def dimension_limit(self) -> DimensionLimit:
        return DimensionLimit(self.annotation.DimensionLimit())

    def dimension_pattern(self) -> DimensionPattern:
        return DimensionPattern(self.annotation.DimensionPattern())

    def envelop_condition(self) -> EnvelopeCondition:
        return EnvelopeCondition(self.annotation.EnvelopeCondition())

    def flag_note(self) -> FlagNote:
        return FlagNote(self.annotation.FlagNote())

    def free_state(self) -> FreeState:
        return FreeState(self.annotation.FreeState())

    def get_surfaces(self, o_safe_array: tuple) -> tuple:
        return self.annotation.GetSurfaces(o_safe_array)

    def get_surfaces_count(self) -> float:
        return self.annotation.GetSurfacesCount()

    def has_a_controlled_radius(self) -> bool:
        return self.annotation.HasAControledRadius()

    def has_a_free_state(self) -> bool:
        return self.annotation.HasAFreeState()

    def has_a_material_condition(self) -> bool:
        return self.annotation.HasAMaterialCondition()

    def has_a_particular_tol_elem(self) -> bool:
        return self.annotation.HasAParticularTolElem()

    def has_a_tolerance_per_unit_basis_restrictive_value(self) -> bool:
        return self.annotation.HasATolerancePerUnitBasisRestrictiveValue()

    def has_an_envelop_condition(self) -> bool:
        return self.annotation.HasAnEnvelopCondition()

    def has_dimension_limit(self) -> bool:
        return self.annotation.HasDimensionLimit()

    def is_a_composite_tolerance(self) -> bool:
        return self.annotation.IsACompositeTolerance()

    def is_a_default_annotation(self) -> bool:
        return self.annotation.IsADefaultAnnotation()

    def is_a_dimension_pattern(self) -> bool:
        return self.annotation.IsADimensionPattern()

    def is_a_projected_tolerance_zone(self) -> bool:
        return self.annotation.IsAProjectedToleranceZone()

    def is_a_shifted_profile_tolerance(self) -> bool:
        return self.annotation.IsAShiftedProfileTolerance()

    def is_a_tangent_plane(self) -> bool:
        return self.annotation.IsATangentPlane()

    def is_a_tolerance_unit_basis_value(self) -> bool:
        return self.annotation.IsAToleranceUnitBasisValue()

    def is_a_tolerance_zone(self) -> bool:
        return self.annotation.IsAToleranceZone()

    def is_an_associated_ref_frame(self) -> bool:
        return self.annotation.IsAnAssociatedRefFrame()

    def material_condition(self) -> MaterialCondition:
        return MaterialCondition(self.annotation.MaterialCondition())

    def modify_visualisation(self) -> None:
        return self.annotation.ModifyVisu()

    def noa(self) -> Noa:
        return Noa(self.annotation.Noa())

    def particular_tol_elem(self) -> ParticularTolElem:
        return ParticularTolElem(self.annotation.ParticularTolElem())

    def projected_tolerance_zone(self) -> ProjectedToleranceZone:
        return ProjectedToleranceZone(self.annotation.ProjectedToleranceZone())

    def reference_frame(self) -> ReferenceFrame:
        return ReferenceFrame(self.annotation.ReferenceFrame())

    def roughness(self) -> Roughness:
        return Roughness(self.annotation.Roughness())

    def set_xy(self, i_x: float, i_y: float) -> None:
        return self.annotation.SetXY(i_x, i_y)

    def shifted_profile_tolerance(self) -> ShiftedProfileTolerance:
        return ShiftedProfileTolerance(self.annotation.ShiftedProfileTolerance())

    def tangent_plane(self) -> TangentPlane:
        return TangentPlane(self.annotation.TangentPlane())

    def text(self) -> Text:
        return Text(self.annotation.Text())

    def tolerance_per_unit_basis_restrictive_value(
        self,
    ) -> TolerancePerUnitBasisRestrictiveValue:
        return TolerancePerUnitBasisRestrictiveValue(
            self.annotation.TolerancePerUnitBasisRestrictiveValue()
        )

    def tolerance_unit_basis_value(self) -> ToleranceUnitBasisValue:
        return ToleranceUnitBasisValue(self.annotation.ToleranceUnitBasisValue())

    def tolerance_zone(self) -> ToleranceZone:
        return ToleranceZone(self.annotation.ToleranceZone())

    def transfert_to_view(self, i_view: TPSView) -> None:
        return self.annotation.TransfertToView(i_view.com_object)

    def __repr__(self):
        return f'Annotation(name="{self.name}")'
