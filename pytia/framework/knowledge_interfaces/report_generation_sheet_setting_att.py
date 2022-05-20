from pytia.framework.system_interfaces.setting_controller import SettingController


class ReportGenerationSheetSettingAtt(SettingController):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.report_generation_sheet_setting_att = com_object

    @property
    def all_checks_report(self) -> int:
        return self.report_generation_sheet_setting_att.AllChecksReport

    @all_checks_report.setter
    def all_checks_report(self, value: int):
        self.report_generation_sheet_setting_att.AllChecksReport = value

    @property
    def check_report_html(self) -> int:
        return self.report_generation_sheet_setting_att.CheckReportHtml

    @check_report_html.setter
    def check_report_html(self, value: int):
        self.report_generation_sheet_setting_att.CheckReportHtml = value

    @property
    def directory_for_input_xsl(self) -> str:
        return self.report_generation_sheet_setting_att.DirectoryForInputXsl

    @directory_for_input_xsl.setter
    def directory_for_input_xsl(self, value: str):
        self.report_generation_sheet_setting_att.DirectoryForInputXsl = value

    @property
    def report_check_advisor(self) -> int:
        return self.report_generation_sheet_setting_att.ReportCheckAdvisor

    @report_check_advisor.setter
    def report_check_advisor(self, value: int):
        self.report_generation_sheet_setting_att.ReportCheckAdvisor = value

    @property
    def report_check_expert(self) -> int:
        return self.report_generation_sheet_setting_att.ReportCheckExpert

    @report_check_expert.setter
    def report_check_expert(self, value: int):
        self.report_generation_sheet_setting_att.ReportCheckExpert = value

    @property
    def report_html_in_catia_session(self) -> int:
        return self.report_generation_sheet_setting_att.ReportHtmlInCatiaSession

    @report_html_in_catia_session.setter
    def report_html_in_catia_session(self, value: int):
        self.report_generation_sheet_setting_att.ReportHtmlInCatiaSession = value

    @property
    def report_objects_information(self) -> int:
        return self.report_generation_sheet_setting_att.ReportObjectsInformation

    @report_objects_information.setter
    def report_objects_information(self, value: int):
        self.report_generation_sheet_setting_att.ReportObjectsInformation = value

    @property
    def report_output_directory(self) -> str:
        return self.report_generation_sheet_setting_att.ReportOutputDirectory

    @report_output_directory.setter
    def report_output_directory(self, value: str):
        self.report_generation_sheet_setting_att.ReportOutputDirectory = value

    @property
    def report_parameters_information(self) -> int:
        return self.report_generation_sheet_setting_att.ReportParametersInformation

    @report_parameters_information.setter
    def report_parameters_information(self, value: int):
        self.report_generation_sheet_setting_att.ReportParametersInformation = value

    @property
    def report_passed_objects(self) -> int:
        return self.report_generation_sheet_setting_att.ReportPassedObjects

    @report_passed_objects.setter
    def report_passed_objects(self, value: int):
        self.report_generation_sheet_setting_att.ReportPassedObjects = value

    def get_all_checks_report_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.report_generation_sheet_setting_att.GetAllChecksReportInfo(
            io_admin_level, io_locked
        )

    def get_check_report_html_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.report_generation_sheet_setting_att.GetCheckReportHtmlInfo(
            io_admin_level, io_locked
        )

    def get_directory_for_input_xsl_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.report_generation_sheet_setting_att.GetDirectoryForInputXslInfo(
            io_admin_level, io_locked
        )

    def get_report_check_advisor_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.report_generation_sheet_setting_att.GetReportCheckAdvisorInfo(
            io_admin_level, io_locked
        )

    def get_report_check_expert_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.report_generation_sheet_setting_att.GetReportCheckExpertInfo(
            io_admin_level, io_locked
        )

    def get_report_html_in_catia_session_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.report_generation_sheet_setting_att.GetReportHtmlInCatiaSessionInfo(
            io_admin_level, io_locked
        )

    def get_report_objects_information_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.report_generation_sheet_setting_att.GetReportObjectsInformationInfo(
            io_admin_level, io_locked
        )

    def get_report_output_directory_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.report_generation_sheet_setting_att.GetReportOutputDirectoryInfo(
            io_admin_level, io_locked
        )

    def get_report_parameters_information_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return (
            self.report_generation_sheet_setting_att.GetReportParametersInformationInfo(
                io_admin_level, io_locked
            )
        )

    def get_report_passed_objects_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.report_generation_sheet_setting_att.GetReportPassedObjectsInfo(
            io_admin_level, io_locked
        )

    def set_all_checks_report_lock(self, i_locked: bool) -> None:
        return self.report_generation_sheet_setting_att.SetAllChecksReportLock(i_locked)

    def set_check_report_html_lock(self, i_locked: bool) -> None:
        return self.report_generation_sheet_setting_att.SetCheckReportHtmlLock(i_locked)

    def set_directory_for_input_xsl_lock(self, i_locked: bool) -> None:
        return self.report_generation_sheet_setting_att.SetDirectoryForInputXslLock(
            i_locked
        )

    def set_report_check_advisor_lock(self, i_locked: bool) -> None:
        return self.report_generation_sheet_setting_att.SetReportCheckAdvisorLock(
            i_locked
        )

    def set_report_check_expert_lock(self, i_locked: bool) -> None:
        return self.report_generation_sheet_setting_att.SetReportCheckExpertLock(
            i_locked
        )

    def set_report_html_in_catia_session_lock(self, i_locked: bool) -> None:
        return self.report_generation_sheet_setting_att.SetReportHtmlInCatiaSessionLock(
            i_locked
        )

    def set_report_objects_information_lock(self, i_locked: bool) -> None:
        return self.report_generation_sheet_setting_att.SetReportObjectsInformationLock(
            i_locked
        )

    def set_report_output_directory_lock(self, i_locked: bool) -> None:
        return self.report_generation_sheet_setting_att.SetReportOutputDirectoryLock(
            i_locked
        )

    def set_report_parameters_information_lock(self, i_locked: bool) -> None:
        return (
            self.report_generation_sheet_setting_att.SetReportParametersInformationLock(
                i_locked
            )
        )

    def set_report_passed_objects_lock(self, i_locked: bool) -> None:
        return self.report_generation_sheet_setting_att.SetReportPassedObjectsLock(
            i_locked
        )

    def __repr__(self):
        return f'ReportGenerationSheetSettingAtt(name="{self.name}")'
