"""
    Wrapper module for handling part documents.
"""

from pathlib import Path

from pycatia.cat_mat_interfaces.material import Material
from pycatia.cat_mat_interfaces.material_manager import MaterialManager
from pycatia.mec_mod_interfaces.part import Part
from pycatia.product_structure_interfaces.product import Product

from pytia import __version__
from pytia.const import FILE_EXTENSION_PART, GET_ITEM_MATERIAL_MANAGER
from pytia.exceptions import PytiaDocumentNameConventionError
from pytia.log import log
from pytia.wrapper.axis_systems import PyAxisSystems
from pytia.wrapper.bodies.bodies import PyBodies
from pytia.wrapper.bodies.hybrid_bodies import PyHybridBodies
from pytia.wrapper.documents.base import PyBaseDocument
from pytia.wrapper.parameters import PyPartParameters
from pytia.wrapper.properties import PyProperties


class PyPartDocument(PyBaseDocument):
    """The wrapper class for CATIA PartDocument (MecModInterfaces Framework)"""

    def __init__(self, strict_naming: bool = True, material_link: bool = True) -> None:
        """
        Inits the base class with CATPart document type. Even

        Args:
            strict_naming (bool, optional): If set to True the partnumber and the filename must \
                always match. Defaults to True.
            material_link (bool, optional): If set to True, the applied material will be linked \
                to the material catalog. Defaults to True.
        """
        self.strict = strict_naming
        super().__init__(doc_type=FILE_EXTENSION_PART)
        self._part: Part
        self._product: Product
        self._parameters: PyPartParameters
        self._properties: PyProperties
        self._bodies: PyBodies
        self._hybrid_bodies: PyHybridBodies
        self._axis_systems: PyAxisSystems
        self._material_manager: MaterialManager
        self._material_link = material_link

    def __bind(self) -> None:
        """Binds properties to the class object."""
        self._part = Part(self.document.part.com_object)  # type: ignore
        self._product = Product(self.document.product.com_object)  # type: ignore
        self._parameters = PyPartParameters(self._part)
        self._properties = PyProperties(self._product)
        self._bodies = PyBodies(self._part)
        self._hybrid_bodies = PyHybridBodies(self._part)
        self._axis_systems = PyAxisSystems(self._part)
        self._material_manager = MaterialManager(
            self._part.get_item(GET_ITEM_MATERIAL_MANAGER).com_object
        )

    @property
    def part(self) -> Part:
        """Returns the catia part object for this part."""
        return self._part

    @property
    def product(self) -> Product:
        """Returns the catia product object for this part."""
        return self._product

    @property
    def properties(self) -> PyProperties:
        """Returns the properties-wrapper object for this part."""
        return self._properties

    @property
    def parameters(self) -> PyPartParameters:
        """Returns the parameters-wrapper object for this part."""
        return self._parameters

    @property
    def bodies(self) -> PyBodies:
        """Returns the bodies-wrapper object for this part."""
        return self._bodies

    @property
    def hybrid_bodies(self) -> PyHybridBodies:
        """Returns the hybrid bodies-wrapper object for this part."""
        return self._hybrid_bodies

    @property
    def axis_systems(self) -> PyAxisSystems:
        """Returns the axis systems-wrapper object for this part."""
        return self._axis_systems

    @property
    def material(self) -> Material:
        """Returns the catia material object of this part."""
        return self._material_manager.get_material_on_part(self._part)

    @material.setter
    def material(self, material: Material) -> None:
        """
        Applies the given catia material object to this part.

        Args:
            material (Material): The catia material object.
        """
        self._material_manager.apply_material_on_part(
            self._part, material, i_link_mode=self._material_link
        )

    def open(self, path: Path) -> None:
        """
        Opens the part document from the given path.

        Args:
            path (Path): The full path to the part document.

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
        Sets the currently open document (ActiveDocument) as PartDocument.

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
        Creates a new PartDocument and sets it as ActiveDocument.
        Filename, PartNumber and MainBody will be set to the given name.

        Args:
            name (str): The name (filename and partnumber) of the new part.
        """
        super().new(name)
        self.__bind()

        old_name = self.document.name
        self.product.part_number = name
        self.part.main_body.name = name

        log.info(f"Renamed document {old_name!r} to {self.document.name!r}")

    def new_from(self, path: Path, name: str) -> None:
        """
        Creates a new PartDocument from an existing one and sets it as ActiveDocument.
        Filename, PartNumber and MainBody will be set to the given name.

        Args:
            path (Path): The full path to the source part document
            name (str): The name (filename and partnumber) of the new part.
        """
        super().new_from(path=path, name=name)
        self.__bind()

        old_name = self.document.name
        self.product.part_number = name
        self.part.main_body.name = name

        log.info(f"Renamed document {old_name!r} to {self.document.name!r}")
