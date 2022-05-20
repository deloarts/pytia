from pytia.framework.system_interfaces.setting_controller import SettingController


class LicenseSettingAtt(SettingController):
    def __init__(self, setting_controller):
        super().__init__(setting_controller.com_object)
        self.license_setting_att = setting_controller.com_object

    @property
    def demo_mode(self):
        return self.license_setting_att.DemoMode

    @demo_mode.setter
    def demo_mode(self, value):
        self.license_setting_att.DemoMode = value

    @property
    def frequency(self):
        return self.license_setting_att.Frequency

    @frequency.setter
    def frequency(self, value):
        self.license_setting_att.Frequency = value

    @property
    def nodelock_alert(self):
        return self.license_setting_att.NodelockAlert

    @nodelock_alert.setter
    def nodelock_alert(self, value):
        self.license_setting_att.NodelockAlert = value

    @property
    def server_time_out(self):
        return self.license_setting_att.ServerTimeOut

    @server_time_out.setter
    def server_time_out(self, value):
        self.license_setting_att.ServerTimeOut = value

    @property
    def show_license(self):
        return self.license_setting_att.ShowLicense

    @show_license.setter
    def show_license(self, value):
        self.license_setting_att.ShowLicense = value

    def get_demo_mode_info(self, io_admin_level, io_locked):
        return self.license_setting_att.GetDemoModeInfo(io_admin_level, io_locked)

    def get_frequency_info(self, io_admin_level, io_locked):
        return self.license_setting_att.GetFrequencyInfo(io_admin_level, io_locked)

    def get_granted_licenses_list(self, i_default_licenses):
        return tuple(
            self.license_setting_att.GetGrantedLicensesList(i_default_licenses)
        )

    def get_license(self, i_license):
        return str(self.license_setting_att.GetLicense(i_license))

    def get_license_info(self, i_license, io_admin_level, io_locked):
        return self.license_setting_att.GetLicenseInfo(
            i_license, io_admin_level, io_locked
        )

    def get_licenses_list(self, i_default_licenses):
        return tuple(self.license_setting_att.GetLicensesList(i_default_licenses))

    def get_licenses_list_info(self, io_admin_level, io_lock):
        return self.license_setting_att.GetLicensesListInfo(io_admin_level, io_lock)

    def get_nodelock_alert_info(self, io_admin_level, io_locked):
        return self.license_setting_att.GetNodelockAlertInfo(io_admin_level, io_locked)

    def get_server_time_out_info(self, io_admin_level, io_locked):
        return self.license_setting_att.GetServerTimeOutInfo(io_admin_level, io_locked)

    def get_show_license_info(self, io_admin_level, io_locked):
        return self.license_setting_att.GetShowLicenseInfo(io_admin_level, io_locked)

    def set_demo_mode_lock(self, i_lock):
        return self.license_setting_att.SetDemoModeLock(i_lock)

    def set_frequency_lock(self, i_lock):
        return self.license_setting_att.SetFrequencyLock(i_lock)

    def set_license(self, i_license, i_value):
        return self.license_setting_att.SetLicense(i_license, i_value)

    def set_license_lock(self, i_license, i_lock):
        return self.license_setting_att.SetLicenseLock(i_license, i_lock)

    def set_licenses_list_lock(self, i_lock):
        return self.license_setting_att.SetLicensesListLock(i_lock)

    def set_nodelock_alert_lock(self, i_lock):
        return self.license_setting_att.SetNodelockAlertLock(i_lock)

    def set_server_time_out_lock(self, i_lock):
        return self.license_setting_att.SetServerTimeOutLock(i_lock)

    def set_show_license_lock(self, i_lock):
        return self.license_setting_att.SetShowLicenseLock(i_lock)

    def __repr__(self):
        return f'LicenseSettingAtt(name="{self.name}")'
