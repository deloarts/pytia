from pytia.framework.system_interfaces.general_statistics_setting_att import (
    GeneralStatisticsSettingAtt,
)


class SessionStatisticsSettingAtt(GeneralStatisticsSettingAtt):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.session_statistics_setting_att = com_object

    def __repr__(self):
        return f'SessionStatisticsSettingAtt(name="{ self.name }")'
