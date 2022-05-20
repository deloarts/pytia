from pytia.framework.hybrid_shape_interfaces.hybrid_shape_symmetry import (
    HybridShapeSymmetry,
)
from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.mec_mod_interfaces.body import Body
from pytia.framework.mec_mod_interfaces.factory import Factory
from pytia.framework.part_interfaces.add import Add
from pytia.framework.part_interfaces.assemble import Assemble
from pytia.framework.part_interfaces.auto_draft import AutoDraft
from pytia.framework.part_interfaces.auto_fillet import AutoFillet
from pytia.framework.part_interfaces.chamfer import Chamfer
from pytia.framework.part_interfaces.circ_pattern import CircPattern
from pytia.framework.part_interfaces.close_surface import CloseSurface
from pytia.framework.part_interfaces.const_rad_edge_fillet import ConstRadEdgeFillet
from pytia.framework.part_interfaces.defeaturing import Defeaturing
from pytia.framework.part_interfaces.draft import Draft
from pytia.framework.part_interfaces.face_fillet import FaceFillet
from pytia.framework.part_interfaces.groove import Groove
from pytia.framework.part_interfaces.hole import Hole
from pytia.framework.part_interfaces.intersect import Intersect
from pytia.framework.part_interfaces.mirror import Mirror
from pytia.framework.part_interfaces.pad import Pad
from pytia.framework.part_interfaces.pocket import Pocket
from pytia.framework.part_interfaces.rect_pattern import RectPattern
from pytia.framework.part_interfaces.remove import Remove
from pytia.framework.part_interfaces.remove_face import RemoveFace
from pytia.framework.part_interfaces.replace_face import ReplaceFace
from pytia.framework.part_interfaces.rib import Rib
from pytia.framework.part_interfaces.scaling import Scaling
from pytia.framework.part_interfaces.sew_surface import SewSurface
from pytia.framework.part_interfaces.shaft import Shaft
from pytia.framework.part_interfaces.shell import Shell
from pytia.framework.part_interfaces.slot import Slot
from pytia.framework.part_interfaces.solid_combine import SolidCombine
from pytia.framework.part_interfaces.split import Split
from pytia.framework.part_interfaces.stiffener import Stiffener
from pytia.framework.part_interfaces.symmetry import Symmetry
from pytia.framework.part_interfaces.thick_surface import ThickSurface
from pytia.framework.part_interfaces.thickness import Thickness
from pytia.framework.part_interfaces.thread import Thread
from pytia.framework.part_interfaces.trim import Trim
from pytia.framework.part_interfaces.tritangent_fillet import TritangentFillet
from pytia.framework.part_interfaces.user_pattern import UserPattern
from pytia.framework.part_interfaces.var_rad_edge_fillet import VarRadEdgeFillet
from pytia.framework.sketcher_interfaces.sketch import Sketch
from pytia.framework.system_interfaces.any_object import AnyObject


class ShapeFactory(Factory):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.shape_factory = com_object

    def add_new_add(self, i_body_to_add: Body) -> Add:
        return Add(self.shape_factory.AddNewAdd(i_body_to_add.com_object))

    def add_new_affinity2(
        self, x_ratio: float, y_ratio: float, z_ratio: float
    ) -> AnyObject:
        return AnyObject(self.shape_factory.AddNewAffinity2(x_ratio, y_ratio, z_ratio))

    def add_new_assemble(self, i_body_to_assemble: Body) -> Assemble:
        return Assemble(
            self.shape_factory.AddNewAssemble(i_body_to_assemble.com_object)
        )

    def add_new_auto_draft(self, i_draft_angle: float) -> AutoDraft:
        return AutoDraft(self.shape_factory.AddNewAutoDraft(i_draft_angle))

    def add_new_auto_fillet(
        self, i_fillet_radius: float, i_round_radius: float
    ) -> AutoFillet:
        return AutoFillet(
            self.shape_factory.AddNewAutoFillet(i_fillet_radius, i_round_radius)
        )

    def add_new_axis_to_axis2(
        self, i_reference: Reference, i_target: Reference
    ) -> AnyObject:
        return AnyObject(
            self.shape_factory.AddNewAxisToAxis2(
                i_reference.com_object, i_target.com_object
            )
        )

    def add_new_blend(self) -> AnyObject:
        return AnyObject(self.shape_factory.AddNewBlend())

    def add_new_chamfer(
        self,
        i_object_to_chamfer: Reference,
        i_propagation: int,
        i_mode: int,
        i_orientation: int,
        i_length1: float,
        i_length2_or_angle: float,
    ) -> Chamfer:
        return Chamfer(
            self.shape_factory.AddNewChamfer(
                i_object_to_chamfer.com_object,
                i_propagation,
                i_mode,
                i_orientation,
                i_length1,
                i_length2_or_angle,
            )
        )

    def add_new_circ_pattern(
        self,
        i_shape_to_copy: AnyObject,
        i_nb_of_copies_in_radial_dir: int,
        i_nb_of_copies_in_angular_dir: int,
        i_step_in_radial_dir: float,
        i_step_in_angular_dir: float,
        i_shape_to_copy_position_along_radial_dir: int,
        i_shape_to_copy_position_along_angular_dir: int,
        i_rotation_center: Reference,
        i_rotation_axis: Reference,
        i_is_reversed_rotation_axis: bool,
        i_rotation_angle: float,
        i_is_radius_aligned: bool,
    ) -> CircPattern:
        return CircPattern(
            self.shape_factory.AddNewCircPattern(
                i_shape_to_copy.com_object,
                i_nb_of_copies_in_radial_dir,
                i_nb_of_copies_in_angular_dir,
                i_step_in_radial_dir,
                i_step_in_angular_dir,
                i_shape_to_copy_position_along_radial_dir,
                i_shape_to_copy_position_along_angular_dir,
                i_rotation_center.com_object,
                i_rotation_axis.com_object,
                i_is_reversed_rotation_axis,
                i_rotation_angle,
                i_is_radius_aligned,
            )
        )

    def add_new_circ_patternof_list(
        self,
        i_shape_to_copy: AnyObject,
        i_nb_of_copies_in_radial_dir: int,
        i_nb_of_copies_in_angular_dir: int,
        i_step_in_radial_dir: float,
        i_step_in_angular_dir: float,
        i_shape_to_copy_position_along_radial_dir: int,
        i_shape_to_copy_position_along_angular_dir: int,
        i_rotation_center: Reference,
        i_rotation_axis: Reference,
        i_is_reversed_rotation_axis: bool,
        i_rotation_angle: float,
        i_is_radius_aligned: bool,
    ) -> CircPattern:
        return CircPattern(
            self.shape_factory.AddNewCircPatternofList(
                i_shape_to_copy.com_object,
                i_nb_of_copies_in_radial_dir,
                i_nb_of_copies_in_angular_dir,
                i_step_in_radial_dir,
                i_step_in_angular_dir,
                i_shape_to_copy_position_along_radial_dir,
                i_shape_to_copy_position_along_angular_dir,
                i_rotation_center.com_object,
                i_rotation_axis.com_object,
                i_is_reversed_rotation_axis,
                i_rotation_angle,
                i_is_radius_aligned,
            )
        )

    def add_new_close_surface(self, i_close_element: Reference) -> CloseSurface:
        return CloseSurface(
            self.shape_factory.AddNewCloseSurface(i_close_element.com_object)
        )

    def add_new_defeaturing(self) -> Defeaturing:
        return Defeaturing(self.shape_factory.AddNewDefeaturing())

    def add_new_draft(
        self,
        i_face_to_draft: Reference,
        i_neutral: Reference,
        i_neutral_mode: int,
        i_parting: Reference,
        i_dir_x: float,
        i_dir_y: float,
        i_dir_z: float,
        i_mode: int,
        i_angle: float,
        i_multiselection_mode: int,
    ) -> Draft:
        return Draft(
            self.shape_factory.AddNewDraft(
                i_face_to_draft.com_object,
                i_neutral.com_object,
                i_neutral_mode,
                i_parting.com_object,
                i_dir_x,
                i_dir_y,
                i_dir_z,
                i_mode,
                i_angle,
                i_multiselection_mode,
            )
        )

    def add_new_edge_fillet_with_constant_radius(
        self, i_edge_to_fillet: Reference, i_propag_mode: int, i_radius: float
    ) -> ConstRadEdgeFillet:
        return ConstRadEdgeFillet(
            self.shape_factory.AddNewEdgeFilletWithConstantRadius(
                i_edge_to_fillet.com_object, i_propag_mode, i_radius
            )
        )

    def add_new_edge_fillet_with_varying_radius(
        self,
        i_edge_to_fillet: Reference,
        i_propag_mode: int,
        i_variation_mode: int,
        i_default_radius: float,
    ) -> VarRadEdgeFillet:
        return VarRadEdgeFillet(
            self.shape_factory.AddNewEdgeFilletWithVaryingRadius(
                i_edge_to_fillet.com_object,
                i_propag_mode,
                i_variation_mode,
                i_default_radius,
            )
        )

    def add_new_face_fillet(
        self, i_f1: Reference, i_f2: Reference, i_radius: float
    ) -> FaceFillet:
        return FaceFillet(
            self.shape_factory.AddNewFaceFillet(
                i_f1.com_object, i_f2.com_object, i_radius
            )
        )

    def add_new_gsd_circ_pattern(
        self,
        i_shape_to_copy: AnyObject,
        i_nb_of_copies_in_radial_dir: int,
        i_nb_of_copies_in_angular_dir: int,
        i_step_in_radial_dir: float,
        i_step_in_angular_dir: float,
        i_shape_to_copy_position_along_radial_dir: int,
        i_shape_to_copy_position_along_angular_dir: int,
        i_rotation_center: Reference,
        i_rotation_axis: Reference,
        i_is_reversed_rotation_axis: bool,
        i_rotation_angle: float,
        i_is_radius_aligned: bool,
        i_complete_crown: bool,
        i_type: float,
    ) -> CircPattern:
        return CircPattern(
            self.shape_factory.AddNewGSDCircPattern(
                i_shape_to_copy.com_object,
                i_nb_of_copies_in_radial_dir,
                i_nb_of_copies_in_angular_dir,
                i_step_in_radial_dir,
                i_step_in_angular_dir,
                i_shape_to_copy_position_along_radial_dir,
                i_shape_to_copy_position_along_angular_dir,
                i_rotation_center.com_object,
                i_rotation_axis.com_object,
                i_is_reversed_rotation_axis,
                i_rotation_angle,
                i_is_radius_aligned,
                i_complete_crown,
                i_type,
            )
        )

    def add_new_gsd_rect_pattern(
        self,
        i_shape_to_copy: AnyObject,
        i_nb_of_copies_in_dir1: int,
        i_nb_of_copies_in_dir2: int,
        i_step_in_dir1: float,
        i_step_in_dir2: float,
        i_shape_to_copy_position_along_dir1: int,
        i_shape_to_copy_position_along_dir2: int,
        i_dir1: Reference,
        i_dir2: Reference,
        i_is_reversed_dir1: bool,
        i_is_reversed_dir2: bool,
        i_rotation_angle: float,
        i_type: float,
    ) -> RectPattern:
        return RectPattern(
            self.shape_factory.AddNewGSDRectPattern(
                i_shape_to_copy.com_object,
                i_nb_of_copies_in_dir1,
                i_nb_of_copies_in_dir2,
                i_step_in_dir1,
                i_step_in_dir2,
                i_shape_to_copy_position_along_dir1,
                i_shape_to_copy_position_along_dir2,
                i_dir1.com_object,
                i_dir2.com_object,
                i_is_reversed_dir1,
                i_is_reversed_dir2,
                i_rotation_angle,
                i_type,
            )
        )

    def add_new_groove(self, i_sketch: Sketch) -> Groove:
        return Groove(self.shape_factory.AddNewGroove(i_sketch.com_object))

    def add_new_groove_from_ref(self, i_profile_elt: Reference) -> Groove:
        return Groove(self.shape_factory.AddNewGrooveFromRef(i_profile_elt.com_object))

    def add_new_hole(self, i_support: Reference, i_depth: float) -> Hole:
        return Hole(self.shape_factory.AddNewHole(i_support.com_object, i_depth))

    def add_new_hole_from_point(
        self, i_x: float, i_y: float, i_z: float, i_support: Reference, i_depth: float
    ) -> Hole:
        return Hole(
            self.shape_factory.AddNewHoleFromPoint(
                i_x, i_y, i_z, i_support.com_object, i_depth
            )
        )

    def add_new_hole_from_ref_point(
        self, i_origin: Reference, i_support: Reference, i_depth: float
    ) -> Hole:
        return Hole(
            self.shape_factory.AddNewHoleFromRefPoint(
                i_origin.com_object, i_support.com_object, i_depth
            )
        )

    def add_new_hole_from_sketch(self, i_sketch: Sketch, i_depth: float) -> Hole:
        return Hole(
            self.shape_factory.AddNewHoleFromSketch(i_sketch.com_object, i_depth)
        )

    def add_new_hole_with2_constraints(
        self,
        i_x: float,
        i_y: float,
        i_z: float,
        i_edge1: Reference,
        i_edge2: Reference,
        i_support: Reference,
        i_depth: float,
    ) -> Hole:
        return Hole(
            self.shape_factory.AddNewHoleWith2Constraints(
                i_x,
                i_y,
                i_z,
                i_edge1.com_object,
                i_edge2.com_object,
                i_support.com_object,
                i_depth,
            )
        )

    def add_new_hole_with_constraint(
        self,
        i_x: float,
        i_y: float,
        i_z: float,
        i_edge: Reference,
        i_support: Reference,
        i_depth: float,
    ) -> Hole:
        return Hole(
            self.shape_factory.AddNewHoleWithConstraint(
                i_x, i_y, i_z, i_edge.com_object, i_support.com_object, i_depth
            )
        )

    def add_new_intersect(self, i_body_to_intersect: Body) -> Intersect:
        return Intersect(
            self.shape_factory.AddNewIntersect(i_body_to_intersect.com_object)
        )

    def add_new_loft(self) -> AnyObject:
        return AnyObject(self.shape_factory.AddNewLoft())

    def add_new_mirror(self, i_mirroring_element: Reference) -> Mirror:
        return Mirror(self.shape_factory.AddNewMirror(i_mirroring_element.com_object))

    def add_new_pad(self, i_sketch: Sketch, i_height: float) -> Pad:
        return Pad(self.shape_factory.AddNewPad(i_sketch.com_object, i_height))

    def add_new_pad_from_ref(self, i_profile_elt: Reference, i_height: float) -> Pad:
        return Pad(
            self.shape_factory.AddNewPadFromRef(i_profile_elt.com_object, i_height)
        )

    def add_new_pocket(self, i_sketch: Sketch, i_height: float) -> Pocket:
        return Pocket(self.shape_factory.AddNewPocket(i_sketch.com_object, i_height))

    def add_new_pocket_from_ref(
        self, i_profile_elt: Reference, i_height: float
    ) -> Pocket:
        return Pocket(
            self.shape_factory.AddNewPocketFromRef(i_profile_elt.com_object, i_height)
        )

    def add_new_rect_pattern(
        self,
        i_shape_to_copy: AnyObject,
        i_nb_of_copies_in_dir1: int,
        i_nb_of_copies_in_dir2: int,
        i_step_in_dir1: float,
        i_step_in_dir2: float,
        i_shape_to_copy_position_along_dir1: int,
        i_shape_to_copy_position_along_dir2: int,
        i_dir1: Reference,
        i_dir2: Reference,
        i_is_reversed_dir1: bool,
        i_is_reversed_dir2: bool,
        i_rotation_angle: float,
    ) -> RectPattern:
        return RectPattern(
            self.shape_factory.AddNewRectPattern(
                i_shape_to_copy.com_object,
                i_nb_of_copies_in_dir1,
                i_nb_of_copies_in_dir2,
                i_step_in_dir1,
                i_step_in_dir2,
                i_shape_to_copy_position_along_dir1,
                i_shape_to_copy_position_along_dir2,
                i_dir1.com_object,
                i_dir2.com_object,
                i_is_reversed_dir1,
                i_is_reversed_dir2,
                i_rotation_angle,
            )
        )

    def add_new_rect_patternof_list(
        self,
        i_shape_to_copy: AnyObject,
        i_nb_of_copies_in_dir1: int,
        i_nb_of_copies_in_dir2: int,
        i_step_in_dir1: float,
        i_step_in_dir2: float,
        i_shape_to_copy_position_along_dir1: int,
        i_shape_to_copy_position_along_dir2: int,
        i_dir1: Reference,
        i_dir2: Reference,
        i_is_reversed_dir1: bool,
        i_is_reversed_dir2: bool,
        i_rotation_angle: float,
    ) -> RectPattern:
        return RectPattern(
            self.shape_factory.AddNewRectPatternofList(
                i_shape_to_copy.com_object,
                i_nb_of_copies_in_dir1,
                i_nb_of_copies_in_dir2,
                i_step_in_dir1,
                i_step_in_dir2,
                i_shape_to_copy_position_along_dir1,
                i_shape_to_copy_position_along_dir2,
                i_dir1.com_object,
                i_dir2.com_object,
                i_is_reversed_dir1,
                i_is_reversed_dir2,
                i_rotation_angle,
            )
        )

    def add_new_remove(self, i_body_to_remove: Body) -> Remove:
        return Remove(self.shape_factory.AddNewRemove(i_body_to_remove.com_object))

    def add_new_remove_face(
        self, i_keep_faces: Reference, i_remove_faces: Reference
    ) -> RemoveFace:
        return RemoveFace(
            self.shape_factory.AddNewRemoveFace(
                i_keep_faces.com_object, i_remove_faces.com_object
            )
        )

    def add_new_removed_blend(self) -> AnyObject:
        return AnyObject(self.shape_factory.AddNewRemovedBlend())

    def add_new_removed_loft(self) -> AnyObject:
        return AnyObject(self.shape_factory.AddNewRemovedLoft())

    def add_new_replace_face(
        self, i_split_plane: Reference, i_remove_face: Reference, i_splitting_side: int
    ) -> ReplaceFace:
        return ReplaceFace(
            self.shape_factory.AddNewReplaceFace(
                i_split_plane.com_object, i_remove_face.com_object, i_splitting_side
            )
        )

    def add_new_rib(self, i_sketch: Sketch, i_center_curve: Sketch) -> Rib:
        return Rib(
            self.shape_factory.AddNewRib(i_sketch.com_object, i_center_curve.com_object)
        )

    def add_new_rib_from_ref(
        self, i_profile: Reference, i_center_curve: Reference
    ) -> Rib:
        return Rib(
            self.shape_factory.AddNewRibFromRef(
                i_profile.com_object, i_center_curve.com_object
            )
        )

    def add_new_scaling(
        self, i_scaling_reference: Reference, i_factor: float
    ) -> Scaling:
        return Scaling(
            self.shape_factory.AddNewScaling(i_scaling_reference.com_object, i_factor)
        )

    def add_new_sew_surface(
        self, i_sewing_element: Reference, i_sewing_side: int
    ) -> SewSurface:
        return SewSurface(
            self.shape_factory.AddNewSewSurface(
                i_sewing_element.com_object, i_sewing_side
            )
        )

    def add_new_shaft(self, i_sketch: Sketch) -> Shaft:
        return Shaft(self.shape_factory.AddNewShaft(i_sketch.com_object))

    def add_new_shaft_from_ref(self, i_profile_elt: Reference) -> Shaft:
        return Shaft(self.shape_factory.AddNewShaftFromRef(i_profile_elt.com_object))

    def add_new_shell(
        self,
        i_face_to_remove: Reference,
        i_internal_thickness: float,
        i_external_thickness: float,
    ) -> Shell:
        return Shell(
            self.shape_factory.AddNewShell(
                i_face_to_remove.com_object, i_internal_thickness, i_external_thickness
            )
        )

    def add_new_slot(self, i_sketch: Sketch, i_center_curve: Sketch) -> Slot:
        return Slot(
            self.shape_factory.AddNewSlot(
                i_sketch.com_object, i_center_curve.com_object
            )
        )

    def add_new_slot_from_ref(
        self, i_profile: Reference, i_center_curve: Reference
    ) -> Slot:
        return Slot(
            self.shape_factory.AddNewSlotFromRef(
                i_profile.com_object, i_center_curve.com_object
            )
        )

    def add_new_solid_combine(
        self, i_profile_elt_first: Reference, i_profile_elt_second: Reference
    ) -> SolidCombine:
        return SolidCombine(
            self.shape_factory.AddNewSolidCombine(
                i_profile_elt_first.com_object, i_profile_elt_second.com_object
            )
        )

    def add_new_solid_edge_fillet_with_constant_radius(
        self, i_edge_to_fillet: Reference, i_propag_mode: int, i_radius: float
    ) -> ConstRadEdgeFillet:
        return ConstRadEdgeFillet(
            self.shape_factory.AddNewSolidEdgeFilletWithConstantRadius(
                i_edge_to_fillet.com_object, i_propag_mode, i_radius
            )
        )

    def add_new_solid_edge_fillet_with_varying_radius(
        self,
        i_edge_to_fillet: Reference,
        i_propag_mode: int,
        i_variation_mode: int,
        i_default_radius: float,
    ) -> VarRadEdgeFillet:
        return VarRadEdgeFillet(
            self.shape_factory.AddNewSolidEdgeFilletWithVaryingRadius(
                i_edge_to_fillet.com_object,
                i_propag_mode,
                i_variation_mode,
                i_default_radius,
            )
        )

    def add_new_solid_face_fillet(
        self, i_f1: Reference, i_f2: Reference, i_radius: float
    ) -> FaceFillet:
        return FaceFillet(
            self.shape_factory.AddNewSolidFaceFillet(
                i_f1.com_object, i_f2.com_object, i_radius
            )
        )

    def add_new_solid_tritangent_fillet(
        self, i_f1: Reference, i_f2: Reference, i_removed_face: Reference
    ) -> TritangentFillet:
        return TritangentFillet(
            self.shape_factory.AddNewSolidTritangentFillet(
                i_f1.com_object, i_f2.com_object, i_removed_face.com_object
            )
        )

    def add_new_split(self, i_splitting_element: Reference, i_split_side: int) -> Split:
        return Split(
            self.shape_factory.AddNewSplit(i_splitting_element.com_object, i_split_side)
        )

    def add_new_stiffener(self, i_sketch: Sketch) -> Stiffener:
        return Stiffener(self.shape_factory.AddNewStiffener(i_sketch.com_object))

    def add_new_stiffener_from_ref(self, i_profile_elt: Reference) -> Stiffener:
        return Stiffener(
            self.shape_factory.AddNewStiffenerFromRef(i_profile_elt.com_object)
        )

    def add_new_surface_edge_fillet_with_constant_radius(
        self, i_edge_to_fillet: Reference, i_propag_mode: int, i_radius: float
    ) -> ConstRadEdgeFillet:
        return ConstRadEdgeFillet(
            self.shape_factory.AddNewSurfaceEdgeFilletWithConstantRadius(
                i_edge_to_fillet.com_object, i_propag_mode, i_radius
            )
        )

    def add_new_surface_edge_fillet_with_varying_radius(
        self,
        i_edge_to_fillet: Reference,
        i_propag_mode: int,
        i_variation_mode: int,
        i_default_radius: float,
    ) -> VarRadEdgeFillet:
        return VarRadEdgeFillet(
            self.shape_factory.AddNewSurfaceEdgeFilletWithVaryingRadius(
                i_edge_to_fillet.com_object,
                i_propag_mode,
                i_variation_mode,
                i_default_radius,
            )
        )

    def add_new_surface_face_fillet(
        self, i_f1: Reference, i_f2: Reference, i_radius: float
    ) -> FaceFillet:
        return FaceFillet(
            self.shape_factory.AddNewSurfaceFaceFillet(
                i_f1.com_object, i_f2.com_object, i_radius
            )
        )

    def add_new_surface_tritangent_fillet(
        self, i_f1: Reference, i_f2: Reference, i_removed_face: Reference
    ) -> TritangentFillet:
        return TritangentFillet(
            self.shape_factory.AddNewSurfaceTritangentFillet(
                i_f1.com_object, i_f2.com_object, i_removed_face.com_object
            )
        )

    def add_new_surfacic_auto_fillet(self, i_fillet_radius: float) -> AutoFillet:
        return AutoFillet(self.shape_factory.AddNewSurfacicAutoFillet(i_fillet_radius))

    def add_new_surfacic_circ_pattern(
        self,
        i_shape_to_copy: AnyObject,
        i_nb_of_copies_in_radial_dir: int,
        i_nb_of_copies_in_angular_dir: int,
        i_step_in_radial_dir: float,
        i_step_in_angular_dir: float,
        i_shape_to_copy_position_along_radial_dir: int,
        i_shape_to_copy_position_along_angular_dir: int,
        i_rotation_center: Reference,
        i_rotation_axis: Reference,
        i_is_reversed_rotation_axis: bool,
        i_rotation_angle: float,
        i_is_radius_aligned: bool,
        i_complete_crown: bool,
    ) -> CircPattern:
        return CircPattern(
            self.shape_factory.AddNewSurfacicCircPattern(
                i_shape_to_copy.com_object,
                i_nb_of_copies_in_radial_dir,
                i_nb_of_copies_in_angular_dir,
                i_step_in_radial_dir,
                i_step_in_angular_dir,
                i_shape_to_copy_position_along_radial_dir,
                i_shape_to_copy_position_along_angular_dir,
                i_rotation_center.com_object,
                i_rotation_axis.com_object,
                i_is_reversed_rotation_axis,
                i_rotation_angle,
                i_is_radius_aligned,
                i_complete_crown,
            )
        )

    def add_new_surfacic_rect_pattern(
        self,
        i_shape_to_copy: AnyObject,
        i_nb_of_copies_in_dir1: int,
        i_nb_of_copies_in_dir2: int,
        i_step_in_dir1: float,
        i_step_in_dir2: float,
        i_shape_to_copy_position_along_dir1: int,
        i_shape_to_copy_position_along_dir2: int,
        i_dir1: Reference,
        i_dir2: Reference,
        i_is_reversed_dir1: bool,
        i_is_reversed_dir2: bool,
        i_rotation_angle: float,
    ) -> RectPattern:
        return RectPattern(
            self.shape_factory.AddNewSurfacicRectPattern(
                i_shape_to_copy.com_object,
                i_nb_of_copies_in_dir1,
                i_nb_of_copies_in_dir2,
                i_step_in_dir1,
                i_step_in_dir2,
                i_shape_to_copy_position_along_dir1,
                i_shape_to_copy_position_along_dir2,
                i_dir1.com_object,
                i_dir2.com_object,
                i_is_reversed_dir1,
                i_is_reversed_dir2,
                i_rotation_angle,
            )
        )

    def add_new_surfacic_sew_surface(
        self,
        i_type: int,
        i_support_surface: Reference,
        i_sewing_element: Reference,
        i_sewing_side: int,
    ) -> SewSurface:
        return SewSurface(
            self.shape_factory.AddNewSurfacicSewSurface(
                i_type,
                i_support_surface.com_object,
                i_sewing_element.com_object,
                i_sewing_side,
            )
        )

    def add_new_surfacic_user_pattern(
        self, i_shape_to_copy: AnyObject, i_nb_of_copies: int
    ) -> UserPattern:
        return UserPattern(
            self.shape_factory.AddNewSurfacicUserPattern(
                i_shape_to_copy.com_object, i_nb_of_copies
            )
        )

    def add_new_symmetry_2(self, i_reference: Reference) -> HybridShapeSymmetry:
        return HybridShapeSymmetry(
            self.shape_factory.AddNewSymmetry2(i_reference.com_object)
        )

    def add_new_thick_surface(
        self,
        i_offset_element: Reference,
        i_isens_offset: int,
        i_top_offset: float,
        i_bot_offset: float,
    ) -> ThickSurface:
        return ThickSurface(
            self.shape_factory.AddNewThickSurface(
                i_offset_element.com_object, i_isens_offset, i_top_offset, i_bot_offset
            )
        )

    def add_new_thickness(
        self, i_face_to_thicken: Reference, i_offset: float
    ) -> Thickness:
        return Thickness(
            self.shape_factory.AddNewThickness(i_face_to_thicken.com_object, i_offset)
        )

    def add_new_thread_with_out_ref(self) -> Thread:
        return Thread(self.shape_factory.AddNewThreadWithOutRef())

    def add_new_thread_with_ref(
        self, i_lateral_face: Reference, i_limit_face: Reference
    ) -> Thread:
        return Thread(
            self.shape_factory.AddNewThreadWithRef(
                i_lateral_face.com_object, i_limit_face.com_object
            )
        )

    def add_new_trim(self, i_body_to_trim: Body) -> Trim:
        return Trim(self.shape_factory.AddNewTrim(i_body_to_trim.com_object))

    def add_new_tritangent_fillet(
        self, i_f1: Reference, i_f2: Reference, i_removed_face: Reference
    ) -> TritangentFillet:
        return TritangentFillet(
            self.shape_factory.AddNewTritangentFillet(
                i_f1.com_object, i_f2.com_object, i_removed_face.com_object
            )
        )

    def add_new_user_pattern(
        self, i_shape_to_copy: AnyObject, i_nb_of_copies: int
    ) -> UserPattern:
        return UserPattern(
            self.shape_factory.AddNewUserPattern(
                i_shape_to_copy.com_object, i_nb_of_copies
            )
        )

    def add_new_user_patternof_list(
        self, i_shape_to_copy: AnyObject, i_nb_of_copies: int
    ) -> UserPattern:
        return UserPattern(
            self.shape_factory.AddNewUserPatternofList(
                i_shape_to_copy.com_object, i_nb_of_copies
            )
        )

    def add_new_volume_add(
        self, i_body1: Reference, i_body2: Reference, i_type: float
    ) -> Add:
        return Add(
            self.shape_factory.AddNewVolumeAdd(
                i_body1.com_object, i_body2.com_object, i_type
            )
        )

    def add_new_volume_close_surface(self, i_close_element: Reference) -> CloseSurface:
        return CloseSurface(
            self.shape_factory.AddNewVolumeCloseSurface(i_close_element.com_object)
        )

    def add_new_volume_intersect(
        self, i_body1: Reference, i_body2: Reference, i_type: float
    ) -> Intersect:
        return Intersect(
            self.shape_factory.AddNewVolumeIntersect(
                i_body1.com_object, i_body2.com_object, i_type
            )
        )

    def add_new_volume_remove(
        self, i_body1: Reference, i_body2: Reference, i_type: float
    ) -> Remove:
        return Remove(
            self.shape_factory.AddNewVolumeRemove(
                i_body1.com_object, i_body2.com_object, i_type
            )
        )

    def add_new_volume_sew_surface(
        self,
        i_type: int,
        i_support_volume: Reference,
        i_sewing_element: Reference,
        i_sewing_side: int,
    ) -> SewSurface:
        return SewSurface(
            self.shape_factory.AddNewVolumeSewSurface(
                i_type,
                i_support_volume.com_object,
                i_sewing_element.com_object,
                i_sewing_side,
            )
        )

    def add_new_volume_shell(
        self,
        i_face_to_remove: Reference,
        i_internal_thickness: float,
        i_external_thickness: float,
        i_volume_support: Reference,
    ) -> Shell:
        return Shell(
            self.shape_factory.AddNewVolumeShell(
                i_face_to_remove.com_object,
                i_internal_thickness,
                i_external_thickness,
                i_volume_support.com_object,
            )
        )

    def add_new_volume_thick_surface(
        self,
        i_offset_element: Reference,
        i_isens_offset: int,
        i_top_offset: float,
        i_bot_offset: float,
    ) -> ThickSurface:
        return ThickSurface(
            self.shape_factory.AddNewVolumeThickSurface(
                i_offset_element.com_object, i_isens_offset, i_top_offset, i_bot_offset
            )
        )

    def add_new_volume_thickness(
        self,
        i_face_to_thicken: Reference,
        i_offset: float,
        i_type: int,
        i_volume_support: Reference,
    ) -> Thickness:
        return Thickness(
            self.shape_factory.AddNewVolumeThickness(
                i_face_to_thicken.com_object,
                i_offset,
                i_type,
                i_volume_support.com_object,
            )
        )

    def add_new_volume_trim(
        self, i_support_volume: Reference, i_cutting_volume: Reference
    ) -> Trim:
        return Trim(
            self.shape_factory.AddNewVolumeTrim(
                i_support_volume.com_object, i_cutting_volume.com_object
            )
        )

    def add_new_volumic_draft(
        self,
        i_face_to_draft: Reference,
        i_neutral: Reference,
        i_neutral_mode: int,
        i_parting: Reference,
        i_dir_x: float,
        i_dir_y: float,
        i_dir_z: float,
        i_mode: int,
        i_angle: float,
        i_multiselection_mode: int,
        i_type: int,
        i_volume_support: Reference,
    ) -> Draft:
        return Draft(
            self.shape_factory.AddNewVolumicDraft(
                i_face_to_draft.com_object,
                i_neutral.com_object,
                i_neutral_mode,
                i_parting.com_object,
                i_dir_x,
                i_dir_y,
                i_dir_z,
                i_mode,
                i_angle,
                i_multiselection_mode,
                i_type,
                i_volume_support.com_object,
            )
        )

    def __repr__(self):
        return f'ShapeFactory(name="{self.name}")'
