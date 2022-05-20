from pytia.framework.system_interfaces.setting_controller import SettingController


class KnowledgeSheetSettingAtt(SettingController):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.knowledge_sheet_setting_att = com_object

    @property
    def design_tables_copy_data(self) -> int:
        return self.knowledge_sheet_setting_att.DesignTablesCopyData

    @design_tables_copy_data.setter
    def design_tables_copy_data(self, value: int):
        self.knowledge_sheet_setting_att.DesignTablesCopyData = value

    @property
    def design_tables_synchronization(self) -> int:
        return self.knowledge_sheet_setting_att.DesignTablesSynchronization

    @design_tables_synchronization.setter
    def design_tables_synchronization(self, value: int):
        self.knowledge_sheet_setting_att.DesignTablesSynchronization = value

    @property
    def parameter_name_surrounded_by_the_symbol(self) -> int:
        return self.knowledge_sheet_setting_att.ParameterNameSurroundedByTheSymbol

    @parameter_name_surrounded_by_the_symbol.setter
    def parameter_name_surrounded_by_the_symbol(self, value: int):
        self.knowledge_sheet_setting_att.ParameterNameSurroundedByTheSymbol = value

    @property
    def parameter_tree_view_with_formula(self) -> int:
        return self.knowledge_sheet_setting_att.ParameterTreeViewWithFormula

    @parameter_tree_view_with_formula.setter
    def parameter_tree_view_with_formula(self, value: int):
        self.knowledge_sheet_setting_att.ParameterTreeViewWithFormula = value

    @property
    def parameter_tree_view_with_value(self) -> int:
        return self.knowledge_sheet_setting_att.ParameterTreeViewWithValue

    @parameter_tree_view_with_value.setter
    def parameter_tree_view_with_value(self, value: int):
        self.knowledge_sheet_setting_att.ParameterTreeViewWithValue = value

    @property
    def relations_update_in_part_context_evaluate_during_update(self) -> int:
        return (
            self.knowledge_sheet_setting_att.RelationsUpdateInPartContextEvaluateDuringUpdate
        )

    @relations_update_in_part_context_evaluate_during_update.setter
    def relations_update_in_part_context_evaluate_during_update(self, value: int):
        self.knowledge_sheet_setting_att.RelationsUpdateInPartContextEvaluateDuringUpdate = (
            value
        )

    @property
    def relations_update_in_part_context_synchronous_relations(self) -> int:
        return (
            self.knowledge_sheet_setting_att.RelationsUpdateInPartContextSynchronousRelations
        )

    @relations_update_in_part_context_synchronous_relations.setter
    def relations_update_in_part_context_synchronous_relations(self, value: int):
        self.knowledge_sheet_setting_att.RelationsUpdateInPartContextSynchronousRelations = (
            value
        )

    def get_design_tables_copy_data_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.knowledge_sheet_setting_att.GetDesignTablesCopyDataInfo(
            io_admin_level, io_locked
        )

    def get_design_tables_synchronization_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.knowledge_sheet_setting_att.GetDesignTablesSynchronizationInfo(
            io_admin_level, io_locked
        )

    def get_parameter_name_surrounded_by_the_symbol_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return (
            self.knowledge_sheet_setting_att.GetParameterNameSurroundedByTheSymbolInfo(
                io_admin_level, io_locked
            )
        )

    def get_parameter_tree_view_with_formula_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.knowledge_sheet_setting_att.GetParameterTreeViewWithFormulaInfo(
            io_admin_level, io_locked
        )

    def get_parameter_tree_view_with_value_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.knowledge_sheet_setting_att.GetParameterTreeViewWithValueInfo(
            io_admin_level, io_locked
        )

    def get_relations_update_in_part_context_evaluate_during_update_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.knowledge_sheet_setting_att.GetRelationsUpdateInPartContextEvaluateDuringUpdateInfo(
            io_admin_level, io_locked
        )

    def get_relations_update_in_part_context_synchronous_relations_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.knowledge_sheet_setting_att.GetRelationsUpdateInPartContextSynchronousRelationsInfo(
            io_admin_level, io_locked
        )

    def set_design_tables_copy_data_lock(self, i_locked: bool) -> None:
        return self.knowledge_sheet_setting_att.SetDesignTablesCopyDataLock(i_locked)

    def set_design_tables_synchronization_lock(self, i_locked: bool) -> None:
        return self.knowledge_sheet_setting_att.SetDesignTablesSynchronizationLock(
            i_locked
        )

    def set_parameter_name_surrounded_by_the_symbol_lock(self, i_locked: bool) -> None:
        return (
            self.knowledge_sheet_setting_att.SetParameterNameSurroundedByTheSymbolLock(
                i_locked
            )
        )

    def set_parameter_tree_view_with_formula_lock(self, i_locked: bool) -> None:
        return self.knowledge_sheet_setting_att.SetParameterTreeViewWithFormulaLock(
            i_locked
        )

    def set_parameter_tree_view_with_value_lock(self, i_locked: bool) -> None:
        return self.knowledge_sheet_setting_att.SetParameterTreeViewWithValueLock(
            i_locked
        )

    def set_relations_update_in_part_context_evaluate_during_update_lock(
        self, i_locked: bool
    ) -> None:
        return self.knowledge_sheet_setting_att.SetRelationsUpdateInPartContextEvaluateDuringUpdateLock(
            i_locked
        )

    def set_relations_update_in_part_context_synchronous_relations_lock(
        self, i_locked: bool
    ) -> None:
        return self.knowledge_sheet_setting_att.SetRelationsUpdateInPartContextSynchronousRelationsLock(
            i_locked
        )

    def __repr__(self):
        return f'KnowledgeSheetSettingAtt(name="{self.name}")'
