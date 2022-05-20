from pytia.framework.system_interfaces.setting_controller import SettingController


class TreeVizManipSettingAtt(SettingController):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.tree_viz_manip_setting_att = com_object

    @property
    def arc_selection_activation(self) -> bool:
        return self.tree_viz_manip_setting_att.ArcSelectionActivation

    @arc_selection_activation.setter
    def arc_selection_activation(self, value: bool):
        self.tree_viz_manip_setting_att.ArcSelectionActivation = value

    @property
    def auto_expand_activation(self) -> bool:
        return self.tree_viz_manip_setting_att.AutoExpandActivation

    @auto_expand_activation.setter
    def auto_expand_activation(self, value: bool):
        self.tree_viz_manip_setting_att.AutoExpandActivation = value

    @property
    def auto_scroll_activation(self) -> bool:
        return self.tree_viz_manip_setting_att.AutoScrollActivation

    @auto_scroll_activation.setter
    def auto_scroll_activation(self, value: bool):
        self.tree_viz_manip_setting_att.AutoScrollActivation = value

    @property
    def display_geom_on_scrolling(self) -> bool:
        return self.tree_viz_manip_setting_att.DisplayGeomOnScrolling

    @display_geom_on_scrolling.setter
    def display_geom_on_scrolling(self, value: bool):
        self.tree_viz_manip_setting_att.DisplayGeomOnScrolling = value

    @property
    def orientation(self) -> int:
        return self.tree_viz_manip_setting_att.Orientation

    @orientation.setter
    def orientation(self, value: int):
        self.tree_viz_manip_setting_att.Orientation = value

    @property
    def show_activation(self) -> bool:
        return self.tree_viz_manip_setting_att.ShowActivation

    @show_activation.setter
    def show_activation(self, value: bool):
        self.tree_viz_manip_setting_att.ShowActivation = value

    @property
    def size(self) -> int:
        return self.tree_viz_manip_setting_att.Size

    @size.setter
    def size(self, value: int):
        self.tree_viz_manip_setting_att.Size = value

    @property
    def size_type(self) -> int:
        return self.tree_viz_manip_setting_att.SizeType

    @size_type.setter
    def size_type(self, value: int):
        self.tree_viz_manip_setting_att.SizeType = value

    @property
    def type(self) -> int:
        return self.tree_viz_manip_setting_att.Type

    @type.setter
    def type(self, value: int):
        self.tree_viz_manip_setting_att.Type = value

    def get_arc_selection_activation_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.tree_viz_manip_setting_att.GetArcSelectionActivationInfo(
            io_admin_level, io_locked
        )

    def get_auto_expand_activation_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.tree_viz_manip_setting_att.GetAutoExpandActivationInfo(
            io_admin_level, io_locked
        )

    def get_auto_scroll_activation_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.tree_viz_manip_setting_att.GetAutoScrollActivationInfo(
            io_admin_level, io_locked
        )

    def get_display_geom_on_scrolling_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.tree_viz_manip_setting_att.GetDisplayGeomOnScrollingInfo(
            io_admin_level, io_locked
        )

    def get_orientation_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.tree_viz_manip_setting_att.GetOrientationInfo(
            io_admin_level, io_locked
        )

    def get_show_activation_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.tree_viz_manip_setting_att.GetShowActivationInfo(
            io_admin_level, io_locked
        )

    def get_size_type_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.tree_viz_manip_setting_att.GetSizeTypeInfo(
            io_admin_level, io_locked
        )

    def get_type_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.tree_viz_manip_setting_att.GetTypeInfo(io_admin_level, io_locked)

    def set_arc_selection_activation_lock(self, i_locked: bool) -> None:
        return self.tree_viz_manip_setting_att.SetArcSelectionActivationLock(i_locked)

    def set_auto_expand_activation_lock(self, i_locked: bool) -> None:
        return self.tree_viz_manip_setting_att.SetAutoExpandActivationLock(i_locked)

    def set_auto_scroll_activation_lock(self, i_locked: bool) -> None:
        return self.tree_viz_manip_setting_att.SetAutoScrollActivationLock(i_locked)

    def set_display_geom_on_scrolling_lock(self, i_locked: bool) -> None:
        return self.tree_viz_manip_setting_att.SetDisplayGeomOnScrollingLock(i_locked)

    def set_orientation_lock(self, i_locked: bool) -> None:
        return self.tree_viz_manip_setting_att.SetOrientationLock(i_locked)

    def set_show_activation_lock(self, i_locked: bool) -> None:
        return self.tree_viz_manip_setting_att.SetShowActivationLock(i_locked)

    def set_size_type_lock(self, i_locked: bool) -> None:
        return self.tree_viz_manip_setting_att.SetSizeTypeLock(i_locked)

    def set_type_lock(self, i_locked: bool) -> None:
        return self.tree_viz_manip_setting_att.SetTypeLock(i_locked)

    def __repr__(self):
        return f'TreeVizManipSettingAtt(name="{ self.name }")'
