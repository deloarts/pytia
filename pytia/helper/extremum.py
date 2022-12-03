"""
    Helper module for CATIA HybridShapeExtremum objects.
"""

from pycatia.hybrid_shape_interfaces.hybrid_shape_direction import HybridShapeDirection
from pycatia.hybrid_shape_interfaces.hybrid_shape_extremum import HybridShapeExtremum
from pycatia.in_interfaces.reference import Reference
from pycatia.mec_mod_interfaces.hybrid_body import HybridBody
from pycatia.mec_mod_interfaces.part import Part

from pytia.decorators import failsafe
from pytia.log import log


@failsafe
def add_extremum_to_hybrid_body(
    part: Part,
    hybrid_body: HybridBody,
    reference: Reference,
    direction: HybridShapeDirection,
    min_max: int,
    name: str = "Extremum",
) -> HybridShapeExtremum:
    """
    Creates a new Extremum within the current body.

    Args:
        part (Part): The part to which the extremum will be added.
        hybrid_body (HybridBody): The hybrid body to which the extremum will be added.
        reference (Reference): The reference object from which the extremum will be added.
        direction (HybridShapeDirection): The direction in which the extremum will be added.
        min_max (int): Toggle min or max calculation.
        name (str, optional): The name of the newly generated extremum. Defaults to "Extremum".

    Returns:
        HybridShapeExtremum: The newly created extremum.
    """
    factory = part.hybrid_shape_factory
    extremum = factory.add_new_extremum(reference, direction, min_max)
    extremum.name = name
    hybrid_body.append_hybrid_shape(extremum)
    extremum.compute()
    part.update_object(hybrid_body)
    log.info(f"Extremum {name!r} created in hybrid body {hybrid_body.name!r}")
    return extremum
