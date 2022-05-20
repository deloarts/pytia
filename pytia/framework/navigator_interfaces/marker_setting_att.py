from pytia.framework.system_interfaces.setting_controller import SettingController


class MarkerSettingAtt(SettingController):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.marker_setting_att = com_object

    @property
    def marker_2d_auto_naming(self) -> bool:
        return self.marker_setting_att.Marker2DAutoNaming

    @marker_2d_auto_naming.setter
    def marker_2d_auto_naming(self, value: bool):
        self.marker_setting_att.Marker2DAutoNaming = value

    @property
    def marker_3d_auto_naming(self) -> bool:
        return self.marker_setting_att.Marker3DAutoNaming

    @marker_3d_auto_naming.setter
    def marker_3d_auto_naming(self, value: bool):
        self.marker_setting_att.Marker3DAutoNaming = value

    @property
    def marker_defaults_dashed(self) -> int:
        return self.marker_setting_att.MarkerDefaultsDashed

    @marker_defaults_dashed.setter
    def marker_defaults_dashed(self, value: int):
        self.marker_setting_att.MarkerDefaultsDashed = value

    @property
    def marker_defaults_weight(self) -> int:
        return self.marker_setting_att.MarkerDefaultsWeight

    @marker_defaults_weight.setter
    def marker_defaults_weight(self, value: int):
        self.marker_setting_att.MarkerDefaultsWeight = value

    @property
    def marker_text_dashed_2d(self) -> int:
        return self.marker_setting_att.MarkerTextDashed2D

    @marker_text_dashed_2d.setter
    def marker_text_dashed_2d(self, value: int):
        self.marker_setting_att.MarkerTextDashed2D = value

    @property
    def marker_text_dashed_3d(self) -> int:
        return self.marker_setting_att.MarkerTextDashed3D

    @marker_text_dashed_3d.setter
    def marker_text_dashed_3d(self, value: int):
        self.marker_setting_att.MarkerTextDashed3D = value

    @property
    def marker_text_defaults_font_2d(self) -> str:
        return self.marker_setting_att.MarkerTextDefaultsFont2D

    @marker_text_defaults_font_2d.setter
    def marker_text_defaults_font_2d(self, value: str):
        self.marker_setting_att.MarkerTextDefaultsFont2D = value

    @property
    def marker_text_defaults_font_3d(self) -> str:
        return self.marker_setting_att.MarkerTextDefaultsFont3D

    @marker_text_defaults_font_3d.setter
    def marker_text_defaults_font_3d(self, value: str):
        self.marker_setting_att.MarkerTextDefaultsFont3D = value

    @property
    def marker_text_defaults_size_2d(self) -> int:
        return self.marker_setting_att.MarkerTextDefaultsSize2D

    @marker_text_defaults_size_2d.setter
    def marker_text_defaults_size_2d(self, value: int):
        self.marker_setting_att.MarkerTextDefaultsSize2D = value

    @property
    def marker_text_defaults_size_3d(self) -> int:
        return self.marker_setting_att.MarkerTextDefaultsSize3D

    @marker_text_defaults_size_3d.setter
    def marker_text_defaults_size_3d(self, value: int):
        self.marker_setting_att.MarkerTextDefaultsSize3D = value

    @property
    def marker_text_weight_2d(self) -> int:
        return self.marker_setting_att.MarkerTextWeight2D

    @marker_text_weight_2d.setter
    def marker_text_weight_2d(self, value: int):
        self.marker_setting_att.MarkerTextWeight2D = value

    @property
    def marker_text_weight_3d(self) -> int:
        return self.marker_setting_att.MarkerTextWeight3D

    @marker_text_weight_3d.setter
    def marker_text_weight_3d(self, value: int):
        self.marker_setting_att.MarkerTextWeight3D = value

    def get_marker_2d_auto_naming_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.marker_setting_att.GetMarker2DAutoNamingInfo(
            io_admin_level, io_locked
        )

    def get_marker_3d_auto_naming_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.marker_setting_att.GetMarker3DAutoNamingInfo(
            io_admin_level, io_locked
        )

    def get_marker_defaults_color(self, o_red: int, o_green: int, o_blue: int) -> None:
        return self.marker_setting_att.GetMarkerDefaultsColor(o_red, o_green, o_blue)

    def get_marker_defaults_color_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.marker_setting_att.GetMarkerDefaultsColorInfo(
            io_admin_level, io_locked
        )

    def get_marker_defaults_dashed_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.marker_setting_att.GetMarkerDefaultsDashedInfo(
            io_admin_level, io_locked
        )

    def get_marker_defaults_weight_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.marker_setting_att.GetMarkerDefaultsWeightInfo(
            io_admin_level, io_locked
        )

    def get_marker_text_color_2d(self, o_red: int, o_green: int, o_blue: int) -> None:
        return self.marker_setting_att.GetMarkerTextColor2D(o_red, o_green, o_blue)

    def get_marker_text_color_2d_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.marker_setting_att.GetMarkerTextColor2DInfo(
            io_admin_level, io_locked
        )

    def get_marker_text_color_3d(self, o_red: int, o_green: int, o_blue: int) -> None:
        return self.marker_setting_att.GetMarkerTextColor3D(o_red, o_green, o_blue)

    def get_marker_text_color_3d_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.marker_setting_att.GetMarkerTextColor3DInfo(
            io_admin_level, io_locked
        )

    def get_marker_text_dashed_2d_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.marker_setting_att.GetMarkerTextDashed2DInfo(
            io_admin_level, io_locked
        )

    def get_marker_text_dashed_3d_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.marker_setting_att.GetMarkerTextDashed3DInfo(
            io_admin_level, io_locked
        )

    def get_marker_text_defaults_font_2d_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.marker_setting_att.GetMarkerTextDefaultsFont2DInfo(
            io_admin_level, io_locked
        )

    def get_marker_text_defaults_font_3d_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.marker_setting_att.GetMarkerTextDefaultsFont3DInfo(
            io_admin_level, io_locked
        )

    def get_marker_text_defaults_size_2d_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.marker_setting_att.GetMarkerTextDefaultsSize2DInfo(
            io_admin_level, io_locked
        )

    def get_marker_text_defaults_size_3d_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.marker_setting_att.GetMarkerTextDefaultsSize3DInfo(
            io_admin_level, io_locked
        )

    def get_marker_text_weight_2d_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.marker_setting_att.GetMarkerTextWeight2DInfo(
            io_admin_level, io_locked
        )

    def get_marker_text_weight_3d_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.marker_setting_att.GetMarkerTextWeight3DInfo(
            io_admin_level, io_locked
        )

    def set_marker_2d_auto_naming_lock(self, i_locked: bool) -> None:
        return self.marker_setting_att.SetMarker2DAutoNamingLock(i_locked)

    def set_marker_3d_auto_naming_lock(self, i_locked: bool) -> None:
        return self.marker_setting_att.SetMarker3DAutoNamingLock(i_locked)

    def set_marker_defaults_color(self, i_red: int, i_green: int, i_blue: int) -> None:
        return self.marker_setting_att.SetMarkerDefaultsColor(i_red, i_green, i_blue)

    def set_marker_defaults_color_lock(self, i_locked: bool) -> None:
        return self.marker_setting_att.SetMarkerDefaultsColorLock(i_locked)

    def set_marker_defaults_dashed_lock(self, i_locked: bool) -> None:
        return self.marker_setting_att.SetMarkerDefaultsDashedLock(i_locked)

    def set_marker_defaults_weight_lock(self, i_locked: bool) -> None:
        return self.marker_setting_att.SetMarkerDefaultsWeightLock(i_locked)

    def set_marker_text_color_2d(self, i_red: int, i_green: int, i_blue: int) -> None:
        return self.marker_setting_att.SetMarkerTextColor2D(i_red, i_green, i_blue)

    def set_marker_text_color_2d_lock(self, i_locked: bool) -> None:
        return self.marker_setting_att.SetMarkerTextColor2DLock(i_locked)

    def set_marker_text_color_3d(self, i_red: int, i_green: int, i_blue: int) -> None:
        return self.marker_setting_att.SetMarkerTextColor3D(i_red, i_green, i_blue)

    def set_marker_text_color_3d_lock(self, i_locked: bool) -> None:
        return self.marker_setting_att.SetMarkerTextColor3DLock(i_locked)

    def set_marker_text_dashed_2d_lock(self, i_locked: bool) -> None:
        return self.marker_setting_att.SetMarkerTextDashed2DLock(i_locked)

    def set_marker_text_dashed_3d_lock(self, i_locked: bool) -> None:
        return self.marker_setting_att.SetMarkerTextDashed3DLock(i_locked)

    def set_marker_text_defaults_font_2d_lock(self, i_locked: bool) -> None:
        return self.marker_setting_att.SetMarkerTextDefaultsFont2DLock(i_locked)

    def set_marker_text_defaults_font_3d_lock(self, i_locked: bool) -> None:
        return self.marker_setting_att.SetMarkerTextDefaultsFont3DLock(i_locked)

    def set_marker_text_defaults_size_2d_lock(self, i_locked: bool) -> None:
        return self.marker_setting_att.SetMarkerTextDefaultsSize2DLock(i_locked)

    def set_marker_text_defaults_size_3d_lock(self, i_locked: bool) -> None:
        return self.marker_setting_att.SetMarkerTextDefaultsSize3DLock(i_locked)

    def set_marker_text_weight_2d_lock(self, i_locked: bool) -> None:
        return self.marker_setting_att.SetMarkerTextWeight2DLock(i_locked)

    def set_marker_text_weight_3d_lock(self, i_locked: bool) -> None:
        return self.marker_setting_att.SetMarkerTextWeight3DLock(i_locked)

    def __repr__(self):
        return f'MarkerSettingAtt(name="{self.name}")'
