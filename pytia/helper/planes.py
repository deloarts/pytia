"""
    Helper module for CATIA Plane objects.
"""

from pycatia.hybrid_shape_interfaces.plane import Plane
from pycatia.hybrid_shape_interfaces.point import Point
from pycatia.in_interfaces.reference import Reference
from pycatia.mec_mod_interfaces.hybrid_body import HybridBody
from pycatia.mec_mod_interfaces.part import Part

from pytia.decorators import failsafe
from pytia.log import log


@failsafe
def add_new_plane_as_offset_from_point(
    part: Part,
    hybrid_body: HybridBody,
    point: Point,
    reference: Reference,
    name: str = "Plane",
) -> Plane:
    """
    Creates a new plane as offset through point from reference.

    Args:
        part (Part): The part in which the plane will be added.
        hybrid_body (HybridBody): The hybrid_body to which the plane will be added.
        point (Point): The point object to which the plane will be added.
        reference (Reference): The reference from which the plane will be added.
        name (str, optional): The name of the plane_zx. Defaults to "Plane".

    Returns:
        Plane: The newly created plane.
    """
    point_reference = part.create_reference_from_object(point)
    plane = part.hybrid_shape_factory.add_new_plane_offset_pt(
        reference, point_reference
    )
    plane.name = name
    plane.compute  # pylint: disable=W0104
    hybrid_body.append_hybrid_shape(plane)
    part.update_object(hybrid_body)
    log.info(
        f"Created new plane {name!r} as offset from point {point.name!r} "
        f"and reference {reference.name!r}"
    )
    return plane
