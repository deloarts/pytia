from pytia.framework.system_interfaces.setting_controller import SettingController


class DraftingSettingAtt(SettingController):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.drafting_setting_att = com_object

    @property
    def create_new_sheet_from(self) -> int:
        return self.drafting_setting_att.CreateNewSheetFrom

    @create_new_sheet_from.setter
    def create_new_sheet_from(self, value: int):
        self.drafting_setting_att.CreateNewSheetFrom = value

    @property
    def display_reset_button(self) -> bool:
        return self.drafting_setting_att.DisplayResetButton

    @display_reset_button.setter
    def display_reset_button(self, value: bool):
        self.drafting_setting_att.DisplayResetButton = value

    @property
    def lock_user_default(self) -> bool:
        return self.drafting_setting_att.LockUserDefault

    @lock_user_default.setter
    def lock_user_default(self, value: bool):
        self.drafting_setting_att.LockUserDefault = value

    @property
    def prevent_background_access(self) -> bool:
        return self.drafting_setting_att.PreventBackgroundAccess

    @prevent_background_access.setter
    def prevent_background_access(self, value: bool):
        self.drafting_setting_att.PreventBackgroundAccess = value

    @property
    def prevent_dim_driving_3d_cstr(self) -> bool:
        return self.drafting_setting_att.PreventDimDriving3DCstr

    @prevent_dim_driving_3d_cstr.setter
    def prevent_dim_driving_3d_cstr(self, value: bool):
        self.drafting_setting_att.PreventDimDriving3DCstr = value

    @property
    def prevent_file_new(self) -> bool:
        return self.drafting_setting_att.PreventFileNew

    @prevent_file_new.setter
    def prevent_file_new(self, value: bool):
        self.drafting_setting_att.PreventFileNew = value

    @property
    def prevent_gen_view_style(self) -> bool:
        return self.drafting_setting_att.PreventGenViewStyle

    @prevent_gen_view_style.setter
    def prevent_gen_view_style(self, value: bool):
        self.drafting_setting_att.PreventGenViewStyle = value

    @property
    def prevent_set_as_default(self) -> bool:
        return self.drafting_setting_att.PreventSetAsDefault

    @prevent_set_as_default.setter
    def prevent_set_as_default(self, value: bool):
        self.drafting_setting_att.PreventSetAsDefault = value

    @property
    def prevent_switch_standard(self) -> bool:
        return self.drafting_setting_att.PreventSwitchStandard

    @prevent_switch_standard.setter
    def prevent_switch_standard(self, value: bool):
        self.drafting_setting_att.PreventSwitchStandard = value

    @property
    def prevent_true_dimension_creation(self) -> bool:
        return self.drafting_setting_att.PreventTrueDimensionCreation

    @prevent_true_dimension_creation.setter
    def prevent_true_dimension_creation(self, value: bool):
        self.drafting_setting_att.PreventTrueDimensionCreation = value

    @property
    def prevent_update_standard(self) -> bool:
        return self.drafting_setting_att.PreventUpdateStandard

    @prevent_update_standard.setter
    def prevent_update_standard(self, value: bool):
        self.drafting_setting_att.PreventUpdateStandard = value

    @property
    def prevent_view_geom_upgrade(self) -> bool:
        return self.drafting_setting_att.PreventViewGeomUpgrade

    @prevent_view_geom_upgrade.setter
    def prevent_view_geom_upgrade(self, value: bool):
        self.drafting_setting_att.PreventViewGeomUpgrade = value

    @property
    def use_style_create_objects(self) -> bool:
        return self.drafting_setting_att.UseStyleCreateObjects

    @use_style_create_objects.setter
    def use_style_create_objects(self, value: bool):
        self.drafting_setting_att.UseStyleCreateObjects = value

    def get_create_new_sheet_from_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.drafting_setting_att.GetCreateNewSheetFromInfo(
            io_admin_level, io_locked
        )

    def get_display_reset_button_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.drafting_setting_att.GetDisplayResetButtonInfo(
            io_admin_level, io_locked
        )

    def get_lock_user_default_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.drafting_setting_att.GetLockUserDefaultInfo(
            io_admin_level, io_locked
        )

    def get_prevent_background_access_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.drafting_setting_att.GetPreventBackgroundAccessInfo(
            io_admin_level, io_locked
        )

    def get_prevent_dim_driving_3d_cstr_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.drafting_setting_att.GetPreventDimDriving3DCstrInfo(
            io_admin_level, io_locked
        )

    def get_prevent_file_new_info(
        self, io_admin_level: str, io_locked: str, o_modified: bool
    ) -> None:
        return self.drafting_setting_att.GetPreventFileNewInfo(
            io_admin_level, io_locked, o_modified
        )

    def get_prevent_gen_view_style_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.drafting_setting_att.GetPreventGenViewStyleInfo(
            io_admin_level, io_locked
        )

    def get_prevent_set_as_default_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.drafting_setting_att.GetPreventSetAsDefaultInfo(
            io_admin_level, io_locked
        )

    def get_prevent_switch_standard_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.drafting_setting_att.GetPreventSwitchStandardInfo(
            io_admin_level, io_locked
        )

    def get_prevent_true_dimension_creation_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.drafting_setting_att.GetPreventTrueDimensionCreationInfo(
            io_admin_level, io_locked
        )

    def get_prevent_update_standard_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.drafting_setting_att.GetPreventUpdateStandardInfo(
            io_admin_level, io_locked
        )

    def get_prevent_view_geom_upgrade_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.drafting_setting_att.GetPreventViewGeomUpgradeInfo(
            io_admin_level, io_locked
        )

    def get_use_style_create_objects_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.drafting_setting_att.GetUseStyleCreateObjectsInfo(
            io_admin_level, io_locked
        )

    def set_create_new_sheet_from_lock(self, i_locked: bool) -> None:
        return self.drafting_setting_att.SetCreateNewSheetFromLock(i_locked)

    def set_display_reset_button_lock(self, i_locked: bool) -> None:
        return self.drafting_setting_att.SetDisplayResetButtonLock(i_locked)

    def set_lock_user_default_lock(self, i_locked: bool) -> None:
        return self.drafting_setting_att.SetLockUserDefaultLock(i_locked)

    def set_prevent_background_access_lock(self, i_locked: bool) -> None:
        return self.drafting_setting_att.SetPreventBackgroundAccessLock(i_locked)

    def set_prevent_dim_driving_3d_cstr_lock(self, i_locked: bool) -> None:
        return self.drafting_setting_att.SetPreventDimDriving3DCstrLock(i_locked)

    def set_prevent_file_new_lock(self, i_locked: bool) -> None:
        return self.drafting_setting_att.SetPreventFileNewLock(i_locked)

    def set_prevent_gen_view_style_lock(self, i_locked: bool) -> None:
        return self.drafting_setting_att.SetPreventGenViewStyleLock(i_locked)

    def set_prevent_set_as_default_lock(self, i_locked: bool) -> None:
        return self.drafting_setting_att.SetPreventSetAsDefaultLock(i_locked)

    def set_prevent_switch_standard_lock(self, i_locked: bool) -> None:
        return self.drafting_setting_att.SetPreventSwitchStandardLock(i_locked)

    def set_prevent_true_dimension_creation_lock(self, i_locked: bool) -> None:
        return self.drafting_setting_att.SetPreventTrueDimensionCreationLock(i_locked)

    def set_prevent_update_standard_lock(self, i_locked: bool) -> None:
        return self.drafting_setting_att.SetPreventUpdateStandardLock(i_locked)

    def set_prevent_view_geom_upgrade_lock(self, i_locked: bool) -> None:
        return self.drafting_setting_att.SetPreventViewGeomUpgradeLock(i_locked)

    def set_use_style_create_objects_lock(self, i_locked: bool) -> None:
        return self.drafting_setting_att.SetUseStyleCreateObjectsLock(i_locked)

    def __repr__(self):
        return f'DraftingSettingAtt(name="{self.name}")'
