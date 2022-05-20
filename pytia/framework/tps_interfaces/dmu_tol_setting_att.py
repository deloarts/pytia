from pytia.framework.system_interfaces.setting_controller import SettingController


class DmuTolSettingAtt(SettingController):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.dmu_tol_setting_att = com_object

    @property
    def design_mode(self) -> bool:
        return self.dmu_tol_setting_att.DesignMode

    @design_mode.setter
    def design_mode(self, value: bool):
        self.dmu_tol_setting_att.DesignMode = value

    @property
    def prev_area(self) -> bool:
        return self.dmu_tol_setting_att.PrevArea

    @prev_area.setter
    def prev_area(self, value: bool):
        self.dmu_tol_setting_att.PrevArea = value

    @property
    def save_cgr(self) -> bool:
        return self.dmu_tol_setting_att.SaveCGR

    @save_cgr.setter
    def save_cgr(self, value: bool):
        self.dmu_tol_setting_att.SaveCGR = value

    @property
    def sect_pattern(self) -> bool:
        return self.dmu_tol_setting_att.SectPattern

    @sect_pattern.setter
    def sect_pattern(self, value: bool):
        self.dmu_tol_setting_att.SectPattern = value

    def get_design_mode_info(self, admin_level: str, o_locked: str) -> bool:
        return self.dmu_tol_setting_att.GetDesignModeInfo(admin_level, o_locked)

    def get_prev_area_info(self, admin_level: str, o_locked: str) -> bool:
        return self.dmu_tol_setting_att.GetPrevAreaInfo(admin_level, o_locked)

    def get_related_colours(
        self, o_related_r: int, o_related_g: int, o_related_b: int
    ) -> None:
        return self.dmu_tol_setting_att.GetRelatedColors(
            o_related_r, o_related_g, o_related_b
        )

    def get_related_colours_info(self, admin_level: str, o_locked: str) -> bool:
        return self.dmu_tol_setting_att.GetRelatedColorsInfo(admin_level, o_locked)

    def get_save_cgr_info(self, admin_level: str, o_locked: str) -> bool:
        return self.dmu_tol_setting_att.GetSaveCGRInfo(admin_level, o_locked)

    def get_sect_pattern_info(self, admin_level: str, o_locked: str) -> bool:
        return self.dmu_tol_setting_att.GetSectPatternInfo(admin_level, o_locked)

    def set_design_mode_lock(self, i_locked: bool) -> None:
        return self.dmu_tol_setting_att.SetDesignModeLock(i_locked)

    def set_prev_area_lock(self, i_locked: bool) -> None:
        return self.dmu_tol_setting_att.SetPrevAreaLock(i_locked)

    def set_related_colours(
        self, i_related_r: int, i_related_g: int, i_related_b: int
    ) -> None:
        return self.dmu_tol_setting_att.SetRelatedColors(
            i_related_r, i_related_g, i_related_b
        )

    def set_related_colours_lock(self, i_locked: bool) -> None:
        return self.dmu_tol_setting_att.SetRelatedColorsLock(i_locked)

    def set_save_cgr_lock(self, i_locked: bool) -> None:
        return self.dmu_tol_setting_att.SetSaveCGRLock(i_locked)

    def set_sect_pattern_lock(self, i_locked: bool) -> None:
        return self.dmu_tol_setting_att.SetSectPatternLock(i_locked)

    def __repr__(self):
        return f'DmuTolSettingAtt(name="{self.name}")'
