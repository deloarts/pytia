import os
from pathlib import Path
from pytia.framework.drafting_interfaces.drawing_page_setup import DrawingPageSetup
from pytia.framework.drafting_interfaces.drawing_views import DrawingViews
from pytia.framework.drafting_interfaces.print_area import PrintArea
from pytia.framework.exception_handling.exceptions import CATIAApplicationException
from pytia.framework.system_interfaces.any_object import AnyObject


class DrawingSheet(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.drawing_sheet = com_object

    @property
    def gen_views_pos_mode(self) -> int:
        return self.drawing_sheet.GenViewsPosMode

    @gen_views_pos_mode.setter
    def gen_views_pos_mode(self, value: int):
        self.drawing_sheet.GenViewsPosMode = value

    @property
    def orientation(self) -> int:
        return self.drawing_sheet.Orientation

    @orientation.setter
    def orientation(self, value: int):
        self.drawing_sheet.Orientation = value

    @property
    def page_setup(self) -> DrawingPageSetup:
        return DrawingPageSetup(self.drawing_sheet.PageSetup)

    @property
    def paper_size(self) -> int:
        return self.drawing_sheet.PaperSize

    @paper_size.setter
    def paper_size(self, value: int):
        self.drawing_sheet.PaperSize = value

    @property
    def print_area(self) -> PrintArea:
        return PrintArea(self.drawing_sheet.PrintArea)

    @property
    def projection_method(self) -> int:
        return self.drawing_sheet.ProjectionMethod

    @projection_method.setter
    def projection_method(self, value: int):
        self.drawing_sheet.ProjectionMethod = value

    @property
    def scale(self) -> float:
        return self.drawing_sheet.Scale

    @scale.setter
    def scale(self, value: float):
        self.drawing_sheet.Scale = value

    @property
    def scale2(self) -> float:
        return self.drawing_sheet.Scale2

    @scale2.setter
    def scale2(self, value: float):
        self.drawing_sheet.Scale2 = value

    @property
    def views(self) -> DrawingViews:
        return DrawingViews(self.drawing_sheet.Views)

    def activate(self) -> None:
        return self.drawing_sheet.Activate()

    def force_update(self) -> None:
        return self.drawing_sheet.ForceUpdate()

    def generate_dimensions(self) -> None:
        return self.drawing_sheet.GenerateDimensions()

    def get_paper_height(self) -> float:
        return self.drawing_sheet.GetPaperHeight()

    def get_paper_width(self) -> float:
        return self.drawing_sheet.GetPaperWidth()

    def is_detail(self) -> bool:
        return self.drawing_sheet.IsDetail()

    def isolate(self) -> None:
        return self.drawing_sheet.Isolate()

    def print_out(self) -> None:
        return self.drawing_sheet.PrintOut()

    def print_to_file(self, file_name: Path, overwrite=False) -> None:
        if not isinstance(file_name, Path):
            file_name = Path(file_name)
        if str(file_name.parent) == ".":
            file_name = Path(os.getcwd(), file_name)
        if not file_name.parent.is_dir():
            raise NotADirectoryError(
                f"Directory {file_name.parent} is not a directory."
            )
        if overwrite is False and file_name.is_file():
            raise FileExistsError(
                f"File: {file_name} already exists. "
                f"Set overwrite=True if you want to overwrite."
            )
        self.drawing_sheet.PrintToFile(file_name)

    def set_as_detail(self) -> None:
        return self.drawing_sheet.SetAsDetail()

    def set_paper_height(self, o_paper_height: float) -> None:
        return self.drawing_sheet.SetPaperHeight(o_paper_height)

    def set_paper_width(self, o_paper_width: float) -> None:
        return self.drawing_sheet.SetPaperWidth(o_paper_width)

    def update(self) -> None:
        return self.drawing_sheet.Update()

    def reorder_views(self, i_ordered_views: tuple) -> None:
        return self.drawing_sheet.reorder_Views(i_ordered_views)

    def __repr__(self):
        return f'DrawingSheet(name="{self.name}")'
