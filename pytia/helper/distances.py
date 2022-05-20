"""
    Helper module for CATIA Distance objects.
"""

from pytia.decorators import failsafe
from pytia.framework.hybrid_shape_interfaces.hybrid_shape_extremum import (
    HybridShapeExtremum,
)
from pytia.framework.hybrid_shape_interfaces.plane import Plane
from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.mec_mod_interfaces.part import Part
from pytia.framework.space_analyses_interfaces.distance import Distance
from pytia.helper.measurables import get_measurable_from_reference


@failsafe
def get_minimum_distance(
    reference: Reference, extremum: HybridShapeExtremum
) -> Distance:
    """
    Returns the minimum distance between the given reference and the given extremum.

    Args:
        reference (Reference): The reference object from which the minimum distance will be \
            calculated.
        extremum (HybridShapeExtremum): The extremum to which the minimum distance will be \
            calculated.

    Returns:
        Distance: The minimum distance.
    """
    measurable = get_measurable_from_reference(reference=reference)
    minimum_distance = measurable.get_minimum_distance(extremum)
    return minimum_distance


@failsafe
def get_minimum_distance_from_plane_to_extremum(
    part: Part, plane: Plane, extremum: HybridShapeExtremum
) -> Distance:
    """
    Returns the minimum distance between the plane and the extremum.

    Args:
        part (Part): The part object.
        plane (Plane): The plane from which the minimum distance will be calculated.
        extremum (HybridShapeExtremum): The extremum to which the minimum distance will be \
            calculated.

    Returns:
        Distance: The minimum distance.
    """
    reference_plane = part.create_reference_from_object(plane)
    return get_minimum_distance(reference=reference_plane, extremum=extremum)
