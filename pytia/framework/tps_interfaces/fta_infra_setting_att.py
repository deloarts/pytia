from pytia.framework.system_interfaces.setting_controller import SettingController


class FtaInfraSettingAtt(SettingController):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.fta_infra_setting_att = com_object

    @property
    def allow_distortions(self) -> bool:
        return self.fta_infra_setting_att.AllowDistortions

    @allow_distortions.setter
    def allow_distortions(self, value: bool):
        self.fta_infra_setting_att.AllowDistortions = value

    @property
    def grid_display(self) -> bool:
        return self.fta_infra_setting_att.GridDisplay

    @grid_display.setter
    def grid_display(self, value: bool):
        self.fta_infra_setting_att.GridDisplay = value

    @property
    def grid_primary_spacing(self) -> float:
        return self.fta_infra_setting_att.GridPrimarySpacing

    @grid_primary_spacing.setter
    def grid_primary_spacing(self, value: float):
        self.fta_infra_setting_att.GridPrimarySpacing = value

    @property
    def grid_secondary_step(self) -> int:
        return self.fta_infra_setting_att.GridSecondaryStep

    @grid_secondary_step.setter
    def grid_secondary_step(self, value: int):
        self.fta_infra_setting_att.GridSecondaryStep = value

    @property
    def grid_snap_point(self) -> bool:
        return self.fta_infra_setting_att.GridSnapPoint

    @grid_snap_point.setter
    def grid_snap_point(self, value: bool):
        self.fta_infra_setting_att.GridSnapPoint = value

    @property
    def grid_v_primary_spacing(self) -> float:
        return self.fta_infra_setting_att.GridVPrimarySpacing

    @grid_v_primary_spacing.setter
    def grid_v_primary_spacing(self, value: float):
        self.fta_infra_setting_att.GridVPrimarySpacing = value

    @property
    def grid_v_secondary_step(self) -> int:
        return self.fta_infra_setting_att.GridVSecondaryStep

    @grid_v_secondary_step.setter
    def grid_v_secondary_step(self, value: int):
        self.fta_infra_setting_att.GridVSecondaryStep = value

    @property
    def leader_associativity(self) -> int:
        return self.fta_infra_setting_att.LeaderAssociativity

    @leader_associativity.setter
    def leader_associativity(self, value: int):
        self.fta_infra_setting_att.LeaderAssociativity = value

    @property
    def man_ref_siz(self) -> float:
        return self.fta_infra_setting_att.ManRefSiz

    @man_ref_siz.setter
    def man_ref_siz(self, value: float):
        self.fta_infra_setting_att.ManRefSiz = value

    @property
    def man_zoo_cap(self) -> bool:
        return self.fta_infra_setting_att.ManZooCap

    @man_zoo_cap.setter
    def man_zoo_cap(self, value: bool):
        self.fta_infra_setting_att.ManZooCap = value

    @property
    def move_after_creation(self) -> bool:
        return self.fta_infra_setting_att.MoveAfterCreation

    @move_after_creation.setter
    def move_after_creation(self, value: bool):
        self.fta_infra_setting_att.MoveAfterCreation = value

    @property
    def save_in_cgr(self) -> bool:
        return self.fta_infra_setting_att.SaveInCGR

    @save_in_cgr.setter
    def save_in_cgr(self, value: bool):
        self.fta_infra_setting_att.SaveInCGR = value

    @property
    def standard(self) -> str:
        return self.fta_infra_setting_att.Standard

    @standard.setter
    def standard(self, value: str):
        self.fta_infra_setting_att.Standard = value

    @property
    def under_feature(self) -> bool:
        return self.fta_infra_setting_att.UnderFeature

    @under_feature.setter
    def under_feature(self, value: bool):
        self.fta_infra_setting_att.UnderFeature = value

    @property
    def under_set(self) -> bool:
        return self.fta_infra_setting_att.UnderSet

    @under_set.setter
    def under_set(self, value: bool):
        self.fta_infra_setting_att.UnderSet = value

    @property
    def under_view(self) -> bool:
        return self.fta_infra_setting_att.UnderView

    @under_view.setter
    def under_view(self, value: bool):
        self.fta_infra_setting_att.UnderView = value

    @property
    def view_associativity(self) -> bool:
        return self.fta_infra_setting_att.ViewAssociativity

    @view_associativity.setter
    def view_associativity(self, value: bool):
        self.fta_infra_setting_att.ViewAssociativity = value

    @property
    def view_profile(self) -> bool:
        return self.fta_infra_setting_att.ViewProfile

    @view_profile.setter
    def view_profile(self, value: bool):
        self.fta_infra_setting_att.ViewProfile = value

    @property
    def view_referential(self) -> bool:
        return self.fta_infra_setting_att.ViewReferential

    @view_referential.setter
    def view_referential(self, value: bool):
        self.fta_infra_setting_att.ViewReferential = value

    @property
    def view_referential_zoomable(self) -> bool:
        return self.fta_infra_setting_att.ViewReferentialZoomable

    @view_referential_zoomable.setter
    def view_referential_zoomable(self, value: bool):
        self.fta_infra_setting_att.ViewReferentialZoomable = value

    def get_allow_distortions_info(self, admin_level: str, o_locked: str) -> bool:
        return self.fta_infra_setting_att.GetAllowDistortionsInfo(admin_level, o_locked)

    def get_grid_display_info(self, admin_level: str, o_locked: str) -> bool:
        return self.fta_infra_setting_att.GetGridDisplayInfo(admin_level, o_locked)

    def get_grid_primary_spacing_info(self, admin_level: str, o_locked: str) -> bool:
        return self.fta_infra_setting_att.GetGridPrimarySpacingInfo(
            admin_level, o_locked
        )

    def get_grid_secondary_step_info(self, admin_level: str, o_locked: str) -> bool:
        return self.fta_infra_setting_att.GetGridSecondaryStepInfo(
            admin_level, o_locked
        )

    def get_grid_snap_point_info(self, admin_level: str, o_locked: str) -> bool:
        return self.fta_infra_setting_att.GetGridSnapPointInfo(admin_level, o_locked)

    def get_grid_v_primary_spacing_info(self, admin_level: str, o_locked: str) -> bool:
        return self.fta_infra_setting_att.GetGridVPrimarySpacingInfo(
            admin_level, o_locked
        )

    def get_grid_v_secondary_step_info(self, admin_level: str, o_locked: str) -> bool:
        return self.fta_infra_setting_att.GetGridVSecondaryStepInfo(
            admin_level, o_locked
        )

    def get_leader_associativity_info(self, admin_level: str, o_locked: str) -> bool:
        return self.fta_infra_setting_att.GetLeaderAssociativityInfo(
            admin_level, o_locked
        )

    def get_man_ref_size_info(self, admin_level: str, o_locked: str) -> bool:
        return self.fta_infra_setting_att.GetManRefSizInfo(admin_level, o_locked)

    def get_man_zoo_cap_info(self, admin_level: str, o_locked: str) -> bool:
        return self.fta_infra_setting_att.GetManZooCapInfo(admin_level, o_locked)

    def get_move_after_creation_info(self, admin_level: str, o_locked: str) -> bool:
        return self.fta_infra_setting_att.GetMoveAfterCreationInfo(
            admin_level, o_locked
        )

    def get_save_in_cgr_info(self, admin_level: str, o_locked: str) -> bool:
        return self.fta_infra_setting_att.GetSaveInCGRInfo(admin_level, o_locked)

    def get_standard_info(self, admin_level: str, o_locked: str) -> bool:
        return self.fta_infra_setting_att.GetStandardInfo(admin_level, o_locked)

    def get_under_feature_info(self, admin_level: str, o_locked: str) -> bool:
        return self.fta_infra_setting_att.GetUnderFeatureInfo(admin_level, o_locked)

    def get_under_set_info(self, admin_level: str, o_locked: str) -> bool:
        return self.fta_infra_setting_att.GetUnderSetInfo(admin_level, o_locked)

    def get_under_view_info(self, admin_level: str, o_locked: str) -> bool:
        return self.fta_infra_setting_att.GetUnderViewInfo(admin_level, o_locked)

    def get_view_associativity_info(self, admin_level: str, o_locked: str) -> bool:
        return self.fta_infra_setting_att.GetViewAssociativityInfo(
            admin_level, o_locked
        )

    def get_view_profile_info(self, admin_level: str, o_locked: str) -> bool:
        return self.fta_infra_setting_att.GetViewProfileInfo(admin_level, o_locked)

    def get_view_referential_info(self, admin_level: str, o_locked: str) -> bool:
        return self.fta_infra_setting_att.GetViewReferentialInfo(admin_level, o_locked)

    def get_view_referential_zoomable_info(
        self, admin_level: str, o_locked: str
    ) -> bool:
        return self.fta_infra_setting_att.GetViewReferentialZoomableInfo(
            admin_level, o_locked
        )

    def set_allow_distortions_lock(self, i_locked: bool) -> None:
        return self.fta_infra_setting_att.SetAllowDistortionsLock(i_locked)

    def set_grid_display_lock(self, i_locked: bool) -> None:
        return self.fta_infra_setting_att.SetGridDisplayLock(i_locked)

    def set_grid_primary_spacing_lock(self, i_locked: bool) -> None:
        return self.fta_infra_setting_att.SetGridPrimarySpacingLock(i_locked)

    def set_grid_secondary_step_lock(self, i_locked: bool) -> None:
        return self.fta_infra_setting_att.SetGridSecondaryStepLock(i_locked)

    def set_grid_snap_point_lock(self, i_locked: bool) -> None:
        return self.fta_infra_setting_att.SetGridSnapPointLock(i_locked)

    def set_grid_v_primary_spacing_lock(self, i_locked: bool) -> None:
        return self.fta_infra_setting_att.SetGridVPrimarySpacingLock(i_locked)

    def set_grid_v_secondary_step_lock(self, i_locked: bool) -> None:
        return self.fta_infra_setting_att.SetGridVSecondaryStepLock(i_locked)

    def set_leader_associativity_lock(self, i_locked: bool) -> None:
        return self.fta_infra_setting_att.SetLeaderAssociativityLock(i_locked)

    def set_man_ref_size_lock(self, i_locked: bool) -> None:
        return self.fta_infra_setting_att.SetManRefSizLock(i_locked)

    def set_man_zoo_cap_lock(self, i_locked: bool) -> None:
        return self.fta_infra_setting_att.SetManZooCapLock(i_locked)

    def set_move_after_creation_lock(self, i_locked: bool) -> None:
        return self.fta_infra_setting_att.SetMoveAfterCreationLock(i_locked)

    def set_save_in_cgr_lock(self, i_locked: bool) -> None:
        return self.fta_infra_setting_att.SetSaveInCGRLock(i_locked)

    def set_standard_lock(self, i_locked: bool) -> None:
        return self.fta_infra_setting_att.SetStandardLock(i_locked)

    def set_under_feature_lock(self, i_locked: bool) -> None:
        return self.fta_infra_setting_att.SetUnderFeatureLock(i_locked)

    def set_under_set_lock(self, i_locked: bool) -> None:
        return self.fta_infra_setting_att.SetUnderSetLock(i_locked)

    def set_under_view_lock(self, i_locked: bool) -> None:
        return self.fta_infra_setting_att.SetUnderViewLock(i_locked)

    def set_view_associativity_lock(self, i_locked: bool) -> None:
        return self.fta_infra_setting_att.SetViewAssociativityLock(i_locked)

    def set_view_profile_lock(self, i_locked: bool) -> None:
        return self.fta_infra_setting_att.SetViewProfileLock(i_locked)

    def set_view_referential_lock(self, i_locked: bool) -> None:
        return self.fta_infra_setting_att.SetViewReferentialLock(i_locked)

    def set_view_referential_zoomable_lock(self, i_locked: bool) -> None:
        return self.fta_infra_setting_att.SetViewReferentialZoomableLock(i_locked)

    def __repr__(self):
        return f'FtaInfraSettingAtt(name="{self.name}")'
