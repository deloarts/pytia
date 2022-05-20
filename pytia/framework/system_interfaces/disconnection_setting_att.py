from pytia.framework.system_interfaces.setting_controller import SettingController


class DisconnectionSettingAtt(SettingController):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.disconnection_setting_att = com_object

    @property
    def activation_state(self):
        return self.disconnection_setting_att.ActivationState

    @activation_state.setter
    def activation_state(self, value):
        self.disconnection_setting_att.ActivationState = value

    @property
    def inactivity_duration(self):
        return self.disconnection_setting_att.InactivityDuration

    @inactivity_duration.setter
    def inactivity_duration(self, value):
        self.disconnection_setting_att.InactivityDuration = value

    def get_activation_state_info(self, admin_level, o_locked):
        return self.disconnection_setting_att.GetActivationStateInfo(
            admin_level, o_locked
        )

    def get_inactivity_duration_info(self, admin_level, o_locked):
        return self.disconnection_setting_att.GetInactivityDurationInfo(
            admin_level, o_locked
        )

    def set_activation_state_lock(self, i_locked):
        return self.disconnection_setting_att.SetActivationStateLock(i_locked)

    def set_inactivity_duration_lock(self, i_locked):
        return self.disconnection_setting_att.SetInactivityDurationLock(i_locked)

    def __repr__(self):
        return f'DisconnectionSettingAtt(name="{ self.name }")'
