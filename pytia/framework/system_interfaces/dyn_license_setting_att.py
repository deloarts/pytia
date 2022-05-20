from pytia.framework.system_interfaces.setting_controller import SettingController


class DynLicenseSettingAtt(SettingController):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.dyn_license_setting_att = com_object

    def get_license(self, i_license):
        return str(self.dyn_license_setting_att.GetLicense(i_license))

    def get_license_info(self, i_license, io_admin_level, io_locked):
        return self.dyn_license_setting_att.GetLicenseInfo(
            i_license, io_admin_level, io_locked
        )

    def get_licenses_list(self):
        return tuple(self.dyn_license_setting_att.GetLicensesList())

    def get_licenses_list_info(self, io_admin_level, io_locked):
        return self.dyn_license_setting_att.GetLicensesListInfo(
            io_admin_level, io_locked
        )

    def set_license_lock(self, i_license, i_lock):
        return self.dyn_license_setting_att.SetLicenseLock(i_license, i_lock)

    def set_licenses_list_lock(self, i_lock):
        return self.dyn_license_setting_att.SetLicensesListLock(i_lock)

    def __repr__(self):
        return f'DynLicenseSettingAtt(name="{self.name}")'
