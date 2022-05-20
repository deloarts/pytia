from pytia.framework.system_interfaces.setting_controller import SettingController


class MacrosSettingAtt(SettingController):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.macros_setting_att = com_object

    def get_default_macro_libraries(self) -> tuple:
        return self.macros_setting_att.GetDefaultMacroLibraries()

    def get_default_macro_libraries_info(self, admin_level: str, o_locked: str) -> bool:
        return self.macros_setting_att.GetDefaultMacroLibrariesInfo(
            admin_level, o_locked
        )

    def get_external_references(self) -> tuple:
        return self.macros_setting_att.GetExternalReferences()

    def get_external_references_info(self, admin_level: str, o_locked: str) -> bool:
        return self.macros_setting_att.GetExternalReferencesInfo(admin_level, o_locked)

    def get_language_editor(self, i_language: int) -> str:
        return self.macros_setting_att.GetLanguageEditor(i_language)

    def get_language_editor_info(self, admin_level: str, o_locked: str) -> bool:
        return self.macros_setting_att.GetLanguageEditorInfo(admin_level, o_locked)

    def set_default_macro_libraries(self, i_libraries: tuple) -> None:
        return self.macros_setting_att.SetDefaultMacroLibraries(i_libraries)

    def set_default_macro_libraries_lock(self, i_locked: bool) -> None:
        return self.macros_setting_att.SetDefaultMacroLibrariesLock(i_locked)

    def set_external_references(self, i_references: tuple) -> None:
        return self.macros_setting_att.SetExternalReferences(i_references)

    def set_external_references_lock(self, i_locked: bool) -> None:
        return self.macros_setting_att.SetExternalReferencesLock(i_locked)

    def set_language_editor(self, i_language: int, i_editor_path: str) -> None:
        return self.macros_setting_att.SetLanguageEditor(i_language, i_editor_path)

    def set_language_editor_lock(self, i_locked: bool) -> None:
        return self.macros_setting_att.SetLanguageEditorLock(i_locked)

    def __repr__(self):
        return f'MacrosSettingAtt(name="{ self.name }")'
