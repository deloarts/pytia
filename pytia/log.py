"""
    Logging module that connects to the pytia logger.
"""

import logging
import logging.handlers
import os
from tempfile import gettempdir
from typing import Optional

from pytia.const import HOSTNAME, USERNAME


class Log:
    """Main class for logging."""

    def __init__(self, debug: bool = False) -> None:
        """
        Inits the logger named pytia at level INFO.

        Args:
            debug (bool, optional): Sets the level to DEBUG if True. Defaults to False.
        """
        self.logger = logging.getLogger("pytia")
        self.format = logging.Formatter(
            f"%(asctime)s\t%(name)s\t%(levelname)s\t{HOSTNAME}\t{USERNAME}\t%(message)s"
        )
        if debug:
            self.logger.setLevel(logging.DEBUG)
        else:
            self.logger.setLevel(logging.INFO)
        self.stream_handler: logging.StreamHandler = None  # type: ignore
        self.file_handler: logging.handlers.RotatingFileHandler = None  # type:ignore

    def add_stream_handler(self):
        """Adds a stream handler for stdout."""
        self.stream_handler = logging.StreamHandler()
        self.stream_handler.setLevel(self.logger.level)
        self.stream_handler.setFormatter(self.format)
        self.logger.addHandler(self.stream_handler)

    def add_file_handler(
        self,
        folder: Optional[str] = None,
        filename: Optional[str] = None,
        backup_count: int = 10,
    ):
        """
        Adds a rotating file handler. Every time the log is initialized,
        a new logfile is created. Backup is 10 files by default.
        """
        if not folder:
            folder = gettempdir()

        if not filename:
            filename = "pytia.log"
        elif not ".log" in filename:
            filename = filename + ".log"

        path = f"{folder}{os.sep}{filename}"

        self.file_handler = logging.handlers.RotatingFileHandler(
            path, mode="w", backupCount=backup_count, delay=True
        )
        self.file_handler.setLevel(self.logger.level)
        self.file_handler.setFormatter(self.format)
        self.logger.addHandler(self.file_handler)
        if os.path.isfile(path):
            self.file_handler.doRollover()

    def set_level_debug(self) -> None:
        """Sets the log-level to DEBUG."""
        self.logger.setLevel(logging.DEBUG)
        if self.stream_handler:
            self.stream_handler.setLevel(logging.DEBUG)
        if self.file_handler:
            self.file_handler.setLevel(logging.DEBUG)

    def set_level_info(self) -> None:
        """Sets the log-level to INFO."""
        self.logger.setLevel(logging.INFO)
        if self.stream_handler:
            self.stream_handler.setLevel(logging.INFO)
        if self.file_handler:
            self.file_handler.setLevel(logging.INFO)

    def set_level_warning(self) -> None:
        """Sets the log-level to WARNING."""
        self.logger.setLevel(logging.WARNING)
        if self.stream_handler:
            self.stream_handler.setLevel(logging.WARNING)
        if self.file_handler:
            self.file_handler.setLevel(logging.WARNING)

    def debug(self, message: str) -> None:
        """Logs a debug message."""
        self.logger.debug(msg=message)

    def info(self, message: str) -> None:
        """Logs an info message."""
        self.logger.info(msg=message)

    def warning(self, message: str) -> None:
        """Logs a warning message."""
        self.logger.warning(msg=message)

    def error(self, message: str) -> None:
        """Logs an error message."""
        self.logger.error(msg=message, exc_info=False)

    def exception(self, message: str) -> None:
        """Logs an error message from an exception."""
        self.logger.exception(msg=message)


log = Log()
