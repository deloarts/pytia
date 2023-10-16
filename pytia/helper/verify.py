"""
    Helper module for verifying objects.
"""

from pathlib import Path
from pathlib import WindowsPath

from pytia.exceptions import PytiaNotAFolderError


def verify_folder(folder: Path, absolute: bool = False) -> Path:
    """
    Returns a given folder as windows style path.

    Args:
        folder (Path): The folder to verify.
        absolute (bool, optional): Verifies if a folder is absolute. Defaults to False.

    Raises:
        PytiaNotAFolderError: Error when the folder cannot be verified.

    Returns:
        str: The input folder without trailing slash in windows style.
    """

    if not folder or not folder.is_dir():
        raise PytiaNotAFolderError(
            f"The given folder {str(folder)!r} is not a directory."
        )

    if absolute and not folder.is_absolute():
        raise PytiaNotAFolderError(
            f"The given folder {folder!r} is not an absolute path."
        )

    return WindowsPath(folder)
