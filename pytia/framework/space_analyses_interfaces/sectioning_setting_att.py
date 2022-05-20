from pytia.framework.system_interfaces.setting_controller import SettingController


class SectioningSettingAtt(SettingController):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.sectioning_setting_att = com_object

    @property
    def clipping_mode(self) -> int:
        return self.sectioning_setting_att.ClippingMode

    @clipping_mode.setter
    def clipping_mode(self, value: int):
        self.sectioning_setting_att.ClippingMode = value

    @property
    def display_cut_in_wireframe(self) -> bool:
        return self.sectioning_setting_att.DisplayCutInWireframe

    @display_cut_in_wireframe.setter
    def display_cut_in_wireframe(self, value: bool):
        self.sectioning_setting_att.DisplayCutInWireframe = value

    @property
    def grid_auto_filtering(self) -> bool:
        return self.sectioning_setting_att.GridAutoFiltering

    @grid_auto_filtering.setter
    def grid_auto_filtering(self, value: bool):
        self.sectioning_setting_att.GridAutoFiltering = value

    @property
    def grid_auto_resize(self) -> bool:
        return self.sectioning_setting_att.GridAutoResize

    @grid_auto_resize.setter
    def grid_auto_resize(self, value: bool):
        self.sectioning_setting_att.GridAutoResize = value

    @property
    def grid_height_step(self) -> float:
        return self.sectioning_setting_att.GridHeightStep

    @grid_height_step.setter
    def grid_height_step(self, value: float):
        self.sectioning_setting_att.GridHeightStep = value

    @property
    def grid_position_mode(self) -> int:
        return self.sectioning_setting_att.GridPositionMode

    @grid_position_mode.setter
    def grid_position_mode(self, value: int):
        self.sectioning_setting_att.GridPositionMode = value

    @property
    def grid_style(self) -> int:
        return self.sectioning_setting_att.GridStyle

    @grid_style.setter
    def grid_style(self, value: int):
        self.sectioning_setting_att.GridStyle = value

    @property
    def grid_width_step(self) -> float:
        return self.sectioning_setting_att.GridWidthStep

    @grid_width_step.setter
    def grid_width_step(self, value: float):
        self.sectioning_setting_att.GridWidthStep = value

    @property
    def hide_plane(self) -> bool:
        return self.sectioning_setting_att.HidePlane

    @hide_plane.setter
    def hide_plane(self, value: bool):
        self.sectioning_setting_att.HidePlane = value

    @property
    def hide_result(self) -> bool:
        return self.sectioning_setting_att.HideResult

    @hide_result.setter
    def hide_result(self, value: bool):
        self.sectioning_setting_att.HideResult = value

    @property
    def plane_normal(self) -> int:
        return self.sectioning_setting_att.PlaneNormal

    @plane_normal.setter
    def plane_normal(self, value: int):
        self.sectioning_setting_att.PlaneNormal = value

    @property
    def plane_origin(self) -> int:
        return self.sectioning_setting_att.PlaneOrigin

    @plane_origin.setter
    def plane_origin(self, value: int):
        self.sectioning_setting_att.PlaneOrigin = value

    @property
    def section_export_type(self) -> bool:
        return self.sectioning_setting_att.SectionExportType

    @section_export_type.setter
    def section_export_type(self, value: bool):
        self.sectioning_setting_att.SectionExportType = value

    @property
    def section_fill(self) -> bool:
        return self.sectioning_setting_att.SectionFill

    @section_fill.setter
    def section_fill(self, value: bool):
        self.sectioning_setting_att.SectionFill = value

    @property
    def update_result(self) -> bool:
        return self.sectioning_setting_att.UpdateResult

    @update_result.setter
    def update_result(self, value: bool):
        self.sectioning_setting_att.UpdateResult = value

    @property
    def viewer_auto_open(self) -> bool:
        return self.sectioning_setting_att.ViewerAutoOpen

    @viewer_auto_open.setter
    def viewer_auto_open(self, value: bool):
        self.sectioning_setting_att.ViewerAutoOpen = value

    @property
    def viewer_auto_reframe(self) -> bool:
        return self.sectioning_setting_att.ViewerAutoReframe

    @viewer_auto_reframe.setter
    def viewer_auto_reframe(self, value: bool):
        self.sectioning_setting_att.ViewerAutoReframe = value

    @property
    def viewer_lock_2d(self) -> bool:
        return self.sectioning_setting_att.ViewerLock2D

    @viewer_lock_2d.setter
    def viewer_lock_2d(self, value: bool):
        self.sectioning_setting_att.ViewerLock2D = value

    @property
    def window_default_height(self) -> int:
        return self.sectioning_setting_att.WindowDefaultHeight

    @window_default_height.setter
    def window_default_height(self, value: int):
        self.sectioning_setting_att.WindowDefaultHeight = value

    @property
    def window_default_width(self) -> int:
        return self.sectioning_setting_att.WindowDefaultWidth

    @window_default_width.setter
    def window_default_width(self, value: int):
        self.sectioning_setting_att.WindowDefaultWidth = value

    @property
    def window_open_mode(self) -> int:
        return self.sectioning_setting_att.WindowOpenMode

    @window_open_mode.setter
    def window_open_mode(self, value: int):
        self.sectioning_setting_att.WindowOpenMode = value

    def get_clipping_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.sectioning_setting_att.GetClippingModeInfo(
            io_admin_level, io_locked
        )

    def get_display_cut_in_wireframe_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.sectioning_setting_att.GetDisplayCutInWireframeInfo(
            io_admin_level, io_locked
        )

    def get_grid_auto_filtering_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.sectioning_setting_att.GetGridAutoFilteringInfo(
            io_admin_level, io_locked
        )

    def get_grid_auto_resize_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.sectioning_setting_att.GetGridAutoResizeInfo(
            io_admin_level, io_locked
        )

    def get_grid_height_step_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.sectioning_setting_att.GetGridHeightStepInfo(
            io_admin_level, io_locked
        )

    def get_grid_position_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.sectioning_setting_att.GetGridPositionModeInfo(
            io_admin_level, io_locked
        )

    def get_grid_style_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.sectioning_setting_att.GetGridStyleInfo(io_admin_level, io_locked)

    def get_grid_width_step_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.sectioning_setting_att.GetGridWidthStepInfo(
            io_admin_level, io_locked
        )

    def get_hide_plane_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.sectioning_setting_att.GetHidePlaneInfo(io_admin_level, io_locked)

    def get_hide_result_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.sectioning_setting_att.GetHideResultInfo(io_admin_level, io_locked)

    def get_plane_color(self, o_r: int, o_g: int, o_b: int) -> None:
        return self.sectioning_setting_att.GetPlaneColor(o_r, o_g, o_b)

    def get_plane_color_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.sectioning_setting_att.GetPlaneColorInfo(io_admin_level, io_locked)

    def get_plane_normal_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.sectioning_setting_att.GetPlaneNormalInfo(io_admin_level, io_locked)

    def get_plane_origin_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.sectioning_setting_att.GetPlaneOriginInfo(io_admin_level, io_locked)

    def get_section_export_type_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.sectioning_setting_att.GetSectionExportTypeInfo(
            io_admin_level, io_locked
        )

    def get_section_fill_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.sectioning_setting_att.GetSectionFillInfo(io_admin_level, io_locked)

    def get_update_result_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.sectioning_setting_att.GetUpdateResultInfo(
            io_admin_level, io_locked
        )

    def get_viewer_auto_open_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.sectioning_setting_att.GetViewerAutoOpenInfo(
            io_admin_level, io_locked
        )

    def get_viewer_auto_reframe_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.sectioning_setting_att.GetViewerAutoReframeInfo(
            io_admin_level, io_locked
        )

    def get_viewer_lock2_d_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.sectioning_setting_att.GetViewerLock2DInfo(
            io_admin_level, io_locked
        )

    def get_window_default_height_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.sectioning_setting_att.GetWindowDefaultHeightInfo(
            io_admin_level, io_locked
        )

    def get_window_default_width_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.sectioning_setting_att.GetWindowDefaultWidthInfo(
            io_admin_level, io_locked
        )

    def get_window_open_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.sectioning_setting_att.GetWindowOpenModeInfo(
            io_admin_level, io_locked
        )

    def set_clipping_mode_lock(self, i_locked: bool) -> None:
        return self.sectioning_setting_att.SetClippingModeLock(i_locked)

    def set_display_cut_in_wireframe_lock(self, i_locked: bool) -> None:
        return self.sectioning_setting_att.SetDisplayCutInWireframeLock(i_locked)

    def set_grid_auto_filtering_lock(self, i_locked: bool) -> None:
        return self.sectioning_setting_att.SetGridAutoFilteringLock(i_locked)

    def set_grid_auto_resize_lock(self, i_locked: bool) -> None:
        return self.sectioning_setting_att.SetGridAutoResizeLock(i_locked)

    def set_grid_height_step_lock(self, i_locked: bool) -> None:
        return self.sectioning_setting_att.SetGridHeightStepLock(i_locked)

    def set_grid_position_mode_lock(self, i_locked: bool) -> None:
        return self.sectioning_setting_att.SetGridPositionModeLock(i_locked)

    def set_grid_style_lock(self, i_locked: bool) -> None:
        return self.sectioning_setting_att.SetGridStyleLock(i_locked)

    def set_grid_width_step_lock(self, i_locked: bool) -> None:
        return self.sectioning_setting_att.SetGridWidthStepLock(i_locked)

    def set_hide_plane_lock(self, i_locked: bool) -> None:
        return self.sectioning_setting_att.SetHidePlaneLock(i_locked)

    def set_hide_result_lock(self, i_locked: bool) -> None:
        return self.sectioning_setting_att.SetHideResultLock(i_locked)

    def set_plane_color(self, i_r: int, i_g: int, i_b: int) -> None:
        return self.sectioning_setting_att.SetPlaneColor(i_r, i_g, i_b)

    def set_plane_color_lock(self, i_locked: bool) -> None:
        return self.sectioning_setting_att.SetPlaneColorLock(i_locked)

    def set_plane_normal_lock(self, i_locked: bool) -> None:
        return self.sectioning_setting_att.SetPlaneNormalLock(i_locked)

    def set_plane_origin_lock(self, i_locked: bool) -> None:
        return self.sectioning_setting_att.SetPlaneOriginLock(i_locked)

    def set_section_export_type_lock(self, i_locked: bool) -> None:
        return self.sectioning_setting_att.SetSectionExportTypeLock(i_locked)

    def set_section_fill_lock(self, i_locked: bool) -> None:
        return self.sectioning_setting_att.SetSectionFillLock(i_locked)

    def set_update_result_lock(self, i_locked: bool) -> None:
        return self.sectioning_setting_att.SetUpdateResultLock(i_locked)

    def set_viewer_auto_open_lock(self, i_locked: bool) -> None:
        return self.sectioning_setting_att.SetViewerAutoOpenLock(i_locked)

    def set_viewer_auto_reframe_lock(self, i_locked: bool) -> None:
        return self.sectioning_setting_att.SetViewerAutoReframeLock(i_locked)

    def set_viewer_lock2_d_lock(self, i_locked: bool) -> None:
        return self.sectioning_setting_att.SetViewerLock2DLock(i_locked)

    def set_window_default_height_lock(self, i_locked: bool) -> None:
        return self.sectioning_setting_att.SetWindowDefaultHeightLock(i_locked)

    def set_window_default_width_lock(self, i_locked: bool) -> None:
        return self.sectioning_setting_att.SetWindowDefaultWidthLock(i_locked)

    def set_window_open_mode_lock(self, i_locked: bool) -> None:
        return self.sectioning_setting_att.SetWindowOpenModeLock(i_locked)

    def __repr__(self):
        return f'SectioningSettingAtt(name="{self.name}")'
