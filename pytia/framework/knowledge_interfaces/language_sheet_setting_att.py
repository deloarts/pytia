from pytia.framework.system_interfaces.setting_controller import SettingController


class LanguageSheetSettingAtt(SettingController):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.language_sheet_setting_att = com_object

    @property
    def knowledge_build_path_directory(self) -> str:
        return self.language_sheet_setting_att.KnowledgeBuildPathDirectory

    @knowledge_build_path_directory.setter
    def knowledge_build_path_directory(self, value: str):
        self.language_sheet_setting_att.KnowledgeBuildPathDirectory = value

    @property
    def list_of_packages_to_load(self) -> str:
        return self.language_sheet_setting_att.ListOfPackagesToLoad

    @list_of_packages_to_load.setter
    def list_of_packages_to_load(self, value: str):
        self.language_sheet_setting_att.ListOfPackagesToLoad = value

    @property
    def load_all_packages(self) -> int:
        return self.language_sheet_setting_att.LoadAllPackages

    @load_all_packages.setter
    def load_all_packages(self, value: int):
        self.language_sheet_setting_att.LoadAllPackages = value

    @property
    def load_extended_language_lib(self) -> int:
        return self.language_sheet_setting_att.LoadExtendedLanguageLib

    @load_extended_language_lib.setter
    def load_extended_language_lib(self, value: int):
        self.language_sheet_setting_att.LoadExtendedLanguageLib = value

    @property
    def reference_directory_for_types(self) -> str:
        return self.language_sheet_setting_att.ReferenceDirectoryForTypes

    @reference_directory_for_types.setter
    def reference_directory_for_types(self, value: str):
        self.language_sheet_setting_att.ReferenceDirectoryForTypes = value

    def get_knowledge_build_path_directory_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.language_sheet_setting_att.GetKnowledgeBuildPathDirectoryInfo(
            io_admin_level, io_locked
        )

    def get_list_of_packages_to_load_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.language_sheet_setting_att.GetListOfPackagesToLoadInfo(
            io_admin_level, io_locked
        )

    def get_load_all_packages_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.language_sheet_setting_att.GetLoadAllPackagesInfo(
            io_admin_level, io_locked
        )

    def get_load_extended_language_lib_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.language_sheet_setting_att.GetLoadExtendedLanguageLibInfo(
            io_admin_level, io_locked
        )

    def get_reference_directory_for_types_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.language_sheet_setting_att.GetReferenceDirectoryForTypesInfo(
            io_admin_level, io_locked
        )

    def set_knowledge_build_path_directory_lock(self, i_locked: bool) -> None:
        return self.language_sheet_setting_att.SetKnowledgeBuildPathDirectoryLock(
            i_locked
        )

    def set_list_of_packages_to_load_lock(self, i_locked: bool) -> None:
        return self.language_sheet_setting_att.SetListOfPackagesToLoadLock(i_locked)

    def set_load_all_packages_lock(self, i_locked: bool) -> None:
        return self.language_sheet_setting_att.SetLoadAllPackagesLock(i_locked)

    def set_load_extended_language_lib_lock(self, i_locked: bool) -> None:
        return self.language_sheet_setting_att.SetLoadExtendedLanguageLibLock(i_locked)

    def set_reference_directory_for_types_lock(self, i_locked: bool) -> None:
        return self.language_sheet_setting_att.SetReferenceDirectoryForTypesLock(
            i_locked
        )

    def __repr__(self):
        return f'LanguageSheetSettingAtt(name="{self.name}")'
