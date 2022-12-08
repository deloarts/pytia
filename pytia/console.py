"""
    Module for handling console output.
"""

import atexit
import sys
from tempfile import gettempdir

from colorama import init as colorama_init

from pytia.const import (
    CONSOLE_GREY,
    CONSOLE_RESET,
    CONSOLE_STATUS_FAIL,
    CONSOLE_STATUS_INFO,
    CONSOLE_STATUS_OK,
    CONSOLE_STATUS_WARN,
    LOG_FILENAME,
)
from pytia.log import log


class Console:
    """
    Main class for handling console output.
    """

    def __init__(
        self, init_msg: str | None = None, show_log_path: bool = False
    ) -> None:
        """Inits the Console class."""
        colorama_init()
        self.__count_nl = 0
        log_folder = gettempdir()

        log.add_file_handler(folder=log_folder, filename=LOG_FILENAME)
        if init_msg is not None:
            print(init_msg)
        if show_log_path:
            atexit.register(
                lambda: print(
                    f"\n{CONSOLE_GREY}See the full output in "
                    f"{log_folder}\\{LOG_FILENAME}{CONSOLE_RESET}\n"
                )
            )

    def __clear_last_line(self) -> None:
        """Clears the last line/lines from the __print function."""
        for _ in range(self.__count_nl):
            sys.stdout.write("\x1b[1A")  # Cursor up one line
            sys.stdout.write("\x1b[2K")  # Delete line
        self.__count_nl = 0

    def __print(
        self,
        *,
        status: str,
        text: str,
        in_current_line: bool,
    ) -> None:
        """
        Prints to stdout.

        Args:
            status (str): The status flag (info, warning, error, etc)
            text (str): The message to print to stdout.
            in_current_line (bool): Prints the message in the current line.
        """
        if in_current_line:
            self.__clear_last_line()
        else:
            self.__count_nl = 0

        for index, line in enumerate(text.split("\n")):
            print(status, end="  ") if index == 0 else print(" " * 10, end="")
            print(line, CONSOLE_RESET)
            self.__count_nl += 1

    def error(self, text: str, in_current_line: bool = False) -> None:
        """
        Prints an error message to stdout.

        Args:
            text (str): The message to print to stdout.
            in_current_line (bool, optional): Prints the message in the current line if set to \
                True. Defaults to False.
        """
        self.__print(
            status=CONSOLE_STATUS_FAIL, text=text, in_current_line=in_current_line
        )

    def warning(self, text: str, in_current_line: bool = False) -> None:
        """
        Prints an warning message to stdout.

        Args:
            text (str): The message to print to stdout.
            in_current_line (bool, optional): Prints the message in the current line if set to \
                True. Defaults to False.
        """
        self.__print(
            status=CONSOLE_STATUS_WARN, text=text, in_current_line=in_current_line
        )

    def info(self, text: str, in_current_line: bool = False) -> None:
        """
        Prints an info message to stdout.

        Args:
            text (str): The message to print to stdout.
            in_current_line (bool, optional): Prints the message in the current line if set to \
                True. Defaults to False.
        """
        self.__print(
            status=CONSOLE_STATUS_INFO, text=text, in_current_line=in_current_line
        )

    def ok(self, text: str, in_current_line: bool = False) -> None:
        """
        Prints an ok message to stdout.

        Args:
            text (str): The message to print to stdout.
            in_current_line (bool, optional): Prints the message in the current line if set to \
                True. Defaults to False.
        """
        self.__print(
            status=CONSOLE_STATUS_OK, text=text, in_current_line=in_current_line
        )
