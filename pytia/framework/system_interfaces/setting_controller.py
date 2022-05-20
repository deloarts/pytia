from pytia.framework.system_interfaces.any_object import AnyObject


class SettingController(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.setting_controller = com_object

    def commit(self):
        return self.setting_controller.Commit()

    def reset_to_admin_values(self):
        return self.setting_controller.ResetToAdminValues()

    def reset_to_admin_values_by_name(self, i_att_list):
        return self.setting_controller.ResetToAdminValuesByName(i_att_list)

    def rollback(self):
        return self.setting_controller.Rollback()

    def save_repository(self):
        return self.setting_controller.SaveRepository()

    def __repr__(self):
        return f'SettingController(name="{self.name}")'
