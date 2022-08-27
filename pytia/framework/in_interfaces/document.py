from pathlib import Path
from typing import TYPE_CHECKING

from pytia.framework.exception_handling import CATIAApplicationException
from pytia.framework.in_interfaces.cameras import Cameras
from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.in_interfaces.window import Window
from pytia.framework.in_interfaces.workbench import Workbench
from pytia.framework.space_analyses_interfaces.spa_workbench import SPAWorkbench
from pytia.framework.system_interfaces.any_object import AnyObject

if TYPE_CHECKING:
    from pytia.framework.in_interfaces.selection import Selection


class Document(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.document = com_object

    @property
    def cameras(self) -> Cameras:
        return Cameras(self.document.Cameras)

    @property
    def current_filter(self) -> str:
        return self.document.CurrentFilter

    @current_filter.setter
    def current_filter(self, value: str):
        self.document.CurrentFilter = value

    @property
    def current_layer(self) -> str:
        return self.document.CurrentLayer

    @current_layer.setter
    def current_layer(self, value: str):
        self.document.CurrentLayer = value

    @property
    def is_part(self):
        try:
            if self.part.part:  # type: ignore
                return True
        except AttributeError:
            return False

    @property
    def is_product(self):
        if self.product.is_catproduct():  # type: ignore
            return True
        return False

    @property
    def is_saved(self):
        return self.document.Saved

    @property
    def full_name(self):
        return str(self.path())

    @property
    def read_only(self) -> bool:
        return self.document.ReadOnly

    @property
    def see_hidden_elements(self):
        return self.document.SeeHiddenElements

    @see_hidden_elements.setter
    def see_hidden_elements(self, value: bool):
        self.document.SeeHiddenElements = value

    @property
    def selection(self) -> "Selection":
        from pytia.framework.in_interfaces.selection import Selection

        return Selection(self.document.Selection)

    def activate(self) -> None:
        return self.document.Activate()

    def close(self) -> None:
        self.document.Close()

    def create_filter(self, i_filter_name: str, i_filter_definition: str) -> None:
        return self.document.CreateFilter(i_filter_name, i_filter_definition)

    def create_reference_from_name(self, i_label: str) -> Reference:
        return Reference(self.document.CreateReferenceFromName(i_label))

    def get_workbench(self, workbench_name: str) -> Workbench:
        return Workbench(self.document.GetWorkbench(workbench_name))

    def export_data(self, file_name: Path, file_type: str, overwrite=False) -> None:
        current_dfa_setting = self.document.Application.DisplayFileAlerts
        if not isinstance(file_name, Path):
            file_name = Path(file_name)
        if file_name.suffix.lower() != "." + file_type.lower():
            raise CATIAApplicationException(
                f'Filename "{file_name}" must have the same suffix as filetype "{file_type}".'
            )
        if not str(file_name).endswith(file_type):
            file_name = Path(f"{file_name}.{file_type}")
        if not file_name.parent.is_dir():
            raise NotADirectoryError(
                f"Directory: {file_name.parent} is not a directory."
            )
        if overwrite is False and file_name.is_file():
            raise FileExistsError(
                f"File: {file_name} already exists. "
                f"Set overwrite=True if you want to overwrite."
            )
        self.document.ExportData(file_name, file_type)
        self.document.Application.DisplayFileAlerts = current_dfa_setting

    def indicate_2d(self, i_message: str, io_document_window_location: tuple) -> str:
        return self.document.Indicate2D(i_message, io_document_window_location)

    def indicate_3d(
        self,
        i_planar_geometric_object: AnyObject,
        i_message: str,
        io_window_location2_d: tuple,
        io_window_location3_d: tuple,
    ) -> str:
        return self.document.Indicate3D(
            i_planar_geometric_object.com_object,
            i_message,
            io_window_location2_d,
            io_window_location3_d,
        )

    def new_window(self):
        return Window(self.document.NewWindow())

    def path(self):
        return Path(self.document.FullName)

    def remove_filter(self, i_filter_name):
        return self.document.RemoveFilter(i_filter_name)

    def save(self) -> None:
        self.document.Save()

    def save_as(self, full_name: Path) -> None:
        self.document.SaveAs(str(full_name))

    def spa_workbench(self):
        return SPAWorkbench(self.com_object)

    def __repr__(self):
        return f'Document(name="{self.name}")'
