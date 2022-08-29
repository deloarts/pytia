"""
    Tests the bounding box utility.
"""

import os
import tempfile
from pathlib import Path

import pytest

test_name = "pytest_test_mirror_main_body"
test_x = 50
test_y = 80
test_z = 20


def test_import():
    """ """
    from pytia.utilities.mirror import mirror_main_body  # noqa: F401


def test_mirror_main_body():
    """
    Tests if the mirror_main_body doesn't break.

    Important: Since this test shall run without any further doing we need to
    create a part with a body first. This is currently not tested somewhere
    else, so if this test breaks it may be also due to a bug in the body
    or part creation.

    This test only passes when CATIA is running.
    """
    from pytia.utilities.mirror import mirror_main_body
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

        original_path = part_document.save_as(folder=Path(tempfile.gettempdir()))

        new_path = mirror_main_body(keep_open=False)

    assert new_path.exists()
    os.remove(original_path)
    os.remove(new_path)


def test_mirror_main_body_empty_body():
    """
    Tests if the mirror_main_body function raises an exception when the main body is empty.
    This test only passes when CATIA is running.
    """
    from pytia.utilities.mirror import mirror_main_body
    from pytia.wrapper.documents.part_documents import PyPartDocument

    with PyPartDocument() as part_document:
        part_document.new(name=test_name)
        with pytest.raises(Exception):
            mirror_main_body()


if __name__ == "__main__":
    from pytia.log import log

    log.set_level_debug()
    log.add_stream_handler()

    test_import()
    test_mirror_main_body()
    test_mirror_main_body_empty_body()
