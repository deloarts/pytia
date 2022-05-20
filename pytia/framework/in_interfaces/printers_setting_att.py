from pytia.framework.system_interfaces.setting_controller import SettingController


class PrintersSettingAtt(SettingController):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.printers_setting_att = com_object

    def add_printer_directory(
        self, i_printer_dir: str, i_printer_dir_state: int
    ) -> None:
        return self.printers_setting_att.AddPrinterDirectory(
            i_printer_dir, i_printer_dir_state
        )

    def add_printer_group(
        self, i_printer_group_name: str, i_printer_names: tuple
    ) -> None:
        return self.printers_setting_att.AddPrinterGroup(
            i_printer_group_name, i_printer_names
        )

    def get_driver_configuration_path(self, o_driver_cfg_path: str) -> None:
        return self.printers_setting_att.GetDriverConfigurationPath(o_driver_cfg_path)

    def get_driver_configuration_path_info(
        self, o_admin_level: str, o_locked: str
    ) -> bool:
        return self.printers_setting_att.GetDriverConfigurationPathInfo(
            o_admin_level, o_locked
        )

    def get_new_printer_directory(self, o_new_printer_dir: str) -> None:
        return self.printers_setting_att.GetNewPrinterDirectory(o_new_printer_dir)

    def get_new_printer_directory_info(self, o_admin_level: str, o_locked: str) -> bool:
        return self.printers_setting_att.GetNewPrinterDirectoryInfo(
            o_admin_level, o_locked
        )

    def get_printer_array_for_group(self, i_printer_group_name: str) -> tuple:
        return self.printers_setting_att.GetPrinterArrayForGroup(i_printer_group_name)

    def get_printer_directories(self) -> tuple:
        return self.printers_setting_att.GetPrinterDirectories()

    def get_printer_directories_info(self, o_admin_level: str, o_locked: str) -> bool:
        return self.printers_setting_att.GetPrinterDirectoriesInfo(
            o_admin_level, o_locked
        )

    def get_printer_directory_state(self, i_printer_dir: str) -> int:
        return self.printers_setting_att.GetPrinterDirectoryState(i_printer_dir)

    def get_printer_groups(self) -> tuple:
        return self.printers_setting_att.GetPrinterGroups()

    def get_printer_groups_info(self, o_admin_level: str, o_locked: str) -> bool:
        return self.printers_setting_att.GetPrinterGroupsInfo(o_admin_level, o_locked)

    def modify_printer_array_for_group(
        self, i_printer_group_name: str, i_printer_names: tuple
    ) -> None:
        return self.printers_setting_att.ModifyPrinterArrayForGroup(
            i_printer_group_name, i_printer_names
        )

    def modify_printer_directory_state(
        self, i_printer_dir: str, i_printer_dir_state: int
    ) -> None:
        return self.printers_setting_att.ModifyPrinterDirectoryState(
            i_printer_dir, i_printer_dir_state
        )

    def remove_all_printer_directories(self) -> None:
        return self.printers_setting_att.RemoveAllPrinterDirectories()

    def remove_all_printer_groups(self) -> None:
        return self.printers_setting_att.RemoveAllPrinterGroups()

    def remove_printer_directory(self, i_printer_dir: str) -> None:
        return self.printers_setting_att.RemovePrinterDirectory(i_printer_dir)

    def remove_printer_group(self, i_printer_group_name: str) -> None:
        return self.printers_setting_att.RemovePrinterGroup(i_printer_group_name)

    def set_driver_configuration_path(self, i_driver_cfg_path: str) -> None:
        return self.printers_setting_att.SetDriverConfigurationPath(i_driver_cfg_path)

    def set_driver_configuration_path_lock(self, i_lock: bool) -> None:
        return self.printers_setting_att.SetDriverConfigurationPathLock(i_lock)

    def set_new_printer_directory(self, i_new_printer_dir: str) -> None:
        return self.printers_setting_att.SetNewPrinterDirectory(i_new_printer_dir)

    def set_new_printer_directory_lock(self, i_lock: bool) -> None:
        return self.printers_setting_att.SetNewPrinterDirectoryLock(i_lock)

    def set_printer_directories_lock(self, i_lock: bool) -> None:
        return self.printers_setting_att.SetPrinterDirectoriesLock(i_lock)

    def set_printer_groups_lock(self, i_lock: bool) -> None:
        return self.printers_setting_att.SetPrinterGroupsLock(i_lock)

    def __repr__(self):
        return f'PrintersSettingAtt(name="{self.name}")'
