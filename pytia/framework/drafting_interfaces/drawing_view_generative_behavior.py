from typing import TYPE_CHECKING
from pytia.framework.system_interfaces.any_object import AnyObject
from pytia.framework.system_interfaces.cat_base_dispatch import CATBaseDispatch

if TYPE_CHECKING:
    from pytia.framework.drafting_interfaces.drawing_view import DrawingView


class DrawingViewGenerativeBehavior(CATBaseDispatch):
    def __init__(self, com_object):
        super().__init__()
        self.drawing_view_generative_behavior = com_object

    @property
    def color_inheritance_mode(self) -> int:
        return self.drawing_view_generative_behavior.ColorInheritanceMode

    @color_inheritance_mode.setter
    def color_inheritance_mode(self, value: int):
        self.drawing_view_generative_behavior.ColorInheritanceMode = value

    @property
    def document(self) -> AnyObject:
        return AnyObject(self.drawing_view_generative_behavior.Document)

    @document.setter
    def document(self, document: AnyObject):
        self.drawing_view_generative_behavior.Document = document.com_object

    @property
    def fillet_representation(self) -> int:
        return self.drawing_view_generative_behavior.FilletRepresentation

    @fillet_representation.setter
    def fillet_representation(self, value: int):
        self.drawing_view_generative_behavior.FilletRepresentation = value

    @property
    def hidden_line_mode(self) -> int:
        return self.drawing_view_generative_behavior.HiddenLineMode

    @hidden_line_mode.setter
    def hidden_line_mode(self, value: int):
        self.drawing_view_generative_behavior.HiddenLineMode = value

    @property
    def image_view_mode(self) -> int:
        return self.drawing_view_generative_behavior.ImageViewMode

    @image_view_mode.setter
    def image_view_mode(self, value: int):
        self.drawing_view_generative_behavior.ImageViewMode = value

    @property
    def limit_bounding_box(self) -> float:
        return self.drawing_view_generative_behavior.LimitBoundingBox

    @limit_bounding_box.setter
    def limit_bounding_box(self, value: float):
        self.drawing_view_generative_behavior.LimitBoundingBox = value

    @property
    def parent_view(self) -> "DrawingView":
        from pytia.framework.drafting_interfaces.drawing_view import DrawingView

        return DrawingView(self.drawing_view_generative_behavior.ParentView)

    @property
    def points_projection_mode(self) -> int:
        return self.drawing_view_generative_behavior.PointsProjectionMode

    @points_projection_mode.setter
    def points_projection_mode(self, value: int):
        self.drawing_view_generative_behavior.PointsProjectionMode = value

    @property
    def points_symbol(self) -> int:
        return self.drawing_view_generative_behavior.PointsSymbol

    @points_symbol.setter
    def points_symbol(self, value: int):
        self.drawing_view_generative_behavior.PointsSymbol = value

    @property
    def representation_mode(self) -> int:
        return self.drawing_view_generative_behavior.RepresentationMode

    @representation_mode.setter
    def representation_mode(self, value: int):
        self.drawing_view_generative_behavior.RepresentationMode = value

    def apply_breakout_to(self, i_parent_view: "DrawingViewGenerativeBehavior") -> None:
        return self.drawing_view_generative_behavior.ApplyBreakoutTo(
            i_parent_view.drawing_view_generative_behavior
        )

    def define_auxiliary_view(
        self,
        i_x_start_point: float,
        i_y_start_point: float,
        i_x_end_point: float,
        y_end_point: float,
        i_side_to_draw: int,
        i_parent_view_generative_behavior: "DrawingViewGenerativeBehavior",
    ) -> None:
        return self.drawing_view_generative_behavior.DefineAuxiliaryView(
            i_x_start_point,
            i_y_start_point,
            i_x_end_point,
            y_end_point,
            i_side_to_draw,
            i_parent_view_generative_behavior.drawing_view_generative_behavior,
        )

    def define_box_3d_view(self, i_boxable_object: AnyObject) -> None:
        return self.drawing_view_generative_behavior.DefineBox3DView(
            i_boxable_object.com_object
        )

    def define_breakout(
        self, i_profil: tuple, i_plane1: tuple, i_plane2: tuple
    ) -> None:
        return self.drawing_view_generative_behavior.DefineBreakout(
            i_profil, i_plane1, i_plane2
        )

    def define_broken_view(
        self,
        i_broken_lines_extremities: tuple,
        i_x_direction: float,
        i_y_direction: float,
    ) -> None:
        return self.drawing_view_generative_behavior.DefineBrokenView(
            i_broken_lines_extremities, i_x_direction, i_y_direction
        )

    def define_circular_clipping_view(
        self, x_center: float, y_center: float, radius: float
    ) -> None:
        return self.drawing_view_generative_behavior.DefineCircularClippingView(
            x_center, y_center, radius
        )

    def define_circular_detail_view(
        self,
        i_x_center: float,
        i_y_center: float,
        i_radius: float,
        i_parent_view_generative_behavior: "DrawingViewGenerativeBehavior",
    ) -> None:
        return self.drawing_view_generative_behavior.DefineCircularDetailView(
            i_x_center,
            i_y_center,
            i_radius,
            i_parent_view_generative_behavior.drawing_view_generative_behavior,
        )

    def define_circular_exact_clipping_view(
        self, x_center: float, y_center: float, radius: float
    ) -> None:
        return self.drawing_view_generative_behavior.DefineCircularExactClippingView(
            x_center, y_center, radius
        )

    def define_front_view(
        self,
        i_x1: float,
        i_y1: float,
        i_z1: float,
        i_x2: float,
        i_y2: float,
        i_z2: float,
    ) -> None:
        return self.drawing_view_generative_behavior.DefineFrontView(
            i_x1, i_y1, i_z1, i_x2, i_y2, i_z2
        )

    def define_isometric_view(
        self,
        i_x1: float,
        i_y1: float,
        i_z1: float,
        i_x2: float,
        i_y2: float,
        i_z2: float,
    ) -> None:
        return self.drawing_view_generative_behavior.DefineIsometricView(
            i_x1, i_y1, i_z1, i_x2, i_y2, i_z2
        )

    def define_polygonal_clipping_view(self, profile: tuple) -> None:
        return self.drawing_view_generative_behavior.DefinePolygonalClippingView(
            profile
        )

    def define_polygonal_detail_view(
        self,
        i_profile: tuple,
        i_parent_view_generative_behavior: "DrawingViewGenerativeBehavior",
    ) -> None:
        return self.drawing_view_generative_behavior.DefinePolygonalDetailView(
            i_profile,
            i_parent_view_generative_behavior.drawing_view_generative_behavior,
        )

    def define_polygonal_exact_clipping_view(self, profile: tuple) -> None:
        return self.drawing_view_generative_behavior.DefinePolygonalExactClippingView(
            profile
        )

    def define_projection_view(
        self,
        i_parent_view_generative_behavior: "DrawingViewGenerativeBehavior",
        i_type: int,
    ) -> None:
        return self.drawing_view_generative_behavior.DefineProjectionView(
            i_parent_view_generative_behavior.drawing_view_generative_behavior, i_type
        )

    def define_section_view(
        self,
        i_profile: tuple,
        i_section_type: str,
        i_profile_type: str,
        i_side_to_draw: int,
        i_parent_view_generative_behavior: "DrawingViewGenerativeBehavior",
    ) -> None:
        return self.drawing_view_generative_behavior.DefineSectionView(
            i_profile,
            i_section_type,
            i_profile_type,
            i_side_to_draw,
            i_parent_view_generative_behavior.drawing_view_generative_behavior,
        )

    def define_stand_alone_section(
        self,
        profile: tuple,
        type_of_section: str,
        type_of_profile: str,
        i_plane: tuple,
        i_side: int,
    ) -> None:
        return self.drawing_view_generative_behavior.DefineStandAloneSection(
            profile, type_of_section, type_of_profile, i_plane, i_side
        )

    def define_tps_section_view(
        self,
        i_profile: tuple,
        i_section_type: str,
        i_profile_type: str,
        i_side_to_draw: int,
        i_parent_view_generative_behavior: "DrawingViewGenerativeBehavior",
    ) -> None:
        return self.drawing_view_generative_behavior.DefineTPSSectionView(
            i_profile,
            i_section_type,
            i_profile_type,
            i_side_to_draw,
            i_parent_view_generative_behavior.drawing_view_generative_behavior,
        )

    def define_unfolded_view(
        self,
        i_x1: float,
        i_y1: float,
        i_z1: float,
        i_x2: float,
        i_y2: float,
        i_z2: float,
    ) -> None:
        return self.drawing_view_generative_behavior.DefineUnfoldedView(
            i_x1, i_y1, i_z1, i_x2, i_y2, i_z2
        )

    def force_update(self) -> None:
        return self.drawing_view_generative_behavior.ForceUpdate()

    def get_axis_system(self, o_product: AnyObject, o_axis_system: AnyObject) -> None:
        return self.drawing_view_generative_behavior.GetAxisSysteme(
            o_product.com_object, o_axis_system.com_object
        )

    def get_gps_name(self) -> str:
        return self.drawing_view_generative_behavior.GetGPSName()

    def get_projection_plane(
        self,
        o_x1: float,
        o_y1: float,
        o_z1: float,
        o_x2: float,
        o_y2: float,
        o_z2: float,
    ) -> None:
        return self.drawing_view_generative_behavior.GetProjectionPlane(
            o_x1, o_y1, o_z1, o_x2, o_y2, o_z2
        )

    def get_projection_plane_normal(
        self, o_x_normal: float, o_y_normal: float, o_z_normal: float
    ) -> None:
        return self.drawing_view_generative_behavior.GetProjectionPlaneNormal(
            o_x_normal, o_y_normal, o_z_normal
        )

    def set_axis_systeme(self, i_product: AnyObject, i_axis_systeme: AnyObject) -> None:
        return self.drawing_view_generative_behavior.SetAxisSysteme(
            i_product.com_object, i_axis_systeme.com_object
        )

    def set_gps_name(self, i_gps_name: str) -> None:
        return self.drawing_view_generative_behavior.SetGPSName(i_gps_name)

    def set_projection_plane(
        self,
        i_x1: float,
        i_y1: float,
        i_z1: float,
        i_x2: float,
        i_y2: float,
        i_z2: float,
    ) -> None:
        return self.drawing_view_generative_behavior.SetProjectionPlane(
            i_x1, i_y1, i_z1, i_x2, i_y2, i_z2
        )

    def un_break(self) -> None:
        return self.drawing_view_generative_behavior.UnBreak()

    def un_breakout(self) -> None:
        return self.drawing_view_generative_behavior.UnBreakout()

    def un_breakout_num(self, i_breakout_number: int) -> None:
        return self.drawing_view_generative_behavior.UnBreakoutNum(i_breakout_number)

    def un_clip(self) -> None:
        return self.drawing_view_generative_behavior.UnClip()

    def update(self) -> None:
        return self.drawing_view_generative_behavior.Update()

    def __repr__(self):
        return f"DrawingViewGenerativeBehavior()"
