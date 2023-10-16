"""
    The framework for interacting with CATIA.

    .. warning::
        The documentation of the framework can be found inside the **V5automation.chm** 
        (/assets/V5Automation.chm) help file.
"""

import atexit
import os

from psutil import process_iter
from pycatia.in_interfaces.application import Application
from win32com.client import CDispatch
from win32com.client import Dispatch

from pytia import __version__
from pytia.exceptions import PytiaApplicationError
from pytia.log import log


class Framework:
    def __init__(self) -> None:
        """Inits the catia application dispatch."""
        if not os.name == "nt":
            raise OSError(f"This operating system is not supported.")

        if "CNEXT.exe" not in (p.name() for p in process_iter()):
            raise PytiaApplicationError(
                "Failed connecting to CATIA: Application not running."
            )

        self._dispatch = Dispatch("CATIA.Application")
        self._catia = Application(self._dispatch)
        self._catia.status_bar = f"Connected to pytia {__version__}"

        atexit.register(self._exit)

        log.info(
            f"Connected to CATIA V{self._catia.system_configuration.version}-"
            f"R{self._catia.system_configuration.release} "
            f"SP{self._catia.system_configuration.service_pack}."
        )

    def _exit(self) -> None:
        """Triggered at exit."""
        self._catia.status_bar = ""
        log.info("Disconnected from CATIA.")

    @property
    def catia(self) -> Application:
        """Returns the catia application."""
        return self._catia

    @property
    def dispatch(self) -> CDispatch:
        """Returns the catia dispatch."""
        return self._dispatch


framework = Framework()
