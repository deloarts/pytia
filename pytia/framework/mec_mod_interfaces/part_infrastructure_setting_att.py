from pytia.framework.system_interfaces.setting_controller import SettingController


class PartInfrastructureSettingAtt(SettingController):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.part_infrastructure_setting_att = com_object

    @property
    def also_delete_exclusive_parents(self) -> bool:
        return self.part_infrastructure_setting_att.AlsoDeleteExclusiveParents

    @also_delete_exclusive_parents.setter
    def also_delete_exclusive_parents(self, value: bool):
        self.part_infrastructure_setting_att.AlsoDeleteExclusiveParents = value

    @property
    def axis_system_size(self) -> int:
        return self.part_infrastructure_setting_att.AxisSystemSize

    @axis_system_size.setter
    def axis_system_size(self, value: int):
        self.part_infrastructure_setting_att.AxisSystemSize = value

    @property
    def bodies_under_operations_in_tree(self) -> bool:
        return self.part_infrastructure_setting_att.BodiesUnderOperationsInTree

    @bodies_under_operations_in_tree.setter
    def bodies_under_operations_in_tree(self, value: bool):
        self.part_infrastructure_setting_att.BodiesUnderOperationsInTree = value

    @property
    def color_synchronization_editability(self) -> bool:
        return self.part_infrastructure_setting_att.ColorSynchronizationEditability

    @color_synchronization_editability.setter
    def color_synchronization_editability(self, value: bool):
        self.part_infrastructure_setting_att.ColorSynchronizationEditability = value

    @property
    def color_synchronization_mode(self) -> bool:
        return self.part_infrastructure_setting_att.ColorSynchronizationMode

    @color_synchronization_mode.setter
    def color_synchronization_mode(self, value: bool):
        self.part_infrastructure_setting_att.ColorSynchronizationMode = value

    @property
    def color_synchronization_mode_manage(self) -> bool:
        return self.part_infrastructure_setting_att.ColorSynchronizationModeManage

    @color_synchronization_mode_manage.setter
    def color_synchronization_mode_manage(self, value: bool):
        self.part_infrastructure_setting_att.ColorSynchronizationModeManage = value

    @property
    def color_synchronization_mode_on_feature(self) -> bool:
        return self.part_infrastructure_setting_att.ColorSynchronizationModeOnFeature

    @color_synchronization_mode_on_feature.setter
    def color_synchronization_mode_on_feature(self, value: bool):
        self.part_infrastructure_setting_att.ColorSynchronizationModeOnFeature = value

    @property
    def color_synchronization_mode_on_sub_elements(self) -> bool:
        return (
            self.part_infrastructure_setting_att.ColorSynchronizationModeOnSubElements
        )

    @color_synchronization_mode_on_sub_elements.setter
    def color_synchronization_mode_on_sub_elements(self, value: bool):
        self.part_infrastructure_setting_att.ColorSynchronizationModeOnSubElements = (
            value
        )

    @property
    def colors3_d_experience_management(self) -> bool:
        return self.part_infrastructure_setting_att.Colors3DExperienceManagement

    @colors3_d_experience_management.setter
    def colors3_d_experience_management(self, value: bool):
        self.part_infrastructure_setting_att.Colors3DExperienceManagement = value

    @property
    def constraints_in_geometry(self) -> bool:
        return self.part_infrastructure_setting_att.ConstraintsInGeometry

    @constraints_in_geometry.setter
    def constraints_in_geometry(self, value: bool):
        self.part_infrastructure_setting_att.ConstraintsInGeometry = value

    @property
    def constraints_node_in_tree(self) -> bool:
        return self.part_infrastructure_setting_att.ConstraintsNodeInTree

    @constraints_node_in_tree.setter
    def constraints_node_in_tree(self, value: bool):
        self.part_infrastructure_setting_att.ConstraintsNodeInTree = value

    @property
    def contextual_features_selectable_at_creation(self) -> bool:
        return (
            self.part_infrastructure_setting_att.ContextualFeaturesSelectableAtCreation
        )

    @contextual_features_selectable_at_creation.setter
    def contextual_features_selectable_at_creation(self, value: bool):
        self.part_infrastructure_setting_att.ContextualFeaturesSelectableAtCreation = (
            value
        )

    @property
    def default_colors_editability(self) -> bool:
        return self.part_infrastructure_setting_att.DefaultColorsEditability

    @default_colors_editability.setter
    def default_colors_editability(self, value: bool):
        self.part_infrastructure_setting_att.DefaultColorsEditability = value

    @property
    def delete_warning_box(self) -> bool:
        return self.part_infrastructure_setting_att.DeleteWarningBox

    @delete_warning_box.setter
    def delete_warning_box(self, value: bool):
        self.part_infrastructure_setting_att.DeleteWarningBox = value

    @property
    def display_geometry_after_current(self) -> bool:
        return self.part_infrastructure_setting_att.DisplayGeometryAfterCurrent

    @display_geometry_after_current.setter
    def display_geometry_after_current(self, value: bool):
        self.part_infrastructure_setting_att.DisplayGeometryAfterCurrent = value

    @property
    def expand_sketch_based_features_node_at_creation(self) -> bool:
        return (
            self.part_infrastructure_setting_att.ExpandSketchBasedFeaturesNodeAtCreation
        )

    @expand_sketch_based_features_node_at_creation.setter
    def expand_sketch_based_features_node_at_creation(self, value: bool):
        self.part_infrastructure_setting_att.ExpandSketchBasedFeaturesNodeAtCreation = (
            value
        )

    @property
    def external_references_as_visible(self) -> bool:
        return self.part_infrastructure_setting_att.ExternalReferencesAsVisible

    @external_references_as_visible.setter
    def external_references_as_visible(self, value: bool):
        self.part_infrastructure_setting_att.ExternalReferencesAsVisible = value

    @property
    def external_references_assembly_root_context(self) -> bool:
        return (
            self.part_infrastructure_setting_att.ExternalReferencesAssemblyRootContext
        )

    @external_references_assembly_root_context.setter
    def external_references_assembly_root_context(self, value: bool):
        self.part_infrastructure_setting_att.ExternalReferencesAssemblyRootContext = (
            value
        )

    @property
    def external_references_node_in_tree(self) -> bool:
        return self.part_infrastructure_setting_att.ExternalReferencesNodeInTree

    @external_references_node_in_tree.setter
    def external_references_node_in_tree(self, value: bool):
        self.part_infrastructure_setting_att.ExternalReferencesNodeInTree = value

    @property
    def hybrid_design_mode(self) -> bool:
        return self.part_infrastructure_setting_att.HybridDesignMode

    @hybrid_design_mode.setter
    def hybrid_design_mode(self, value: bool):
        self.part_infrastructure_setting_att.HybridDesignMode = value

    @property
    def knowledge_in_hybrid_design_mode(self) -> bool:
        return self.part_infrastructure_setting_att.KnowledgeInHybridDesignMode

    @knowledge_in_hybrid_design_mode.setter
    def knowledge_in_hybrid_design_mode(self, value: bool):
        self.part_infrastructure_setting_att.KnowledgeInHybridDesignMode = value

    @property
    def linked_external_references(self) -> bool:
        return self.part_infrastructure_setting_att.LinkedExternalReferences

    @linked_external_references.setter
    def linked_external_references(self, value: bool):
        self.part_infrastructure_setting_att.LinkedExternalReferences = value

    @property
    def linked_external_references_only_on_publication(self) -> bool:
        return (
            self.part_infrastructure_setting_att.LinkedExternalReferencesOnlyOnPublication
        )

    @linked_external_references_only_on_publication.setter
    def linked_external_references_only_on_publication(self, value: bool):
        self.part_infrastructure_setting_att.LinkedExternalReferencesOnlyOnPublication = (
            value
        )

    @property
    def linked_external_references_warning_at_creation(self) -> bool:
        return (
            self.part_infrastructure_setting_att.LinkedExternalReferencesWarningAtCreation
        )

    @linked_external_references_warning_at_creation.setter
    def linked_external_references_warning_at_creation(self, value: bool):
        self.part_infrastructure_setting_att.LinkedExternalReferencesWarningAtCreation = (
            value
        )

    @property
    def naming_mode(self) -> int:
        return self.part_infrastructure_setting_att.NamingMode

    @naming_mode.setter
    def naming_mode(self, value: int):
        self.part_infrastructure_setting_att.NamingMode = value

    @property
    def new_with3_d_support(self) -> bool:
        return self.part_infrastructure_setting_att.NewWith3DSupport

    @new_with3_d_support.setter
    def new_with3_d_support(self, value: bool):
        self.part_infrastructure_setting_att.NewWith3DSupport = value

    @property
    def new_with_axis_system(self) -> bool:
        return self.part_infrastructure_setting_att.NewWithAxisSystem

    @new_with_axis_system.setter
    def new_with_axis_system(self, value: bool):
        self.part_infrastructure_setting_att.NewWithAxisSystem = value

    @property
    def new_with_gs(self) -> bool:
        return self.part_infrastructure_setting_att.NewWithGS

    @new_with_gs.setter
    def new_with_gs(self, value: bool):
        self.part_infrastructure_setting_att.NewWithGS = value

    @property
    def new_with_ogs(self) -> bool:
        return self.part_infrastructure_setting_att.NewWithOGS

    @new_with_ogs.setter
    def new_with_ogs(self, value: bool):
        self.part_infrastructure_setting_att.NewWithOGS = value

    @property
    def new_with_panel(self) -> bool:
        return self.part_infrastructure_setting_att.NewWithPanel

    @new_with_panel.setter
    def new_with_panel(self, value: bool):
        self.part_infrastructure_setting_att.NewWithPanel = value

    @property
    def only_current_operated_solid_set_in_geometry(self) -> bool:
        return (
            self.part_infrastructure_setting_att.OnlyCurrentOperatedSolidSetInGeometry
        )

    @only_current_operated_solid_set_in_geometry.setter
    def only_current_operated_solid_set_in_geometry(self, value: bool):
        self.part_infrastructure_setting_att.OnlyCurrentOperatedSolidSetInGeometry = (
            value
        )

    @property
    def only_current_solid_set_in_geometry(self) -> bool:
        return self.part_infrastructure_setting_att.OnlyCurrentSolidSetInGeometry

    @only_current_solid_set_in_geometry.setter
    def only_current_solid_set_in_geometry(self, value: bool):
        self.part_infrastructure_setting_att.OnlyCurrentSolidSetInGeometry = value

    @property
    def parameters_node_in_tree(self) -> bool:
        return self.part_infrastructure_setting_att.ParametersNodeInTree

    @parameters_node_in_tree.setter
    def parameters_node_in_tree(self, value: bool):
        self.part_infrastructure_setting_att.ParametersNodeInTree = value

    @property
    def publish_topological_elements(self) -> bool:
        return self.part_infrastructure_setting_att.PublishTopologicalElements

    @publish_topological_elements.setter
    def publish_topological_elements(self, value: bool):
        self.part_infrastructure_setting_att.PublishTopologicalElements = value

    @property
    def relations_node_in_tree(self) -> bool:
        return self.part_infrastructure_setting_att.RelationsNodeInTree

    @relations_node_in_tree.setter
    def relations_node_in_tree(self, value: bool):
        self.part_infrastructure_setting_att.RelationsNodeInTree = value

    @property
    def replace_only_after_current(self) -> bool:
        return self.part_infrastructure_setting_att.ReplaceOnlyAfterCurrent

    @replace_only_after_current.setter
    def replace_only_after_current(self, value: bool):
        self.part_infrastructure_setting_att.ReplaceOnlyAfterCurrent = value

    @property
    def surface_elements_location(self) -> int:
        return self.part_infrastructure_setting_att.SurfaceElementsLocation

    @surface_elements_location.setter
    def surface_elements_location(self, value: int):
        self.part_infrastructure_setting_att.SurfaceElementsLocation = value

    @property
    def true_color_mode(self) -> bool:
        return self.part_infrastructure_setting_att.TrueColorMode

    @true_color_mode.setter
    def true_color_mode(self, value: bool):
        self.part_infrastructure_setting_att.TrueColorMode = value

    @property
    def update_elements_refreshed(self) -> bool:
        return self.part_infrastructure_setting_att.UpdateElementsRefreshed

    @update_elements_refreshed.setter
    def update_elements_refreshed(self, value: bool):
        self.part_infrastructure_setting_att.UpdateElementsRefreshed = value

    @property
    def update_linked_external_references(self) -> bool:
        return self.part_infrastructure_setting_att.UpdateLinkedExternalReferences

    @update_linked_external_references.setter
    def update_linked_external_references(self, value: bool):
        self.part_infrastructure_setting_att.UpdateLinkedExternalReferences = value

    @property
    def update_mode(self) -> int:
        return self.part_infrastructure_setting_att.UpdateMode

    @update_mode.setter
    def update_mode(self, value: int):
        self.part_infrastructure_setting_att.UpdateMode = value

    @property
    def update_stopped_on_error(self) -> bool:
        return self.part_infrastructure_setting_att.UpdateStoppedOnError

    @update_stopped_on_error.setter
    def update_stopped_on_error(self, value: bool):
        self.part_infrastructure_setting_att.UpdateStoppedOnError = value

    def get_also_delete_exclusive_parents_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.part_infrastructure_setting_att.GetAlsoDeleteExclusiveParentsInfo(
            io_admin_level, io_locked
        )

    def get_axis_system_size_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.part_infrastructure_setting_att.GetAxisSystemSizeInfo(
            io_admin_level, io_locked
        )

    def get_bodies_under_operations_in_tree_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.part_infrastructure_setting_att.GetBodiesUnderOperationsInTreeInfo(
            io_admin_level, io_locked
        )

    def get_color_synchronization_editability_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return (
            self.part_infrastructure_setting_att.GetColorSynchronizationEditabilityInfo(
                io_admin_level, io_locked
            )
        )

    def get_color_synchronization_mode_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.part_infrastructure_setting_att.GetColorSynchronizationModeInfo(
            io_admin_level, io_locked
        )

    def get_color_synchronization_mode_manage_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return (
            self.part_infrastructure_setting_att.GetColorSynchronizationModeManageInfo(
                io_admin_level, io_locked
            )
        )

    def get_color_synchronization_mode_on_feature_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.part_infrastructure_setting_att.GetColorSynchronizationModeOnFeatureInfo(
            io_admin_level, io_locked
        )

    def get_color_synchronization_mode_on_sub_elements_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.part_infrastructure_setting_att.GetColorSynchronizationModeOnSubElementsInfo(
            io_admin_level, io_locked
        )

    def get_colors3_d_experience_management_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.part_infrastructure_setting_att.GetColors3DExperienceManagementInfo(
            io_admin_level, io_locked
        )

    def get_constraints_in_geometry_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.part_infrastructure_setting_att.GetConstraintsInGeometryInfo(
            io_admin_level, io_locked
        )

    def get_constraints_node_in_tree_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.part_infrastructure_setting_att.GetConstraintsNodeInTreeInfo(
            io_admin_level, io_locked
        )

    def get_contextual_features_selectable_at_creation_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.part_infrastructure_setting_att.GetContextualFeaturesSelectableAtCreationInfo(
            io_admin_level, io_locked
        )

    def get_default_colors_editability_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.part_infrastructure_setting_att.GetDefaultColorsEditabilityInfo(
            io_admin_level, io_locked
        )

    def get_delete_warning_box_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.part_infrastructure_setting_att.GetDeleteWarningBoxInfo(
            io_admin_level, io_locked
        )

    def get_display_geometry_after_current_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.part_infrastructure_setting_att.GetDisplayGeometryAfterCurrentInfo(
            io_admin_level, io_locked
        )

    def get_expand_sketch_based_features_node_at_creation_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.part_infrastructure_setting_att.GetExpandSketchBasedFeaturesNodeAtCreationInfo(
            io_admin_level, io_locked
        )

    def get_external_references_as_visible_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.part_infrastructure_setting_att.GetExternalReferencesAsVisibleInfo(
            io_admin_level, io_locked
        )

    def get_external_references_assembly_root_context_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.part_infrastructure_setting_att.GetExternalReferencesAssemblyRootContextInfo(
            io_admin_level, io_locked
        )

    def get_external_references_node_in_tree_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.part_infrastructure_setting_att.GetExternalReferencesNodeInTreeInfo(
            io_admin_level, io_locked
        )

    def get_hybrid_design_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.part_infrastructure_setting_att.GetHybridDesignModeInfo(
            io_admin_level, io_locked
        )

    def get_knowledge_in_hybrid_design_mode_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.part_infrastructure_setting_att.GetKnowledgeInHybridDesignModeInfo(
            io_admin_level, io_locked
        )

    def get_linked_external_references_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.part_infrastructure_setting_att.GetLinkedExternalReferencesInfo(
            io_admin_level, io_locked
        )

    def get_linked_external_references_only_on_publication_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.part_infrastructure_setting_att.GetLinkedExternalReferencesOnlyOnPublicationInfo(
            io_admin_level, io_locked
        )

    def get_linked_external_references_warning_at_creation_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.part_infrastructure_setting_att.GetLinkedExternalReferencesWarningAtCreationInfo(
            io_admin_level, io_locked
        )

    def get_naming_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.part_infrastructure_setting_att.GetNamingModeInfo(
            io_admin_level, io_locked
        )

    def get_new_with3_d_support_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.part_infrastructure_setting_att.GetNewWith3DSupportInfo(
            io_admin_level, io_locked
        )

    def get_new_with_axis_system_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.part_infrastructure_setting_att.GetNewWithAxisSystemInfo(
            io_admin_level, io_locked
        )

    def get_new_with_gs_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.part_infrastructure_setting_att.GetNewWithGSInfo(
            io_admin_level, io_locked
        )

    def get_new_with_ogs_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.part_infrastructure_setting_att.GetNewWithOGSInfo(
            io_admin_level, io_locked
        )

    def get_new_with_panel_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.part_infrastructure_setting_att.GetNewWithPanelInfo(
            io_admin_level, io_locked
        )

    def get_only_current_operated_solid_set_in_geometry_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.part_infrastructure_setting_att.GetOnlyCurrentOperatedSolidSetInGeometryInfo(
            io_admin_level, io_locked
        )

    def get_only_current_solid_set_in_geometry_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return (
            self.part_infrastructure_setting_att.GetOnlyCurrentSolidSetInGeometryInfo(
                io_admin_level, io_locked
            )
        )

    def get_parameters_node_in_tree_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.part_infrastructure_setting_att.GetParametersNodeInTreeInfo(
            io_admin_level, io_locked
        )

    def get_publish_topological_elements_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.part_infrastructure_setting_att.GetPublishTopologicalElementsInfo(
            io_admin_level, io_locked
        )

    def get_relations_node_in_tree_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.part_infrastructure_setting_att.GetRelationsNodeInTreeInfo(
            io_admin_level, io_locked
        )

    def get_replace_only_after_current_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.part_infrastructure_setting_att.GetReplaceOnlyAfterCurrentInfo(
            io_admin_level, io_locked
        )

    def get_surface_elements_location_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.part_infrastructure_setting_att.GetSurfaceElementsLocationInfo(
            io_admin_level, io_locked
        )

    def get_true_color_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.part_infrastructure_setting_att.GetTrueColorModeInfo(
            io_admin_level, io_locked
        )

    def get_update_elements_refreshed_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.part_infrastructure_setting_att.GetUpdateElementsRefreshedInfo(
            io_admin_level, io_locked
        )

    def get_update_linked_external_references_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return (
            self.part_infrastructure_setting_att.GetUpdateLinkedExternalReferencesInfo(
                io_admin_level, io_locked
            )
        )

    def get_update_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.part_infrastructure_setting_att.GetUpdateModeInfo(
            io_admin_level, io_locked
        )

    def get_update_stopped_on_error_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.part_infrastructure_setting_att.GetUpdateStoppedOnErrorInfo(
            io_admin_level, io_locked
        )

    def set_also_delete_exclusive_parents_lock(self, i_locked: bool) -> None:
        return self.part_infrastructure_setting_att.SetAlsoDeleteExclusiveParentsLock(
            i_locked
        )

    def set_axis_system_size_lock(self, i_locked: bool) -> None:
        return self.part_infrastructure_setting_att.SetAxisSystemSizeLock(i_locked)

    def set_bodies_under_operations_in_tree_lock(self, i_locked: bool) -> None:
        return self.part_infrastructure_setting_att.SetBodiesUnderOperationsInTreeLock(
            i_locked
        )

    def set_color_synchronization_editability_lock(self, i_locked: bool) -> None:
        return (
            self.part_infrastructure_setting_att.SetColorSynchronizationEditabilityLock(
                i_locked
            )
        )

    def set_color_synchronization_mode_lock(self, i_locked: bool) -> None:
        return self.part_infrastructure_setting_att.SetColorSynchronizationModeLock(
            i_locked
        )

    def set_color_synchronization_mode_manage_lock(self, i_locked: bool) -> None:
        return (
            self.part_infrastructure_setting_att.SetColorSynchronizationModeManageLock(
                i_locked
            )
        )

    def set_color_synchronization_mode_on_feature_lock(self, i_locked: bool) -> None:
        return self.part_infrastructure_setting_att.SetColorSynchronizationModeOnFeatureLock(
            i_locked
        )

    def set_color_synchronization_mode_on_sub_elements_lock(
        self, i_locked: bool
    ) -> None:
        return self.part_infrastructure_setting_att.SetColorSynchronizationModeOnSubElementsLock(
            i_locked
        )

    def set_colors3_d_experience_management_lock(self, i_locked: bool) -> None:
        return self.part_infrastructure_setting_att.SetColors3DExperienceManagementLock(
            i_locked
        )

    def set_constraints_in_geometry_lock(self, i_locked: bool) -> None:
        return self.part_infrastructure_setting_att.SetConstraintsInGeometryLock(
            i_locked
        )

    def set_constraints_node_in_tree_lock(self, i_locked: bool) -> None:
        return self.part_infrastructure_setting_att.SetConstraintsNodeInTreeLock(
            i_locked
        )

    def set_contextual_features_selectable_at_creation_lock(
        self, i_locked: bool
    ) -> None:
        return self.part_infrastructure_setting_att.SetContextualFeaturesSelectableAtCreationLock(
            i_locked
        )

    def set_default_colors_editability_lock(self, i_locked: bool) -> None:
        return self.part_infrastructure_setting_att.SetDefaultColorsEditabilityLock(
            i_locked
        )

    def set_delete_warning_box_lock(self, i_locked: bool) -> None:
        return self.part_infrastructure_setting_att.SetDeleteWarningBoxLock(i_locked)

    def set_display_geometry_after_current_lock(self, i_locked: bool) -> None:
        return self.part_infrastructure_setting_att.SetDisplayGeometryAfterCurrentLock(
            i_locked
        )

    def set_expand_sketch_based_features_node_at_creation_lock(
        self, i_locked: bool
    ) -> None:
        return self.part_infrastructure_setting_att.SetExpandSketchBasedFeaturesNodeAtCreationLock(
            i_locked
        )

    def set_external_references_as_visible_lock(self, i_locked: bool) -> None:
        return self.part_infrastructure_setting_att.SetExternalReferencesAsVisibleLock(
            i_locked
        )

    def set_external_references_assembly_root_context_lock(
        self, i_locked: bool
    ) -> None:
        return self.part_infrastructure_setting_att.SetExternalReferencesAssemblyRootContextLock(
            i_locked
        )

    def set_external_references_node_in_tree_lock(self, i_locked: bool) -> None:
        return self.part_infrastructure_setting_att.SetExternalReferencesNodeInTreeLock(
            i_locked
        )

    def set_hybrid_design_mode_lock(self, i_locked: bool) -> None:
        return self.part_infrastructure_setting_att.SetHybridDesignModeLock(i_locked)

    def set_knowledge_in_hybrid_design_mode_lock(self, i_locked: bool) -> None:
        return self.part_infrastructure_setting_att.SetKnowledgeInHybridDesignModeLock(
            i_locked
        )

    def set_linked_external_references_lock(self, i_locked: bool) -> None:
        return self.part_infrastructure_setting_att.SetLinkedExternalReferencesLock(
            i_locked
        )

    def set_linked_external_references_only_on_publication_lock(
        self, i_locked: bool
    ) -> None:
        return self.part_infrastructure_setting_att.SetLinkedExternalReferencesOnlyOnPublicationLock(
            i_locked
        )

    def set_linked_external_references_warning_at_creation_lock(
        self, i_locked: bool
    ) -> None:
        return self.part_infrastructure_setting_att.SetLinkedExternalReferencesWarningAtCreationLock(
            i_locked
        )

    def set_naming_mode_lock(self, i_locked: bool) -> None:
        return self.part_infrastructure_setting_att.SetNamingModeLock(i_locked)

    def set_new_with3_d_support_lock(self, i_locked: bool) -> None:
        return self.part_infrastructure_setting_att.SetNewWith3DSupportLock(i_locked)

    def set_new_with_axis_system_lock(self, i_locked: bool) -> None:
        return self.part_infrastructure_setting_att.SetNewWithAxisSystemLock(i_locked)

    def set_new_with_gs_lock(self, i_locked: bool) -> None:
        return self.part_infrastructure_setting_att.SetNewWithGSLock(i_locked)

    def set_new_with_ogs_lock(self, i_locked: bool) -> None:
        return self.part_infrastructure_setting_att.SetNewWithOGSLock(i_locked)

    def set_new_with_panel_lock(self, i_locked: bool) -> None:
        return self.part_infrastructure_setting_att.SetNewWithPanelLock(i_locked)

    def set_only_current_operated_solid_set_in_geometry_lock(
        self, i_locked: bool
    ) -> None:
        return self.part_infrastructure_setting_att.SetOnlyCurrentOperatedSolidSetInGeometryLock(
            i_locked
        )

    def set_only_current_solid_set_in_geometry_lock(self, i_locked: bool) -> None:
        return (
            self.part_infrastructure_setting_att.SetOnlyCurrentSolidSetInGeometryLock(
                i_locked
            )
        )

    def set_parameters_node_in_tree_lock(self, i_locked: bool) -> None:
        return self.part_infrastructure_setting_att.SetParametersNodeInTreeLock(
            i_locked
        )

    def set_publish_topological_elements_lock(self, i_locked: bool) -> None:
        return self.part_infrastructure_setting_att.SetPublishTopologicalElementsLock(
            i_locked
        )

    def set_relations_node_in_tree_lock(self, i_locked: bool) -> None:
        return self.part_infrastructure_setting_att.SetRelationsNodeInTreeLock(i_locked)

    def set_replace_only_after_current_lock(self, i_locked: bool) -> None:
        return self.part_infrastructure_setting_att.SetReplaceOnlyAfterCurrentLock(
            i_locked
        )

    def set_surface_elements_location_lock(self, i_locked: bool) -> None:
        return self.part_infrastructure_setting_att.SetSurfaceElementsLocationLock(
            i_locked
        )

    def set_update_elements_refreshed_lock(self, i_locked: bool) -> None:
        return self.part_infrastructure_setting_att.SetUpdateElementsRefreshedLock(
            i_locked
        )

    def set_update_linked_external_references_lock(self, i_locked: bool) -> None:
        return (
            self.part_infrastructure_setting_att.SetUpdateLinkedExternalReferencesLock(
                i_locked
            )
        )

    def set_update_mode_lock(self, i_locked: bool) -> None:
        return self.part_infrastructure_setting_att.SetUpdateModeLock(i_locked)

    def set_update_stopped_on_error_lock(self, i_locked: bool) -> None:
        return self.part_infrastructure_setting_att.SetUpdateStoppedOnErrorLock(
            i_locked
        )

    def __repr__(self):
        return f'PartInfrastructureSettingAtt(name="{self.name}")'
