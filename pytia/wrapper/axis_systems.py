"""
    Wrapper module for CATIA axis systems.
"""

from typing import List

from pycatia.mec_mod_interfaces.axis_system import AxisSystem
from pycatia.mec_mod_interfaces.axis_systems import AxisSystems
from pycatia.mec_mod_interfaces.part import Part

from pytia.exceptions import PytiaAxisSystemExistsError
from pytia.exceptions import PytiaAxisSystemNotFoundError
from pytia.log import log


class PyAxisSystems:
    """The wrapper class for CATIA AxisSystems (MecModInterfaces Framework)"""

    def __init__(self, part: Part) -> None:
        """Inits the wrapper class for CATIA AxisSystems."""
        self._part = part
        self._axis_systems = part.axis_systems

    def __call__(self) -> AxisSystems:
        """Returns the axis system."""
        return self._axis_systems

    def __repr__(self) -> str:
        """Returns the representation of the object."""
        return f"PyAxisSystems({self._part.name})"

    @property
    def axis_systems(self) -> List[AxisSystem]:
        # def get_all(self) -> List[str]:
        """
        Returns a list of all axis systems in the part.

        Returns:
            List[AxisSystem]: The list of all axis systems in the part.
        """
        output = []
        for i in range(1, self._axis_systems.count + 1):
            output.append(self._axis_systems.item(i))
        return output

    @property
    def names(self) -> List[str]:
        # def get_all(self) -> List[str]:
        """
        Returns all axis systems as a list of their names.

        Returns:
            List[str]: The list of all axis systems names.
        """
        output = []
        for i in range(1, self._axis_systems.count + 1):
            output.append(self._axis_systems.item(i).name)
        return output

    def exists(self, name: str) -> bool:
        """
        Returns True if an axis system of the given name already exists.

        Args:
            name (str): The name of the desired axis system.

        Returns:
            bool: True if an axis system of the given name exists, False otherwise.
        """
        for i in range(1, self._axis_systems.count + 1):
            if self._axis_systems.item(i).name == name:
                return True
        return False

    def get_by_name(self, name: str) -> AxisSystem:
        """
        Returns an axis system by its name.

        Args:
            name (str): The name of the desired axis system.

        Raises:
            PytiaAxisSystemNotFoundError: Raised when the desired axis system does not exist.

        Returns:
            AxisSystem: Returns the axis system of the given name.
        """
        if self.exists(name=name):
            return self._axis_systems.item(name)
        raise PytiaAxisSystemNotFoundError(
            f"Axis system {name!r} not found in part {self._part.name!r}"
        )

    def create(self, name: str = "AxisSystem", recycle: bool = False) -> AxisSystem:
        """
        Creates an axis system.

        Args:
            name (str, optional): The name of the new axis system. Defaults to "AxisSystem".
            recycle (bool, optional): If set to True an existing axis system with the same name \
                will be used. Defaults to False.

        Raises:
            PytiaAxisSystemExistsError: Is raised if the axis system already exists and \
                recycle is set to False.

        Returns:
            AxisSystem: The newly created axis system.
        """
        if self.exists(name=name):
            if recycle:
                axis_system = self.get_by_name(name)
                log.warning(
                    "Found existing axis system. Skipping creation, using this one."
                )
            else:
                raise PytiaAxisSystemExistsError(
                    f"Axis system {name!r} already exists in part {self._part.name!r}"
                )
        else:
            axis_system = self._axis_systems.add()
            axis_system.name = name
        self._part.update()
        log.info(f"Created axis system {name!r} in part {self._part.name!r}")
        return axis_system
