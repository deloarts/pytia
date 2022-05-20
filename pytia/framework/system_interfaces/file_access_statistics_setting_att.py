from pytia.framework.system_interfaces.general_statistics_setting_att import (
    GeneralStatisticsSettingAtt,
)


class FileAccessStatisticsSettingAtt(GeneralStatisticsSettingAtt):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.file_access_statistics_setting_att = com_object

    def __repr__(self):
        return f'FileAccessStatisticsSettingAtt(name="{ self.name }")'
