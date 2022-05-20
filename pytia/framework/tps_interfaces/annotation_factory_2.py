from pytia.framework.mec_mod_interfaces.factory import Factory
from pytia.framework.tps_interfaces.annotation_2 import Annotation2
from pytia.framework.drafting_interfaces.drawing_component import DrawingComponent
from pytia.framework.tps_interfaces.user_surface import UserSurface
from pytia.framework.cat_types.general import cat_variant


class AnnotationFactory2(Factory):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.annotation_factory_2 = com_object

    def create_datum(self, i_surf: UserSurface) -> Annotation2:
        return Annotation2(self.annotation_factory_2.CreateDatum(i_surf.com_object))

    def create_datum_reference_frame(self) -> Annotation2:
        return Annotation2(self.annotation_factory_2.CreateDatumReferenceFrame())

    def create_datum_target(
        self, i_surf: UserSurface, i_datum: Annotation2
    ) -> Annotation2:
        return Annotation2(
            self.annotation_factory_2.CreateDatumTarget(
                i_surf.com_object, i_datum.com_object
            )
        )

    def create_ditto_noa(
        self,
        i_surf: UserSurface,
        i_noa_type: str,
        i_ditto: DrawingComponent,
        i_stick_to_geometry_option: bool,
    ) -> Annotation2:
        return Annotation2(
            self.annotation_factory_2.CreateDittoNOA(
                i_surf.com_object,
                i_noa_type,
                i_ditto.com_object,
                i_stick_to_geometry_option,
            )
        )

    def create_evaluate_datum(
        self,
        i_surf: "UserSurface",
        i_x: float,
        i_y: float,
        i_z: float,
        i_with_leader: bool,
    ) -> Annotation2:
        return Annotation2(
            self.annotation_factory_2.CreateEvoluateDatum(
                i_surf.com_object, i_x, i_y, i_z, i_with_leader
            )
        )

    def create_evaluate_text(
        self,
        i_surf: "UserSurface",
        i_x: float,
        i_y: float,
        i_z: float,
        i_with_leader: bool,
    ) -> Annotation2:
        return Annotation2(
            self.annotation_factory_2.CreateEvoluateText(
                i_surf.com_object, i_x, i_y, i_z, i_with_leader
            )
        )

    def create_flag_note(self, i_surf: "UserSurface") -> Annotation2:
        return Annotation2(self.annotation_factory_2.CreateFlagNote(i_surf.com_object))

    def create_non_semantic_dimension(
        self, i_surf: "UserSurface", i_type: cat_variant, i_sub_type: cat_variant
    ) -> Annotation2:
        return Annotation2(
            self.annotation_factory_2.CreateNonSemanticDimension(
                i_surf.com_object, i_type, i_sub_type
            )
        )

    def create_roughness(self, i_surf: UserSurface) -> Annotation2:
        return Annotation2(self.annotation_factory_2.CreateRoughness(i_surf.com_object))

    def create_semantic_dimension(
        self, i_surf: UserSurface, i_type: cat_variant, i_sub_type: cat_variant
    ) -> Annotation2:
        return Annotation2(
            self.annotation_factory_2.CreateSemanticDimension(
                i_surf.com_object, i_type, i_sub_type
            )
        )

    def create_text(self, i_surf: UserSurface) -> Annotation2:
        return Annotation2(self.annotation_factory_2.CreateText(i_surf.com_object))

    def create_text_noa(self, i_surf: UserSurface) -> Annotation2:
        return Annotation2(self.annotation_factory_2.CreateTextNOA(i_surf.com_object))

    def create_text_note_object_attribute(
        self, i_surf: UserSurface, i_noa_type: str
    ) -> Annotation2:
        return Annotation2(
            self.annotation_factory_2.CreateTextNoteObjectAttribute(
                i_surf.com_object, i_noa_type
            )
        )

    def create_text_on_annot(self, i_text: str, i_annot: Annotation2) -> Annotation2:
        return Annotation2(
            self.annotation_factory_2.CreateTextOnAnnot(i_text, i_annot.com_object)
        )

    def create_tolerance_with_drf(
        self, i_index: cat_variant, i_surf: UserSurface, i_drf: Annotation2
    ) -> Annotation2:
        return Annotation2(
            self.annotation_factory_2.CreateToleranceWithDRF(
                i_index, i_surf.com_object, i_drf.com_object
            )
        )

    def create_tolerance_without_drf(
        self, i_index: cat_variant, i_surf: UserSurface
    ) -> Annotation2:
        return Annotation2(
            self.annotation_factory_2.CreateToleranceWithoutDRF(
                i_index, i_surf.com_object
            )
        )

    def create_weld(self, i_surf: UserSurface) -> Annotation2:
        return Annotation2(self.annotation_factory_2.CreateWeld(i_surf.com_object))

    def instantiate_noa(self, i_noa: Annotation2, i_surf: UserSurface) -> Annotation2:
        return Annotation2(
            self.annotation_factory_2.InstanciateNOA(
                i_noa.com_object, i_surf.com_object
            )
        )

    def __repr__(self):
        return f'AnnotationFactory2(name="{self.name}")'
