from pytia.framework.system_interfaces.setting_controller import SettingController


class GlobalStatisticsSettingAtt(SettingController):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.global_statistics_setting_att = com_object

    @property
    def buffer_size(self):
        return self.global_statistics_setting_att.BufferSize

    @buffer_size.setter
    def buffer_size(self, value):
        self.global_statistics_setting_att.BufferSize = value

    @property
    def copy_directory(self):
        return self.global_statistics_setting_att.CopyDirectory

    @copy_directory.setter
    def copy_directory(self, value):
        self.global_statistics_setting_att.CopyDirectory = value

    @property
    def max_copy_file(self):
        return self.global_statistics_setting_att.MaxCopyFile

    @max_copy_file.setter
    def max_copy_file(self, value):
        self.global_statistics_setting_att.MaxCopyFile = value

    @property
    def max_size_per_file(self):
        return self.global_statistics_setting_att.MaxSizePerFile

    @max_size_per_file.setter
    def max_size_per_file(self, value):
        self.global_statistics_setting_att.MaxSizePerFile = value

    def get_thematics_parameter_info(self, admin_level, o_locked):
        return self.global_statistics_setting_att.GetThematicsParameterInfo(
            admin_level, o_locked
        )

    def set_thematics_parameter_lock(self, i_locked):
        return self.global_statistics_setting_att.SetThematicsParameterLock(i_locked)

    def __repr__(self):
        return f'GlobalStatisticsSettingAtt(name="{ self.name }")'
