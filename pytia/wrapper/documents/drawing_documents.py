"""
    Wrapper module for CATIA drawing documents.
"""
import os
from pathlib import Path

from pytia import __version__
from pytia.const import FILE_EXTENSION_DRAWING
from pytia.exceptions import PytiaFileExistsError
from pytia.framework.drafting_interfaces.drawing_document import DrawingDocument
from pytia.helper.verify import verify_folder
from pytia.log import log
from pytia.wrapper.documents.base import PyBaseDocument


class PyDrawingDocument(PyBaseDocument):
    """The wrapper class for CATIA Drawing (DraftingInterfaces Framework)"""

    def __init__(self) -> None:
        """Inits the base class with CATDrawing document type."""
        super().__init__(doc_type=FILE_EXTENSION_DRAWING)
        self._drawing_document: DrawingDocument
        self._name: str
        # Note to the _name class var: For a drawing document the name must be stored in the class.
        # The reason is, that it is not possible to set the name of the drawing document directly,
        # you have to save the document first, and then the filename will be the name.

    @property
    def drawing_document(self) -> DrawingDocument:
        """Returns the DrawingDocument object."""
        return self._drawing_document

    @property
    def name(self) -> str:
        """Returns the name of the drawing document."""
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        """Sets the name of the drawing document."""
        self._name = value

    def __bind(self) -> None:
        """Binds properties to the class object."""
        self._drawing_document = DrawingDocument(self.document.com_object)

    def load(self, path: Path) -> None:
        """
        Loads the given drawing file without creating a window.

        Args:
            path (Path): The full file path to the drawing file.
        """
        super().load(path)
        self.__bind()
        self._name = self._drawing_document.name.split(".CATDrawing")[0]

    def open(self, path: Path) -> None:
        """
        Opens the given drawing file.

        Args:
            path (Path): The full file path to the drawing file.
        """
        super().open(path)
        self.__bind()
        self._name = self._drawing_document.name.split(".CATDrawing")[0]

    def current(self) -> None:
        """
        Sets the currently open drawing document as active document.
        """
        super().current()
        self.__bind()
        self._name = self._drawing_document.name.split(".CATDrawing")[0]

    def new(self, name: str) -> None:
        """
        Creates a new drawing document.

        Args:
            name (str): The name of the new drawing document.
        """
        super().new(name)
        self.__bind()
        self._name = name

    def new_from(self, path: Path, name: str) -> None:
        """
        Creates a new drawing document from an existing one.

        Args:
            path (Path): The path to the original document.
            name (str): The name of the new drawing document.
        """
        super().new_from(path=path, name=name)
        self.__bind()
        self._name = name

    def save_as(self, folder: Path, overwrite: bool = True) -> Path:
        """
        Saves the drawing document in the given folder.
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
        # Same as above: We have to introduce a separate save_as method, because the
        # base-save_as method is originally written for parts and products, which is based on
        # the assumption, that you can change the documents name before saving it (the doc name
        # is the partnumber in this case).
        # But with drawings it's not possible to do so, at this it's necessary to use the class
        # variable _name instead.
        # Maybe it's time to change the base-save_as method ...

        filepath = Path(
            verify_folder(folder=folder, absolute=True), self._name + ".CATDrawing"
        )

        if os.path.exists(filepath):
            if overwrite:
                os.remove(filepath)
            else:
                raise PytiaFileExistsError(
                    f"Failed saving the {self._name!r} to {folder!r}: "
                    f"Already exists."
                )
        if not os.path.exists(folder):
            os.makedirs(folder)

        self.document.save_as(filepath)
        log.info(
            f"Saved document {self.document.name!r} to {self.document.full_name!r}"
        )
        return Path(self.document.full_name)
