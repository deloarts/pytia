"""
    Base wrapper module for CATIA bodies.
"""

from pycatia.cat_mat_interfaces.material_manager import MaterialManager
from pycatia.mec_mod_interfaces.body import Body
from pycatia.mec_mod_interfaces.hybrid_body import HybridBody
from pycatia.mec_mod_interfaces.part import Part

from pytia.const import GET_ITEM_MATERIAL_MANAGER


class PyBodiesBase:
    """Base class for the CATIA Bodies and HybridBodies (MecModInterfaces Framework)"""

    def __init__(self, part: Part) -> None:
        """Inits the wrapper class for the CATIA bodies."""
        self._part = part
        self._material_manager = MaterialManager(
            self._part.get_item(GET_ITEM_MATERIAL_MANAGER).com_object
        )

    def __repr__(self) -> str:
        return f"PyBodiesBase({self._part.name})"

    @staticmethod
    def is_empty(
        body: Body | HybridBody,
        count_shapes: bool = True,
        count_hybrid_bodies: bool = True,
        count_sketches: bool = True,
    ) -> bool:
        """
        Returns True if the body is empty.

        Args:
            body (Body | HybridBody): The body to check.
            count_shapes (bool, optional): Allow shapes. Defaults to True.
            count_hybrid_bodies (bool, optional): Allow hybrid bodies. Defaults to True.
            count_sketches (bool, optional): Allow sketches. Defaults to True.

        Returns:
            bool: True if the body is empty, False otherwise.
        """
        # This is ugly, needs to be changed ...
        try:
            shapes = body.shapes.count if count_shapes else None  # type: ignore
        except:  # pylint: disable=W0702
            shapes = None
        try:
            hybrid_bodies = body.hybrid_bodies.count if count_hybrid_bodies else None
        except:  # pylint: disable=W0702
            hybrid_bodies = None
        try:
            sketches = body.sketches.count if count_sketches else None  # type: ignore
        except:  # pylint: disable=W0702
            sketches = None

        return not any([shapes, hybrid_bodies, sketches])
