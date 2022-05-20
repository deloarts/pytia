"""
    Utility module for retrieving the dimension of a parts main body.
"""


from pytia.exceptions import PytiaBaseError, PytiaBodyEmptyError
from pytia.helper.directions import add_new_direction
from pytia.helper.distances import get_minimum_distance_from_plane_to_extremum
from pytia.helper.extremum import add_extremum_to_hybrid_body
from pytia.helper.planes import add_new_plane_as_offset_from_point
from pytia.helper.points import create_point_from_point_object, get_center_of_gravity
from pytia.helper.references import (
    create_reference_from_axis_system,
    create_reference_from_body,
)
from pytia.log import log
from pytia.wrapper.documents.part_documents import PyPartDocument


def get_bounding_box(
    n_digits: int = 1, clean_after: bool = True
) -> tuple[float, float, float]:
    """
    Returns the bounding box of the current parts main body.

    Args:
        n_digits (int, optional): The precision of the resulting. Defaults to 1.
        clean_after (bool, optional): Remove created objects from the part. Defaults to True.

    Raises:
        PytiaBodyEmptyError: Raised when the body is empty or has no solid elements.
        PytiaBaseError: Raised when the source of the issue is unknown.

    Returns:
        tuple[float, float, float]: The bounding box values of all axes (x, y, z) in mm.
    """

    index_direction = {0: "Z", 1: "X", 2: "Y"}
    measurements = [0] * 3

    part_document = PyPartDocument()
    part_document.current()
    part = part_document.part

    log.info(f"Calculating bounding box for {part.name!r}.")

    main_body = part_document.bodies.main_body
    if part_document.bodies.is_empty(
        main_body, count_hybrid_bodies=False, count_sketches=False
    ):
        raise PytiaBodyEmptyError("Cannot calculate bounding box: Main body is empty.")

    hybrid_body = part_document.hybrid_bodies.create(
        name=f"BoundingBox ({main_body.name})", recycle=True
    )
    axis_system = part_document.axis_systems.create(
        name="BoundingBoxAxisSystem", recycle=True
    )

    try:
        cog_point = get_center_of_gravity(part=part, body=main_body)
        create_point_from_point_object(
            part=part, hybrid_body=hybrid_body, point=cog_point
        )

        # Do everything for all three directions (x, y & z)
        for i in [1, 2, 0]:
            # Create a new reference from the axis system
            reference_from_axis_system = create_reference_from_axis_system(
                part=part,
                axis_system=axis_system,
                brep_direction=i + 1,
            )

            # Create a plane in the center of gravity as offset from the axis system
            cog_plane = add_new_plane_as_offset_from_point(
                part=part,
                hybrid_body=hybrid_body,
                point=cog_point,
                reference=reference_from_axis_system,
                name=f"ReferencePlane{index_direction[i]}",
            )

            # Add a new direction for the extremum
            direction = add_new_direction(
                part=part,
                reference=reference_from_axis_system,
                name=f"Direction{index_direction[i]}",
            )

            # Add an extremum for the positive side
            positive_reference = create_reference_from_body(part=part, body=main_body)
            positive_extremum = add_extremum_to_hybrid_body(
                part=part,
                hybrid_body=hybrid_body,
                reference=positive_reference,
                direction=direction,
                min_max=1,
                name=f"PositiveExtremum{index_direction[i]}",
            )

            # Add an extremum for the negative side
            negative_reference = create_reference_from_body(part=part, body=main_body)
            negative_extremum = add_extremum_to_hybrid_body(
                part=part,
                hybrid_body=hybrid_body,
                reference=negative_reference,
                direction=direction,
                min_max=0,
                name=f"NegativeExtremum{index_direction[i]}",
            )

            # Calculate the distance between the positive and the negative extremum
            positive_distance = get_minimum_distance_from_plane_to_extremum(
                part, plane=cog_plane, extremum=positive_extremum
            )
            negative_distance = get_minimum_distance_from_plane_to_extremum(
                part, plane=cog_plane, extremum=negative_extremum
            )
            distance = positive_distance + negative_distance  # type: ignore

            measurements[i] = round(abs(distance), n_digits)

        part.update_object(part)
        part.in_work_object = main_body

        x = float(measurements[1])
        y = float(measurements[2])
        z = float(measurements[0])

        log.info(f"Bounding box: x={x}, y={y}, z={z}")
        return (x, y, z)

    except Exception as e:
        raise PytiaBaseError(f"Cannot calculate bounding box: {e}") from e

    finally:
        if clean_after:
            part_document.delete_objects(objects=[axis_system, hybrid_body])
