"""
    Helper module for CATIA HybridShapeSymmetry objects.
"""

from pytia.decorators import failsafe
from pytia.framework.hybrid_shape_interfaces.hybrid_shape_symmetry import (
    HybridShapeSymmetry,
)
from pytia.framework.mec_mod_interfaces.part import Part
from pytia.log import log


@failsafe
def create_symmetry_of_main_body_zx(part: Part) -> HybridShapeSymmetry:
    """
    Creates and returns a HybridShapeSymmetry of the parts ZX plane.

    Args:
        part (Part): The part of which the symmetry will be created.

    Returns:
        HybridShapeSymmetry: The created HybridShapeSymmetry.
    """
    part.in_work_object = part.main_body
    mirror_reference = part.create_reference_from_object(part.origin_elements.plane_zx)
    shape_factory = part.shape_factory
    mirror_symmetry = shape_factory.add_new_symmetry_2(mirror_reference)
    mirror_symmetry.hybrid_shape  # pylint: disable=W0104
    part.in_work_object = part.main_body
    part.update_object(part.main_body)
    log.info(f"Created symmetry of {part}'s main body on ZX plane.")
    return mirror_symmetry
