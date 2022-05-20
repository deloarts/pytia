from typing import TYPE_CHECKING
from pytia.framework.system_interfaces.any_object import AnyObject
from pytia.framework.tps_interfaces.datum_simple import DatumSimple
from pytia.framework.tps_interfaces.datum_target import DatumTarget
from pytia.framework.tps_interfaces.default_annotation import DefaultAnnotation
from pytia.framework.tps_interfaces.dimension_3d import Dimension3D
from pytia.framework.tps_interfaces.flag_note import FlagNote
from pytia.framework.tps_interfaces.noa import Noa
from pytia.framework.tps_interfaces.non_semantic_datum import NonSemanticDatum
from pytia.framework.tps_interfaces.non_semantic_datum_target import (
    NonSemanticDatumTarget,
)
from pytia.framework.tps_interfaces.non_semantic_dimension import NonSemanticDimension
from pytia.framework.tps_interfaces.non_semantic_gdt import NonSemanticGDT
from pytia.framework.tps_interfaces.roughness import Roughness
from pytia.framework.tps_interfaces.semantic_gdt import SemanticGDT
from pytia.framework.tps_interfaces.text import Text
from pytia.framework.tps_interfaces.tps_view import TPSView
from pytia.framework.tps_interfaces.weld import Weld

if TYPE_CHECKING:
    from pytia.framework.tps_interfaces.reference_frame import ReferenceFrame


class Annotation2(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.annotation_2 = com_object

    @property
    def super_type(self) -> str:
        return self.annotation_2.SuperType

    @property
    def tps_status(self) -> str:
        return self.annotation_2.TPSStatus

    @property
    def type(self) -> str:
        return self.annotation_2.Type

    @property
    def z(self) -> float:
        return self.annotation_2.Z

    @z.setter
    def z(self, value: float):
        self.annotation_2.Z = value

    def add_leader(self) -> None:
        return self.annotation_2.AddLeader()

    def datum_simple(self) -> DatumSimple:
        return DatumSimple(self.annotation_2.DatumSimple())

    def datum_target(self) -> DatumTarget:
        return DatumTarget(self.annotation_2.DatumTarget())

    def default_annotation(self) -> DefaultAnnotation:
        return DefaultAnnotation(self.annotation_2.DefaultAnnotation())

    def dimension_3d(self) -> Dimension3D:
        return Dimension3D(self.annotation_2.Dimension3D())

    def flag_note(self) -> FlagNote:
        return FlagNote(self.annotation_2.FlagNote())

    def get_surfaces(self, o_safe_array: tuple) -> None:
        return self.annotation_2.GetSurfaces(o_safe_array)

    def get_surfaces_count(self) -> int:
        return self.annotation_2.GetSurfacesCount()

    def has_a_visualization_dimension(self) -> bool:
        return self.annotation_2.HasAVisualizationDimension()

    def is_a_default_annotation(self) -> bool:
        return self.annotation_2.IsADefaultAnnotation()

    def modify_visu(self) -> None:
        return self.annotation_2.ModifyVisu()

    def noa(self) -> Noa:
        return Noa(self.annotation_2.Noa())

    def non_semantic_datum(self) -> NonSemanticDatum:
        return NonSemanticDatum(self.annotation_2.NonSemanticDatum())

    def non_semantic_datum_target(self) -> NonSemanticDatumTarget:
        return NonSemanticDatumTarget(self.annotation_2.NonSemanticDatumTarget())

    def non_semantic_dimension(self) -> NonSemanticDimension:
        return NonSemanticDimension(self.annotation_2.NonSemanticDimension())

    def non_semantic_gdt(self) -> NonSemanticGDT:
        return NonSemanticGDT(self.annotation_2.NonSemanticGDT())

    def reference_frame(self) -> "ReferenceFrame":
        from pytia.framework.tps_interfaces.reference_frame import ReferenceFrame

        return ReferenceFrame(self.annotation_2.ReferenceFrame())

    def roughness(self) -> Roughness:
        return Roughness(self.annotation_2.Roughness())

    def semantic_gdt(self) -> SemanticGDT:
        return SemanticGDT(self.annotation_2.SemanticGDT())

    def set_xy(self, i_x: float, i_y: float) -> None:
        return self.annotation_2.SetXY(i_x, i_y)

    def text(self) -> Text:
        return Text(self.annotation_2.Text())

    def transfert_to_view(self, i_view: TPSView) -> None:
        return self.annotation_2.TransfertToView(i_view.com_object)

    def visualization_dimension(self) -> Dimension3D:
        return Dimension3D(self.annotation_2.VisualizationDimension())

    def weld(self) -> Weld:
        return Weld(self.annotation_2.Weld())

    def __repr__(self):
        return f'Annotation2(name="{self.name}")'
