"""
    Tests the bounding box utility.
"""
import pytest

test_name = "pytest_test_bounding_box"
test_x = 50
test_y = 80
test_z = 20


def test_import():
    """
    Tests if the module import works.
    This test only passes when CATIA is running.
    """
    from pytia.utilities.bounding_box import get_bounding_box  # noqa: F401


def test_bounding_box():
    """
    Tests if the get_bounding_box function returns valid values.

    Important: Since this test shall run without any further doing we need to
    create a part with a body first. This is currently not tested somewhere
    else, so if this test breaks it may be also due to a bug in the body
    or part creation.

    Test preperation:
        Creates a simple pad inside the parts main body.
        Note: This is not the correct way of creating a pad!
              This created pad is not editable after creation,
              because there are no relations set. This method
              is purely to test the bounding box utility.

    This test only passes when CATIA is running.
    """
    from pytia.utilities.bounding_box import get_bounding_box
    from pytia.wrapper.documents.part_documents import PyPartDocument

    with PyPartDocument() as part_document:
        part_document.new(name=test_name)

        main_body = part_document.bodies.main_body

        reference_plane = part_document.part.create_reference_from_object(
            part_document.part.origin_elements.plane_xy
        )
        profile_sketch = main_body.sketches.add(reference_plane)
        part_document.part.in_work_object = profile_sketch

        factory2D1 = profile_sketch.open_edition()
        factory2D1.create_line(test_x / 2, test_y / 2, test_x / 2, -test_y / 2)
        factory2D1.create_line(test_x / 2, -test_y / 2, -test_x / 2, -test_y / 2)
        factory2D1.create_line(-test_x / 2, -test_y / 2, -test_x / 2, test_y / 2)
        factory2D1.create_line(-test_x / 2, test_y / 2, test_x / 2, test_y / 2)

        profile_sketch.close_edition
        part_document.part.in_work_object = profile_sketch
        part_document.part.update()
        part_document.part.shape_factory.add_new_pad(profile_sketch, test_z)
        part_document.part.update_object(main_body)

        x, y, z = get_bounding_box(clean_after=True)

    assert x == test_x
    assert isinstance(x, float)
    assert y == test_y
    assert isinstance(y, float)
    assert z == test_z
    assert isinstance(z, float)


def test_bounding_box_empty_body():
    """
    Tests if the get_bounding_box function raises an exception when the main body is empty.
    This test only passes when CATIA is running.
    """
    from pytia.utilities.bounding_box import get_bounding_box
    from pytia.wrapper.documents.part_documents import PyPartDocument

    with PyPartDocument() as part_document:
        part_document.new(name=test_name)
        with pytest.raises(Exception):
            get_bounding_box()


def test_bounding_box_no_shapes():
    """
    Tests if the get_bounding_box function raises an exception when the main body has no shapes.
    This test only passes when CATIA is running.

    Test preperation: Creates a simple sketch inside the parts main body.
    """
    from pytia.utilities.bounding_box import get_bounding_box
    from pytia.wrapper.documents.part_documents import PyPartDocument

    with PyPartDocument() as part_document:
        part_document.new(name=test_name)

        main_body = part_document.bodies.main_body

        reference_plane = part_document.part.create_reference_from_object(
            part_document.part.origin_elements.plane_xy
        )
        profile_sketch = main_body.sketches.add(reference_plane)
        part_document.part.in_work_object = profile_sketch

        factory2D1 = profile_sketch.open_edition()
        factory2D1.create_line(test_x / 2, test_y / 2, test_x / 2, -test_y / 2)
        factory2D1.create_line(test_x / 2, -test_y / 2, -test_x / 2, -test_y / 2)
        factory2D1.create_line(-test_x / 2, -test_y / 2, -test_x / 2, test_y / 2)
        factory2D1.create_line(-test_x / 2, test_y / 2, test_x / 2, test_y / 2)

        profile_sketch.close_edition
        part_document.part.in_work_object = profile_sketch
        part_document.part.update()
        with pytest.raises(Exception):
            get_bounding_box()


if __name__ == "__main__":
    from pytia.log import log

    log.set_level_debug()
    log.add_stream_handler()

    test_import()
    test_bounding_box()
    test_bounding_box_empty_body()
    test_bounding_box_no_shapes()
