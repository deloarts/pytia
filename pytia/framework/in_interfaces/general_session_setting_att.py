from pytia.framework.system_interfaces.setting_controller import SettingController


class GeneralSessionSettingAtt(SettingController):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.general_session_setting_att = com_object

    @property
    def auto_save(self) -> int:
        return self.general_session_setting_att.AutoSave

    @auto_save.setter
    def auto_save(self, value: int):
        self.general_session_setting_att.AutoSave = value

    @property
    def conferencing(self) -> int:
        return self.general_session_setting_att.Conferencing

    @conferencing.setter
    def conferencing(self, value: int):
        self.general_session_setting_att.Conferencing = value

    @property
    def drag_drop(self) -> bool:
        return self.general_session_setting_att.DragDrop

    @drag_drop.setter
    def drag_drop(self, value: bool):
        self.general_session_setting_att.DragDrop = value

    @property
    def ref_doc(self) -> bool:
        return self.general_session_setting_att.RefDoc

    @ref_doc.setter
    def ref_doc(self, value: bool):
        self.general_session_setting_att.RefDoc = value

    @property
    def time_roll(self) -> int:
        return self.general_session_setting_att.TimeRoll

    @time_roll.setter
    def time_roll(self, value: int):
        self.general_session_setting_att.TimeRoll = value

    @property
    def ui_style(self) -> int:
        return self.general_session_setting_att.UIStyle

    @ui_style.setter
    def ui_style(self, value: int):
        self.general_session_setting_att.UIStyle = value

    def get_auto_save_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.general_session_setting_att.GetAutoSaveInfo(
            io_admin_level, io_locked
        )

    def get_conferencing_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.general_session_setting_att.GetConferencingInfo(
            io_admin_level, io_locked
        )

    def get_drag_drop_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.general_session_setting_att.GetDragDropInfo(
            io_admin_level, io_locked
        )

    def get_ref_doc_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.general_session_setting_att.GetRefDocInfo(io_admin_level, io_locked)

    def get_ui_style_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.general_session_setting_att.GetUIStyleInfo(
            io_admin_level, io_locked
        )

    def set_auto_save_lock(self, i_locked: bool) -> None:
        return self.general_session_setting_att.SetAutoSaveLock(i_locked)

    def set_conferencing_lock(self, i_locked: bool) -> None:
        return self.general_session_setting_att.SetConferencingLock(i_locked)

    def set_drag_drop_lock(self, i_locked: bool) -> None:
        return self.general_session_setting_att.SetDragDropLock(i_locked)

    def set_ref_doc_lock(self, i_locked: bool) -> None:
        return self.general_session_setting_att.SetRefDocLock(i_locked)

    def set_ui_style_lock(self, i_locked: bool) -> None:
        return self.general_session_setting_att.SetUIStyleLock(i_locked)

    def __repr__(self):
        return f'GeneralSessionSettingAtt(name="{ self.name }")'
