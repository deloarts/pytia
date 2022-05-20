"""
    Helper module for verifying objects.
"""

import os

from pytia.exceptions import PytiaNotAFolderError


def verify_folder(folder: str, absolute: bool = False) -> str:
    """
    Returns a given folder as windows style without trailing slash.

    Args:
        folder (str): The folder to verify.
        absolute (bool, optional): Verifies if a folder is absolute. Defaults to False.

    Raises:
        PytiaNotAFolderError: Error when the folder cannot be verified.

    Returns:
        str: The input folder without trailing slash in windows style.
    """

    if not folder or not os.path.isdir(folder):
        raise PytiaNotAFolderError(f"The given folder {folder!r} is not a directory.")

    if absolute and not os.path.isabs(folder):
        raise PytiaNotAFolderError(
            f"The given folder {folder!r} is not an absolute path."
        )

    folder = folder.replace("/", os.sep)
    while folder[-1] == os.sep:
        folder = folder[:-1]

    return folder
