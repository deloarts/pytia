"""
    Wrapper module for CATIA material documents.
"""
from pathlib import Path

from pycatia.cat_mat_interfaces.material_document import MaterialDocument

from pytia import __version__
from pytia.const import FILE_EXTENSION_MATERIAL
from pytia.exceptions import PytiaNotImplementedError
from pytia.wrapper.documents.base import PyBaseDocument
from pytia.wrapper.material_catalogs import PyMaterialCatalog


class PyMaterialDocument(PyBaseDocument):
    """The wrapper class for CATIA MaterialDocument (CATMatInterfaces Framework)"""

    def __init__(self) -> None:
        """Inits the base class with CATMaterial document type."""
        super().__init__(doc_type=FILE_EXTENSION_MATERIAL)
        self._material_document: MaterialDocument
        self._catalog: PyMaterialCatalog

    @property
    def material_document(self) -> MaterialDocument:
        """Returns the MaterialDocument object."""
        return self._material_document

    @property
    def catalog(self) -> PyMaterialCatalog:
        """Returns the catalog object from the materials wrapper."""
        return self._catalog

    def __bind(self) -> None:
        """Binds properties to the class object."""
        self._material_document = MaterialDocument(self.document.com_object)
        self._catalog = PyMaterialCatalog(self._material_document)

    def load(self, path: Path) -> None:
        """
        Loads the given material file without creating a window.

        Args:
            path (Path): The full file path to the material catalog.
        """
        super().load(path)
        self.__bind()

    def open(self, path: Path) -> None:
        """
        Opens the given material file.

        .. warning::
            Not implemented yet.

        Args:
            path (Path): The full file path to the material catalog.

        Raises:
            PytiaNotImplementedError: Always raised.
        """
        raise PytiaNotImplementedError()

    def current(self) -> None:
        """
        Sets the currently open material document as active document.

        .. warning::
            Not implemented yet.

        Raises:
            PytiaNotImplementedError: Always raised.
        """
        raise PytiaNotImplementedError()

    def new(self, name: str) -> None:
        """
        Creates a new material document.

        .. warning::
            Not implemented yet.

        Args:
            name (str): The name of the new material document.

        Raises:
            PytiaNotImplementedError: Always raised.
        """
        raise PytiaNotImplementedError()

    def new_from(self, path: Path, name: str) -> None:
        """
        Creates a new material document from an existing one.

        .. warning::
            Not implemented yet.

        Args:
            path (Path): The path to the original material document.
            name (str): The name of the new material document.

        Raises:
            PytiaNotImplementedError: Always raised.
        """
        raise PytiaNotImplementedError()
