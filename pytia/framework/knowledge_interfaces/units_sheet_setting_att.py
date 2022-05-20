from pytia.framework.system_interfaces.setting_controller import SettingController


class UnitsSheetSettingAtt(SettingController):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.units_sheet_setting_att = com_object

    @property
    def display_trailing_zeros(self) -> int:
        return self.units_sheet_setting_att.DisplayTrailingZeros

    @display_trailing_zeros.setter
    def display_trailing_zeros(self, value: int):
        self.units_sheet_setting_att.DisplayTrailingZeros = value

    @property
    def exp_notation_values_greater(self) -> float:
        return self.units_sheet_setting_att.ExpNotationValuesGreater

    @exp_notation_values_greater.setter
    def exp_notation_values_greater(self, value: float):
        self.units_sheet_setting_att.ExpNotationValuesGreater = value

    @property
    def exp_notation_values_lower(self) -> float:
        return self.units_sheet_setting_att.ExpNotationValuesLower

    @exp_notation_values_lower.setter
    def exp_notation_values_lower(self, value: float):
        self.units_sheet_setting_att.ExpNotationValuesLower = value

    @property
    def list_of_magnitudes(self) -> tuple:
        return self.units_sheet_setting_att.ListOfMagnitudes

    @property
    def list_of_magnitudes_size(self) -> float:
        return self.units_sheet_setting_att.ListOfMagnitudesSize

    @property
    def same_display(self) -> int:
        return self.units_sheet_setting_att.SameDisplay

    @same_display.setter
    def same_display(self, value: int):
        self.units_sheet_setting_att.SameDisplay = value

    def commit_for_units(self) -> None:
        return self.units_sheet_setting_att.CommitForUnits()

    def get_decimal_read_only(
        self, i_magnitude_name: str, o_decimal_place_read_only: float
    ) -> None:
        return self.units_sheet_setting_att.GetDecimalReadOnly(
            i_magnitude_name, o_decimal_place_read_only
        )

    def get_decimal_read_write(
        self, i_magnitude_name: str, o_decimal_place_read_write: float
    ) -> None:
        return self.units_sheet_setting_att.GetDecimalReadWrite(
            i_magnitude_name, o_decimal_place_read_write
        )

    def get_dimensions_display_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.units_sheet_setting_att.GetDimensionsDisplayInfo(
            io_admin_level, io_locked
        )

    def get_display_trailing_zeros_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.units_sheet_setting_att.GetDisplayTrailingZerosInfo(
            io_admin_level, io_locked
        )

    def get_exp_notation_values_greater_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.units_sheet_setting_att.GetExpNotationValuesGreaterInfo(
            io_admin_level, io_locked
        )

    def get_exp_notation_values_lower_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.units_sheet_setting_att.GetExpNotationValuesLowerInfo(
            io_admin_level, io_locked
        )

    def get_list_of_magnitudes_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.units_sheet_setting_att.GetListOfMagnitudesInfo(
            io_admin_level, io_locked
        )

    def get_magnitude_values(
        self,
        i_magnitude_name: str,
        o_unit_name: str,
        o_decimal_place_read_write: float,
        o_decimal_place_read_only: float,
    ) -> None:
        return self.units_sheet_setting_att.GetMagnitudeValues(
            i_magnitude_name,
            o_unit_name,
            o_decimal_place_read_write,
            o_decimal_place_read_only,
        )

    def get_same_display_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.units_sheet_setting_att.GetSameDisplayInfo(
            io_admin_level, io_locked
        )

    def reset_to_admin_values_for_units(self) -> None:
        return self.units_sheet_setting_att.ResetToAdminValuesForUnits()

    def rollback_for_units(self) -> None:
        return self.units_sheet_setting_att.RollbackForUnits()

    def save_repository_for_units(self) -> None:
        return self.units_sheet_setting_att.SaveRepositoryForUnits()

    def set_dimensions_display_lock(self, i_locked: bool) -> None:
        return self.units_sheet_setting_att.SetDimensionsDisplayLock(i_locked)

    def set_display_trailing_zeros_lock(self, i_locked: bool) -> None:
        return self.units_sheet_setting_att.SetDisplayTrailingZerosLock(i_locked)

    def set_exp_notation_values_greater_lock(self, i_locked: bool) -> None:
        return self.units_sheet_setting_att.SetExpNotationValuesGreaterLock(i_locked)

    def set_exp_notation_values_lower_lock(self, i_locked: bool) -> None:
        return self.units_sheet_setting_att.SetExpNotationValuesLowerLock(i_locked)

    def set_list_of_magnitudes_lock(self, i_locked: bool) -> None:
        return self.units_sheet_setting_att.SetListOfMagnitudesLock(i_locked)

    def set_magnitude_values(
        self,
        i_magnitude_name: str,
        i_unit_name: str,
        i_decimal_place_read_write: float,
        i_decimal_place_read_only: float,
    ) -> None:
        return self.units_sheet_setting_att.SetMagnitudeValues(
            i_magnitude_name,
            i_unit_name,
            i_decimal_place_read_write,
            i_decimal_place_read_only,
        )

    def set_same_display_lock(self, i_locked: bool) -> None:
        return self.units_sheet_setting_att.SetSameDisplayLock(i_locked)

    def __repr__(self):
        return f'UnitsSheetSettingAtt(name="{self.name}")'
