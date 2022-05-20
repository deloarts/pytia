"""
    Helper module for CATIA Reference objects.
"""
from pytia.decorators import failsafe
from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.mec_mod_interfaces.axis_system import AxisSystem
from pytia.framework.mec_mod_interfaces.body import Body
from pytia.framework.mec_mod_interfaces.part import Part
from pytia.log import log


@failsafe
def create_reference_from_axis_system(
    *, part: Part, axis_system: AxisSystem, brep_direction: int
) -> Reference:
    """
    Creates a reference from a GenericNaming label. This allows manipulation of
    B-Rep (Type Functional and Relimited) that are not easy to access.

    Args:
        part (Part): The part that holds the reference axis system.
        axis_system (AxisSystem): The axis system that will be used as reference.
        brep_direction (int): The brep direction (a.k.a the coordinates: x=1, y=2, z=3).

    Returns:
        Reference: The newly created reference.
    """
    reference = part.create_reference_from_b_rep_name(
        f"RSur:("
        f"Face:("
        f"Brp:("
        f"{axis_system.name};"
        f"{brep_direction});"
        f"None:();"
        f"Cf11:());"
        f"WithPermanentBody;"
        f"WithoutBuildError;"
        f"WithSelectingFeatureSupport;"
        f"MFBRepVersion_CXR14)",
        axis_system,
    )
    log.info(
        f"Created the reference {reference.name!r} from the axis system {axis_system.name!r} \
            in direction {brep_direction!r}"
    )
    return reference


@failsafe
def create_reference_from_body(part: Part, body: Body) -> Reference:
    """
    Creates a reference from a body.

    Args:
        part (Part): The part that holds the body from which the reference will be created.
        body (Body): The body from which the reference will be created.

    Returns:
        Reference: The newly created reference.
    """
    reference = part.create_reference_from_object(body)
    log.info(f"Created the reference {reference.name!r} from the body {body.name!r}")
    return reference
