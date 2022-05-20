from typing import TYPE_CHECKING
from pytia.framework.drafting_interfaces.drawing_arrows import DrawingArrows
from pytia.framework.drafting_interfaces.drawing_components import DrawingComponents
from pytia.framework.drafting_interfaces.drawing_dimensions import DrawingDimensions
from pytia.framework.drafting_interfaces.drawing_pictures import DrawingPictures
from pytia.framework.drafting_interfaces.drawing_tables import DrawingTables
from pytia.framework.drafting_interfaces.drawing_texts import DrawingTexts
from pytia.framework.drafting_interfaces.drawing_threads import DrawingThreads
from pytia.framework.drafting_interfaces.drawing_view_generative_behavior import (
    DrawingViewGenerativeBehavior,
)
from pytia.framework.drafting_interfaces.drawing_view_generative_links import (
    DrawingViewGenerativeLinks,
)
from pytia.framework.drafting_interfaces.drawing_weldings import DrawingWeldings
from pytia.framework.mec_mod_interfaces.geometric_elements import GeometricElements
from pytia.framework.sketcher_interfaces.factory_2D import Factory2D
from pytia.framework.system_interfaces.any_object import AnyObject

if TYPE_CHECKING:
    from pytia.framework.drafting_interfaces.drawing_text import DrawingText


class DrawingView(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.drawing_view = com_object

    @property
    def angle(self) -> float:
        return self.drawing_view.Angle

    @angle.setter
    def angle(self, value: float):
        self.drawing_view.Angle = value

    @property
    def arrows(self) -> DrawingArrows:
        return DrawingArrows(self.drawing_view.Arrows)

    @property
    def components(self) -> DrawingComponents:
        return DrawingComponents(self.drawing_view.Components)

    @property
    def dimensions(self) -> DrawingDimensions:
        return DrawingDimensions(self.drawing_view.Dimensions)

    @property
    def factory_2d(self) -> Factory2D:
        return Factory2D(self.drawing_view.Factory2D)

    @property
    def frame_visualization(self) -> bool:
        return self.drawing_view.FrameVisualization

    @frame_visualization.setter
    def frame_visualization(self, value: bool):
        self.drawing_view.FrameVisualization = value

    @property
    def generative_behavior(self) -> DrawingViewGenerativeBehavior:
        return DrawingViewGenerativeBehavior(self.drawing_view.GenerativeBehavior)

    @property
    def generative_links(self) -> DrawingViewGenerativeLinks:
        return DrawingViewGenerativeLinks(self.drawing_view.GenerativeLinks)

    @property
    def geometric_elements(self) -> GeometricElements:
        return GeometricElements(self.drawing_view.GeometricElements)

    @property
    def lock_status(self) -> bool:
        return self.drawing_view.LockStatus

    @lock_status.setter
    def lock_status(self, value: bool):
        self.drawing_view.LockStatus = value

    @property
    def pictures(self) -> DrawingPictures:
        return DrawingPictures(self.drawing_view.Pictures)

    @property
    def reference_view(self) -> "DrawingView":
        return DrawingView(self.drawing_view.ReferenceView)

    @reference_view.setter
    def reference_view(self, value: "DrawingView"):
        self.drawing_view.ReferenceView = value

    @property
    def scale(self) -> float:
        return self.drawing_view.Scale

    @scale.setter
    def scale(self, value: float):
        self.drawing_view.Scale = value

    @property
    def scale2(self) -> float:
        return self.drawing_view.Scale2

    @scale2.setter
    def scale2(self, value: float):
        self.drawing_view.Scale2 = value

    @property
    def tables(self) -> DrawingTables:
        return DrawingTables(self.drawing_view.Tables)

    @property
    def texts(self) -> DrawingTexts:
        return DrawingTexts(self.drawing_view.Texts)

    @property
    def threads(self) -> DrawingThreads:
        return DrawingThreads(self.drawing_view.Threads)

    @property
    def view_type(self) -> int:
        return self.drawing_view.ViewType

    @property
    def weldings(self) -> DrawingWeldings:
        return DrawingWeldings(self.drawing_view.Weldings)

    @property
    def x(self) -> float:
        return self.drawing_view.x

    @x.setter
    def x(self, value: float):
        self.drawing_view.x = value

    @property
    def x_axis_data(self) -> float:
        return self.drawing_view.xAxisData

    @x_axis_data.setter
    def x_axis_data(self, value: float):
        self.drawing_view.xAxisData = value

    @property
    def y(self) -> float:
        return self.drawing_view.y

    @y.setter
    def y(self, value: float):
        self.drawing_view.y = value

    @property
    def y_axis_data(self) -> float:
        return self.drawing_view.yAxisData

    @y_axis_data.setter
    def y_axis_data(self, value: float):
        self.drawing_view.yAxisData = value

    def activate(self) -> None:
        return self.drawing_view.Activate()

    def aligned_with_reference_view(self) -> None:
        return self.drawing_view.AlignedWithReferenceView()

    def get_view_name(
        self, i_view_name_prefix: str, i_view_name_ident: str, i_view_name_suffix: str
    ) -> None:
        return self.drawing_view.GetViewName(
            i_view_name_prefix, i_view_name_ident, i_view_name_suffix
        )

    def insert_view_angle(self, i_first: int, io_text: "DrawingText") -> None:
        return self.drawing_view.InsertViewAngle(i_first, io_text.com_object)

    def insert_view_scale(self, i_first: int, io_text: "DrawingText") -> None:
        return self.drawing_view.InsertViewScale(i_first, io_text.com_object)

    def is_generative(self) -> bool:
        return self.drawing_view.IsGenerative()

    def isolate(self) -> None:
        return self.drawing_view.Isolate()

    def save_edition(self) -> None:
        return self.drawing_view.SaveEdition()

    def set_view_name(
        self, i_view_name_prefix: str, i_view_name_ident: str, i_view_name_suffix: str
    ) -> None:
        return self.drawing_view.SetViewName(
            i_view_name_prefix, i_view_name_ident, i_view_name_suffix
        )

    def size(self, o_values: tuple) -> float:
        return self.drawing_view.Size(o_values)

    def un_aligned_with_reference_view(self) -> None:
        return self.drawing_view.UnAlignedWithReferenceView()

    def __repr__(self):
        return f'DrawingView(name="{self.name}")'
