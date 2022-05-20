from pytia.framework.system_interfaces.setting_controller import SettingController


class CgrAdhesionSettingAtt(SettingController):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.cgr_adhesion_setting_att = com_object

    @property
    def v4_v5_fdt(self) -> bool:
        return self.cgr_adhesion_setting_att.V4V5_FDT

    @v4_v5_fdt.setter
    def v4_v5_fdt(self, value: bool):
        self.cgr_adhesion_setting_att.V4V5_FDT = value

    @property
    def v4_model_comment_page(self) -> bool:
        return self.cgr_adhesion_setting_att.V4_Model_CommentPage

    @v4_model_comment_page.setter
    def v4_model_comment_page(self, value: bool):
        self.cgr_adhesion_setting_att.V4_Model_CommentPage = value

    @property
    def v4_model_ln_f(self) -> bool:
        return self.cgr_adhesion_setting_att.V4_Model_LnF

    @v4_model_ln_f.setter
    def v4_model_ln_f(self, value: bool):
        self.cgr_adhesion_setting_att.V4_Model_LnF = value

    @property
    def v5_spa(self) -> bool:
        return self.cgr_adhesion_setting_att.V5_SPA

    @v5_spa.setter
    def v5_spa(self, value: bool):
        self.cgr_adhesion_setting_att.V5_SPA = value

    @property
    def voxels(self) -> bool:
        return self.cgr_adhesion_setting_att.Voxels

    @voxels.setter
    def voxels(self, value: bool):
        self.cgr_adhesion_setting_att.Voxels = value

    def get_v4_v5_fdt_info(self, admin_level: str, o_locked: str) -> bool:
        return self.cgr_adhesion_setting_att.GetV4V5_FDTInfo(admin_level, o_locked)

    def get_v4_model_comment_page_info(self, admin_level: str, o_locked: str) -> bool:
        return self.cgr_adhesion_setting_att.GetV4_Model_CommentPageInfo(
            admin_level, o_locked
        )

    def get_v4_model_ln_f_info(self, admin_level: str, o_locked: str) -> bool:
        return self.cgr_adhesion_setting_att.GetV4_Model_LnFInfo(admin_level, o_locked)

    def get_v5_spa_info(self, admin_level: str, o_locked: str) -> bool:
        return self.cgr_adhesion_setting_att.GetV5_SPAInfo(admin_level, o_locked)

    def get_voxels_info(self, admin_level: str, o_locked: str) -> bool:
        return self.cgr_adhesion_setting_att.GetVoxelsInfo(admin_level, o_locked)

    def set_v4_v5_fdt_lock(self, i_locked: bool) -> None:
        return self.cgr_adhesion_setting_att.SetV4V5_FDTLock(i_locked)

    def set_v4_model_comment_page_lock(self, i_locked: bool) -> None:
        return self.cgr_adhesion_setting_att.SetV4_Model_CommentPageLock(i_locked)

    def set_v4_model_ln_f_lock(self, i_locked: bool) -> None:
        return self.cgr_adhesion_setting_att.SetV4_Model_LnFLock(i_locked)

    def set_v5_spa_lock(self, i_locked: bool) -> None:
        return self.cgr_adhesion_setting_att.SetV5_SPALock(i_locked)

    def set_voxels_lock(self, i_locked: bool) -> None:
        return self.cgr_adhesion_setting_att.SetVoxelsLock(i_locked)

    def __repr__(self):
        return f'CgrAdhesionSettingAtt(name="{ self.name }")'
