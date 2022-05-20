from pytia.framework.system_interfaces.setting_controller import SettingController


class MemoryWarningSettingAtt(SettingController):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.memory_warning_setting_att = com_object

    @property
    def activation_state(self):
        return self.memory_warning_setting_att.ActivationState

    @activation_state.setter
    def activation_state(self, value):
        self.memory_warning_setting_att.ActivationState = value

    @property
    def memory_stopper_state(self):
        return self.memory_warning_setting_att.MemoryStopperState

    @memory_stopper_state.setter
    def memory_stopper_state(self, value):
        self.memory_warning_setting_att.MemoryStopperState = value

    @property
    def usage_limit(self):
        return self.memory_warning_setting_att.UsageLimit

    @usage_limit.setter
    def usage_limit(self, value):
        self.memory_warning_setting_att.UsageLimit = value

    def get_activation_state_info(self, admin_level, o_locked):
        return self.memory_warning_setting_att.GetActivationStateInfo(
            admin_level, o_locked
        )

    def get_memory_stopper_state_info(self, admin_level, o_locked):
        return self.memory_warning_setting_att.GetMemoryStopperStateInfo(
            admin_level, o_locked
        )

    def get_usage_limit_info(self, admin_level, o_locked):
        return self.memory_warning_setting_att.GetUsageLimitInfo(admin_level, o_locked)

    def set_activation_state_lock(self, i_locked):
        return self.memory_warning_setting_att.SetActivationStateLock(i_locked)

    def set_memory_stopper_state_lock(self, i_locked):
        return self.memory_warning_setting_att.SetMemoryStopperStateLock(i_locked)

    def set_usage_limit_lock(self, i_locked):
        return self.memory_warning_setting_att.SetUsageLimitLock(i_locked)

    def __repr__(self):
        return f'MemoryWarningSettingAtt(name="{ self.name }")'
