from pytia.framework.system_interfaces.setting_controller import SettingController


class CacheSettingAtt(SettingController):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.cache_setting_att = com_object

    @property
    def activation_mode(self):
        return self.cache_setting_att.ActivationMode

    @activation_mode.setter
    def activation_mode(self, value):
        self.cache_setting_att.ActivationMode = value

    @property
    def cache_max_size_mo(self):
        return self.cache_setting_att.CacheMaxSizeMo

    @cache_max_size_mo.setter
    def cache_max_size_mo(self, value):
        self.cache_setting_att.CacheMaxSizeMo = value

    @property
    def lod_mode(self):
        return self.cache_setting_att.LODMode

    @lod_mode.setter
    def lod_mode(self, value):
        self.cache_setting_att.LODMode = value

    @property
    def local_path(self):
        return self.cache_setting_att.LocalPath

    @local_path.setter
    def local_path(self, value):
        self.cache_setting_att.LocalPath = value

    @property
    def released_voxel(self):
        return self.cache_setting_att.ReleasedVoxel

    @released_voxel.setter
    def released_voxel(self, value):
        self.cache_setting_att.ReleasedVoxel = value

    @property
    def size_control(self):
        return self.cache_setting_att.SizeControl

    @size_control.setter
    def size_control(self, value):
        self.cache_setting_att.SizeControl = value

    @property
    def timestamp_mode(self):
        return self.cache_setting_att.TimestampMode

    @timestamp_mode.setter
    def timestamp_mode(self, value):
        self.cache_setting_att.TimestampMode = value

    @property
    def utc_time_format(self):
        return self.cache_setting_att.UTCTimeFormat

    @utc_time_format.setter
    def utc_time_format(self, value):
        self.cache_setting_att.UTCTimeFormat = value

    def get_activation_mode_info(self, admin_level, o_locked):
        return self.cache_setting_att.GetActivationModeInfo(admin_level, o_locked)

    def get_cache_max_size_mo_info(self, admin_level, o_locked):
        return self.cache_setting_att.GetCacheMaxSizeMoInfo(admin_level, o_locked)

    def get_lod_mode_info(self, admin_level, o_locked):
        return self.cache_setting_att.GetLODModeInfo(admin_level, o_locked)

    def get_local_path_info(self, admin_level, o_locked):
        return self.cache_setting_att.GetLocalPathInfo(admin_level, o_locked)

    def get_release_path(self):
        return tuple(self.cache_setting_att.GetReleasePath())

    def get_release_path_info(self, admin_level, locked):
        return self.cache_setting_att.GetReleasePathInfo(admin_level, locked)

    def get_released_voxel_info(self, admin_level, o_locked):
        return self.cache_setting_att.GetReleasedVoxelInfo(admin_level, o_locked)

    def get_size_control_info(self, admin_level, o_locked):
        return self.cache_setting_att.GetSizeControlInfo(admin_level, o_locked)

    def get_timestamp_mode_info(self, admin_level, o_locked):
        return self.cache_setting_att.GetTimestampModeInfo(admin_level, o_locked)

    def get_utc_time_format_info(self, admin_level, o_locked):
        return self.cache_setting_att.GetUTCTimeFormatInfo(admin_level, o_locked)

    def put_release_path(self, i_rel_path):
        return self.cache_setting_att.PutReleasePath(i_rel_path)

    def set_activation_mode_lock(self, i_locked):
        return self.cache_setting_att.SetActivationModeLock(i_locked)

    def set_cache_max_size_mo_lock(self, i_locked):
        return self.cache_setting_att.SetCacheMaxSizeMoLock(i_locked)

    def set_lod_mode_lock(self, i_locked):
        return self.cache_setting_att.SetLODModeLock(i_locked)

    def set_local_path_lock(self, i_locked):
        return self.cache_setting_att.SetLocalPathLock(i_locked)

    def set_release_path_lock(self, i_locked):
        return self.cache_setting_att.SetReleasePathLock(i_locked)

    def set_released_voxel_lock(self, i_locked):
        return self.cache_setting_att.SetReleasedVoxelLock(i_locked)

    def set_size_control_lock(self, i_locked):
        return self.cache_setting_att.SetSizeControlLock(i_locked)

    def set_timestamp_mode_lock(self, i_locked):
        return self.cache_setting_att.SetTimestampModeLock(i_locked)

    def set_utc_time_format_lock(self, i_locked):
        return self.cache_setting_att.SetUTCTimeFormatLock(i_locked)

    def __repr__(self):
        return f'CacheSettingAtt(name="{ self.name }")'
