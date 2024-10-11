"""
    Path utility functions
"""

import os
import re
from pathlib import Path

from exceptions import PytiaEnvVarNotFound
from exceptions import PytiaWorkspaceFolderNotFound


def expand_env_vars(path: str, ignore_not_found: bool = False) -> str:
    """
    Expands windows environment variables from a given path.
    E.g.: Expands %ONEDRIVE%/foo/bar to "C:/Users/.../OneDrive/foo/bar

    The variable to replace must be between two percentage symbols.

    Args:
        path (str): The path from which to expand the env var.
        ignore_not_found (bool, optional): Returns the given path if there is no
            env var in it. Defaults to False.

    Raises:
        PytiaEnvVarNotFound: Raised when there is no env var in the given path and
            ignore_not_found is False.

    Returns:
        str: The full path.
    """
    output = path
    filter_result = re.findall(r"\%(.*?)\%", path)
    for key in filter_result:
        if key in os.environ:
            output = path.replace(f"%{key}%", os.environ[key])  # type: ignore
        elif ignore_not_found:
            return path
        else:
            raise PytiaEnvVarNotFound(
                f"The environment variable {key!r} is not set on this computer"
            )
    return output


def create_path_symlink(path: Path) -> str:
    """
    Replaces the parts of the given path with the environment variable, if the env var exists.
    Starts with the deepest folder and runs upwards.

    E.g.: Replaces `C:/Users/.../OneDrive/foo/bar` with `%ONEDRIVE%/foo/bar`

    The environment variable will be encapsuled within two percentage symbols.

    Returns the original path if no symlink is found.

    Args:
        path (Path): The path which to symlink.

    Raises:
        PytiaEnvVarNotFound: Raised when there is no env var in the given path.

    Returns:
        str: The symlinked path as str.
    """
    path_str = str(path)
    for parent in path.parents:
        for key, value in os.environ.items():
            if str(parent) == value:
                symlinked = path_str.replace(str(parent), f"%{key}%")
                return symlinked
    raise PytiaEnvVarNotFound("The given path doesn't contain an environment variable")


def create_path_workspace_level(path: Path, workspace_folder: Path) -> str:
    """
    Replaces the workspace-root-parts of the given path with `.\\`, if the given path
    contains the workspace-root (workspace_folder).

    E.g.: Replaces `C:\\Projects\\MyWorkspace\\foo\\bar` with `.\\foo\\bar`.
    The given workspace_folder path must be `C:\\Projects\\MyWorkspace` in this example.

    Returns the original given path if the workspace folder ist not in the path.

    Args:
        path (Path): The path to alter.
        workspace_folder (Path): The workspace file folder path.

    Raises:
        PytiaWorkspaceFolderNotFound: Raised when there is no workspace folder present
            in the given path.

    Returns:
        str: The altered path as str.
    """
    path_str = str(path)
    workspace_folder_str = str(workspace_folder)
    if workspace_folder_str in path_str:
        return "." + path_str.split(workspace_folder_str)[-1]
    raise PytiaWorkspaceFolderNotFound(
        "The path doesn't contain the given workspace folder"
    )
