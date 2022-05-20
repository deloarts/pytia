from typing import TYPE_CHECKING
from pytia.framework.mec_mod_interfaces.factory import Factory
from pytia.framework.tps_interfaces.noa import Noa
from pytia.framework.tps_interfaces.user_surface import UserSurface
from pytia.framework.cat_types.general import cat_variant

if TYPE_CHECKING:
    from pytia.framework.tps_interfaces.annotation import Annotation


class AnnotationFactory(Factory):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.annotation_factory = com_object

    def create_datum(self, i_surf: UserSurface) -> "Annotation":
        from pytia.framework.tps_interfaces.annotation import Annotation

        return Annotation(self.annotation_factory.CreateDatum(i_surf.com_object))

    def create_datum_reference_frame(self) -> "Annotation":
        from pytia.framework.tps_interfaces.annotation import Annotation

        return Annotation(self.annotation_factory.CreateDatumReferenceFrame())

    def create_datum_target(
        self, i_surf: UserSurface, i_datum: "Annotation"
    ) -> "Annotation":
        from pytia.framework.tps_interfaces.annotation import Annotation

        return Annotation(
            self.annotation_factory.CreateDatumTarget(
                i_surf.com_object, i_datum.com_object
            )
        )

    def create_evaluate_datum(
        self,
        i_surf: UserSurface,
        i_x: float,
        i_y: float,
        i_z: float,
        i_with_leader: bool,
    ) -> "Annotation":
        from pytia.framework.tps_interfaces.annotation import Annotation

        return Annotation(
            self.annotation_factory.CreateEvoluateDatum(
                i_surf.com_object, i_x, i_y, i_z, i_with_leader
            )
        )

    def create_evaluate_text(
        self,
        i_surf: UserSurface,
        i_x: float,
        i_y: float,
        i_z: float,
        i_with_leader: bool,
    ) -> "Annotation":
        from pytia.framework.tps_interfaces.annotation import Annotation

        return Annotation(
            self.annotation_factory.CreateEvoluateText(
                i_surf.com_object, i_x, i_y, i_z, i_with_leader
            )
        )

    def create_flag_note(self, i_surf: UserSurface) -> "Annotation":
        from pytia.framework.tps_interfaces.annotation import Annotation

        return Annotation(self.annotation_factory.CreateFlagNote(i_surf.com_object))

    def create_non_semantic_dimension(
        self,
        i_surf: UserSurface,
        i_dimension_type: cat_variant,
        i_linear_dim_sub_type: cat_variant,
    ) -> "Annotation":
        from pytia.framework.tps_interfaces.annotation import Annotation

        return Annotation(
            self.annotation_factory.CreateNonSemanticDimension(
                i_surf.com_object, i_dimension_type, i_linear_dim_sub_type
            )
        )

    def create_roughness(self, i_surf: UserSurface) -> "Annotation":
        from pytia.framework.tps_interfaces.annotation import Annotation

        return Annotation(self.annotation_factory.CreateRoughness(i_surf.com_object))

    def create_semantic_dimension(
        self, i_surf: UserSurface, i_type: cat_variant, i_sub_type: cat_variant
    ) -> "Annotation":
        from pytia.framework.tps_interfaces.annotation import Annotation

        return Annotation(
            self.annotation_factory.CreateSemanticDimension(
                i_surf.com_object, i_type, i_sub_type
            )
        )

    def create_text(self, i_surf: UserSurface) -> "Annotation":
        from pytia.framework.tps_interfaces.annotation import Annotation

        return Annotation(self.annotation_factory.CreateText(i_surf.com_object))

    def create_text_noa(self, i_surf: UserSurface) -> Noa:
        return Noa(self.annotation_factory.CreateTextNOA(i_surf.com_object))

    def create_text_note_object_attribute(
        self, i_surf: UserSurface, i_noa_type: str
    ) -> Noa:
        return Noa(
            self.annotation_factory.CreateTextNoteObjectAttribute(
                i_surf.com_object, i_noa_type
            )
        )

    def create_text_on_annot(self, i_text: str, i_annot: "Annotation") -> "Annotation":
        from pytia.framework.tps_interfaces.annotation import Annotation

        return Annotation(
            self.annotation_factory.CreateTextOnAnnot(i_text, i_annot.com_object)
        )

    def create_tolerance_with_drf(
        self, i_index: cat_variant, i_surf: UserSurface, i_drf: "Annotation"
    ) -> "Annotation":
        from pytia.framework.tps_interfaces.annotation import Annotation

        return Annotation(
            self.annotation_factory.CreateToleranceWithDRF(
                i_index, i_surf.com_object, i_drf.com_object
            )
        )

    def create_tolerance_without_drf(
        self, i_index: cat_variant, i_surf: UserSurface
    ) -> "Annotation":
        from pytia.framework.tps_interfaces.annotation import Annotation

        return Annotation(
            self.annotation_factory.CreateToleranceWithoutDRF(
                i_index, i_surf.com_object
            )
        )

    def instantiate_noa(self, i_noa: Noa, i_surf: UserSurface) -> "Annotation":
        from pytia.framework.tps_interfaces.annotation import Annotation

        return Annotation(
            self.annotation_factory.InstanciateNOA(i_noa.com_object, i_surf.com_object)
        )

    def __repr__(self):
        return f'AnnotationFactory(name="{self.name}")'
