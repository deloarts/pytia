from pytia.framework.system_interfaces.setting_controller import SettingController


class DlNameSettingAtt(SettingController):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.dl_name_setting_att = com_object

    @property
    def dl_name_creation_right(self):
        return self.dl_name_setting_att.DLNameCreationRight

    @dl_name_creation_right.setter
    def dl_name_creation_right(self, value):
        self.dl_name_setting_att.DLNameCreationRight = value

    @property
    def root_dl_name_creation_right(self):
        return self.dl_name_setting_att.RootDLNameCreationRight

    @root_dl_name_creation_right.setter
    def root_dl_name_creation_right(self, value):
        self.dl_name_setting_att.RootDLNameCreationRight = value

    def get_dl_name(self, i_dl_name, o_real_name_unix, o_real_name_nt, o_father):
        return self.dl_name_setting_att.GetDLName(
            i_dl_name, o_real_name_unix, o_real_name_nt, o_father
        )

    def get_dl_name_creation_right_info(self, admin_level, o_locked):
        return self.dl_name_setting_att.GetDLNameCreationRightInfo(
            admin_level, o_locked
        )

    def get_dl_name_exp(self, i_dl_name, o_real_name_unix, o_real_name_nt, o_father):
        return self.dl_name_setting_att.GetDLNameExp(
            i_dl_name, o_real_name_unix, o_real_name_nt, o_father
        )

    def get_dl_name_info(self, i_dl_name, admin_level, o_locked):
        return self.dl_name_setting_att.GetDLNameInfo(i_dl_name, admin_level, o_locked)

    def get_dl_name_list(self):
        return tuple(self.dl_name_setting_att.GetDLNameList())

    def get_dl_name_sub_list(self, i_dl_name):
        return tuple(self.dl_name_setting_att.GetDLNameSubList(i_dl_name))

    def get_root_dl_name_creation_right_info(self, admin_level, o_locked):
        return self.dl_name_setting_att.GetRootDLNameCreationRightInfo(
            admin_level, o_locked
        )

    def remove_dl_name(self, i_dl_name):
        return self.dl_name_setting_att.RemoveDLName(i_dl_name)

    def rename_dl_name(self, i_dl_name, i_new_name):
        return self.dl_name_setting_att.RenameDLName(i_dl_name, i_new_name)

    def set_dl_name(
        self, i_dl_name, i_real_name_unix, i_real_name_nt, i_father, i_verif_directory
    ):
        return self.dl_name_setting_att.SetDLName(
            i_dl_name, i_real_name_unix, i_real_name_nt, i_father, i_verif_directory
        )

    def set_dl_name_creation_right_lock(self, i_locked):
        return self.dl_name_setting_att.SetDLNameCreationRightLock(i_locked)

    def set_dl_name_lock(self, i_dl_name, i_locked):
        return self.dl_name_setting_att.SetDLNameLock(i_dl_name, i_locked)

    def set_root_dl_name_creation_right_lock(self, i_locked):
        return self.dl_name_setting_att.SetRootDLNameCreationRightLock(i_locked)

    def __repr__(self):
        return f'DlNameSettingAtt(name="{self.name}")'
