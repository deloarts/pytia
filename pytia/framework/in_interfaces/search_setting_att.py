from pytia.framework.system_interfaces.setting_controller import SettingController


class SearchSettingAtt(SettingController):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.search_setting_att = com_object

    @property
    def deep_search_activation(self) -> bool:
        return self.search_setting_att.DeepSearchActivation

    @deep_search_activation.setter
    def deep_search_activation(self, value: bool):
        self.search_setting_att.DeepSearchActivation = value

    @property
    def default_power_input_context_priority(self) -> bool:
        return self.search_setting_att.DefaultPowerInputContextPriority

    @default_power_input_context_priority.setter
    def default_power_input_context_priority(self, value: bool):
        self.search_setting_att.DefaultPowerInputContextPriority = value

    @property
    def default_power_input_context_scope(self) -> int:
        return self.search_setting_att.DefaultPowerInputContextScope

    @default_power_input_context_scope.setter
    def default_power_input_context_scope(self, value: int):
        self.search_setting_att.DefaultPowerInputContextScope = value

    @property
    def default_power_input_prefix(self) -> str:
        return self.search_setting_att.DefaultPowerInputPrefix

    @default_power_input_prefix.setter
    def default_power_input_prefix(self, value: str):
        self.search_setting_att.DefaultPowerInputPrefix = value

    @property
    def max_displayed_results(self) -> int:
        return self.search_setting_att.MaxDisplayedResults

    @max_displayed_results.setter
    def max_displayed_results(self, value: int):
        self.search_setting_att.MaxDisplayedResults = value

    @property
    def max_pre_highlighted_elements(self) -> int:
        return self.search_setting_att.MaxPreHighlightedElements

    @max_pre_highlighted_elements.setter
    def max_pre_highlighted_elements(self, value: int):
        self.search_setting_att.MaxPreHighlightedElements = value

    def get_deep_search_activation_info(
        self, o_admin_level: str, o_locked: str
    ) -> bool:
        return self.search_setting_att.GetDeepSearchActivationInfo(
            o_admin_level, o_locked
        )

    def get_default_power_input_context_priority_info(
        self, o_admin_level: str, o_locked: str
    ) -> bool:
        return self.search_setting_att.GetDefaultPowerInputContextPriorityInfo(
            o_admin_level, o_locked
        )

    def get_default_power_input_context_scope_info(
        self, o_admin_level: str, o_locked: str
    ) -> bool:
        return self.search_setting_att.GetDefaultPowerInputContextScopeInfo(
            o_admin_level, o_locked
        )

    def get_default_power_input_prefix_info(
        self, o_admin_level: str, o_locked: str
    ) -> bool:
        return self.search_setting_att.GetDefaultPowerInputPrefixInfo(
            o_admin_level, o_locked
        )

    def get_max_displayed_results_info(self, o_admin_level: str, o_locked: str) -> bool:
        return self.search_setting_att.GetMaxDisplayedResultsInfo(
            o_admin_level, o_locked
        )

    def get_max_pre_highlighted_elements_info(
        self, o_admin_level: str, o_locked: str
    ) -> bool:
        return self.search_setting_att.GetMaxPreHighlightedElementsInfo(
            o_admin_level, o_locked
        )

    def set_deep_search_activation_lock(self, i_locked: bool) -> None:
        return self.search_setting_att.SetDeepSearchActivationLock(i_locked)

    def set_default_power_input_context_priority_lock(self, i_locked: bool) -> None:
        return self.search_setting_att.SetDefaultPowerInputContextPriorityLock(i_locked)

    def set_default_power_input_context_scope_lock(self, i_locked: bool) -> None:
        return self.search_setting_att.SetDefaultPowerInputContextScopeLock(i_locked)

    def set_default_power_input_prefix_lock(self, i_locked: bool) -> None:
        return self.search_setting_att.SetDefaultPowerInputPrefixLock(i_locked)

    def set_max_displayed_results_lock(self, i_locked: bool) -> None:
        return self.search_setting_att.SetMaxDisplayedResultsLock(i_locked)

    def set_max_pre_highlighted_elements_lock(self, i_locked: bool) -> None:
        return self.search_setting_att.SetMaxPreHighlightedElementsLock(i_locked)

    def __repr__(self):
        return f'SearchSettingAtt(name="{ self.name }")'
