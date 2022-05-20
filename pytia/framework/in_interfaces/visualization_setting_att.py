from pytia.framework.system_interfaces.setting_controller import SettingController


class VisualizationSettingAtt(SettingController):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.visualization_setting_att = com_object

    @property
    def accurate_picking_mode(self) -> bool:
        return self.visualization_setting_att.AccuratePickingMode

    @accurate_picking_mode.setter
    def accurate_picking_mode(self, value: bool):
        self.visualization_setting_att.AccuratePickingMode = value

    @property
    def accurate_picking_window_size(self) -> int:
        return self.visualization_setting_att.AccuratePickingWindowSize

    @accurate_picking_window_size.setter
    def accurate_picking_window_size(self, value: int):
        self.visualization_setting_att.AccuratePickingWindowSize = value

    @property
    def all_z_buffer_element_mode(self) -> bool:
        return self.visualization_setting_att.AllZBufferElementMode

    @all_z_buffer_element_mode.setter
    def all_z_buffer_element_mode(self, value: bool):
        self.visualization_setting_att.AllZBufferElementMode = value

    @property
    def ambient_activation(self) -> int:
        return self.visualization_setting_att.AmbientActivation

    @ambient_activation.setter
    def ambient_activation(self, value: int):
        self.visualization_setting_att.AmbientActivation = value

    @property
    def anti_aliasing_mode(self) -> bool:
        return self.visualization_setting_att.AntiAliasingMode

    @anti_aliasing_mode.setter
    def anti_aliasing_mode(self, value: bool):
        self.visualization_setting_att.AntiAliasingMode = value

    @property
    def anti_aliasing_offset(self) -> float:
        return self.visualization_setting_att.AntiAliasingOffset

    @anti_aliasing_offset.setter
    def anti_aliasing_offset(self, value: float):
        self.visualization_setting_att.AntiAliasingOffset = value

    @property
    def auxiliary_drill_viewer(self) -> bool:
        return self.visualization_setting_att.AuxiliaryDrillViewer

    @auxiliary_drill_viewer.setter
    def auxiliary_drill_viewer(self, value: bool):
        self.visualization_setting_att.AuxiliaryDrillViewer = value

    @property
    def back_face_culling_mode(self) -> bool:
        return self.visualization_setting_att.BackFaceCullingMode

    @back_face_culling_mode.setter
    def back_face_culling_mode(self, value: bool):
        self.visualization_setting_att.BackFaceCullingMode = value

    @property
    def border_edges_mode(self) -> bool:
        return self.visualization_setting_att.BorderEdgesMode

    @border_edges_mode.setter
    def border_edges_mode(self, value: bool):
        self.visualization_setting_att.BorderEdgesMode = value

    @property
    def border_edges_thickness(self) -> int:
        return self.visualization_setting_att.BorderEdgesThickness

    @border_edges_thickness.setter
    def border_edges_thickness(self, value: int):
        self.visualization_setting_att.BorderEdgesThickness = value

    @property
    def bounding_box_selection_mode(self) -> bool:
        return self.visualization_setting_att.BoundingBoxSelectionMode

    @bounding_box_selection_mode.setter
    def bounding_box_selection_mode(self, value: bool):
        self.visualization_setting_att.BoundingBoxSelectionMode = value

    @property
    def color_background_mode(self) -> bool:
        return self.visualization_setting_att.ColorBackgroundMode

    @color_background_mode.setter
    def color_background_mode(self, value: bool):
        self.visualization_setting_att.ColorBackgroundMode = value

    @property
    def default_diffuse_ambient_coefficient(self) -> float:
        return self.visualization_setting_att.DefaultDiffuseAmbientCoefficient

    @default_diffuse_ambient_coefficient.setter
    def default_diffuse_ambient_coefficient(self, value: float):
        self.visualization_setting_att.DefaultDiffuseAmbientCoefficient = value

    @property
    def default_shininess(self) -> float:
        return self.visualization_setting_att.DefaultShininess

    @default_shininess.setter
    def default_shininess(self, value: float):
        self.visualization_setting_att.DefaultShininess = value

    @property
    def default_specular_coefficient(self) -> float:
        return self.visualization_setting_att.DefaultSpecularCoefficient

    @default_specular_coefficient.setter
    def default_specular_coefficient(self, value: float):
        self.visualization_setting_att.DefaultSpecularCoefficient = value

    @property
    def display_current_scale(self) -> bool:
        return self.visualization_setting_att.DisplayCurrentScale

    @display_current_scale.setter
    def display_current_scale(self, value: bool):
        self.visualization_setting_att.DisplayCurrentScale = value

    @property
    def display_drill_list(self) -> bool:
        return self.visualization_setting_att.DisplayDrillList

    @display_drill_list.setter
    def display_drill_list(self, value: bool):
        self.visualization_setting_att.DisplayDrillList = value

    @property
    def display_immersive_drill_viewer(self) -> bool:
        return self.visualization_setting_att.DisplayImmersiveDrillViewer

    @display_immersive_drill_viewer.setter
    def display_immersive_drill_viewer(self, value: bool):
        self.visualization_setting_att.DisplayImmersiveDrillViewer = value

    @property
    def dynamic_cull(self) -> int:
        return self.visualization_setting_att.DynamicCull

    @dynamic_cull.setter
    def dynamic_cull(self, value: int):
        self.visualization_setting_att.DynamicCull = value

    @property
    def dynamic_lod(self) -> float:
        return self.visualization_setting_att.DynamicLOD

    @dynamic_lod.setter
    def dynamic_lod(self, value: float):
        self.visualization_setting_att.DynamicLOD = value

    @property
    def face_hl_drill(self) -> bool:
        return self.visualization_setting_att.FaceHLDrill

    @face_hl_drill.setter
    def face_hl_drill(self, value: bool):
        self.visualization_setting_att.FaceHLDrill = value

    @property
    def fly_collision_mode(self) -> bool:
        return self.visualization_setting_att.FlyCollisionMode

    @fly_collision_mode.setter
    def fly_collision_mode(self, value: bool):
        self.visualization_setting_att.FlyCollisionMode = value

    @property
    def fly_collision_sphere_radius(self) -> float:
        return self.visualization_setting_att.FlyCollisionSphereRadius

    @fly_collision_sphere_radius.setter
    def fly_collision_sphere_radius(self, value: float):
        self.visualization_setting_att.FlyCollisionSphereRadius = value

    @property
    def fly_collision_type(self) -> int:
        return self.visualization_setting_att.FlyCollisionType

    @fly_collision_type.setter
    def fly_collision_type(self, value: int):
        self.visualization_setting_att.FlyCollisionType = value

    @property
    def fly_sensitivity(self) -> int:
        return self.visualization_setting_att.FlySensitivity

    @fly_sensitivity.setter
    def fly_sensitivity(self, value: int):
        self.visualization_setting_att.FlySensitivity = value

    @property
    def fly_speed(self) -> int:
        return self.visualization_setting_att.FlySpeed

    @fly_speed.setter
    def fly_speed(self, value: int):
        self.visualization_setting_att.FlySpeed = value

    @property
    def fly_speed_mode(self) -> int:
        return self.visualization_setting_att.FlySpeedMode

    @fly_speed_mode.setter
    def fly_speed_mode(self, value: int):
        self.visualization_setting_att.FlySpeedMode = value

    @property
    def follow_ground_altitude(self) -> float:
        return self.visualization_setting_att.FollowGroundAltitude

    @follow_ground_altitude.setter
    def follow_ground_altitude(self, value: float):
        self.visualization_setting_att.FollowGroundAltitude = value

    @property
    def follow_ground_mode(self) -> bool:
        return self.visualization_setting_att.FollowGroundMode

    @follow_ground_mode.setter
    def follow_ground_mode(self, value: bool):
        self.visualization_setting_att.FollowGroundMode = value

    @property
    def full_scene_anti_aliasing_mode(self) -> int:
        return self.visualization_setting_att.FullSceneAntiAliasingMode

    @full_scene_anti_aliasing_mode.setter
    def full_scene_anti_aliasing_mode(self, value: int):
        self.visualization_setting_att.FullSceneAntiAliasingMode = value

    @property
    def gravity(self) -> bool:
        return self.visualization_setting_att.Gravity

    @gravity.setter
    def gravity(self, value: bool):
        self.visualization_setting_att.Gravity = value

    @property
    def gravity_axis(self) -> int:
        return self.visualization_setting_att.GravityAxis

    @gravity_axis.setter
    def gravity_axis(self, value: int):
        self.visualization_setting_att.GravityAxis = value

    @property
    def halo_mode(self) -> bool:
        return self.visualization_setting_att.HaloMode

    @halo_mode.setter
    def halo_mode(self, value: bool):
        self.visualization_setting_att.HaloMode = value

    @property
    def isopar_generation_mode(self) -> bool:
        return self.visualization_setting_att.IsoparGenerationMode

    @isopar_generation_mode.setter
    def isopar_generation_mode(self, value: bool):
        self.visualization_setting_att.IsoparGenerationMode = value

    @property
    def keyboard_rotation_angle_value(self) -> int:
        return self.visualization_setting_att.KeyboardRotationAngleValue

    @keyboard_rotation_angle_value.setter
    def keyboard_rotation_angle_value(self, value: int):
        self.visualization_setting_att.KeyboardRotationAngleValue = value

    @property
    def light_viewer_mode(self) -> bool:
        return self.visualization_setting_att.LightViewerMode

    @light_viewer_mode.setter
    def light_viewer_mode(self, value: bool):
        self.visualization_setting_att.LightViewerMode = value

    @property
    def lineic_cgr_mode(self) -> bool:
        return self.visualization_setting_att.LineicCgrMode

    @lineic_cgr_mode.setter
    def lineic_cgr_mode(self, value: bool):
        self.visualization_setting_att.LineicCgrMode = value

    @property
    def max_selection_move(self) -> int:
        return self.visualization_setting_att.MaxSelectionMove

    @max_selection_move.setter
    def max_selection_move(self, value: int):
        self.visualization_setting_att.MaxSelectionMove = value

    @property
    def minimum_fps_mode(self) -> bool:
        return self.visualization_setting_att.MinimumFPSMode

    @minimum_fps_mode.setter
    def minimum_fps_mode(self, value: bool):
        self.visualization_setting_att.MinimumFPSMode = value

    @property
    def minimum_space_fps_mode(self) -> bool:
        return self.visualization_setting_att.MinimumSpaceFPSMode

    @minimum_space_fps_mode.setter
    def minimum_space_fps_mode(self, value: bool):
        self.visualization_setting_att.MinimumSpaceFPSMode = value

    @property
    def mouse_double_clic_delay(self) -> int:
        return self.visualization_setting_att.MouseDoubleClicDelay

    @mouse_double_clic_delay.setter
    def mouse_double_clic_delay(self, value: int):
        self.visualization_setting_att.MouseDoubleClicDelay = value

    @property
    def mouse_speed_value(self) -> int:
        return self.visualization_setting_att.MouseSpeedValue

    @mouse_speed_value.setter
    def mouse_speed_value(self, value: int):
        self.visualization_setting_att.MouseSpeedValue = value

    @property
    def nb_isopars(self) -> int:
        return self.visualization_setting_att.NbIsopars

    @nb_isopars.setter
    def nb_isopars(self, value: int):
        self.visualization_setting_att.NbIsopars = value

    @property
    def no_z_buffer_selection_mode(self) -> bool:
        return self.visualization_setting_att.NoZBufferSelectionMode

    @no_z_buffer_selection_mode.setter
    def no_z_buffer_selection_mode(self, value: bool):
        self.visualization_setting_att.NoZBufferSelectionMode = value

    @property
    def number_of_minimum_fps(self) -> int:
        return self.visualization_setting_att.NumberOfMinimumFPS

    @number_of_minimum_fps.setter
    def number_of_minimum_fps(self, value: int):
        self.visualization_setting_att.NumberOfMinimumFPS = value

    @property
    def number_of_minimum_space_fps(self) -> int:
        return self.visualization_setting_att.NumberOfMinimumSpaceFPS

    @number_of_minimum_space_fps.setter
    def number_of_minimum_space_fps(self, value: int):
        self.visualization_setting_att.NumberOfMinimumSpaceFPS = value

    @property
    def occlusion_culling_mode(self) -> bool:
        return self.visualization_setting_att.OcclusionCullingMode

    @occlusion_culling_mode.setter
    def occlusion_culling_mode(self, value: bool):
        self.visualization_setting_att.OcclusionCullingMode = value

    @property
    def opaque_faces(self) -> bool:
        return self.visualization_setting_att.OpaqueFaces

    @opaque_faces.setter
    def opaque_faces(self, value: bool):
        self.visualization_setting_att.OpaqueFaces = value

    @property
    def other_selection_timeout(self) -> float:
        return self.visualization_setting_att.OtherSelectionTimeout

    @other_selection_timeout.setter
    def other_selection_timeout(self, value: float):
        self.visualization_setting_att.OtherSelectionTimeout = value

    @property
    def other_selection_timeout_activity(self) -> bool:
        return self.visualization_setting_att.OtherSelectionTimeoutActivity

    @other_selection_timeout_activity.setter
    def other_selection_timeout_activity(self, value: bool):
        self.visualization_setting_att.OtherSelectionTimeoutActivity = value

    @property
    def picking_window_size(self) -> int:
        return self.visualization_setting_att.PickingWindowSize

    @picking_window_size.setter
    def picking_window_size(self, value: int):
        self.visualization_setting_att.PickingWindowSize = value

    @property
    def pre_selection_mode(self) -> bool:
        return self.visualization_setting_att.PreSelectionMode

    @pre_selection_mode.setter
    def pre_selection_mode(self, value: bool):
        self.visualization_setting_att.PreSelectionMode = value

    @property
    def preselected_element_linetype(self) -> int:
        return self.visualization_setting_att.PreselectedElementLinetype

    @preselected_element_linetype.setter
    def preselected_element_linetype(self, value: int):
        self.visualization_setting_att.PreselectedElementLinetype = value

    @property
    def rotation_sphere_mode(self) -> bool:
        return self.visualization_setting_att.RotationSphereMode

    @rotation_sphere_mode.setter
    def rotation_sphere_mode(self, value: bool):
        self.visualization_setting_att.RotationSphereMode = value

    @property
    def shader_mode(self) -> bool:
        return self.visualization_setting_att.ShaderMode

    @shader_mode.setter
    def shader_mode(self, value: bool):
        self.visualization_setting_att.ShaderMode = value

    @property
    def static_cull(self) -> int:
        return self.visualization_setting_att.StaticCull

    @static_cull.setter
    def static_cull(self, value: int):
        self.visualization_setting_att.StaticCull = value

    @property
    def static_lod(self) -> float:
        return self.visualization_setting_att.StaticLOD

    @static_lod.setter
    def static_lod(self, value: float):
        self.visualization_setting_att.StaticLOD = value

    @property
    def stereo_mode(self) -> bool:
        return self.visualization_setting_att.StereoMode

    @stereo_mode.setter
    def stereo_mode(self, value: bool):
        self.visualization_setting_att.StereoMode = value

    @property
    def transparency_mode(self) -> bool:
        return self.visualization_setting_att.TransparencyMode

    @transparency_mode.setter
    def transparency_mode(self, value: bool):
        self.visualization_setting_att.TransparencyMode = value

    @property
    def two_side_lighting_mode(self) -> bool:
        return self.visualization_setting_att.TwoSideLightingMode

    @two_side_lighting_mode.setter
    def two_side_lighting_mode(self, value: bool):
        self.visualization_setting_att.TwoSideLightingMode = value

    @property
    def viewpoint_animation_mode(self) -> bool:
        return self.visualization_setting_att.ViewpointAnimationMode

    @viewpoint_animation_mode.setter
    def viewpoint_animation_mode(self, value: bool):
        self.visualization_setting_att.ViewpointAnimationMode = value

    @property
    def viz2_d_accuracy_mode(self) -> bool:
        return self.visualization_setting_att.Viz2DAccuracyMode

    @viz2_d_accuracy_mode.setter
    def viz2_d_accuracy_mode(self, value: bool):
        self.visualization_setting_att.Viz2DAccuracyMode = value

    @property
    def viz2_d_fixed_accuracy(self) -> float:
        return self.visualization_setting_att.Viz2DFixedAccuracy

    @viz2_d_fixed_accuracy.setter
    def viz2_d_fixed_accuracy(self, value: float):
        self.visualization_setting_att.Viz2DFixedAccuracy = value

    @property
    def viz2_d_proportionnal_accuracy(self) -> float:
        return self.visualization_setting_att.Viz2DProportionnalAccuracy

    @viz2_d_proportionnal_accuracy.setter
    def viz2_d_proportionnal_accuracy(self, value: float):
        self.visualization_setting_att.Viz2DProportionnalAccuracy = value

    @property
    def viz3_d_accuracy_mode(self) -> bool:
        return self.visualization_setting_att.Viz3DAccuracyMode

    @viz3_d_accuracy_mode.setter
    def viz3_d_accuracy_mode(self, value: bool):
        self.visualization_setting_att.Viz3DAccuracyMode = value

    @property
    def viz3_d_curve_accuracy(self) -> float:
        return self.visualization_setting_att.Viz3DCurveAccuracy

    @viz3_d_curve_accuracy.setter
    def viz3_d_curve_accuracy(self, value: float):
        self.visualization_setting_att.Viz3DCurveAccuracy = value

    @property
    def viz3_d_fixed_accuracy(self) -> float:
        return self.visualization_setting_att.Viz3DFixedAccuracy

    @viz3_d_fixed_accuracy.setter
    def viz3_d_fixed_accuracy(self, value: float):
        self.visualization_setting_att.Viz3DFixedAccuracy = value

    @property
    def viz3_d_proportionnal_accuracy(self) -> float:
        return self.visualization_setting_att.Viz3DProportionnalAccuracy

    @viz3_d_proportionnal_accuracy.setter
    def viz3_d_proportionnal_accuracy(self, value: float):
        self.visualization_setting_att.Viz3DProportionnalAccuracy = value

    def get_accurate_picking_mode_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.visualization_setting_att.GetAccuratePickingModeInfo(
            io_admin_level, io_locked
        )

    def get_accurate_picking_window_size_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.visualization_setting_att.GetAccuratePickingWindowSizeInfo(
            io_admin_level, io_locked
        )

    def get_all_z_buffer_element_mode_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.visualization_setting_att.GetAllZBufferElementModeInfo(
            io_admin_level, io_locked
        )

    def get_ambient_activation_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.visualization_setting_att.GetAmbientActivationInfo(
            io_admin_level, io_locked
        )

    def get_anti_aliasing_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.visualization_setting_att.GetAntiAliasingModeInfo(
            io_admin_level, io_locked
        )

    def get_anti_aliasing_offset_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.visualization_setting_att.GetAntiAliasingOffsetInfo(
            io_admin_level, io_locked
        )

    def get_auxiliary_drill_viewer_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.visualization_setting_att.GetAuxiliaryDrillViewerInfo(
            io_admin_level, io_locked
        )

    def get_back_face_culling_mode(self) -> int:
        return self.visualization_setting_att.GetBackFaceCullingMode()

    def get_back_face_culling_mode_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.visualization_setting_att.GetBackFaceCullingModeInfo(
            io_admin_level, io_locked
        )

    def get_background_rgb(self, io_r: int, io_g: int, io_b: int) -> None:
        return self.visualization_setting_att.GetBackgroundRGB(io_r, io_g, io_b)

    def get_background_rgb_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.visualization_setting_att.GetBackgroundRGBInfo(
            io_admin_level, io_locked
        )

    def get_border_edges_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.visualization_setting_att.GetBorderEdgesModeInfo(
            io_admin_level, io_locked
        )

    def get_border_edges_rgb(self, io_r: int, io_g: int, io_b: int) -> None:
        return self.visualization_setting_att.GetBorderEdgesRGB(io_r, io_g, io_b)

    def get_border_edges_rgb_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.visualization_setting_att.GetBorderEdgesRGBInfo(
            io_admin_level, io_locked
        )

    def get_border_edges_thickness_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.visualization_setting_att.GetBorderEdgesThicknessInfo(
            io_admin_level, io_locked
        )

    def get_bounding_box_selection_mode_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.visualization_setting_att.GetBoundingBoxSelectionModeInfo(
            io_admin_level, io_locked
        )

    def get_color_background_mode_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.visualization_setting_att.GetColorBackgroundModeInfo(
            io_admin_level, io_locked
        )

    def get_default_diffuse_ambient_coefficient_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.visualization_setting_att.GetDefaultDiffuseAmbientCoefficientInfo(
            io_admin_level, io_locked
        )

    def get_default_shininess_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.visualization_setting_att.GetDefaultShininessInfo(
            io_admin_level, io_locked
        )

    def get_default_specular_coefficient_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.visualization_setting_att.GetDefaultSpecularCoefficientInfo(
            io_admin_level, io_locked
        )

    def get_display_current_scale_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.visualization_setting_att.GetDisplayCurrentScaleInfo(
            io_admin_level, io_locked
        )

    def get_display_drill_list_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.visualization_setting_att.GetDisplayDrillListInfo(
            io_admin_level, io_locked
        )

    def get_display_immersive_drill_viewer_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.visualization_setting_att.GetDisplayImmersiveDrillViewerInfo(
            io_admin_level, io_locked
        )

    def get_dynamic_cull_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.visualization_setting_att.GetDynamicCullInfo(
            io_admin_level, io_locked
        )

    def get_dynamic_lod_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.visualization_setting_att.GetDynamicLODInfo(
            io_admin_level, io_locked
        )

    def get_face_hl_drill_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.visualization_setting_att.GetFaceHLDrillInfo(
            io_admin_level, io_locked
        )

    def get_fly_collision_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.visualization_setting_att.GetFlyCollisionModeInfo(
            io_admin_level, io_locked
        )

    def get_fly_collision_sphere_radius_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.visualization_setting_att.GetFlyCollisionSphereRadiusInfo(
            io_admin_level, io_locked
        )

    def get_fly_collision_type_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.visualization_setting_att.GetFlyCollisionTypeInfo(
            io_admin_level, io_locked
        )

    def get_fly_sensitivity_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.visualization_setting_att.GetFlySensitivityInfo(
            io_admin_level, io_locked
        )

    def get_fly_speed_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.visualization_setting_att.GetFlySpeedInfo(io_admin_level, io_locked)

    def get_fly_speed_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.visualization_setting_att.GetFlySpeedModeInfo(
            io_admin_level, io_locked
        )

    def get_follow_ground_altitude_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.visualization_setting_att.GetFollowGroundAltitudeInfo(
            io_admin_level, io_locked
        )

    def get_follow_ground_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.visualization_setting_att.GetFollowGroundModeInfo(
            io_admin_level, io_locked
        )

    def get_full_scene_anti_aliasing_mode_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.visualization_setting_att.GetFullSceneAntiAliasingModeInfo(
            io_admin_level, io_locked
        )

    def get_gravity_axis_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.visualization_setting_att.GetGravityAxisInfo(
            io_admin_level, io_locked
        )

    def get_gravity_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.visualization_setting_att.GetGravityInfo(io_admin_level, io_locked)

    def get_halo_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.visualization_setting_att.GetHaloModeInfo(io_admin_level, io_locked)

    def get_handles_rgb(self, io_r: int, io_g: int, io_b: int) -> None:
        return self.visualization_setting_att.GetHandlesRGB(io_r, io_g, io_b)

    def get_handles_rgb_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.visualization_setting_att.GetHandlesRGBInfo(
            io_admin_level, io_locked
        )

    def get_isopar_generation_mode_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.visualization_setting_att.GetIsoparGenerationModeInfo(
            io_admin_level, io_locked
        )

    def get_keyboard_rotation_angle_value_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.visualization_setting_att.GetKeyboardRotationAngleValueInfo(
            io_admin_level, io_locked
        )

    def get_light_viewer_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.visualization_setting_att.GetLightViewerModeInfo(
            io_admin_level, io_locked
        )

    def get_lineic_cgr_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.visualization_setting_att.GetLineicCgrModeInfo(
            io_admin_level, io_locked
        )

    def get_max_selection_move_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.visualization_setting_att.GetMaxSelectionMoveInfo(
            io_admin_level, io_locked
        )

    def get_minimum_fps_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.visualization_setting_att.GetMinimumFPSModeInfo(
            io_admin_level, io_locked
        )

    def get_minimum_space_fps_mode_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.visualization_setting_att.GetMinimumSpaceFPSModeInfo(
            io_admin_level, io_locked
        )

    def get_mouse_double_clic_delay_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.visualization_setting_att.GetMouseDoubleClicDelayInfo(
            io_admin_level, io_locked
        )

    def get_mouse_speed_value_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.visualization_setting_att.GetMouseSpeedValueInfo(
            io_admin_level, io_locked
        )

    def get_nb_isopars_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.visualization_setting_att.GetNbIsoparsInfo(
            io_admin_level, io_locked
        )

    def get_no_show_background_rgb(self, io_r: int, io_g: int, io_b: int) -> None:
        return self.visualization_setting_att.GetNoShowBackgroundRGB(io_r, io_g, io_b)

    def get_no_show_background_rgb_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.visualization_setting_att.GetNoShowBackgroundRGBInfo(
            io_admin_level, io_locked
        )

    def get_no_z_buffer_selection_mode_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.visualization_setting_att.GetNoZBufferSelectionModeInfo(
            io_admin_level, io_locked
        )

    def get_number_of_minimum_fps_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.visualization_setting_att.GetNumberOfMinimumFPSInfo(
            io_admin_level, io_locked
        )

    def get_number_of_minimum_space_fps_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.visualization_setting_att.GetNumberOfMinimumSpaceFPSInfo(
            io_admin_level, io_locked
        )

    def get_occlusion_culling_mode_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.visualization_setting_att.GetOcclusionCullingModeInfo(
            io_admin_level, io_locked
        )

    def get_opaque_faces_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.visualization_setting_att.GetOpaqueFacesInfo(
            io_admin_level, io_locked
        )

    def get_other_selection_timeout_activity_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.visualization_setting_att.GetOtherSelectionTimeoutActivityInfo(
            io_admin_level, io_locked
        )

    def get_other_selection_timeout_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.visualization_setting_att.GetOtherSelectionTimeoutInfo(
            io_admin_level, io_locked
        )

    def get_picking_window_size_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.visualization_setting_att.GetPickingWindowSizeInfo(
            io_admin_level, io_locked
        )

    def get_pre_selection_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.visualization_setting_att.GetPreSelectionModeInfo(
            io_admin_level, io_locked
        )

    def get_preselected_element_linetype_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.visualization_setting_att.GetPreselectedElementLinetypeInfo(
            io_admin_level, io_locked
        )

    def get_preselected_element_rgb(self, io_r: int, io_g: int, io_b: int) -> None:
        return self.visualization_setting_att.GetPreselectedElementRGB(io_r, io_g, io_b)

    def get_preselected_element_rgb_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.visualization_setting_att.GetPreselectedElementRGBInfo(
            io_admin_level, io_locked
        )

    def get_rotation_sphere_mode_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.visualization_setting_att.GetRotationSphereModeInfo(
            io_admin_level, io_locked
        )

    def get_selected_edge_rgb(self, io_r: int, io_g: int, io_b: int) -> None:
        return self.visualization_setting_att.GetSelectedEdgeRGB(io_r, io_g, io_b)

    def get_selected_edge_rgb_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.visualization_setting_att.GetSelectedEdgeRGBInfo(
            io_admin_level, io_locked
        )

    def get_selected_element_rgb(self, io_r: int, io_g: int, io_b: int) -> None:
        return self.visualization_setting_att.GetSelectedElementRGB(io_r, io_g, io_b)

    def get_selected_element_rgb_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.visualization_setting_att.GetSelectedElementRGBInfo(
            io_admin_level, io_locked
        )

    def get_shader_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.visualization_setting_att.GetShaderModeInfo(
            io_admin_level, io_locked
        )

    def get_static_cull_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.visualization_setting_att.GetStaticCullInfo(
            io_admin_level, io_locked
        )

    def get_static_lod_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.visualization_setting_att.GetStaticLODInfo(
            io_admin_level, io_locked
        )

    def get_stereo_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.visualization_setting_att.GetStereoModeInfo(
            io_admin_level, io_locked
        )

    def get_transparency_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.visualization_setting_att.GetTransparencyModeInfo(
            io_admin_level, io_locked
        )

    def get_two_side_lighting_mode_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.visualization_setting_att.GetTwoSideLightingModeInfo(
            io_admin_level, io_locked
        )

    def get_under_intensified_rgb(self, io_r: int, io_g: int, io_b: int) -> None:
        return self.visualization_setting_att.GetUnderIntensifiedRGB(io_r, io_g, io_b)

    def get_under_intensified_rgb_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.visualization_setting_att.GetUnderIntensifiedRGBInfo(
            io_admin_level, io_locked
        )

    def get_update_needed_rgb(self, io_r: int, io_g: int, io_b: int) -> None:
        return self.visualization_setting_att.GetUpdateNeededRGB(io_r, io_g, io_b)

    def get_update_needed_rgb_info(self, io_admin_level: str, io_locked: str) -> bool:
        return self.visualization_setting_att.GetUpdateNeededRGBInfo(
            io_admin_level, io_locked
        )

    def get_viewpoint_animation_mode_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.visualization_setting_att.GetViewpointAnimationModeInfo(
            io_admin_level, io_locked
        )

    def get_viz2_d_accuracy_mode_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.visualization_setting_att.GetViz2DAccuracyModeInfo(
            io_admin_level, io_locked
        )

    def get_viz2_d_fixed_accuracy_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.visualization_setting_att.GetViz2DFixedAccuracyInfo(
            io_admin_level, io_locked
        )

    def get_viz2_d_proportionnal_accuracy_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.visualization_setting_att.GetViz2DProportionnalAccuracyInfo(
            io_admin_level, io_locked
        )

    def get_viz3_d_accuracy_mode_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.visualization_setting_att.GetViz3DAccuracyModeInfo(
            io_admin_level, io_locked
        )

    def get_viz3_d_curve_accuracy_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.visualization_setting_att.GetViz3DCurveAccuracyInfo(
            io_admin_level, io_locked
        )

    def get_viz3_d_fixed_accuracy_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.visualization_setting_att.GetViz3DFixedAccuracyInfo(
            io_admin_level, io_locked
        )

    def get_viz3_d_proportionnal_accuracy_info(
        self, io_admin_level: str, io_locked: str
    ) -> bool:
        return self.visualization_setting_att.GetViz3DProportionnalAccuracyInfo(
            io_admin_level, io_locked
        )

    def put_back_face_culling_mode(self, i_back_face_culling_mode: int) -> None:
        return self.visualization_setting_att.PutBackFaceCullingMode(
            i_back_face_culling_mode
        )

    def set_accurate_picking_mode_lock(self, i_locked: bool) -> None:
        return self.visualization_setting_att.SetAccuratePickingModeLock(i_locked)

    def set_accurate_picking_window_size_lock(self, i_locked: bool) -> None:
        return self.visualization_setting_att.SetAccuratePickingWindowSizeLock(i_locked)

    def set_all_z_buffer_element_mode_lock(self, i_locked: bool) -> None:
        return self.visualization_setting_att.SetAllZBufferElementModeLock(i_locked)

    def set_ambient_activation_lock(self, i_locked: bool) -> None:
        return self.visualization_setting_att.SetAmbientActivationLock(i_locked)

    def set_anti_aliasing_mode_lock(self, i_locked: bool) -> None:
        return self.visualization_setting_att.SetAntiAliasingModeLock(i_locked)

    def set_anti_aliasing_offset_lock(self, i_locked: bool) -> None:
        return self.visualization_setting_att.SetAntiAliasingOffsetLock(i_locked)

    def set_auxiliary_drill_viewer_lock(self, i_locked: bool) -> None:
        return self.visualization_setting_att.SetAuxiliaryDrillViewerLock(i_locked)

    def set_back_face_culling_mode_lock(self, i_locked: bool) -> None:
        return self.visualization_setting_att.SetBackFaceCullingModeLock(i_locked)

    def set_background_rgb(self, i_r: int, i_g: int, i_b: int) -> None:
        return self.visualization_setting_att.SetBackgroundRGB(i_r, i_g, i_b)

    def set_background_rgb_lock(self, i_locked: bool) -> None:
        return self.visualization_setting_att.SetBackgroundRGBLock(i_locked)

    def set_border_edges_mode_lock(self, i_locked: bool) -> None:
        return self.visualization_setting_att.SetBorderEdgesModeLock(i_locked)

    def set_border_edges_rgb(self, i_r: int, i_g: int, i_b: int) -> None:
        return self.visualization_setting_att.SetBorderEdgesRGB(i_r, i_g, i_b)

    def set_border_edges_rgb_lock(self, i_locked: bool) -> None:
        return self.visualization_setting_att.SetBorderEdgesRGBLock(i_locked)

    def set_border_edges_thickness_lock(self, i_locked: bool) -> None:
        return self.visualization_setting_att.SetBorderEdgesThicknessLock(i_locked)

    def set_bounding_box_selection_mode_lock(self, i_locked: bool) -> None:
        return self.visualization_setting_att.SetBoundingBoxSelectionModeLock(i_locked)

    def set_color_background_mode_lock(self, i_locked: bool) -> None:
        return self.visualization_setting_att.SetColorBackgroundModeLock(i_locked)

    def set_default_diffuse_ambient_coefficient_lock(self, i_locked: bool) -> None:
        return self.visualization_setting_att.SetDefaultDiffuseAmbientCoefficientLock(
            i_locked
        )

    def set_default_shininess_lock(self, i_locked: bool) -> None:
        return self.visualization_setting_att.SetDefaultShininessLock(i_locked)

    def set_default_specular_coefficient_lock(self, i_locked: bool) -> None:
        return self.visualization_setting_att.SetDefaultSpecularCoefficientLock(
            i_locked
        )

    def set_display_current_scale_lock(self, i_locked: bool) -> None:
        return self.visualization_setting_att.SetDisplayCurrentScaleLock(i_locked)

    def set_display_drill_list_lock(self, i_locked: bool) -> None:
        return self.visualization_setting_att.SetDisplayDrillListLock(i_locked)

    def set_display_immersive_drill_viewer_lock(self, i_locked: bool) -> None:
        return self.visualization_setting_att.SetDisplayImmersiveDrillViewerLock(
            i_locked
        )

    def set_dynamic_cull_lock(self, i_locked: bool) -> None:
        return self.visualization_setting_att.SetDynamicCullLock(i_locked)

    def set_dynamic_lod_lock(self, i_locked: bool) -> None:
        return self.visualization_setting_att.SetDynamicLODLock(i_locked)

    def set_face_hl_drill_lock(self, i_locked: bool) -> None:
        return self.visualization_setting_att.SetFaceHLDrillLock(i_locked)

    def set_fly_collision_mode_lock(self, i_locked: bool) -> None:
        return self.visualization_setting_att.SetFlyCollisionModeLock(i_locked)

    def set_fly_collision_sphere_radius_lock(self, i_locked: bool) -> None:
        return self.visualization_setting_att.SetFlyCollisionSphereRadiusLock(i_locked)

    def set_fly_collision_type_lock(self, i_locked: bool) -> None:
        return self.visualization_setting_att.SetFlyCollisionTypeLock(i_locked)

    def set_fly_sensitivity_lock(self, i_locked: bool) -> None:
        return self.visualization_setting_att.SetFlySensitivityLock(i_locked)

    def set_fly_speed_lock(self, i_locked: bool) -> None:
        return self.visualization_setting_att.SetFlySpeedLock(i_locked)

    def set_fly_speed_mode_lock(self, i_locked: bool) -> None:
        return self.visualization_setting_att.SetFlySpeedModeLock(i_locked)

    def set_follow_ground_altitude_lock(self, i_locked: bool) -> None:
        return self.visualization_setting_att.SetFollowGroundAltitudeLock(i_locked)

    def set_follow_ground_mode_lock(self, i_locked: bool) -> None:
        return self.visualization_setting_att.SetFollowGroundModeLock(i_locked)

    def set_full_scene_anti_aliasing_mode_lock(self, i_locked: bool) -> None:
        return self.visualization_setting_att.SetFullSceneAntiAliasingModeLock(i_locked)

    def set_gravity_axis_lock(self, i_locked: bool) -> None:
        return self.visualization_setting_att.SetGravityAxisLock(i_locked)

    def set_gravity_lock(self, i_locked: bool) -> None:
        return self.visualization_setting_att.SetGravityLock(i_locked)

    def set_halo_mode_lock(self, i_locked: bool) -> None:
        return self.visualization_setting_att.SetHaloModeLock(i_locked)

    def set_handles_rgb(self, i_r: int, i_g: int, i_b: int) -> None:
        return self.visualization_setting_att.SetHandlesRGB(i_r, i_g, i_b)

    def set_handles_rgb_lock(self, i_locked: bool) -> None:
        return self.visualization_setting_att.SetHandlesRGBLock(i_locked)

    def set_isopar_generation_mode_lock(self, i_locked: bool) -> None:
        return self.visualization_setting_att.SetIsoparGenerationModeLock(i_locked)

    def set_keyboard_rotation_angle_value_lock(self, i_locked: bool) -> None:
        return self.visualization_setting_att.SetKeyboardRotationAngleValueLock(
            i_locked
        )

    def set_light_viewer_mode_lock(self, i_locked: bool) -> None:
        return self.visualization_setting_att.SetLightViewerModeLock(i_locked)

    def set_lineic_cgr_mode_lock(self, i_locked: bool) -> None:
        return self.visualization_setting_att.SetLineicCgrModeLock(i_locked)

    def set_max_selection_move_lock(self, i_locked: bool) -> None:
        return self.visualization_setting_att.SetMaxSelectionMoveLock(i_locked)

    def set_minimum_fps_mode_lock(self, i_locked: bool) -> None:
        return self.visualization_setting_att.SetMinimumFPSModeLock(i_locked)

    def set_minimum_space_fps_mode_lock(self, i_locked: bool) -> None:
        return self.visualization_setting_att.SetMinimumSpaceFPSModeLock(i_locked)

    def set_mouse_double_clic_delay_lock(self, i_locked: bool) -> None:
        return self.visualization_setting_att.SetMouseDoubleClicDelayLock(i_locked)

    def set_mouse_speed_value_lock(self, i_locked: bool) -> None:
        return self.visualization_setting_att.SetMouseSpeedValueLock(i_locked)

    def set_nb_isopars_lock(self, i_locked: bool) -> None:
        return self.visualization_setting_att.SetNbIsoparsLock(i_locked)

    def set_no_show_background_rgb(self, i_r: int, i_g: int, i_b: int) -> None:
        return self.visualization_setting_att.SetNoShowBackgroundRGB(i_r, i_g, i_b)

    def set_no_show_background_rgb_lock(self, i_locked: bool) -> None:
        return self.visualization_setting_att.SetNoShowBackgroundRGBLock(i_locked)

    def set_no_z_buffer_selection_mode_lock(self, i_locked: bool) -> None:
        return self.visualization_setting_att.SetNoZBufferSelectionModeLock(i_locked)

    def set_number_of_minimum_fps_lock(self, i_locked: bool) -> None:
        return self.visualization_setting_att.SetNumberOfMinimumFPSLock(i_locked)

    def set_number_of_minimum_space_fps_lock(self, i_locked: bool) -> None:
        return self.visualization_setting_att.SetNumberOfMinimumSpaceFPSLock(i_locked)

    def set_occlusion_culling_mode_lock(self, i_locked: bool) -> None:
        return self.visualization_setting_att.SetOcclusionCullingModeLock(i_locked)

    def set_opaque_faces_lock(self, i_locked: bool) -> None:
        return self.visualization_setting_att.SetOpaqueFacesLock(i_locked)

    def set_other_selection_timeout_activity_lock(self, i_locked: bool) -> None:
        return self.visualization_setting_att.SetOtherSelectionTimeoutActivityLock(
            i_locked
        )

    def set_other_selection_timeout_lock(self, i_locked: bool) -> None:
        return self.visualization_setting_att.SetOtherSelectionTimeoutLock(i_locked)

    def set_picking_window_size_lock(self, i_locked: bool) -> None:
        return self.visualization_setting_att.SetPickingWindowSizeLock(i_locked)

    def set_pre_selection_mode_lock(self, i_locked: bool) -> None:
        return self.visualization_setting_att.SetPreSelectionModeLock(i_locked)

    def set_preselected_element_linetype_lock(self, i_locked: bool) -> None:
        return self.visualization_setting_att.SetPreselectedElementLinetypeLock(
            i_locked
        )

    def set_preselected_element_rgb(self, i_r: int, i_g: int, i_b: int) -> None:
        return self.visualization_setting_att.SetPreselectedElementRGB(i_r, i_g, i_b)

    def set_preselected_element_rgb_lock(self, i_locked: bool) -> None:
        return self.visualization_setting_att.SetPreselectedElementRGBLock(i_locked)

    def set_rotation_sphere_mode_lock(self, i_locked: bool) -> None:
        return self.visualization_setting_att.SetRotationSphereModeLock(i_locked)

    def set_selected_edge_rgb(self, i_r: int, i_g: int, i_b: int) -> None:
        return self.visualization_setting_att.SetSelectedEdgeRGB(i_r, i_g, i_b)

    def set_selected_edge_rgb_lock(self, i_locked: bool) -> None:
        return self.visualization_setting_att.SetSelectedEdgeRGBLock(i_locked)

    def set_selected_element_rgb(self, i_r: int, i_g: int, i_b: int) -> None:
        return self.visualization_setting_att.SetSelectedElementRGB(i_r, i_g, i_b)

    def set_selected_element_rgb_lock(self, i_locked: bool) -> None:
        return self.visualization_setting_att.SetSelectedElementRGBLock(i_locked)

    def set_shader_mode_lock(self, i_locked: bool) -> None:
        return self.visualization_setting_att.SetShaderModeLock(i_locked)

    def set_static_cull_lock(self, i_locked: bool) -> None:
        return self.visualization_setting_att.SetStaticCullLock(i_locked)

    def set_static_lod_lock(self, i_locked: bool) -> None:
        return self.visualization_setting_att.SetStaticLODLock(i_locked)

    def set_stereo_mode_lock(self, i_locked: bool) -> None:
        return self.visualization_setting_att.SetStereoModeLock(i_locked)

    def set_transparency_mode_lock(self, i_locked: bool) -> None:
        return self.visualization_setting_att.SetTransparencyModeLock(i_locked)

    def set_two_side_lighting_mode_lock(self, i_locked: bool) -> None:
        return self.visualization_setting_att.SetTwoSideLightingModeLock(i_locked)

    def set_under_intensified_rgb(self, i_r: int, i_g: int, i_b: int) -> None:
        return self.visualization_setting_att.SetUnderIntensifiedRGB(i_r, i_g, i_b)

    def set_under_intensified_rgb_lock(self, i_locked: bool) -> None:
        return self.visualization_setting_att.SetUnderIntensifiedRGBLock(i_locked)

    def set_update_needed_rgb(self, i_r: int, i_g: int, i_b: int) -> None:
        return self.visualization_setting_att.SetUpdateNeededRGB(i_r, i_g, i_b)

    def set_update_needed_rgb_lock(self, i_locked: bool) -> None:
        return self.visualization_setting_att.SetUpdateNeededRGBLock(i_locked)

    def set_viewpoint_animation_mode_lock(self, i_locked: bool) -> None:
        return self.visualization_setting_att.SetViewpointAnimationModeLock(i_locked)

    def set_viz2_d_accuracy_mode_lock(self, i_locked: bool) -> None:
        return self.visualization_setting_att.SetViz2DAccuracyModeLock(i_locked)

    def set_viz2_d_fixed_accuracy_lock(self, i_locked: bool) -> None:
        return self.visualization_setting_att.SetViz2DFixedAccuracyLock(i_locked)

    def set_viz2_d_proportionnal_accuracy_lock(self, i_locked: bool) -> None:
        return self.visualization_setting_att.SetViz2DProportionnalAccuracyLock(
            i_locked
        )

    def set_viz3_d_accuracy_mode_lock(self, i_locked: bool) -> None:
        return self.visualization_setting_att.SetViz3DAccuracyModeLock(i_locked)

    def set_viz3_d_curve_accuracy_lock(self, i_locked: bool) -> None:
        return self.visualization_setting_att.SetViz3DCurveAccuracyLock(i_locked)

    def set_viz3_d_fixed_accuracy_lock(self, i_locked: bool) -> None:
        return self.visualization_setting_att.SetViz3DFixedAccuracyLock(i_locked)

    def set_viz3_d_proportionnal_accuracy_lock(self, i_locked: bool) -> None:
        return self.visualization_setting_att.SetViz3DProportionnalAccuracyLock(
            i_locked
        )

    def __repr__(self):
        return f'VisualizationSettingAtt(name="{self.name}")'
