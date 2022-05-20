"""
    Wrapper module for CATIA hybrid bodies.
"""

from typing import List

from pytia.exceptions import PytiaBodyExistsError
from pytia.framework.cat_mat_interfaces.material import Material
from pytia.framework.mec_mod_interfaces.hybrid_body import HybridBody
from pytia.framework.mec_mod_interfaces.part import Part
from pytia.log import log
from pytia.wrapper.bodies.base import PyBodiesBase


class PyHybridBodies(PyBodiesBase):
    """Wrapper class for the CATIA Hybrid Bodies (MecModInterfaces Framework)"""

    def __init__(self, part: Part) -> None:
        """
        Inits the wrapper class.

        Args:
            part (Part): The parent part of the hybrid body.
        """
        super().__init__(part)
        self._hybrid_bodies = part.hybrid_bodies

    @property
    def hybrid_bodies(self) -> List[HybridBody]:
        """Returns a list of all hybrid bodies of type HybridBody."""
        output = []
        for i in range(1, self._hybrid_bodies.count + 1):
            output.append(self._hybrid_bodies.item(i))
        return output

    @property
    def names(self) -> List[str]:
        """Returns a list of the names of all hybrid bodies of type HybridBody."""
        output = []
        for i in range(1, self._hybrid_bodies.count + 1):
            output.append(self._hybrid_bodies.item(i).name)
        return output

    def exists(self, name: str) -> bool:
        """
        Returns True if a hybrid body with the given name exists in the part.

        Args:
            name (str): The hybrid body name to check.

        Returns:
            bool: True if a hybrid body with the given name exists in the part.
        """
        for i in range(1, self._hybrid_bodies.count + 1):
            if self._hybrid_bodies.item(i).name == name:
                return True
        return False

    def get_by_name(self, name: str) -> HybridBody:
        """
        Returns a hybrid body by its name.

        Args:
            name (str): The name of the hybrid body to get.

        Returns:
            Body: The hybrid body with the given name.
        """
        return self._hybrid_bodies.item(name)

    def create(self, name: str, recycle: bool = False) -> HybridBody:
        """
        Creates a new hybrid body and sets it as in work object.

        Args:
            name (str): The name of the hybrid body to create.

        Raises:
            PytiaBodyExistsError: Raised if a hybrid body with the given name already exists.

        Returns:
            Body: The newly created hybrid body.
        """
        if self.exists(name):
            if recycle:
                hybrid_body = self.get_by_name(name)
                log.warning(
                    "Found existing hybrid body. Skipping creation, using this one."
                )
            else:
                raise PytiaBodyExistsError(
                    f"Failed creating body {name!r}: Already exists in part {self._part.name!r}"
                )
        else:
            hybrid_body = self._hybrid_bodies.add()
            hybrid_body.name = name

        self._part.in_work_object = hybrid_body
        self._part.update_object(hybrid_body)
        log.info(f"Created hybrid body {name!r} in part {self._part.name!r}")
        return hybrid_body

    def get_material(self, hybrid_body: HybridBody) -> Material:
        """
        Returns the material applied to the hybrid body.

        Args:
            body (Body): The hybrid body from which to retrieve the material.

        Returns:
            Material: The CATIA material object.
        """
        return self._material_manager.get_material_on_hybrid_body(hybrid_body)

    def apply_material(
        self, hybrid_body: HybridBody, material: Material, linked: bool = True
    ) -> None:
        """
        Apply the material to the hybrid body.

        Args:
            hybrid_body (HybridBody): The hybrid body to apply the material to.
            material (Material): The CATIA material which should be applied to the hybrid body.
            linked (bool, optional): Link the material to the catalog file. Defaults to True.
        """
        self._material_manager.apply_material_on_hybrid_body(
            i_hybrid_body=hybrid_body, i_material=material, i_link_mode=linked
        )
