"""
    Wrapper module for CATIA bodies.
"""

from typing import List

from pytia.exceptions import PytiaBodyExistsError
from pytia.framework.cat_mat_interfaces.material import Material
from pytia.framework.mec_mod_interfaces.body import Body
from pytia.framework.mec_mod_interfaces.part import Part
from pytia.log import log
from pytia.wrapper.bodies.base import PyBodiesBase


class PyBodies(PyBodiesBase):
    """Wrapper class for the CATIA Bodies (MecModInterfaces Framework)"""

    def __init__(self, part: Part) -> None:
        """
        Inits the wrapper class.

        Args:
            part (Part): The parent part of the body.
        """
        super().__init__(part)
        self._bodies = part.bodies

    @property
    def main_body(self) -> Body:
        """Returns the parts main body."""
        return self._part.main_body

    @property
    def bodies(self) -> List[Body]:
        """Returns a list of all bodies of type Body."""
        output = []
        for i in range(1, self._bodies.count + 1):
            output.append(self._bodies.item(i))
        return output

    @property
    def names(self) -> List[str]:
        """Returns a list of the names of all bodies of type Body."""
        output = []
        for i in range(1, self._bodies.count + 1):
            output.append(self._bodies.item(i).name)
        return output

    def exists(self, name: str) -> bool:
        """
        Returns True if a body with the given name exists in the part.

        Args:
            name (str): The body name to check.

        Returns:
            bool: True if a body with the given name exists in the part.
        """
        for i in range(1, self._bodies.count + 1):
            if self._bodies.item(i).name == name:
                return True
        return False

    def get_by_name(self, name: str) -> Body:
        """
        Returns a body by its name.

        Args:
            name (str): The name of the body to get.

        Returns:
            Body: The body with the given name.
        """
        return self._bodies.item(name)

    def create(self, name: str) -> Body:
        """
        Creates a new body and sets it as in work object.

        Args:
            name (str): The name of the body to create.

        Raises:
            PytiaBodyExistsError: Raised if a body with the given name already exists.

        Returns:
            Body: The newly created body.
        """
        if self.exists(name):
            raise PytiaBodyExistsError(
                f"Failed creating body {name!r}: Already exists in part {self._part.name!r}"
            )
        body = self._bodies.add()
        body.name = name
        self._part.in_work_object = body
        self._part.update_object(body)
        log.info(f"Created body {name!r} in part {self._part.name!r}")
        return body

    def get_material(self, body: Body) -> Material:
        """
        Returns the material applied to the body.

        Args:
            body (Body): The body from which to retrieve the material.

        Returns:
            Material: The CATIA material object.
        """
        return self._material_manager.get_material_on_body(body)

    def apply_material(
        self, body: Body, material: Material, linked: bool = True
    ) -> None:
        """
        Apply the material to the body.

        Args:
            body (Body): The body to apply the material to.
            material (Material): The CATIA material which should be applied to the body.
            linked (bool, optional): Link the material to the catalog file. Defaults to True.
        """
        self._material_manager.apply_material_on_body(
            i_body=body, i_material=material, i_link_mode=linked
        )
