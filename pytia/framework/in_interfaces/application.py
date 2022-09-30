from pathlib import Path

from pytia.framework.cat_types.document_types import document_type
from pytia.framework.enumeration.enumeration_types import cat_script_language
from pytia.exceptions import PytiaApplicationError
from pytia.framework.in_interfaces.document import Document
from pytia.framework.in_interfaces.documents import Documents
from pytia.framework.in_interfaces.file_system import FileSystem
from pytia.framework.in_interfaces.printer import Printer
from pytia.framework.in_interfaces.printers import Printers
from pytia.framework.in_interfaces.send_to_service import SendToService
from pytia.framework.in_interfaces.setting_controllers import SettingControllers
from pytia.framework.in_interfaces.system_configuration import SystemConfiguration
from pytia.framework.in_interfaces.window import Window
from pytia.framework.in_interfaces.windows import Windows
from pytia.framework.system_interfaces.any_object import AnyObject
from pytia.framework.system_interfaces.system_service import SystemService


class Application(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def active_document(self) -> Document:
        try:
            active_doc_com = self.com_object.ActiveDocument
            doc_suffix = active_doc_com.Name.split(".")[-1]
            return document_type[doc_suffix](active_doc_com)
        except Exception as e:
            raise PytiaApplicationError("No active document found.")

    @property
    def active_printer(self) -> Printer:
        return Printer(self.com_object.ActivePrinter)

    @active_printer.setter
    def active_printer(self, value: Printer):
        self.com_object.ActivePrinter = value

    @property
    def active_window(self) -> Window:
        return Window(self.com_object.ActiveWindow)

    @property
    def cache_size(self) -> int:
        return self.com_object.CacheSize

    @cache_size.setter
    def cache_size(self, value: int):
        self.com_object.CacheSize = value

    @property
    def caption(self) -> str:
        return self.com_object.Caption

    @caption.setter
    def caption(self, value: str):
        self.com_object.Caption = value

    @property
    def display_file_alerts(self) -> bool:
        return self.com_object.DisplayFileAlerts

    @display_file_alerts.setter
    def display_file_alerts(self, value: bool):
        self.com_object.DisplayFileAlerts = value

    @property
    def documents(self) -> Documents:
        return Documents(self.com_object.Documents)

    @property
    def file_search_order(self) -> str:
        return self.com_object.FileSearchOrder

    @file_search_order.setter
    def file_search_order(self, value: str):
        self.com_object.FileSearchOrder = value

    @property
    def file_system(self) -> FileSystem:
        return FileSystem(self.com_object.FileSystem)

    @property
    def full_name(self) -> str:
        return self.com_object.FullName

    @property
    def hso_synchronized(self) -> bool:
        return self.com_object.HSOSynchronized

    @hso_synchronized.setter
    def hso_synchronized(self, value: bool):
        self.com_object.HSOSynchronized = value

    @property
    def height(self) -> float:
        return self.com_object.Height

    @height.setter
    def height(self, value: float):
        self.com_object.Height = value

    @property
    def interactive(self) -> bool:
        return self.com_object.Interactive

    @interactive.setter
    def interactive(self, value: bool):
        self.com_object.Interactive = value

    @property
    def left(self) -> float:
        return self.com_object.Left

    @left.setter
    def left(self, value: float):
        self.com_object.Left = value

    @property
    def local_cache(self) -> str:
        return self.com_object.LocalCache

    @local_cache.setter
    def local_cache(self, value: str):
        self.com_object.LocalCache = value

    @property
    def path(self) -> Path:
        return Path(self.com_object.Path)

    @property
    def printers(self) -> Printers:
        return Printers(self.com_object.Printers)

    @property
    def refresh_display(self) -> bool:
        return self.com_object.RefreshDisplay

    @refresh_display.setter
    def refresh_display(self, value: bool):
        self.com_object.RefreshDisplay = value

    @property
    def status_bar(self) -> str:
        return self.com_object.StatusBar

    @status_bar.setter
    def status_bar(self, value: str):
        self.com_object.StatusBar = value

    @property
    def system_configuration(self) -> SystemConfiguration:
        return SystemConfiguration(self.com_object.SystemConfiguration)

    @property
    def system_service(self) -> SystemService:
        return SystemService(self.com_object.SystemService)

    @property
    def top(self) -> float:
        return self.com_object.Top

    @top.setter
    def top(self, value: float):
        self.com_object.Top = value

    @property
    def undo_redo_lock(self) -> bool:
        return self.com_object.UndoRedoLock

    @undo_redo_lock.setter
    def undo_redo_lock(self, value: bool):
        self.com_object.UndoRedoLock = value

    @property
    def visible(self) -> bool:
        return self.com_object.Visible

    @visible.setter
    def visible(self, value: bool):
        self.com_object.Visible = value

    @property
    def width(self) -> float:
        return self.com_object.Width

    @width.setter
    def width(self, value: float):
        self.com_object.Width = value

    @property
    def windows(self) -> Windows:
        return Windows(self.com_object.Windows)

    def create_send_to(self) -> SendToService:
        return SendToService(self.com_object.CreateSendTo())

    def disable_new_undo_redo_transaction(self) -> None:
        return self.com_object.DisableNewUndoRedoTransaction()

    def enable_new_undo_redo_transaction(self) -> None:
        return self.com_object.EnableNewUndoRedoTransaction()

    def file_selection_box(self, i_title: str, i_extension: str, i_mode: int) -> str:
        return self.com_object.FileSelectionBox(i_title, i_extension, i_mode)

    def get_workbench_id(self) -> str:
        return self.com_object.GetWorkbenchId()

    def help(self, i_help_id: str) -> None:
        return self.com_object.Help(i_help_id)

    def message_box(self, message_text: str, buttons: int = 0, title: str = ""):
        function_name = "message_box"
        msg_box = (
            f"Public Function {function_name}(message_text, buttons, title)\n"
            f"    {function_name} = MsgBox(message_text, buttons, title)\n"
            "End Function"
        )
        return self.system_service.evaluate(
            msg_box,
            cat_script_language.index("CATVBScriptLanguage"),
            function_name,
            [message_text, buttons, title],
        )

    def quit(self) -> None:
        return self.com_object.Quit()

    def setting_controllers(self):
        return SettingControllers(self.com_object.SettingControllers)

    def start_command(self, i_command_id: str) -> None:
        return self.com_object.StartCommand(i_command_id)

    def start_workbench(self, iworkbench_id: str) -> None:
        return self.com_object.StartWorkbench(iworkbench_id)

    def __repr__(self):
        return f'Application(name="{self.name}")'
