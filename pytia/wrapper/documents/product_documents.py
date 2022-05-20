"""
    Wrapper module for handling product documents.
"""

from pytia import __version__
from pytia.const import FILE_EXTENSION_PRODUCT, GET_ITEM_MATERIAL_MANAGER
from pytia.exceptions import PytiaDocumentNameConventionError
from pytia.framework.cat_mat_interfaces.material import Material
from pytia.framework.cat_mat_interfaces.material_manager import MaterialManager
from pytia.framework.product_structure_interfaces.product import Product
from pytia.log import log
from pytia.wrapper.documents.base import PyBaseDocument
from pytia.wrapper.properties import PyProperties


class PyProductDocument(PyBaseDocument):
    """The wrapper class for CATIA ProductDocument (ProductStructureInterfaces Framework)"""

    def __init__(self, strict_naming: bool = True) -> None:
        """
        Inits the base class with CATProduct document type. Even

        Args:
            strict_naming (bool, optional): If set to True the partnumber and the filename must \
                always match. Defaults to True.
        """
        self.strict = strict_naming
        super().__init__(doc_type=FILE_EXTENSION_PRODUCT)
        self._product: Product
        self._properties: PyProperties
        self._material_manager: MaterialManager

    def __bind(self) -> None:
        """Binds properties to the class object."""
        self._product = Product(self.document.product.com_object)  # type: ignore
        self._properties = PyProperties(self._product)
        self._material_manager = MaterialManager(
            self._product.get_item(GET_ITEM_MATERIAL_MANAGER).com_object
        )

    @property
    def product(self) -> Product:
        """Returns the catia product object for this product."""
        return self._product

    @property
    def properties(self) -> PyProperties:
        """Returns the properties-wrapper object for this product."""
        return self._properties

    @property
    def material(self) -> Material:
        """Returns the catia material object of this product."""
        return self._material_manager.get_material_on_product(self._product)

    @material.setter
    def material(self, material: Material) -> None:
        """
        Applies the given catia material object to this product.

        Args:
            material (Material): The catia material object.
        """
        self._material_manager.apply_material_on_product(
            self._product, material, i_link_mode=True
        )

    def open(self, path: str) -> None:
        """
        Opens the product document from the given path.

        Args:
            path (str): The full path to the product document.

        Raises:
            PytiaDocumentNameConventionError: Raised when strict mode is enabled and the filename \
                does not match the partnumber.
        """
        super().open(path)
        self.__bind()

        if self.strict and self.product.name not in self.document.name:
            raise PytiaDocumentNameConventionError(
                f"Failed to open document {self.document.name}: Partnumber does not match filename."
            )

    def current(self) -> None:
        """
        Sets the currently open document (ActiveDocument) as ProductDocument.

        Raises:
            PytiaDocumentNameConventionError: Raised when strict mode is enabled and the filename \
                does not match the partnumber.
        """
        super().current()
        self.__bind()

        if self.strict and self.product.name not in self.document.name:
            raise PytiaDocumentNameConventionError(
                f"Failed to set document {self.document.name} as active document: Partnumber does "
                f"not match filename."
            )

    def new(self, name: str) -> None:
        """
        Creates a new ProductDocument and sets it as ActiveDocument.
        Filename and partnumber will be set to the given name.

        Args:
            name (str): The name (filename and partnumber) of the new product.
        """
        super().new(name)
        self.__bind()

        old_name = self.document.name
        self.product.part_number = name

        log.info(f"Renamed document {old_name!r} to {self.document.name!r}")

    def new_from(self, path: str, name: str) -> None:
        """
        Creates a new ProductDocument from an existing one and sets it as ActiveDocument.
        Filename and partnumber will be set to the given name.

        Args:
            path (str): The full path to the source part document
            name (str): The name (filename and partnumber) of the new product.
        """
        super().new_from(path=path, name=name)
        self.__bind()

        old_name = self.document.name
        self.product.part_number = name

        log.info(f"Renamed document {old_name!r} to {self.document.name!r}")
