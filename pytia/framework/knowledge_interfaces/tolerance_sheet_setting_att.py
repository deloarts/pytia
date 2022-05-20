from pytia.framework.system_interfaces.setting_controller import SettingController


class ToleranceSheetSettingAtt(SettingController):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.tolerance_sheet_setting_att = com_object

    @property
    def angle_max_tolerance(self) -> float:
        return self.tolerance_sheet_setting_att.AngleMaxTolerance

    @angle_max_tolerance.setter
    def angle_max_tolerance(self, value: float):
        self.tolerance_sheet_setting_att.AngleMaxTolerance = value

    @property
    def angle_min_tolerance(self) -> float:
        return self.tolerance_sheet_setting_att.AngleMinTolerance

    @angle_min_tolerance.setter
    def angle_min_tolerance(self, value: float):
        self.tolerance_sheet_setting_att.AngleMinTolerance = value

    @property
    def default_tolerance(self) -> int:
        return self.tolerance_sheet_setting_att.DefaultTolerance

    @default_tolerance.setter
    def default_tolerance(self, value: int):
        self.tolerance_sheet_setting_att.DefaultTolerance = value

    @property
    def length_max_tolerance(self) -> float:
        return self.tolerance_sheet_setting_att.LengthMaxTolerance

    @length_max_tolerance.setter
    def length_max_tolerance(self, value: float):
        self.tolerance_sheet_setting_att.LengthMaxTolerance = value

    @property
    def length_min_tolerance(self) -> float:
        return self.tolerance_sheet_setting_att.LengthMinTolerance

    @length_min_tolerance.setter
    def length_min_tolerance(self, value: float):
        self.tolerance_sheet_setting_att.LengthMinTolerance = value

    def get_angle_max_tolerance_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.tolerance_sheet_setting_att.GetAngleMaxToleranceInfo(
            io_admin_level, io_locked
        )

    def get_angle_min_tolerance_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.tolerance_sheet_setting_att.GetAngleMinToleranceInfo(
            io_admin_level, io_locked
        )

    def get_default_tolerance_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.tolerance_sheet_setting_att.GetDefaultToleranceInfo(
            io_admin_level, io_locked
        )

    def get_length_max_tolerance_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.tolerance_sheet_setting_att.GetLengthMaxToleranceInfo(
            io_admin_level, io_locked
        )

    def get_length_min_tolerance_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.tolerance_sheet_setting_att.GetLengthMinToleranceInfo(
            io_admin_level, io_locked
        )

    def set_angle_max_tolerance_lock(self, i_locked: bool) -> None:
        return self.tolerance_sheet_setting_att.SetAngleMaxToleranceLock(i_locked)

    def set_angle_min_tolerance_lock(self, i_locked: bool) -> None:
        return self.tolerance_sheet_setting_att.SetAngleMinToleranceLock(i_locked)

    def set_default_tolerance_lock(self, i_locked: bool) -> None:
        return self.tolerance_sheet_setting_att.SetDefaultToleranceLock(i_locked)

    def set_length_max_tolerance_lock(self, i_locked: bool) -> None:
        return self.tolerance_sheet_setting_att.SetLengthMaxToleranceLock(i_locked)

    def set_length_min_tolerance_lock(self, i_locked: bool) -> None:
        return self.tolerance_sheet_setting_att.SetLengthMinToleranceLock(i_locked)

    def __repr__(self):
        return f'ToleranceSheetSettingAtt(name="{self.name}")'
