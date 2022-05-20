from pytia.framework.system_interfaces.setting_controller import SettingController


class SettingRepository(SettingController):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.setting_repository = com_object

    def get_attr(self, i_attr_name):
        return self.setting_repository.GetAttr(i_attr_name)

    def get_attr_array(self, i_attr_name):
        return tuple(self.setting_repository.GetAttrArray(i_attr_name))

    def get_attr_info(self, i_attr_name, admin_level, locked, o_modified):
        return self.setting_repository.GetAttrInfo(
            i_attr_name, admin_level, locked, o_modified
        )

    def put_attr(self, i_attr_name, i_attr):
        return self.setting_repository.PutAttr(i_attr_name, i_attr)

    def put_attr_array(self, i_attr_name, i_array):
        return self.setting_repository.PutAttrArray(i_attr_name, i_array)

    def set_attr_lock(self, i_attr_name, i_locked):
        return self.setting_repository.SetAttrLock(i_attr_name, i_locked)

    def __repr__(self):
        return f'SettingRepository(name="{self.name}")'
