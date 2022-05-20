from pytia.framework.system_interfaces.general_statistics_setting_att import (
    GeneralStatisticsSettingAtt,
)


class ErrorlogStatisticsSettingAtt(GeneralStatisticsSettingAtt):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.errorlog_statistics_setting_att = com_object

    @property
    def abnd(self):
        return self.errorlog_statistics_setting_att.ABND

    @abnd.setter
    def abnd(self, value):
        self.errorlog_statistics_setting_att.ABND = value

    @property
    def cerr(self):
        return self.errorlog_statistics_setting_att.CERR

    @cerr.setter
    def cerr(self, value):
        self.errorlog_statistics_setting_att.CERR = value

    @property
    def cmnd(self):
        return self.errorlog_statistics_setting_att.CMND

    @cmnd.setter
    def cmnd(self, value):
        self.errorlog_statistics_setting_att.CMND = value

    @property
    def comt(self):
        return self.errorlog_statistics_setting_att.COMT

    @comt.setter
    def comt(self, value):
        self.errorlog_statistics_setting_att.COMT = value

    @property
    def msge(self):
        return self.errorlog_statistics_setting_att.MSGE

    @msge.setter
    def msge(self, value):
        self.errorlog_statistics_setting_att.MSGE = value

    @property
    def urep(self):
        return self.errorlog_statistics_setting_att.UREP

    @urep.setter
    def urep(self, value):
        self.errorlog_statistics_setting_att.UREP = value

    @property
    def warn(self):
        return self.errorlog_statistics_setting_att.WARN

    @warn.setter
    def warn(self, value):
        self.errorlog_statistics_setting_att.WARN = value

    @property
    def wkbn(self):
        return self.errorlog_statistics_setting_att.WKBN

    @wkbn.setter
    def wkbn(self, value):
        self.errorlog_statistics_setting_att.WKBN = value

    def __repr__(self):
        return f'ErrorlogStatisticsSettingAtt(name="{ self.name }")'
