from pytia.framework.system_interfaces.setting_controller import SettingController


class FTASettingAtt(SettingController):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.fta_setting_att = com_object

    @property
    def alphabetic_order(self) -> bool:
        return self.fta_setting_att.AlphabeticOrder

    @alphabetic_order.setter
    def alphabetic_order(self, value: bool):
        self.fta_setting_att.AlphabeticOrder = value

    @property
    def analysis_display_mode(self) -> bool:
        return self.fta_setting_att.AnalysisDisplayMode

    @analysis_display_mode.setter
    def analysis_display_mode(self, value: bool):
        self.fta_setting_att.AnalysisDisplayMode = value

    @property
    def angulaire_general_tol_class(self) -> int:
        return self.fta_setting_att.AngulaireGeneralTolClass

    @angulaire_general_tol_class.setter
    def angulaire_general_tol_class(self, value: int):
        self.fta_setting_att.AngulaireGeneralTolClass = value

    @property
    def annot_dim_invalid(self) -> bool:
        return self.fta_setting_att.AnnotDimInvalid

    @annot_dim_invalid.setter
    def annot_dim_invalid(self, value: bool):
        self.fta_setting_att.AnnotDimInvalid = value

    @property
    def annot_dim_on_deleted_geom(self) -> bool:
        return self.fta_setting_att.AnnotDimOnDeletedGeom

    @annot_dim_on_deleted_geom.setter
    def annot_dim_on_deleted_geom(self, value: bool):
        self.fta_setting_att.AnnotDimOnDeletedGeom = value

    @property
    def annot_dim_on_unloaded_geom(self) -> bool:
        return self.fta_setting_att.AnnotDimOnUnloadedGeom

    @annot_dim_on_unloaded_geom.setter
    def annot_dim_on_unloaded_geom(self, value: bool):
        self.fta_setting_att.AnnotDimOnUnloadedGeom = value

    @property
    def annot_on_zero_z_setting(self) -> bool:
        return self.fta_setting_att.AnnotOnZeroZSetting

    @annot_on_zero_z_setting.setter
    def annot_on_zero_z_setting(self, value: bool):
        self.fta_setting_att.AnnotOnZeroZSetting = value

    @property
    def body_hide_in_capture(self) -> int:
        return self.fta_setting_att.BodyHideInCapture

    @body_hide_in_capture.setter
    def body_hide_in_capture(self, value: int):
        self.fta_setting_att.BodyHideInCapture = value

    @property
    def cat_fta_chamfer_general_tol_class(self) -> int:
        return self.fta_setting_att.CATFTAChamferGeneralTolClass

    @cat_fta_chamfer_general_tol_class.setter
    def cat_fta_chamfer_general_tol_class(self, value: int):
        self.fta_setting_att.CATFTAChamferGeneralTolClass = value

    @property
    def cat_fta_edges_line_type(self) -> int:
        return self.fta_setting_att.CATFTAEdgesLineType

    @cat_fta_edges_line_type.setter
    def cat_fta_edges_line_type(self, value: int):
        self.fta_setting_att.CATFTAEdgesLineType = value

    @property
    def cat_fta_edges_thickness(self) -> int:
        return self.fta_setting_att.CATFTAEdgesThickness

    @cat_fta_edges_thickness.setter
    def cat_fta_edges_thickness(self, value: int):
        self.fta_setting_att.CATFTAEdgesThickness = value

    @property
    def cat_ftauf_auto_tolerancing(self) -> str:
        return self.fta_setting_att.CATFTAUFAutoTolerancing

    @cat_ftauf_auto_tolerancing.setter
    def cat_ftauf_auto_tolerancing(self, value: str):
        self.fta_setting_att.CATFTAUFAutoTolerancing = value

    @property
    def cat_fta_use_last_tolerances(self) -> bool:
        return self.fta_setting_att.CATFTAUseLastTolerances

    @cat_fta_use_last_tolerances.setter
    def cat_fta_use_last_tolerances(self, value: bool):
        self.fta_setting_att.CATFTAUseLastTolerances = value

    @property
    def dim_after_cre(self) -> bool:
        return self.fta_setting_att.DimAfterCre

    @dim_after_cre.setter
    def dim_after_cre(self, value: bool):
        self.fta_setting_att.DimAfterCre = value

    @property
    def dim_after_mod(self) -> bool:
        return self.fta_setting_att.DimAfterMod

    @dim_after_mod.setter
    def dim_after_mod(self, value: bool):
        self.fta_setting_att.DimAfterMod = value

    @property
    def dim_before_cre(self) -> bool:
        return self.fta_setting_att.DimBeforeCre

    @dim_before_cre.setter
    def dim_before_cre(self, value: bool):
        self.fta_setting_att.DimBeforeCre = value

    @property
    def dim_before_mod(self) -> bool:
        return self.fta_setting_att.DimBeforeMod

    @dim_before_mod.setter
    def dim_before_mod(self, value: bool):
        self.fta_setting_att.DimBeforeMod = value

    @property
    def dim_blanking_cre(self) -> bool:
        return self.fta_setting_att.DimBlankingCre

    @dim_blanking_cre.setter
    def dim_blanking_cre(self, value: bool):
        self.fta_setting_att.DimBlankingCre = value

    @property
    def dim_blanking_mod(self) -> bool:
        return self.fta_setting_att.DimBlankingMod

    @dim_blanking_mod.setter
    def dim_blanking_mod(self, value: bool):
        self.fta_setting_att.DimBlankingMod = value

    @property
    def dim_configure_snapping(self) -> int:
        return self.fta_setting_att.DimConfigureSnapping

    @dim_configure_snapping.setter
    def dim_configure_snapping(self, value: int):
        self.fta_setting_att.DimConfigureSnapping = value

    @property
    def dim_constant_offset(self) -> bool:
        return self.fta_setting_att.DimConstantOffset

    @dim_constant_offset.setter
    def dim_constant_offset(self, value: bool):
        self.fta_setting_att.DimConstantOffset = value

    @property
    def dim_create_on(self) -> int:
        return self.fta_setting_att.DimCreateOn

    @dim_create_on.setter
    def dim_create_on(self, value: int):
        self.fta_setting_att.DimCreateOn = value

    @property
    def dim_line_pos_value(self) -> float:
        return self.fta_setting_att.DimLinePosValue

    @dim_line_pos_value.setter
    def dim_line_pos_value(self, value: float):
        self.fta_setting_att.DimLinePosValue = value

    @property
    def dim_line_up_base_angle(self) -> float:
        return self.fta_setting_att.DimLineUpBaseAngle

    @dim_line_up_base_angle.setter
    def dim_line_up_base_angle(self, value: float):
        self.fta_setting_att.DimLineUpBaseAngle = value

    @property
    def dim_line_up_base_length(self) -> float:
        return self.fta_setting_att.DimLineUpBaseLength

    @dim_line_up_base_length.setter
    def dim_line_up_base_length(self, value: float):
        self.fta_setting_att.DimLineUpBaseLength = value

    @property
    def dim_line_up_cumul(self) -> bool:
        return self.fta_setting_att.DimLineUpCumul

    @dim_line_up_cumul.setter
    def dim_line_up_cumul(self, value: bool):
        self.fta_setting_att.DimLineUpCumul = value

    @property
    def dim_line_up_funnel(self) -> bool:
        return self.fta_setting_att.DimLineUpFunnel

    @dim_line_up_funnel.setter
    def dim_line_up_funnel(self, value: bool):
        self.fta_setting_att.DimLineUpFunnel = value

    @property
    def dim_line_up_offset_bet_dim_angle(self) -> float:
        return self.fta_setting_att.DimLineUpOffsetBetDimAngle

    @dim_line_up_offset_bet_dim_angle.setter
    def dim_line_up_offset_bet_dim_angle(self, value: float):
        self.fta_setting_att.DimLineUpOffsetBetDimAngle = value

    @property
    def dim_line_up_offset_bet_dim_length(self) -> float:
        return self.fta_setting_att.DimLineUpOffsetBetDimLength

    @dim_line_up_offset_bet_dim_length.setter
    def dim_line_up_offset_bet_dim_length(self, value: float):
        self.fta_setting_att.DimLineUpOffsetBetDimLength = value

    @property
    def dim_line_up_offset_to_ref_angle(self) -> float:
        return self.fta_setting_att.DimLineUpOffsetToRefAngle

    @dim_line_up_offset_to_ref_angle.setter
    def dim_line_up_offset_to_ref_angle(self, value: float):
        self.fta_setting_att.DimLineUpOffsetToRefAngle = value

    @property
    def dim_line_up_offset_to_ref_length(self) -> float:
        return self.fta_setting_att.DimLineUpOffsetToRefLength

    @dim_line_up_offset_to_ref_length.setter
    def dim_line_up_offset_to_ref_length(self, value: float):
        self.fta_setting_att.DimLineUpOffsetToRefLength = value

    @property
    def dim_line_up_stack(self) -> bool:
        return self.fta_setting_att.DimLineUpStack

    @dim_line_up_stack.setter
    def dim_line_up_stack(self, value: bool):
        self.fta_setting_att.DimLineUpStack = value

    @property
    def dim_manual_positionning(self) -> bool:
        return self.fta_setting_att.DimManualPositionning

    @dim_manual_positionning.setter
    def dim_manual_positionning(self, value: bool):
        self.fta_setting_att.DimManualPositionning = value

    @property
    def dim_move_2d_part_cre(self) -> bool:
        return self.fta_setting_att.DimMove2dPartCre

    @dim_move_2d_part_cre.setter
    def dim_move_2d_part_cre(self, value: bool):
        self.fta_setting_att.DimMove2dPartCre = value

    @property
    def dim_move_2d_part_mod(self) -> bool:
        return self.fta_setting_att.DimMove2dPartMod

    @dim_move_2d_part_mod.setter
    def dim_move_2d_part_mod(self, value: bool):
        self.fta_setting_att.DimMove2dPartMod = value

    @property
    def dim_move_dim_line_cre(self) -> bool:
        return self.fta_setting_att.DimMoveDimLineCre

    @dim_move_dim_line_cre.setter
    def dim_move_dim_line_cre(self, value: bool):
        self.fta_setting_att.DimMoveDimLineCre = value

    @property
    def dim_move_dim_line_mod(self) -> bool:
        return self.fta_setting_att.DimMoveDimLineMod

    @dim_move_dim_line_mod.setter
    def dim_move_dim_line_mod(self, value: bool):
        self.fta_setting_att.DimMoveDimLineMod = value

    @property
    def dim_move_leader_cre(self) -> bool:
        return self.fta_setting_att.DimMoveLeaderCre

    @dim_move_leader_cre.setter
    def dim_move_leader_cre(self, value: bool):
        self.fta_setting_att.DimMoveLeaderCre = value

    @property
    def dim_move_leader_mod(self) -> bool:
        return self.fta_setting_att.DimMoveLeaderMod

    @dim_move_leader_mod.setter
    def dim_move_leader_mod(self, value: bool):
        self.fta_setting_att.DimMoveLeaderMod = value

    @property
    def dim_move_sub_part(self) -> bool:
        return self.fta_setting_att.DimMoveSubPart

    @dim_move_sub_part.setter
    def dim_move_sub_part(self, value: bool):
        self.fta_setting_att.DimMoveSubPart = value

    @property
    def dim_move_value_cre(self) -> bool:
        return self.fta_setting_att.DimMoveValueCre

    @dim_move_value_cre.setter
    def dim_move_value_cre(self, value: bool):
        self.fta_setting_att.DimMoveValueCre = value

    @property
    def dim_move_value_mod(self) -> bool:
        return self.fta_setting_att.DimMoveValueMod

    @dim_move_value_mod.setter
    def dim_move_value_mod(self, value: bool):
        self.fta_setting_att.DimMoveValueMod = value

    @property
    def dim_o_run_cre(self) -> bool:
        return self.fta_setting_att.DimORunCre

    @dim_o_run_cre.setter
    def dim_o_run_cre(self, value: bool):
        self.fta_setting_att.DimORunCre = value

    @property
    def dim_o_run_mod(self) -> bool:
        return self.fta_setting_att.DimORunMod

    @dim_o_run_mod.setter
    def dim_o_run_mod(self, value: bool):
        self.fta_setting_att.DimORunMod = value

    @property
    def dim_ori_default_symb(self) -> bool:
        return self.fta_setting_att.DimOriDefaultSymb

    @dim_ori_default_symb.setter
    def dim_ori_default_symb(self, value: bool):
        self.fta_setting_att.DimOriDefaultSymb = value

    @property
    def dim_snapping(self) -> bool:
        return self.fta_setting_att.DimSnapping

    @dim_snapping.setter
    def dim_snapping(self, value: bool):
        self.fta_setting_att.DimSnapping = value

    @property
    def general_tol_class(self) -> int:
        return self.fta_setting_att.GeneralTolClass

    @general_tol_class.setter
    def general_tol_class(self, value: int):
        self.fta_setting_att.GeneralTolClass = value

    @property
    def highlight_def_annot(self) -> bool:
        return self.fta_setting_att.HighlightDefAnnot

    @highlight_def_annot.setter
    def highlight_def_annot(self, value: bool):
        self.fta_setting_att.HighlightDefAnnot = value

    @property
    def noa_creation(self) -> bool:
        return self.fta_setting_att.NoaCreation

    @noa_creation.setter
    def noa_creation(self, value: bool):
        self.fta_setting_att.NoaCreation = value

    @property
    def non_semantic_always_upgrade(self) -> bool:
        return self.fta_setting_att.NonSemanticAllwaysUpgrade

    @non_semantic_always_upgrade.setter
    def non_semantic_always_upgrade(self, value: bool):
        self.fta_setting_att.NonSemanticAllwaysUpgrade = value

    @property
    def non_semantic_always_upgrade_general_tol(self) -> bool:
        return self.fta_setting_att.NonSemanticAllwaysUpgradeGeneralTol

    @non_semantic_always_upgrade_general_tol.setter
    def non_semantic_always_upgrade_general_tol(self, value: bool):
        self.fta_setting_att.NonSemanticAllwaysUpgradeGeneralTol = value

    @property
    def non_semantic_dim_allowed(self) -> bool:
        return self.fta_setting_att.NonSemanticDimAllowed

    @non_semantic_dim_allowed.setter
    def non_semantic_dim_allowed(self, value: bool):
        self.fta_setting_att.NonSemanticDimAllowed = value

    @property
    def non_semantic_marked(self) -> bool:
        return self.fta_setting_att.NonSemanticMarked

    @non_semantic_marked.setter
    def non_semantic_marked(self, value: bool):
        self.fta_setting_att.NonSemanticMarked = value

    @property
    def non_semantic_tol_allowed(self) -> bool:
        return self.fta_setting_att.NonSemanticTolAllowed

    @non_semantic_tol_allowed.setter
    def non_semantic_tol_allowed(self, value: bool):
        self.fta_setting_att.NonSemanticTolAllowed = value

    @property
    def parameters_in_tree(self) -> bool:
        return self.fta_setting_att.ParametersInTree

    @parameters_in_tree.setter
    def parameters_in_tree(self, value: bool):
        self.fta_setting_att.ParametersInTree = value

    @property
    def rotation_snap_angle(self) -> float:
        return self.fta_setting_att.RotationSnapAngle

    @rotation_snap_angle.setter
    def rotation_snap_angle(self, value: float):
        self.fta_setting_att.RotationSnapAngle = value

    @property
    def rotation_snap_auto(self) -> bool:
        return self.fta_setting_att.RotationSnapAuto

    @rotation_snap_auto.setter
    def rotation_snap_auto(self, value: bool):
        self.fta_setting_att.RotationSnapAuto = value

    @property
    def sect_pattern(self) -> bool:
        return self.fta_setting_att.SectPattern

    @sect_pattern.setter
    def sect_pattern(self, value: bool):
        self.fta_setting_att.SectPattern = value

    @property
    def select_published_geometry(self) -> bool:
        return self.fta_setting_att.SelectPublishedGeometry

    @select_published_geometry.setter
    def select_published_geometry(self, value: bool):
        self.fta_setting_att.SelectPublishedGeometry = value

    @property
    def shifted_profile(self) -> bool:
        return self.fta_setting_att.ShiftedProfile

    @shifted_profile.setter
    def shifted_profile(self, value: bool):
        self.fta_setting_att.ShiftedProfile = value

    @property
    def true_dimension(self) -> bool:
        return self.fta_setting_att.TrueDimension

    @true_dimension.setter
    def true_dimension(self, value: bool):
        self.fta_setting_att.TrueDimension = value

    def get_alphabetic_order_info(self, admin_level: str, o_locked: str) -> bool:
        return self.fta_setting_att.GetAlphabeticOrderInfo(admin_level, o_locked)

    def get_analysis_display_mode_info(self, admin_level: str, o_locked: str) -> bool:
        return self.fta_setting_att.GetAnalysisDisplayModeInfo(admin_level, o_locked)

    def get_angulaire_general_tol_class_info(
        self, admin_level: str, o_locked: str
    ) -> bool:
        return self.fta_setting_att.GetAngulaireGeneralTolClassInfo(
            admin_level, o_locked
        )

    def get_annot_dim_invalid_colour(
        self, o_value_r: int, o_value_g: int, o_value_b: int
    ) -> None:
        return self.fta_setting_att.GetAnnotDimInvalidColor(
            o_value_r, o_value_g, o_value_b
        )

    def get_annot_dim_invalid_colour_info(
        self, io_admin_level: str, io_locked: str, o_modified: bool
    ) -> None:
        return self.fta_setting_att.GetAnnotDimInvalidColorInfo(
            io_admin_level, io_locked, o_modified
        )

    def get_annot_dim_invalid_info(self, admin_level: str, o_locked: str) -> bool:
        return self.fta_setting_att.GetAnnotDimInvalidInfo(admin_level, o_locked)

    def get_annot_dim_on_deleted_geom_colour(
        self, o_value_r: int, o_value_g: int, o_value_b: int
    ) -> None:
        return self.fta_setting_att.GetAnnotDimOnDeletedGeomColor(
            o_value_r, o_value_g, o_value_b
        )

    def get_annot_dim_on_deleted_geom_colour_info(
        self, io_admin_level: str, io_locked: str, o_modified: bool
    ) -> None:
        return self.fta_setting_att.GetAnnotDimOnDeletedGeomColorInfo(
            io_admin_level, io_locked, o_modified
        )

    def get_annot_dim_on_deleted_geom_info(
        self, admin_level: str, o_locked: str
    ) -> bool:
        return self.fta_setting_att.GetAnnotDimOnDeletedGeomInfo(admin_level, o_locked)

    def get_annot_dim_on_unloaded_geom_colour(
        self, o_value_r: int, o_value_g: int, o_value_b: int
    ) -> None:
        return self.fta_setting_att.GetAnnotDimOnUnloadedGeomColor(
            o_value_r, o_value_g, o_value_b
        )

    def get_annot_dim_on_unloaded_geom_colour_info(
        self, io_admin_level: str, io_locked: str, o_modified: bool
    ) -> None:
        return self.fta_setting_att.GetAnnotDimOnUnloadedGeomColorInfo(
            io_admin_level, io_locked, o_modified
        )

    def get_annot_dim_on_unloaded_geom_info(
        self, admin_level: str, o_locked: str
    ) -> bool:
        return self.fta_setting_att.GetAnnotDimOnUnloadedGeomInfo(admin_level, o_locked)

    def get_annot_on_zero_z_setting_info(self, admin_level: str, o_locked: str) -> bool:
        return self.fta_setting_att.GetAnnotOnZeroZSettingInfo(admin_level, o_locked)

    def get_body_hide_in_capture_info(self, admin_level: str, o_locked: str) -> bool:
        return self.fta_setting_att.GetBodyHideInCaptureInfo(admin_level, o_locked)

    def get_cat_fta_chamfer_general_tol_class_info(
        self, admin_level: str, o_locked: str
    ) -> bool:
        return self.fta_setting_att.GetCATFTAChamferGeneralTolClassInfo(
            admin_level, o_locked
        )

    def get_cat_fta_edges_colour(
        self, o_value_r: int, o_value_g: int, o_value_b: int
    ) -> None:
        return self.fta_setting_att.GetCATFTAEdgesColor(o_value_r, o_value_g, o_value_b)

    def get_cat_fta_edges_colour_info(
        self, io_admin_level: str, io_locked: str, o_modified: bool
    ) -> None:
        return self.fta_setting_att.GetCATFTAEdgesColorInfo(
            io_admin_level, io_locked, o_modified
        )

    def get_cat_fta_edges_line_type_info(
        self, io_admin_level: str, io_locked: str, o_modified: bool
    ) -> None:
        return self.fta_setting_att.GetCATFTAEdgesLineTypeInfo(
            io_admin_level, io_locked, o_modified
        )

    def get_cat_fta_edges_thickness_info(
        self, io_admin_level: str, io_locked: str, o_modified: bool
    ) -> None:
        return self.fta_setting_att.GetCATFTAEdgesThicknessInfo(
            io_admin_level, io_locked, o_modified
        )

    def get_cat_fta_uf_auto_tolerancing_info(
        self, io_admin_level: str, io_locked: str, o_modified: bool
    ) -> None:
        return self.fta_setting_att.GetCATFTAUFAutoTolerancingInfo(
            io_admin_level, io_locked, o_modified
        )

    def get_cat_fta_use_last_tolerances_info(
        self, admin_level: str, o_locked: str
    ) -> bool:
        return self.fta_setting_att.GetCATFTAUseLastTolerancesInfo(
            admin_level, o_locked
        )

    def get_dim_after_cre_info(self, admin_level: str, o_locked: str) -> bool:
        return self.fta_setting_att.GetDimAfterCreInfo(admin_level, o_locked)

    def get_dim_after_mod_info(self, admin_level: str, o_locked: str) -> bool:
        return self.fta_setting_att.GetDimAfterModInfo(admin_level, o_locked)

    def get_dim_before_cre_info(self, admin_level: str, o_locked: str) -> bool:
        return self.fta_setting_att.GetDimBeforeCreInfo(admin_level, o_locked)

    def get_dim_before_mod_info(self, admin_level: str, o_locked: str) -> bool:
        return self.fta_setting_att.GetDimBeforeModInfo(admin_level, o_locked)

    def get_dim_blanking_cre_info(self, admin_level: str, o_locked: str) -> bool:
        return self.fta_setting_att.GetDimBlankingCreInfo(admin_level, o_locked)

    def get_dim_blanking_mod_info(self, admin_level: str, o_locked: str) -> bool:
        return self.fta_setting_att.GetDimBlankingModInfo(admin_level, o_locked)

    def get_dim_configure_snapping_info(self, admin_level: str, o_locked: str) -> bool:
        return self.fta_setting_att.GetDimConfigureSnappingInfo(admin_level, o_locked)

    def get_dim_constant_offset_info(self, admin_level: str, o_locked: str) -> bool:
        return self.fta_setting_att.GetDimConstantOffsetInfo(admin_level, o_locked)

    def get_dim_create_on_info(self, admin_level: str, o_locked: str) -> bool:
        return self.fta_setting_att.GetDimCreateOnInfo(admin_level, o_locked)

    def get_dim_line_pos_value_info(self, admin_level: str, o_locked: str) -> bool:
        return self.fta_setting_att.GetDimLinePosValueInfo(admin_level, o_locked)

    def get_dim_line_up_base_angle_info(self, admin_level: str, o_locked: str) -> bool:
        return self.fta_setting_att.GetDimLineUpBaseAngleInfo(admin_level, o_locked)

    def get_dim_line_up_base_length_info(self, admin_level: str, o_locked: str) -> bool:
        return self.fta_setting_att.GetDimLineUpBaseLengthInfo(admin_level, o_locked)

    def get_dim_line_up_cumul_info(self, admin_level: str, o_locked: str) -> bool:
        return self.fta_setting_att.GetDimLineUpCumulInfo(admin_level, o_locked)

    def get_dim_line_up_funnel_info(self, admin_level: str, o_locked: str) -> bool:
        return self.fta_setting_att.GetDimLineUpFunnelInfo(admin_level, o_locked)

    def get_dim_line_up_offset_bet_dim_angle_info(
        self, admin_level: str, o_locked: str
    ) -> bool:
        return self.fta_setting_att.GetDimLineUpOffsetBetDimAngleInfo(
            admin_level, o_locked
        )

    def get_dim_line_up_offset_bet_dim_length_info(
        self, admin_level: str, o_locked: str
    ) -> bool:
        return self.fta_setting_att.GetDimLineUpOffsetBetDimLengthInfo(
            admin_level, o_locked
        )

    def get_dim_line_up_offset_to_ref_angle_info(
        self, admin_level: str, o_locked: str
    ) -> bool:
        return self.fta_setting_att.GetDimLineUpOffsetToRefAngleInfo(
            admin_level, o_locked
        )

    def get_dim_line_up_offset_to_ref_length_info(
        self, admin_level: str, o_locked: str
    ) -> bool:
        return self.fta_setting_att.GetDimLineUpOffsetToRefLengthInfo(
            admin_level, o_locked
        )

    def get_dim_line_up_stack_info(self, admin_level: str, o_locked: str) -> bool:
        return self.fta_setting_att.GetDimLineUpStackInfo(admin_level, o_locked)

    def get_dim_manual_positioning_info(self, admin_level: str, o_locked: str) -> bool:
        return self.fta_setting_att.GetDimManualPositionningInfo(admin_level, o_locked)

    def get_dim_move_2d_part_cre_info(self, admin_level: str, o_locked: str) -> bool:
        return self.fta_setting_att.GetDimMove2dPartCreInfo(admin_level, o_locked)

    def get_dim_move_2d_part_mod_info(self, admin_level: str, o_locked: str) -> bool:
        return self.fta_setting_att.GetDimMove2dPartModInfo(admin_level, o_locked)

    def get_dim_move_dim_line_cre_info(self, admin_level: str, o_locked: str) -> bool:
        return self.fta_setting_att.GetDimMoveDimLineCreInfo(admin_level, o_locked)

    def get_dim_move_dim_line_mod_info(self, admin_level: str, o_locked: str) -> bool:
        return self.fta_setting_att.GetDimMoveDimLineModInfo(admin_level, o_locked)

    def get_dim_move_leader_cre_info(self, admin_level: str, o_locked: str) -> bool:
        return self.fta_setting_att.GetDimMoveLeaderCreInfo(admin_level, o_locked)

    def get_dim_move_leader_mod_info(self, admin_level: str, o_locked: str) -> bool:
        return self.fta_setting_att.GetDimMoveLeaderModInfo(admin_level, o_locked)

    def get_dim_move_sub_part_info(self, admin_level: str, o_locked: str) -> bool:
        return self.fta_setting_att.GetDimMoveSubPartInfo(admin_level, o_locked)

    def get_dim_move_value_cre_info(self, admin_level: str, o_locked: str) -> bool:
        return self.fta_setting_att.GetDimMoveValueCreInfo(admin_level, o_locked)

    def get_dim_move_value_mod_info(self, admin_level: str, o_locked: str) -> bool:
        return self.fta_setting_att.GetDimMoveValueModInfo(admin_level, o_locked)

    def get_dim_o_run_cre_info(self, admin_level: str, o_locked: str) -> bool:
        return self.fta_setting_att.GetDimORunCreInfo(admin_level, o_locked)

    def get_dim_o_run_mod_info(self, admin_level: str, o_locked: str) -> bool:
        return self.fta_setting_att.GetDimORunModInfo(admin_level, o_locked)

    def get_dim_ori_default_symb_info(self, admin_level: str, o_locked: str) -> bool:
        return self.fta_setting_att.GetDimOriDefaultSymbInfo(admin_level, o_locked)

    def get_dim_snapping_info(self, admin_level: str, o_locked: str) -> bool:
        return self.fta_setting_att.GetDimSnappingInfo(admin_level, o_locked)

    def get_general_tol_class_info(self, admin_level: str, o_locked: str) -> bool:
        return self.fta_setting_att.GetGeneralTolClassInfo(admin_level, o_locked)

    def get_highlight_def_annot_info(self, admin_level: str, o_locked: str) -> bool:
        return self.fta_setting_att.GetHighlightDefAnnotInfo(admin_level, o_locked)

    def get_noa_creation_info(self, admin_level: str, o_locked: str) -> bool:
        return self.fta_setting_att.GetNoaCreationInfo(admin_level, o_locked)

    def get_non_semantic_always_upgrade_general_tol_info(
        self, admin_level: str, o_locked: str
    ) -> bool:
        return self.fta_setting_att.GetNonSemanticAllwaysUpgradeGeneralTolInfo(
            admin_level, o_locked
        )

    def get_non_semantic_always_upgrade_info(
        self, admin_level: str, o_locked: str
    ) -> bool:
        return self.fta_setting_att.GetNonSemanticAllwaysUpgradeInfo(
            admin_level, o_locked
        )

    def get_non_semantic_dim_allowed_info(
        self, admin_level: str, o_locked: str
    ) -> bool:
        return self.fta_setting_att.GetNonSemanticDimAllowedInfo(admin_level, o_locked)

    def get_non_semantic_marked_info(self, admin_level: str, o_locked: str) -> bool:
        return self.fta_setting_att.GetNonSemanticMarkedInfo(admin_level, o_locked)

    def get_non_semantic_tol_allowed_info(
        self, admin_level: str, o_locked: str
    ) -> bool:
        return self.fta_setting_att.GetNonSemanticTolAllowedInfo(admin_level, o_locked)

    def get_parameters_in_tree_info(self, admin_level: str, o_locked: str) -> bool:
        return self.fta_setting_att.GetParametersInTreeInfo(admin_level, o_locked)

    def get_rotation_snap_angle_info(self, admin_level: str, o_locked: str) -> bool:
        return self.fta_setting_att.GetRotationSnapAngleInfo(admin_level, o_locked)

    def get_rotation_snap_auto_info(self, admin_level: str, o_locked: str) -> bool:
        return self.fta_setting_att.GetRotationSnapAutoInfo(admin_level, o_locked)

    def get_sect_pattern_info(self, admin_level: str, o_locked: str) -> bool:
        return self.fta_setting_att.GetSectPatternInfo(admin_level, o_locked)

    def get_select_published_geometry_info(
        self, admin_level: str, o_locked: str
    ) -> bool:
        return self.fta_setting_att.GetSelectPublishedGeometryInfo(
            admin_level, o_locked
        )

    def get_shifted_profile_info(self, admin_level: str, o_locked: str) -> bool:
        return self.fta_setting_att.GetShiftedProfileInfo(admin_level, o_locked)

    def get_true_dimension_colour(
        self, o_value_r: int, o_value_g: int, o_value_b: int
    ) -> None:
        return self.fta_setting_att.GetTrueDimensionColor(
            o_value_r, o_value_g, o_value_b
        )

    def get_true_dimension_colour_info(
        self, io_admin_level: str, io_locked: str, o_modified: bool
    ) -> None:
        return self.fta_setting_att.GetTrueDimensionColorInfo(
            io_admin_level, io_locked, o_modified
        )

    def get_true_dimension_info(self, admin_level: str, o_locked: str) -> bool:
        return self.fta_setting_att.GetTrueDimensionInfo(admin_level, o_locked)

    def set_alphabetic_order_lock(self, i_locked: bool) -> None:
        return self.fta_setting_att.SetAlphabeticOrderLock(i_locked)

    def set_analysis_display_mode_lock(self, i_locked: bool) -> None:
        return self.fta_setting_att.SetAnalysisDisplayModeLock(i_locked)

    def set_angulaire_general_tol_class_lock(self, i_locked: bool) -> None:
        return self.fta_setting_att.SetAngulaireGeneralTolClassLock(i_locked)

    def set_annot_dim_invalid_colour(
        self, i_value_r: int, i_value_g: int, i_value_b: int
    ) -> None:
        return self.fta_setting_att.SetAnnotDimInvalidColor(
            i_value_r, i_value_g, i_value_b
        )

    def set_annot_dim_invalid_colour_lock(self, i_locked: bool) -> None:
        return self.fta_setting_att.SetAnnotDimInvalidColorLock(i_locked)

    def set_annot_dim_invalid_lock(self, i_locked: bool) -> None:
        return self.fta_setting_att.SetAnnotDimInvalidLock(i_locked)

    def set_annot_dim_on_deleted_geom_colour(
        self, i_value_r: int, i_value_g: int, i_value_b: int
    ) -> None:
        return self.fta_setting_att.SetAnnotDimOnDeletedGeomColor(
            i_value_r, i_value_g, i_value_b
        )

    def set_annot_dim_on_deleted_geom_colour_lock(self, i_locked: bool) -> None:
        return self.fta_setting_att.SetAnnotDimOnDeletedGeomColorLock(i_locked)

    def set_annot_dim_on_deleted_geom_lock(self, i_locked: bool) -> None:
        return self.fta_setting_att.SetAnnotDimOnDeletedGeomLock(i_locked)

    def set_annot_dim_on_unloaded_geom_colour(
        self, i_value_r: int, i_value_g: int, i_value_b: int
    ) -> None:
        return self.fta_setting_att.SetAnnotDimOnUnloadedGeomColor(
            i_value_r, i_value_g, i_value_b
        )

    def set_annot_dim_on_unloaded_geom_colour_lock(self, i_locked: bool) -> None:
        return self.fta_setting_att.SetAnnotDimOnUnloadedGeomColorLock(i_locked)

    def set_annot_dim_on_unloaded_geom_lock(self, i_locked: bool) -> None:
        return self.fta_setting_att.SetAnnotDimOnUnloadedGeomLock(i_locked)

    def set_annot_on_zero_z_setting_lock(self, i_locked: bool) -> None:
        return self.fta_setting_att.SetAnnotOnZeroZSettingLock(i_locked)

    def set_body_hide_in_capture_lock(self, i_locked: bool) -> None:
        return self.fta_setting_att.SetBodyHideInCaptureLock(i_locked)

    def set_cat_fta_chamfer_general_tol_class_lock(self, i_locked: bool) -> None:
        return self.fta_setting_att.SetCATFTAChamferGeneralTolClassLock(i_locked)

    def set_cat_fta_edges_colour(
        self, i_value_r: int, i_value_g: int, i_value_b: int
    ) -> None:
        return self.fta_setting_att.SetCATFTAEdgesColor(i_value_r, i_value_g, i_value_b)

    def set_cat_fta_edges_colour_lock(self, i_locked: bool) -> None:
        return self.fta_setting_att.SetCATFTAEdgesColorLock(i_locked)

    def set_cat_fta_edges_line_type_lock(self, i_locked: bool) -> None:
        return self.fta_setting_att.SetCATFTAEdgesLineTypeLock(i_locked)

    def set_cat_fta_edges_thickness_lock(self, i_locked: bool) -> None:
        return self.fta_setting_att.SetCATFTAEdgesThicknessLock(i_locked)

    def set_cat_ftauf_auto_tolerancing_lock(self, i_locked: bool) -> None:
        return self.fta_setting_att.SetCATFTAUFAutoTolerancingLock(i_locked)

    def set_cat_fta_use_last_tolerances_lock(self, i_locked: bool) -> None:
        return self.fta_setting_att.SetCATFTAUseLastTolerancesLock(i_locked)

    def set_dim_after_cre_lock(self, i_locked: bool) -> None:
        return self.fta_setting_att.SetDimAfterCreLock(i_locked)

    def set_dim_after_mod_lock(self, i_locked: bool) -> None:
        return self.fta_setting_att.SetDimAfterModLock(i_locked)

    def set_dim_before_cre_lock(self, i_locked: bool) -> None:
        return self.fta_setting_att.SetDimBeforeCreLock(i_locked)

    def set_dim_before_mod_lock(self, i_locked: bool) -> None:
        return self.fta_setting_att.SetDimBeforeModLock(i_locked)

    def set_dim_blanking_cre_lock(self, i_locked: bool) -> None:
        return self.fta_setting_att.SetDimBlankingCreLock(i_locked)

    def set_dim_blanking_mod_lock(self, i_locked: bool) -> None:
        return self.fta_setting_att.SetDimBlankingModLock(i_locked)

    def set_dim_configure_snapping_lock(self, i_locked: bool) -> None:
        return self.fta_setting_att.SetDimConfigureSnappingLock(i_locked)

    def set_dim_constant_offset_lock(self, i_locked: bool) -> None:
        return self.fta_setting_att.SetDimConstantOffsetLock(i_locked)

    def set_dim_create_on_lock(self, i_locked: bool) -> None:
        return self.fta_setting_att.SetDimCreateOnLock(i_locked)

    def set_dim_line_pos_value_lock(self, i_locked: bool) -> None:
        return self.fta_setting_att.SetDimLinePosValueLock(i_locked)

    def set_dim_line_up_base_angle_lock(self, i_locked: bool) -> None:
        return self.fta_setting_att.SetDimLineUpBaseAngleLock(i_locked)

    def set_dim_line_up_base_length_lock(self, i_locked: bool) -> None:
        return self.fta_setting_att.SetDimLineUpBaseLengthLock(i_locked)

    def set_dim_line_up_cumul_lock(self, i_locked: bool) -> None:
        return self.fta_setting_att.SetDimLineUpCumulLock(i_locked)

    def set_dim_line_up_funnel_lock(self, i_locked: bool) -> None:
        return self.fta_setting_att.SetDimLineUpFunnelLock(i_locked)

    def set_dim_line_up_offset_bet_dim_angle_lock(self, i_locked: bool) -> None:
        return self.fta_setting_att.SetDimLineUpOffsetBetDimAngleLock(i_locked)

    def set_dim_line_up_offset_bet_dim_length_lock(self, i_locked: bool) -> None:
        return self.fta_setting_att.SetDimLineUpOffsetBetDimLengthLock(i_locked)

    def set_dim_line_up_offset_to_ref_angle_lock(self, i_locked: bool) -> None:
        return self.fta_setting_att.SetDimLineUpOffsetToRefAngleLock(i_locked)

    def set_dim_line_up_offset_to_ref_length_lock(self, i_locked: bool) -> None:
        return self.fta_setting_att.SetDimLineUpOffsetToRefLengthLock(i_locked)

    def set_dim_line_up_stack_lock(self, i_locked: bool) -> None:
        return self.fta_setting_att.SetDimLineUpStackLock(i_locked)

    def set_dim_manual_positioning_lock(self, i_locked: bool) -> None:
        return self.fta_setting_att.SetDimManualPositionningLock(i_locked)

    def set_dim_move_2d_part_cre_lock(self, i_locked: bool) -> None:
        return self.fta_setting_att.SetDimMove2dPartCreLock(i_locked)

    def set_dim_move_2d_part_mod_lock(self, i_locked: bool) -> None:
        return self.fta_setting_att.SetDimMove2dPartModLock(i_locked)

    def set_dim_move_dim_line_cre_lock(self, i_locked: bool) -> None:
        return self.fta_setting_att.SetDimMoveDimLineCreLock(i_locked)

    def set_dim_move_dim_line_mod_lock(self, i_locked: bool) -> None:
        return self.fta_setting_att.SetDimMoveDimLineModLock(i_locked)

    def set_dim_move_leader_cre_lock(self, i_locked: bool) -> None:
        return self.fta_setting_att.SetDimMoveLeaderCreLock(i_locked)

    def set_dim_move_leader_mod_lock(self, i_locked: bool) -> None:
        return self.fta_setting_att.SetDimMoveLeaderModLock(i_locked)

    def set_dim_move_sub_part_lock(self, i_locked: bool) -> None:
        return self.fta_setting_att.SetDimMoveSubPartLock(i_locked)

    def set_dim_move_value_cre_lock(self, i_locked: bool) -> None:
        return self.fta_setting_att.SetDimMoveValueCreLock(i_locked)

    def set_dim_move_value_mod_lock(self, i_locked: bool) -> None:
        return self.fta_setting_att.SetDimMoveValueModLock(i_locked)

    def set_dim_o_run_cre_lock(self, i_locked: bool) -> None:
        return self.fta_setting_att.SetDimORunCreLock(i_locked)

    def set_dim_o_run_mod_lock(self, i_locked: bool) -> None:
        return self.fta_setting_att.SetDimORunModLock(i_locked)

    def set_dim_ori_default_symb_lock(self, i_locked: bool) -> None:
        return self.fta_setting_att.SetDimOriDefaultSymbLock(i_locked)

    def set_dim_snapping_lock(self, i_locked: bool) -> None:
        return self.fta_setting_att.SetDimSnappingLock(i_locked)

    def set_general_tol_class_lock(self, i_locked: bool) -> None:
        return self.fta_setting_att.SetGeneralTolClassLock(i_locked)

    def set_highlight_def_annot_lock(self, i_locked: bool) -> None:
        return self.fta_setting_att.SetHighlightDefAnnotLock(i_locked)

    def set_noa_creation_lock(self, i_locked: bool) -> None:
        return self.fta_setting_att.SetNoaCreationLock(i_locked)

    def set_non_semantic_always_upgrade_general_tol_lock(self, i_locked: bool) -> None:
        return self.fta_setting_att.SetNonSemanticAllwaysUpgradeGeneralTolLock(i_locked)

    def set_non_semantic_always_upgrade_lock(self, i_locked: bool) -> None:
        return self.fta_setting_att.SetNonSemanticAllwaysUpgradeLock(i_locked)

    def set_non_semantic_dim_allowed_lock(self, i_locked: bool) -> None:
        return self.fta_setting_att.SetNonSemanticDimAllowedLock(i_locked)

    def set_non_semantic_marked_lock(self, i_locked: bool) -> None:
        return self.fta_setting_att.SetNonSemanticMarkedLock(i_locked)

    def set_non_semantic_tol_allowed_lock(self, i_locked: bool) -> None:
        return self.fta_setting_att.SetNonSemanticTolAllowedLock(i_locked)

    def set_parameters_in_tree_lock(self, i_locked: bool) -> None:
        return self.fta_setting_att.SetParametersInTreeLock(i_locked)

    def set_rotation_snap_angle_lock(self, i_locked: bool) -> None:
        return self.fta_setting_att.SetRotationSnapAngleLock(i_locked)

    def set_rotation_snap_auto_lock(self, i_locked: bool) -> None:
        return self.fta_setting_att.SetRotationSnapAutoLock(i_locked)

    def set_sect_pattern_lock(self, i_locked: bool) -> None:
        return self.fta_setting_att.SetSectPatternLock(i_locked)

    def set_select_published_geometry_lock(self, i_locked: bool) -> None:
        return self.fta_setting_att.SetSelectPublishedGeometryLock(i_locked)

    def set_shifted_profile_lock(self, i_locked: bool) -> None:
        return self.fta_setting_att.SetShiftedProfileLock(i_locked)

    def set_true_dimension_color(
        self, i_value_r: int, i_value_g: int, i_value_b: int
    ) -> None:
        return self.fta_setting_att.SetTrueDimensionColor(
            i_value_r, i_value_g, i_value_b
        )

    def set_true_dimension_color_lock(self, i_locked: bool) -> None:
        return self.fta_setting_att.SetTrueDimensionColorLock(i_locked)

    def set_true_dimension_lock(self, i_locked: bool) -> None:
        return self.fta_setting_att.SetTrueDimensionLock(i_locked)

    def __repr__(self):
        return f'FtaSettingAtt(name="{self.name}")'
