from pytia.framework.system_interfaces.general_statistics_setting_att import (
    GeneralStatisticsSettingAtt,
)


class AccesslogStatisticsSettingAtt(GeneralStatisticsSettingAtt):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.accesslog_statistics_setting_att = com_object

    def __repr__(self):
        return f'AccesslogStatisticsSettingAtt(name="{ self.name }")'
