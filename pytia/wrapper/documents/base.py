"""
    Wrapper module for handling CATIA documents.
"""

import os
from pathlib import Path
from typing import Any, List, Optional

from pycatia.in_interfaces.document import Document
from pycatia.in_interfaces.selection import Selection

from pytia import __version__
from pytia.const import VALID_FILE_EXTENSIONS
from pytia.exceptions import (
    PytiaDocumentExistsError,
    PytiaDocumentNotOpenError,
    PytiaDocumentNotSavedError,
    PytiaDocumentOperationError,
    PytiaFileExistsError,
    PytiaFileNotFoundError,
    PytiaNoDocumentOpenError,
    PytiaWrongDocumentTypeError,
)
from pytia.framework import framework
from pytia.helper.verify import verify_folder
from pytia.log import log


class PyBaseDocument:
    """The base class for CATIA Documents (InfInterfaces Framework)"""

    def __init__(self, doc_type: str) -> None:
        """
        Inits the Documents object.

        Args:
            doc_type (str): The type of the document (must be one of the items in the \
                VALID_FILE_EXTENSIONS list.)

        Raises:
            PytiaWrongDocumentTypeError: Is raised when the provided document type is not in the \
                VALID_FILE_EXTENSIONS list.
        """
        self._framework = framework
        self._doctype = doc_type
        self.documents = self._framework.catia.documents
        self.document: Document = None  # type: ignore

        if doc_type not in VALID_FILE_EXTENSIONS:
            raise PytiaWrongDocumentTypeError(
                f"Failed initializing document: Wrong type. Must be {VALID_FILE_EXTENSIONS}, "
                f"got {doc_type!r}"
            )

    def __del__(self):
        """
        Callback on object deletion.
        """
        # self.close()

    def __enter__(self):
        """
        Entering the context manager.
        """
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        """
        Exiting the context manager.
        """
        self.close()

    def __call__(self) -> Document:
        """Returns the active document."""
        return self.document

    def __repr__(self) -> str:
        """Returns the representation of the object."""
        return f"PyDocuments({self.document.name})"

    def load(self, path: Path) -> Document:
        """
        Loads the document without creating a window.

        Args:
            path (Path): The path to the document to load.

        Raises:
            PytiaFileNotFoundError: Raised if the document does not exist.
            PytiaWrongDocumentTypeError: Raised if the document is not of the correct type.
            PytiaDocumentOperationError: Raised if the cannot be opened.

        Returns:
            Document: _description_
        """
        if not path.exists():
            raise PytiaFileNotFoundError(
                f"Failed loading file {str(path)!r}: Does not exist"
            )

        if not self._doctype in str(path):
            raise PytiaWrongDocumentTypeError(
                f"Failed loading file {str(path)!r}: Not a {self._doctype}"
            )

        try:
            self.document = self.documents.read(file_name=str(path))
        except Exception as e:
            raise PytiaDocumentOperationError(
                f"Failed opening document from {str(path)!r}: {e}"
            ) from e

        log.info(
            f"Opened document {self.document.name!r} from {self.document.full_name!r} "
            f"(document is now active)."
        )
        return self.document

    def open(self, path: Path) -> Document:
        """
        Opens the document from the given path.

        Args:
            path (Path): The path to the document to open.

        Raises:
            PytiaFileNotFoundError: Raised if the document does not exist.
            PytiaWrongDocumentTypeError: Raised if the document is not of the correct type.
            PytiaDocumentOperationError: Raised if the cannot be opened.

        Returns:
            Document: The opened document.
        """
        if not path.exists():
            raise PytiaFileNotFoundError(
                f"Failed opening file {str(path)!r}: Does not exist"
            )

        if not self._doctype in str(path):
            raise PytiaWrongDocumentTypeError(
                f"Failed opening file {str(path)!r}: Not a {self._doctype}"
            )

        try:
            self.documents.open(str(path))
        except Exception as e:
            raise PytiaDocumentOperationError(
                f"Failed opening document from {str(path)!r}: {e}"
            ) from e

        self.document = self._framework.catia.active_document
        log.info(
            f"Opened document {self.document.name!r} from {self.document.full_name!r} "
            f"(document is now active)."
        )
        return self.document

    def current(self) -> Document:
        """
        Sets the currently open document as ActiveDocument.

        Raises:
            PytiaNoDocumentOpenError: Raised if no document is open.
            PytiaWrongDocumentTypeError: Raised if the open document is not of the correct type.

        Returns:
            Document: The current document object.
        """
        if not self.anything_open():
            raise PytiaNoDocumentOpenError(
                "Failed loading current document: No document open."
            )

        self.document = self._framework.catia.active_document

        if not self._doctype in self.document.name:
            raise PytiaWrongDocumentTypeError(
                f"Failed loading current document as {self._doctype!r}: Wrong document type."
            )

        log.debug(f"{self.document.name!r} is now the ActiveDocument.")
        return self.document

    def new(self, name: str) -> Document:
        """
        Creates a new Document and sets it as ActiveDocument.

        Args:
            name (str): The name of the new document.

        Raises:
            PytiaDocumentExistsError: Raised if the name already exists in the session.

        Returns:
            Document: The newly created document object.
        """
        if not self.filename_is_unique(f"{name}.{self._doctype}"):
            raise PytiaDocumentExistsError(
                f"Cannot create {self._doctype!r} with name {name!r}: Already exists in session."
            )

        self.documents.add(self._doctype.split("CAT")[-1])
        self.document = self._framework.catia.active_document

        log.info(f"Created new document {self.document.name!r}")
        return self.document

    def new_from(self, path: Path, name: str) -> Document:
        """
        Creates a new Document from an existing one and sets it as ActiveDocument.

        Args:
            path (Path): The path to the original document.
            name (str): The name of the new document.

        Raises:
            PytiaDocumentExistsError: Raised if the name already exists in the session.

        Returns:
            Document: The document object.
        """
        if not self.filename_is_unique(f"{name}.{self._doctype}"):
            raise PytiaDocumentExistsError(
                f"Cannot create {self._doctype!r} with name {name!r}: Already exists in session."
            )

        self.documents.new_from(str(path))
        self.document = self._framework.catia.active_document

        log.info(f"Created new document {self.document.name!r} from {str(path)!r}")
        return self.document

    def close(self) -> None:
        """Closes the document."""
        if self.document is not None:
            try:
                self.document.close()
                log.info(f"Closed document {self.document.name!r}")
            except PytiaDocumentNotOpenError:
                log.warning(
                    f"Failed closing document {self.document.name!r}: "
                    f"Must have already been closed."
                )

    def save(self) -> str:
        """
        Saves the document.
        Returns the path (folder & filename) of the saved document.

        Raises:
            PytiaDocumentNotSavedError: Raised if the document cannot be saved due to an unset \
                destination folder.

        Returns:
            str: The full path to the saved document with filename and extension.
        """
        if self.document.name == self.document.full_name:
            raise PytiaDocumentNotSavedError(
                "Failed saving document: No folder specified (Use 'save as' instead)."
            )

        if self.document.is_saved:
            log.info(f"Did not save document {self.document.name!r}: Already saved.")
        else:
            self.document.save()
            log.info(
                f"Saved document {self.document.name!r} to {self.document.full_name!r}"
            )
        return self.document.full_name

    def save_as(self, folder: Path, overwrite: bool = True) -> Path:
        """
        Saves the document in the given folder.
        Overwrites any existing document by default.
        Returns the path (folder & filename) of the saved document.

        Args:
            folder (Path): The folder in which the document should be saved.
            overwrite (bool, optional): Overwrites any existing files. EachDefaults to True.

        Raises:
            PytiaFileExistsError: Raised if the file already exists and overwrite is False.

        Returns:
            Path: The full path to the saved document with filename and extension.
        """
        filepath = Path(verify_folder(folder=folder, absolute=True), self.document.name)

        if os.path.exists(filepath):
            if overwrite:
                os.remove(filepath)
            else:
                raise PytiaFileExistsError(
                    f"Failed saving the {self.document.name!r} to {self.document.full_name!r}: "
                    f"Already exists."
                )
        if not os.path.exists(folder):
            os.makedirs(folder)

        self.document.save_as(filepath)
        log.info(
            f"Saved document {self.document.name!r} to {self.document.full_name!r}"
        )
        return Path(self.document.full_name)

    def delete_objects(self, objects: List[Any]) -> None:
        """Deletes all objects of the given list. Uses the documents selection."""
        sel: Selection = self.document.selection

        self.remove_selection(sel)
        for obj in objects:
            sel.add(obj)
            log.info(f"Deleted {obj.name!r} from {self.document.name!r}")
        sel.delete()
        self.remove_selection(sel)

    def anything_open(self) -> bool:
        """Returns True if any document is open."""
        return self.documents.count > 0

    def filename_is_unique(self, filename: str) -> bool:
        """Returns True if the given name is unique in the session."""
        for i in range(self.documents.count):
            if self.documents[i].name == filename:
                return False
        return True

    def remove_selection(self, selection: Optional[Selection] = None) -> None:
        """
        Removes all objects of the given selection.
        """
        if not selection:
            selection = self.document.selection

        selection.clear  # pylint: disable=W0104
        for _ in range(1, selection.count + 1):
            selection.remove(1)
            log.debug(f"Removed {selection.name!r} from {self.document.name}")
        selection.clear  # pylint: disable=W0104
