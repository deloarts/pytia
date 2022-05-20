from pytia.framework.system_interfaces.setting_controller import SettingController


class N4DNavigatorSettingAtt(SettingController):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.n_4d_navigator_setting_att = com_object

    @property
    def clearance_voxel(self) -> float:
        return self.n_4d_navigator_setting_att.ClearanceVoxel

    @clearance_voxel.setter
    def clearance_voxel(self, value: float):
        self.n_4d_navigator_setting_att.ClearanceVoxel = value

    @property
    def dmu_clash_preview(self) -> bool:
        return self.n_4d_navigator_setting_att.DMUClashPreview

    @dmu_clash_preview.setter
    def dmu_clash_preview(self, value: bool):
        self.n_4d_navigator_setting_att.DMUClashPreview = value

    @property
    def dmu_cut_3d_preview(self) -> bool:
        return self.n_4d_navigator_setting_att.DMUCut3DPreview

    @dmu_cut_3d_preview.setter
    def dmu_cut_3d_preview(self, value: bool):
        self.n_4d_navigator_setting_att.DMUCut3DPreview = value

    @property
    def dmu_distance_preview(self) -> bool:
        return self.n_4d_navigator_setting_att.DMUDistancePreview

    @dmu_distance_preview.setter
    def dmu_distance_preview(self, value: bool):
        self.n_4d_navigator_setting_att.DMUDistancePreview = value

    @property
    def dmu_free_space_preview(self) -> bool:
        return self.n_4d_navigator_setting_att.DMUFreeSpacePreview

    @dmu_free_space_preview.setter
    def dmu_free_space_preview(self, value: bool):
        self.n_4d_navigator_setting_att.DMUFreeSpacePreview = value

    @property
    def dmu_group_preview(self) -> bool:
        return self.n_4d_navigator_setting_att.DMUGroupPreview

    @dmu_group_preview.setter
    def dmu_group_preview(self, value: bool):
        self.n_4d_navigator_setting_att.DMUGroupPreview = value

    @property
    def dmu_group_preview_hidden_objects_display_mode(self) -> int:
        return self.n_4d_navigator_setting_att.DMUGroupPreviewHiddenObjectsDisplayMode

    @dmu_group_preview_hidden_objects_display_mode.setter
    def dmu_group_preview_hidden_objects_display_mode(self, value: int):
        self.n_4d_navigator_setting_att.DMUGroupPreviewHiddenObjectsDisplayMode = value

    @property
    def dmu_group_preview_hidden_objects_low_int(self) -> bool:
        return self.n_4d_navigator_setting_att.DMUGroupPreviewHiddenObjectsLowInt

    @dmu_group_preview_hidden_objects_low_int.setter
    def dmu_group_preview_hidden_objects_low_int(self, value: bool):
        self.n_4d_navigator_setting_att.DMUGroupPreviewHiddenObjectsLowInt = value

    @property
    def dmu_group_preview_hidden_objects_opacity(self) -> int:
        return self.n_4d_navigator_setting_att.DMUGroupPreviewHiddenObjectsOpacity

    @dmu_group_preview_hidden_objects_opacity.setter
    def dmu_group_preview_hidden_objects_opacity(self, value: int):
        self.n_4d_navigator_setting_att.DMUGroupPreviewHiddenObjectsOpacity = value

    @property
    def dmu_group_preview_hidden_objects_pick(self) -> bool:
        return self.n_4d_navigator_setting_att.DMUGroupPreviewHiddenObjectsPick

    @dmu_group_preview_hidden_objects_pick.setter
    def dmu_group_preview_hidden_objects_pick(self, value: bool):
        self.n_4d_navigator_setting_att.DMUGroupPreviewHiddenObjectsPick = value

    @property
    def dmu_merger_preview(self) -> bool:
        return self.n_4d_navigator_setting_att.DMUMergerPreview

    @dmu_merger_preview.setter
    def dmu_merger_preview(self, value: bool):
        self.n_4d_navigator_setting_att.DMUMergerPreview = value

    @property
    def dmu_offset_preview(self) -> bool:
        return self.n_4d_navigator_setting_att.DMUOffsetPreview

    @dmu_offset_preview.setter
    def dmu_offset_preview(self, value: bool):
        self.n_4d_navigator_setting_att.DMUOffsetPreview = value

    @property
    def dmu_review_name(self) -> str:
        return self.n_4d_navigator_setting_att.DMUReviewName

    @dmu_review_name.setter
    def dmu_review_name(self, value: str):
        self.n_4d_navigator_setting_att.DMUReviewName = value

    @property
    def dmu_section_preview(self) -> bool:
        return self.n_4d_navigator_setting_att.DMUSectionPreview

    @dmu_section_preview.setter
    def dmu_section_preview(self, value: bool):
        self.n_4d_navigator_setting_att.DMUSectionPreview = value

    @property
    def dmu_shuttle_preview(self) -> bool:
        return self.n_4d_navigator_setting_att.DMUShuttlePreview

    @dmu_shuttle_preview.setter
    def dmu_shuttle_preview(self, value: bool):
        self.n_4d_navigator_setting_att.DMUShuttlePreview = value

    @property
    def dmu_silhouette_preview(self) -> bool:
        return self.n_4d_navigator_setting_att.DMUSilhouettePreview

    @dmu_silhouette_preview.setter
    def dmu_silhouette_preview(self, value: bool):
        self.n_4d_navigator_setting_att.DMUSilhouettePreview = value

    @property
    def dmu_simplif_preview(self) -> bool:
        return self.n_4d_navigator_setting_att.DMUSimplifPreview

    @dmu_simplif_preview.setter
    def dmu_simplif_preview(self, value: bool):
        self.n_4d_navigator_setting_att.DMUSimplifPreview = value

    @property
    def dmu_swept_vol_preview(self) -> bool:
        return self.n_4d_navigator_setting_att.DMUSweptVolPreview

    @dmu_swept_vol_preview.setter
    def dmu_swept_vol_preview(self, value: bool):
        self.n_4d_navigator_setting_att.DMUSweptVolPreview = value

    @property
    def dmu_thickness_preview(self) -> bool:
        return self.n_4d_navigator_setting_att.DMUThicknessPreview

    @dmu_thickness_preview.setter
    def dmu_thickness_preview(self, value: bool):
        self.n_4d_navigator_setting_att.DMUThicknessPreview = value

    @property
    def dmu_vibration_vol_preview(self) -> bool:
        return self.n_4d_navigator_setting_att.DMUVibrationVolPreview

    @dmu_vibration_vol_preview.setter
    def dmu_vibration_vol_preview(self, value: bool):
        self.n_4d_navigator_setting_att.DMUVibrationVolPreview = value

    @property
    def dmu_wrapping_preview(self) -> bool:
        return self.n_4d_navigator_setting_att.DMUWrappingPreview

    @dmu_wrapping_preview.setter
    def dmu_wrapping_preview(self, value: bool):
        self.n_4d_navigator_setting_att.DMUWrappingPreview = value

    @property
    def force_clearance_voxel(self) -> bool:
        return self.n_4d_navigator_setting_att.ForceClearanceVoxel

    @force_clearance_voxel.setter
    def force_clearance_voxel(self, value: bool):
        self.n_4d_navigator_setting_att.ForceClearanceVoxel = value

    @property
    def force_voxel(self) -> bool:
        return self.n_4d_navigator_setting_att.ForceVoxel

    @force_voxel.setter
    def force_voxel(self, value: bool):
        self.n_4d_navigator_setting_att.ForceVoxel = value

    @property
    def insert_level(self) -> bool:
        return self.n_4d_navigator_setting_att.InsertLevel

    @insert_level.setter
    def insert_level(self, value: bool):
        self.n_4d_navigator_setting_att.InsertLevel = value

    @property
    def insert_mode(self) -> int:
        return self.n_4d_navigator_setting_att.InsertMode

    @insert_mode.setter
    def insert_mode(self, value: int):
        self.n_4d_navigator_setting_att.InsertMode = value

    @property
    def marker_2d_auto_naming(self) -> bool:
        return self.n_4d_navigator_setting_att.Marker2DAutoNaming

    @marker_2d_auto_naming.setter
    def marker_2d_auto_naming(self, value: bool):
        self.n_4d_navigator_setting_att.Marker2DAutoNaming = value

    @property
    def marker_3d_auto_naming(self) -> bool:
        return self.n_4d_navigator_setting_att.Marker3DAutoNaming

    @marker_3d_auto_naming.setter
    def marker_3d_auto_naming(self, value: bool):
        self.n_4d_navigator_setting_att.Marker3DAutoNaming = value

    @property
    def marker_auto_update(self) -> bool:
        return self.n_4d_navigator_setting_att.MarkerAutoUpdate

    @marker_auto_update.setter
    def marker_auto_update(self, value: bool):
        self.n_4d_navigator_setting_att.MarkerAutoUpdate = value

    @property
    def marker_defaults_dashed(self) -> int:
        return self.n_4d_navigator_setting_att.MarkerDefaultsDashed

    @marker_defaults_dashed.setter
    def marker_defaults_dashed(self, value: int):
        self.n_4d_navigator_setting_att.MarkerDefaultsDashed = value

    @property
    def marker_defaults_font(self) -> str:
        return self.n_4d_navigator_setting_att.MarkerDefaultsFont

    @marker_defaults_font.setter
    def marker_defaults_font(self, value: str):
        self.n_4d_navigator_setting_att.MarkerDefaultsFont = value

    @property
    def marker_defaults_size(self) -> int:
        return self.n_4d_navigator_setting_att.MarkerDefaultsSize

    @marker_defaults_size.setter
    def marker_defaults_size(self, value: int):
        self.n_4d_navigator_setting_att.MarkerDefaultsSize = value

    @property
    def marker_defaults_weight(self) -> int:
        return self.n_4d_navigator_setting_att.MarkerDefaultsWeight

    @marker_defaults_weight.setter
    def marker_defaults_weight(self, value: int):
        self.n_4d_navigator_setting_att.MarkerDefaultsWeight = value

    @property
    def marker_text_dashed(self) -> int:
        return self.n_4d_navigator_setting_att.MarkerTextDashed

    @marker_text_dashed.setter
    def marker_text_dashed(self, value: int):
        self.n_4d_navigator_setting_att.MarkerTextDashed = value

    @property
    def marker_text_weight(self) -> int:
        return self.n_4d_navigator_setting_att.MarkerTextWeight

    @marker_text_weight.setter
    def marker_text_weight(self, value: int):
        self.n_4d_navigator_setting_att.MarkerTextWeight = value

    @property
    def num_url_name(self) -> bool:
        return self.n_4d_navigator_setting_att.NumUrlName

    @num_url_name.setter
    def num_url_name(self, value: bool):
        self.n_4d_navigator_setting_att.NumUrlName = value

    @property
    def publish_auto_launch_browser(self) -> bool:
        return self.n_4d_navigator_setting_att.PublishAutoLaunchBrowser

    @publish_auto_launch_browser.setter
    def publish_auto_launch_browser(self, value: bool):
        self.n_4d_navigator_setting_att.PublishAutoLaunchBrowser = value

    def get_clearance_voxel_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.n_4d_navigator_setting_att.GetClearanceVoxelInfo(
            io_admin_level, io_locked
        )

    def get_dmu_clash_preview_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.n_4d_navigator_setting_att.GetDMUClashPreviewInfo(
            io_admin_level, io_locked
        )

    def get_dmu_cut_3d_preview_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.n_4d_navigator_setting_att.GetDMUCut3DPreviewInfo(
            io_admin_level, io_locked
        )

    def get_dmu_distance_preview_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.n_4d_navigator_setting_att.GetDMUDistancePreviewInfo(
            io_admin_level, io_locked
        )

    def get_dmu_free_space_preview_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.n_4d_navigator_setting_att.GetDMUFreeSpacePreviewInfo(
            io_admin_level, io_locked
        )

    def get_dmu_group_preview_hidden_objects_color(
        self, o_red: int, o_green: int, o_blue: int
    ) -> None:
        return self.n_4d_navigator_setting_att.GetDMUGroupPreviewHiddenObjectsColor(
            o_red, o_green, o_blue
        )

    def get_dmu_group_preview_hidden_objects_color_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.n_4d_navigator_setting_att.GetDMUGroupPreviewHiddenObjectsColorInfo(
            io_admin_level, io_locked
        )

    def get_dmu_group_preview_hidden_objects_display_mode_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.n_4d_navigator_setting_att.GetDMUGroupPreviewHiddenObjectsDisplayModeInfo(
            io_admin_level, io_locked
        )

    def get_dmu_group_preview_hidden_objects_low_int_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return (
            self.n_4d_navigator_setting_att.GetDMUGroupPreviewHiddenObjectsLowIntInfo(
                io_admin_level, io_locked
            )
        )

    def get_dmu_group_preview_hidden_objects_opacity_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return (
            self.n_4d_navigator_setting_att.GetDMUGroupPreviewHiddenObjectsOpacityInfo(
                io_admin_level, io_locked
            )
        )

    def get_dmu_group_preview_hidden_objects_pick_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.n_4d_navigator_setting_att.GetDMUGroupPreviewHiddenObjectsPickInfo(
            io_admin_level, io_locked
        )

    def get_dmu_group_preview_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.n_4d_navigator_setting_att.GetDMUGroupPreviewInfo(
            io_admin_level, io_locked
        )

    def get_dmu_merger_preview_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.n_4d_navigator_setting_att.GetDMUMergerPreviewInfo(
            io_admin_level, io_locked
        )

    def get_dmu_offset_preview_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.n_4d_navigator_setting_att.GetDMUOffsetPreviewInfo(
            io_admin_level, io_locked
        )

    def get_dmu_review_name_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.n_4d_navigator_setting_att.GetDMUReviewNameInfo(
            io_admin_level, io_locked
        )

    def get_dmu_section_preview_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.n_4d_navigator_setting_att.GetDMUSectionPreviewInfo(
            io_admin_level, io_locked
        )

    def get_dmu_shuttle_preview_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.n_4d_navigator_setting_att.GetDMUShuttlePreviewInfo(
            io_admin_level, io_locked
        )

    def get_dmu_silhouette_preview_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.n_4d_navigator_setting_att.GetDMUSilhouettePreviewInfo(
            io_admin_level, io_locked
        )

    def get_dmu_simplif_preview_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.n_4d_navigator_setting_att.GetDMUSimplifPreviewInfo(
            io_admin_level, io_locked
        )

    def get_dmu_swept_vol_preview_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.n_4d_navigator_setting_att.GetDMUSweptVolPreviewInfo(
            io_admin_level, io_locked
        )

    def get_dmu_thickness_preview_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.n_4d_navigator_setting_att.GetDMUThicknessPreviewInfo(
            io_admin_level, io_locked
        )

    def get_dmu_vibration_vol_preview_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.n_4d_navigator_setting_att.GetDMUVibrationVolPreviewInfo(
            io_admin_level, io_locked
        )

    def get_dmu_wrapping_preview_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.n_4d_navigator_setting_att.GetDMUWrappingPreviewInfo(
            io_admin_level, io_locked
        )

    def get_force_clearance_voxel_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.n_4d_navigator_setting_att.GetForceClearanceVoxelInfo(
            io_admin_level, io_locked
        )

    def get_force_voxel_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.n_4d_navigator_setting_att.GetForceVoxelInfo(
            io_admin_level, io_locked
        )

    def get_insert_level_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.n_4d_navigator_setting_att.GetInsertLevelInfo(
            io_admin_level, io_locked
        )

    def get_insert_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.n_4d_navigator_setting_att.GetInsertModeInfo(
            io_admin_level, io_locked
        )

    def get_marker_2d_auto_naming_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.n_4d_navigator_setting_att.GetMarker2DAutoNamingInfo(
            io_admin_level, io_locked
        )

    def get_marker_3d_auto_naming_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.n_4d_navigator_setting_att.GetMarker3DAutoNamingInfo(
            io_admin_level, io_locked
        )

    def get_marker_auto_update_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.n_4d_navigator_setting_att.GetMarkerAutoUpdateInfo(
            io_admin_level, io_locked
        )

    def get_marker_defaults_color(self, o_red: int, o_green: int, o_blue: int) -> None:
        return self.n_4d_navigator_setting_att.GetMarkerDefaultsColor(
            o_red, o_green, o_blue
        )

    def get_marker_defaults_color_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.n_4d_navigator_setting_att.GetMarkerDefaultsColorInfo(
            io_admin_level, io_locked
        )

    def get_marker_defaults_dashed_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.n_4d_navigator_setting_att.GetMarkerDefaultsDashedInfo(
            io_admin_level, io_locked
        )

    def get_marker_defaults_font_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.n_4d_navigator_setting_att.GetMarkerDefaultsFontInfo(
            io_admin_level, io_locked
        )

    def get_marker_defaults_size_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.n_4d_navigator_setting_att.GetMarkerDefaultsSizeInfo(
            io_admin_level, io_locked
        )

    def get_marker_defaults_weight_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.n_4d_navigator_setting_att.GetMarkerDefaultsWeightInfo(
            io_admin_level, io_locked
        )

    def get_marker_text_color(self, o_red: int, o_green: int, o_blue: int) -> None:
        return self.n_4d_navigator_setting_att.GetMarkerTextColor(
            o_red, o_green, o_blue
        )

    def get_marker_text_color_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.n_4d_navigator_setting_att.GetMarkerTextColorInfo(
            io_admin_level, io_locked
        )

    def get_marker_text_dashed_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.n_4d_navigator_setting_att.GetMarkerTextDashedInfo(
            io_admin_level, io_locked
        )

    def get_marker_text_weight_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.n_4d_navigator_setting_att.GetMarkerTextWeightInfo(
            io_admin_level, io_locked
        )

    def get_num_url_name_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.n_4d_navigator_setting_att.GetNumUrlNameInfo(
            io_admin_level, io_locked
        )

    def get_publish_auto_launch_browser_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.n_4d_navigator_setting_att.GetPublishAutoLaunchBrowserInfo(
            io_admin_level, io_locked
        )

    def get_scene_defaults_color(self, o_r: int, o_g: int, o_b: int) -> None:
        return self.n_4d_navigator_setting_att.GetSceneDefaultsColor(o_r, o_g, o_b)

    def get_scene_defaults_color_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.n_4d_navigator_setting_att.GetSceneDefaultsColorInfo(
            io_admin_level, io_locked
        )

    def set_clearance_voxel_lock(self, i_locked: bool) -> None:
        return self.n_4d_navigator_setting_att.SetClearanceVoxelLock(i_locked)

    def set_dmu_clash_preview_lock(self, i_locked: bool) -> None:
        return self.n_4d_navigator_setting_att.SetDMUClashPreviewLock(i_locked)

    def set_dmu_cut_3d_preview_lock(self, i_locked: bool) -> None:
        return self.n_4d_navigator_setting_att.SetDMUCut3DPreviewLock(i_locked)

    def set_dmu_distance_preview_lock(self, i_locked: bool) -> None:
        return self.n_4d_navigator_setting_att.SetDMUDistancePreviewLock(i_locked)

    def set_dmu_free_space_preview_lock(self, i_locked: bool) -> None:
        return self.n_4d_navigator_setting_att.SetDMUFreeSpacePreviewLock(i_locked)

    def set_dmu_group_preview_hidden_objects_color(
        self, i_red: int, i_green: int, i_blue: int
    ) -> None:
        return self.n_4d_navigator_setting_att.SetDMUGroupPreviewHiddenObjectsColor(
            i_red, i_green, i_blue
        )

    def set_dmu_group_preview_hidden_objects_color_lock(self, i_locked: bool) -> None:
        return self.n_4d_navigator_setting_att.SetDMUGroupPreviewHiddenObjectsColorLock(
            i_locked
        )

    def set_dmu_group_preview_hidden_objects_display_mode_lock(
        self, i_locked: bool
    ) -> None:
        return self.n_4d_navigator_setting_att.SetDMUGroupPreviewHiddenObjectsDisplayModeLock(
            i_locked
        )

    def set_dmu_group_preview_hidden_objects_low_int_lock(self, i_locked: bool) -> None:
        return (
            self.n_4d_navigator_setting_att.SetDMUGroupPreviewHiddenObjectsLowIntLock(
                i_locked
            )
        )

    def set_dmu_group_preview_hidden_objects_opacity_lock(self, i_locked: bool) -> None:
        return (
            self.n_4d_navigator_setting_att.SetDMUGroupPreviewHiddenObjectsOpacityLock(
                i_locked
            )
        )

    def set_dmu_group_preview_hidden_objects_pick_lock(self, i_locked: bool) -> None:
        return self.n_4d_navigator_setting_att.SetDMUGroupPreviewHiddenObjectsPickLock(
            i_locked
        )

    def set_dmu_group_preview_lock(self, i_locked: bool) -> None:
        return self.n_4d_navigator_setting_att.SetDMUGroupPreviewLock(i_locked)

    def set_dmu_merger_preview_lock(self, i_locked: bool) -> None:
        return self.n_4d_navigator_setting_att.SetDMUMergerPreviewLock(i_locked)

    def set_dmu_offset_preview_lock(self, i_locked: bool) -> None:
        return self.n_4d_navigator_setting_att.SetDMUOffsetPreviewLock(i_locked)

    def set_dmu_review_name_lock(self, i_locked: bool) -> None:
        return self.n_4d_navigator_setting_att.SetDMUReviewNameLock(i_locked)

    def set_dmu_section_preview_lock(self, i_locked: bool) -> None:
        return self.n_4d_navigator_setting_att.SetDMUSectionPreviewLock(i_locked)

    def set_dmu_shuttle_preview_lock(self, i_locked: bool) -> None:
        return self.n_4d_navigator_setting_att.SetDMUShuttlePreviewLock(i_locked)

    def set_dmu_silhouette_preview_lock(self, i_locked: bool) -> None:
        return self.n_4d_navigator_setting_att.SetDMUSilhouettePreviewLock(i_locked)

    def set_dmu_simplif_preview_lock(self, i_locked: bool) -> None:
        return self.n_4d_navigator_setting_att.SetDMUSimplifPreviewLock(i_locked)

    def set_dmu_swept_vol_preview_lock(self, i_locked: bool) -> None:
        return self.n_4d_navigator_setting_att.SetDMUSweptVolPreviewLock(i_locked)

    def set_dmu_thickness_preview_lock(self, i_locked: bool) -> None:
        return self.n_4d_navigator_setting_att.SetDMUThicknessPreviewLock(i_locked)

    def set_dmu_vibration_vol_preview_lock(self, i_locked: bool) -> None:
        return self.n_4d_navigator_setting_att.SetDMUVibrationVolPreviewLock(i_locked)

    def set_dmu_wrapping_preview_lock(self, i_locked: bool) -> None:
        return self.n_4d_navigator_setting_att.SetDMUWrappingPreviewLock(i_locked)

    def set_force_clearance_voxel_lock(self, i_locked: bool) -> None:
        return self.n_4d_navigator_setting_att.SetForceClearanceVoxelLock(i_locked)

    def set_force_voxel_lock(self, i_locked: bool) -> None:
        return self.n_4d_navigator_setting_att.SetForceVoxelLock(i_locked)

    def set_insert_level_lock(self, i_locked: bool) -> None:
        return self.n_4d_navigator_setting_att.SetInsertLevelLock(i_locked)

    def set_insert_mode_lock(self, i_locked: bool) -> None:
        return self.n_4d_navigator_setting_att.SetInsertModeLock(i_locked)

    def set_marker_2d_auto_naming_lock(self, i_locked: bool) -> None:
        return self.n_4d_navigator_setting_att.SetMarker2DAutoNamingLock(i_locked)

    def set_marker_3d_auto_naming_lock(self, i_locked: bool) -> None:
        return self.n_4d_navigator_setting_att.SetMarker3DAutoNamingLock(i_locked)

    def set_marker_auto_update_lock(self, i_locked: bool) -> None:
        return self.n_4d_navigator_setting_att.SetMarkerAutoUpdateLock(i_locked)

    def set_marker_defaults_color(self, i_red: int, i_green: int, i_blue: int) -> None:
        return self.n_4d_navigator_setting_att.SetMarkerDefaultsColor(
            i_red, i_green, i_blue
        )

    def set_marker_defaults_color_lock(self, i_locked: bool) -> None:
        return self.n_4d_navigator_setting_att.SetMarkerDefaultsColorLock(i_locked)

    def set_marker_defaults_dashed_lock(self, i_locked: bool) -> None:
        return self.n_4d_navigator_setting_att.SetMarkerDefaultsDashedLock(i_locked)

    def set_marker_defaults_font_lock(self, i_locked: bool) -> None:
        return self.n_4d_navigator_setting_att.SetMarkerDefaultsFontLock(i_locked)

    def set_marker_defaults_size_lock(self, i_locked: bool) -> None:
        return self.n_4d_navigator_setting_att.SetMarkerDefaultsSizeLock(i_locked)

    def set_marker_defaults_weight_lock(self, i_locked: bool) -> None:
        return self.n_4d_navigator_setting_att.SetMarkerDefaultsWeightLock(i_locked)

    def set_marker_text_color(self, i_red: int, i_green: int, i_blue: int) -> None:
        return self.n_4d_navigator_setting_att.SetMarkerTextColor(
            i_red, i_green, i_blue
        )

    def set_marker_text_color_lock(self, i_locked: bool) -> None:
        return self.n_4d_navigator_setting_att.SetMarkerTextColorLock(i_locked)

    def set_marker_text_dashed_lock(self, i_locked: bool) -> None:
        return self.n_4d_navigator_setting_att.SetMarkerTextDashedLock(i_locked)

    def set_marker_text_weight_lock(self, i_locked: bool) -> None:
        return self.n_4d_navigator_setting_att.SetMarkerTextWeightLock(i_locked)

    def set_num_url_name_lock(self, i_locked: bool) -> None:
        return self.n_4d_navigator_setting_att.SetNumUrlNameLock(i_locked)

    def set_publish_auto_launch_browser_lock(self, i_locked: bool) -> None:
        return self.n_4d_navigator_setting_att.SetPublishAutoLaunchBrowserLock(i_locked)

    def set_scene_defaults_color(self, i_r: int, i_g: int, i_b: int) -> None:
        return self.n_4d_navigator_setting_att.SetSceneDefaultsColor(i_r, i_g, i_b)

    def set_scene_defaults_color_lock(self, i_locked: bool) -> None:
        return self.n_4d_navigator_setting_att.SetSceneDefaultsColorLock(i_locked)

    def __repr__(self):
        return f'N4DNavigatorSettingAtt(name="{self.name}")'
