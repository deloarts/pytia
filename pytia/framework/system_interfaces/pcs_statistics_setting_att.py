from pytia.framework.system_interfaces.general_statistics_setting_att import (
    GeneralStatisticsSettingAtt,
)


class PcsStatisticsSettingAtt(GeneralStatisticsSettingAtt):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.pcs_statistics_setting_att = com_object

    @property
    def mem_use(self):
        return self.pcs_statistics_setting_att.MemUse

    @mem_use.setter
    def mem_use(self, value):
        self.pcs_statistics_setting_att.MemUse = value

    def __repr__(self):
        return f'PcsStatisticsSettingAtt(name="{ self.name }")'
