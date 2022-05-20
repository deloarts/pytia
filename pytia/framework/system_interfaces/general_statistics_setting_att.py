from pytia.framework.system_interfaces.setting_controller import SettingController


class GeneralStatisticsSettingAtt(SettingController):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.general_statistics_setting_att = com_object

    @property
    def activation(self):
        return self.general_statistics_setting_att.Activation

    @activation.setter
    def activation(self, value):
        self.general_statistics_setting_att.Activation = value

    @property
    def cpus(self):
        return self.general_statistics_setting_att.CPUS

    @cpus.setter
    def cpus(self, value):
        self.general_statistics_setting_att.CPUS = value

    @property
    def cumulation_mode(self):
        return self.general_statistics_setting_att.CumulationMode

    @cumulation_mode.setter
    def cumulation_mode(self, value):
        self.general_statistics_setting_att.CumulationMode = value

    @property
    def date_format(self):
        return self.general_statistics_setting_att.DateFormat

    @date_format.setter
    def date_format(self, value):
        self.general_statistics_setting_att.DateFormat = value

    @property
    def elps(self):
        return self.general_statistics_setting_att.ELPS

    @elps.setter
    def elps(self, value):
        self.general_statistics_setting_att.ELPS = value

    @property
    def host(self):
        return self.general_statistics_setting_att.HOST

    @host.setter
    def host(self, value):
        self.general_statistics_setting_att.HOST = value

    @property
    def output(self):
        return self.general_statistics_setting_att.Output

    @output.setter
    def output(self, value):
        self.general_statistics_setting_att.Output = value

    @property
    def output_file(self):
        return self.general_statistics_setting_att.OutputFile

    @output_file.setter
    def output_file(self, value):
        self.general_statistics_setting_att.OutputFile = value

    @property
    def output_format(self):
        return self.general_statistics_setting_att.OutputFormat

    @output_format.setter
    def output_format(self, value):
        self.general_statistics_setting_att.OutputFormat = value

    @property
    def rtim(self):
        return self.general_statistics_setting_att.RTIM

    @rtim.setter
    def rtim(self, value):
        self.general_statistics_setting_att.RTIM = value

    @property
    def them(self):
        return self.general_statistics_setting_att.THEM

    @them.setter
    def them(self, value):
        self.general_statistics_setting_att.THEM = value

    @property
    def time(self):
        return self.general_statistics_setting_att.TIME

    @time.setter
    def time(self, value):
        self.general_statistics_setting_att.TIME = value

    @property
    def time_unit(self):
        return self.general_statistics_setting_att.TimeUnit

    @time_unit.setter
    def time_unit(self, value):
        self.general_statistics_setting_att.TimeUnit = value

    @property
    def upid(self):
        return self.general_statistics_setting_att.UPID

    @upid.setter
    def upid(self, value):
        self.general_statistics_setting_att.UPID = value

    @property
    def user(self):
        return self.general_statistics_setting_att.USER

    @user.setter
    def user(self, value):
        self.general_statistics_setting_att.USER = value

    def get_format_mode(self, flag):
        return bool(self.general_statistics_setting_att.GetFormatMode(flag))

    def get_thematics_parameter_info(self, admin_level, o_locked):
        return self.general_statistics_setting_att.GetThematicsParameterInfo(
            admin_level, o_locked
        )

    def set_format_mode(self, i_format_mode, flag):
        return self.general_statistics_setting_att.SetFormatMode(i_format_mode, flag)

    def set_thematics_parameter_lock(self, i_locked):
        return self.general_statistics_setting_att.SetThematicsParameterLock(i_locked)

    def __repr__(self):
        return f'GeneralStatisticsSettingAtt(name="{ self.name }")'
