"""
    Helper module for CATIA HybridShapeDirections objects.
"""

from pytia.decorators import failsafe
from pytia.framework.hybrid_shape_interfaces.hybrid_shape_direction import (
    HybridShapeDirection,
)
from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.mec_mod_interfaces.part import Part
from pytia.log import log


@failsafe
def add_new_direction(
    part: Part, reference: Reference, name: str = "Direction"
) -> HybridShapeDirection:
    """
    Creates a new direction specified by an element within the current body.

    Args:
        part (Part): The Part to which the direction will be added.
        reference (Reference): The reference object from which the direction will be referenced.
        name (str, optional): The name of the direction. Defaults to "Direction".

    Returns:
        HybridShapeDirection: The newly created direction.
    """
    factory = part.hybrid_shape_factory
    direction = factory.add_new_direction(reference)
    direction.name = name
    log.info(
        f"Added new direction {direction.name!r} from reference {reference.name!r}"
    )
    return direction
