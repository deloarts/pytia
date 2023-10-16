"""
    Wrapper module for CATIA materials.
"""

from typing import Dict
from typing import List

from pycatia.cat_mat_interfaces.material import Material
from pycatia.cat_mat_interfaces.material_document import MaterialDocument
from pycatia.cat_mat_interfaces.material_family import MaterialFamily

from pytia.exceptions import PytiaMaterialNotFound


class PyMaterialCatalog:
    """The wrapper class for CATIA Materials (CATMatInterfaces Framework)"""

    def __init__(self, material_document: MaterialDocument) -> None:
        """
        Inits the wrapper class for CATIA materials.

        Args:
            material_document (MaterialDocument): The CATMaterial document.
        """
        self._material_document = material_document
        self._families = [
            MaterialFamily(self._material_document.families.item(i).com_object)
            for i in range(1, self._material_document.families.count + 1)
        ]
        self._materials = {}
        for family in self._families:
            self._materials[family] = [
                family.materials.item(i) for i in range(1, family.materials.count + 1)
            ]

    @property
    def material_document(self) -> MaterialDocument:
        """Returns the material document."""
        return self._material_document

    @property
    def families(self) -> List[MaterialFamily]:
        """Returns a list of all material families in the catalog."""
        return self._families

    @property
    def families_str(self) -> List[str]:
        """Returns a list of all material family names in the catalog."""
        return [f.name for f in self._families]

    @property
    def materials(self) -> Dict[MaterialFamily, List[Material]]:
        """Returns a dictionary mapping material families to material objects."""
        return self._materials

    @property
    def materials_str(self) -> Dict[str, List[str]]:
        """Returns a dictionary mapping material family names to material objects."""
        values = {}
        for family, materials in self.materials.items():
            items: list = []
            values[family.name] = items
            for material in materials:
                items.append(material.name)
        return values

    def __repr__(self) -> str:
        """Returns the representation of the object."""
        return f"PyMaterials({self._material_document})"

    def material_exists(self, query: str | Material) -> bool:
        """
        Returns wether the given name exists in the material document.

        Args:
            name (str): The name of the material to check.

        Returns:
            bool: True if a material with the given name exists.
        """
        for materials in self.materials.values():
            for material in materials:
                if isinstance(query, str) and material.name == query:
                    return True
                if isinstance(query, Material) and material == query:
                    return True
        return False

    def get_material(self, name: str) -> Material:
        """
        Returns a material by its name from the material document.

        Args:
            name (str): The name of the material to retrieve.

        Raises:
            PytiaMaterialNotFound: Raised if no material with the given name does not exist in \
                the catalog.

        Returns:
            Material: The material from the given name.
        """
        for family in self._materials:
            for material in self.materials[family]:
                if material.name == name:
                    return material
        raise PytiaMaterialNotFound(
            f"Unable to find {name!r} in {self._material_document.name!r}"
        )
