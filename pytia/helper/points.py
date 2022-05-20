"""
    Helper module for CATIA Point objects.
"""

from pytia.decorators import failsafe
from pytia.framework.hybrid_shape_interfaces.point import Point
from pytia.framework.mec_mod_interfaces.body import Body
from pytia.framework.mec_mod_interfaces.hybrid_body import HybridBody
from pytia.framework.mec_mod_interfaces.part import Part
from pytia.helper.measurables import get_measurable_from_body
from pytia.log import log


@failsafe
def get_point_object(part: Part, x: int, y: int, z: int, name: str = "Point") -> Point:
    """
    Returns a HybridShapeFactory point object from the given part at the given coordinates.
    Name defaults to "Point".

    Args:
        part (Part): The part from which the point object will be returned.
        x (int): X coordinate of the point.
        y (int): Y coordinate of the point.
        z (int): Z coordinate of the point.
        name (str, optional): The points name. Defaults to "Point".

    Returns:
        Point: The newly created point.
    """
    point = part.hybrid_shape_factory.add_new_point_coord(x, y, z)
    point.compute  # pylint: disable=W0104
    point.name = name
    return point


@failsafe
def get_center_of_gravity(
    part: Part, body: Body, name: str = "CenterOfGravity"
) -> Point:
    """
    Returns a HybridShapeFactory Point object at the center of gravity from the
    given body.

    Args:
        part (Part): The part which hold the body from which the COG will be retrieved.
        body (Body): The body from which the COG will be retrieved.
        name (str, optional): The name of the point. Defaults to "CenterOfGravity".

    Returns:
        Point: The newly created point.
    """
    measurable = get_measurable_from_body(part=part, body=body)
    cog_coords = measurable.get_cog()
    cog = get_point_object(
        part=part, x=cog_coords[0], y=cog_coords[1], z=cog_coords[2], name=name
    )
    log.info(f"Created center of gravity point from body: {body.name!r}")
    return cog


@failsafe
def create_point_from_point_object(
    part: Part, hybrid_body: HybridBody, point: Point
) -> None:
    """
    Creates a point inside the given hybrid body from the given
    HybridShapeFactory point object. The point object must already
    have a name and must be computed!

    Args:
        part (Part): The part which holds the hybrid body in which the point will be created.
        hybrid_body (HybridBody): The hybrid body in which the point will be created.
        point (Point): The point object that will be created.
    """
    hybrid_body.append_hybrid_shape(point)
    part.update_object(hybrid_body)
    log.info(f"Created point in hybrid body {hybrid_body.name!r}")


@failsafe
def create_point_from_coordinates(
    part: Part, hybrid_body: HybridBody, x: int, y: int, z: int, name: str = "Point"
) -> None:
    """
    Creates a point inside the given hybrid body from the given coordinates.

    Args:
        part (Part): The part that holds the hybrid body in which the point will be created.
        hybrid_body (HybridBody): The hybrid body in which the point will be created.
        x (int): The X coordinate of the point.
        y (int): The Y coordinate of the point.
        z (int): The Z coordinate of the point.
        name (str, optional): The points name. Defaults to "Point".
    """
    point = get_point_object(part=part, x=x, y=y, z=z, name=name)
    hybrid_body.append_hybrid_shape(point)
    part.update_object(hybrid_body)
    log.info(f"Created point in hybrid body {hybrid_body.name!r}")
