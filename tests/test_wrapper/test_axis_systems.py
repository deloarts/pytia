import os
from tempfile import gettempdir

import pytest

test_name = "pytest_test_axis_systems"
test_folder = gettempdir()
test_path = f"{test_folder}{os.sep}{test_name}.CATPart"


def test_import():
    """ """
    from pytia.wrapper.axis_systems import PyAxisSystems  # noqa: F401
    from pytia.wrapper.documents.part_documents import PyPartDocument  # noqa: F401


def test_axis_systems_create():
    """
    Creates a new document and a new axis system.
    Test if no error occurs.
    This test only passes when CATIA is running.
    """
    from pytia.wrapper.documents.part_documents import PyPartDocument

    with PyPartDocument() as part_document:
        part_document.new(name=test_name)
        part_document.axis_systems.create()
        count = len(part_document.axis_systems.axis_systems)
    assert count == 1


def test_axis_systems_create_multi_same_name():
    """
    Creates a new document and a new axis system. Tests if multiple
    axis systems with the same name can be handled (Error mus be raised)
    This test only passes when CATIA is running.
    """
    from pytia.exceptions import PytiaAxisSystemExistsError
    from pytia.wrapper.documents.part_documents import PyPartDocument

    with pytest.raises(PytiaAxisSystemExistsError):
        with PyPartDocument() as part_document:
            part_document.new(name=test_name)
            part_document.axis_systems.create()
            # This one will raise an exception!
            # Same local names are not allowed
            # without the recycle flag.
            part_document.axis_systems.create()


def test_axis_systems_create_multi_same_name_recycle():
    """
    Creates a new document and a new axis system. Tests if multiple
    axis systems with the same name can be handled with the recycle flag.
    This test only passes when CATIA is running.
    """
    from pytia.wrapper.documents.part_documents import PyPartDocument

    with PyPartDocument() as part_document:
        part_document.new(name=test_name)
        part_document.axis_systems.create()
        part_document.axis_systems.create(recycle=True)
        count_obj = len(part_document.axis_systems.axis_systems)
        count_name = len(part_document.axis_systems.names)
        assert (
            part_document.axis_systems.axis_systems[0].name
            == part_document.axis_systems.names[0]
        )
    assert count_obj == 1
    assert count_name == 1


def test_axis_systems_create_and_save():
    """
    Tests if the file can be saved with an axis system.
    This test only passes when CATIA is running.
    """
    from pytia.wrapper.documents.part_documents import PyPartDocument

    with PyPartDocument() as part_document:
        part_document.new(name=test_name)
        part_document.axis_systems.create(name=test_name)
        part_document.save_as(folder=test_folder)
    assert os.path.exists(test_path)


def test_axis_systems_get_all_names():
    """ """
    from pytia.wrapper.documents.part_documents import PyPartDocument

    with PyPartDocument() as part_document:
        part_document.open(path=test_path)
        axis_systems = part_document.axis_systems.names
    assert test_name in axis_systems


def test_axis_system_exists():
    """ """
    from pytia.wrapper.documents.part_documents import PyPartDocument

    with PyPartDocument() as part_document:
        part_document.open(path=test_path)
        should_be_true = part_document.axis_systems.exists(test_name)
    assert should_be_true


def test_axis_systems_get_by_name():
    """
    Tests if the previously created file can be opened, and if the axis
    system has been saved correct.
    This test only passes when CATIA is running.
    """
    from pytia.wrapper.documents.part_documents import PyPartDocument

    with PyPartDocument() as part_document:
        part_document.open(path=test_path)
        axis_system = part_document.axis_systems.get_by_name(test_name)
        axis_system_name = axis_system.name
    assert axis_system_name == test_name
    os.remove(test_path)


if __name__ == "__main__":
    from pytia.log import log

    log.set_level_debug()
    log.add_stream_handler()

    test_import()
    test_axis_systems_create()
    test_axis_systems_create_multi_same_name()
    test_axis_systems_create_and_save()
    test_axis_systems_get_all_names()
    test_axis_system_exists()
    test_axis_systems_get_by_name()
