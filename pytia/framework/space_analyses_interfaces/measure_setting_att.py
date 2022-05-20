from pytia.framework.system_interfaces.setting_controller import SettingController
from pytia.framework.system_interfaces.system_service import SystemService


class MeasureSettingAtt(SettingController):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.measure_setting_att = com_object

    @property
    def box_display(self) -> bool:
        return self.measure_setting_att.BoxDisplay

    @box_display.setter
    def box_display(self, value: bool):
        self.measure_setting_att.BoxDisplay = value

    @property
    def line_width(self) -> int:
        return self.measure_setting_att.LineWidth

    @line_width.setter
    def line_width(self, value: int):
        self.measure_setting_att.LineWidth = value

    @property
    def part_update_status(self) -> bool:
        return self.measure_setting_att.PartUpdateStatus

    @part_update_status.setter
    def part_update_status(self, value: bool):
        self.measure_setting_att.PartUpdateStatus = value

    @property
    def product_update_status(self) -> bool:
        return self.measure_setting_att.ProductUpdateStatus

    @product_update_status.setter
    def product_update_status(self, value: bool):
        self.measure_setting_att.ProductUpdateStatus = value

    @property
    def tilde_display(self) -> bool:
        return self.measure_setting_att.TildeDisplay

    @tilde_display.setter
    def tilde_display(self, value: bool):
        self.measure_setting_att.TildeDisplay = value

    def get_box_display_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.measure_setting_att.GetBoxDisplayInfo(io_admin_level, io_locked)

    def get_label_color(self) -> tuple:
        return self.measure_setting_att.GetLabelColor()

    def get_label_color_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.measure_setting_att.GetLabelColorInfo(io_admin_level, io_locked)

    def get_line_width_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.measure_setting_att.GetLineWidthInfo(io_admin_level, io_locked)

    def get_part_update_status_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.measure_setting_att.GetPartUpdateStatusInfo(
            io_admin_level, io_locked
        )

    def get_product_update_status_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.measure_setting_att.GetProductUpdateStatusInfo(
            io_admin_level, io_locked
        )

    def get_text_color(self) -> tuple:
        vba_function_name = "get_text_color"
        vba_code = """
        Public Function get_text_color(measurable)
            Dim oR long
            Dim oG long
            Dim oB long
            inertia.GetTextColor oR oG oB
            get_principal_moments = (oR, oG, oB)
        End Function
        """
        system_service = self.application.system_service
        return system_service.evaluate(
            vba_code, 0, vba_function_name, [self.com_object]
        )

    def get_text_color_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.measure_setting_att.GetTextColorInfo(io_admin_level, io_locked)

    def get_tilde_display_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.measure_setting_att.GetTildeDisplayInfo(io_admin_level, io_locked)

    def set_box_display_lock(self, i_locked: bool) -> None:
        return self.measure_setting_att.SetBoxDisplayLock(i_locked)

    def set_label_color(self, i_r: int, i_g: int, i_b: int) -> None:
        return self.measure_setting_att.SetLabelColor(i_r, i_g, i_b)

    def set_label_color_lock(self, i_locked: bool) -> None:
        return self.measure_setting_att.SetLabelColorLock(i_locked)

    def set_line_width_lock(self, i_locked: bool) -> None:
        return self.measure_setting_att.SetLineWidthLock(i_locked)

    def set_part_update_status_lock(self, i_locked: bool) -> None:
        return self.measure_setting_att.SetPartUpdateStatusLock(i_locked)

    def set_product_update_status_lock(self, i_locked: bool) -> None:
        return self.measure_setting_att.SetProductUpdateStatusLock(i_locked)

    def set_text_color(self, i_r: int, i_g: int, i_b: int) -> None:
        return self.measure_setting_att.SetTextColor(i_r, i_g, i_b)

    def set_text_color_lock(self, i_locked: bool) -> None:
        return self.measure_setting_att.SetTextColorLock(i_locked)

    def set_tilde_display_lock(self, i_locked: bool) -> None:
        return self.measure_setting_att.SetTildeDisplayLock(i_locked)

    def __repr__(self):
        return f'MeasureSettingAtt(name="{self.name}")'
