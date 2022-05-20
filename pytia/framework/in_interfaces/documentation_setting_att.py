from pytia.framework.system_interfaces.setting_controller import SettingController


class DocumentationSettingAtt(SettingController):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.documentation_setting_att = com_object

    @property
    def companion_path(self) -> str:
        return self.documentation_setting_att.CompanionPath

    @companion_path.setter
    def companion_path(self, value: str):
        self.documentation_setting_att.CompanionPath = value

    @property
    def doc_language(self) -> int:
        return self.documentation_setting_att.DocLanguage

    @doc_language.setter
    def doc_language(self, value: int):
        self.documentation_setting_att.DocLanguage = value

    @property
    def priority(self) -> int:
        return self.documentation_setting_att.Priority

    @priority.setter
    def priority(self, value: int):
        self.documentation_setting_att.Priority = value

    @property
    def technical_documentation_path(self) -> str:
        return self.documentation_setting_att.TechnicalDocumentationPath

    @technical_documentation_path.setter
    def technical_documentation_path(self, value: str):
        self.documentation_setting_att.TechnicalDocumentationPath = value

    def get_companion_path_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.documentation_setting_att.GetCompanionPathInfo(
            io_admin_level, io_locked
        )

    def get_doc_language_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.documentation_setting_att.GetDocLanguageInfo(
            io_admin_level, io_locked
        )

    def get_priority_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.documentation_setting_att.GetPriorityInfo(io_admin_level, io_locked)

    def get_technical_documentation_path_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.documentation_setting_att.GetTechnicalDocumentationPathInfo(
            io_admin_level, io_locked
        )

    def set_companion_path_lock(self, i_locked: bool) -> None:
        return self.documentation_setting_att.SetCompanionPathLock(i_locked)

    def set_doc_language_lock(self, i_locked: bool) -> None:
        return self.documentation_setting_att.SetDocLanguageLock(i_locked)

    def set_priority_lock(self, i_locked: bool) -> None:
        return self.documentation_setting_att.SetPriorityLock(i_locked)

    def set_technical_documentation_path_lock(self, i_locked: bool) -> None:
        return self.documentation_setting_att.SetTechnicalDocumentationPathLock(
            i_locked
        )

    def __repr__(self):
        return f'DocumentationSettingAtt(name="{ self.name }")'
