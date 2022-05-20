import os
from random import randint
from tempfile import gettempdir

import pytest

test_name = "pytest_test_bodies"
test_folder = gettempdir()
test_path = f"{test_folder}{os.sep}{test_name}.CATPart"
test_body_name = "body_" + str(randint(10000, 99999))


def test_import():
    """ """
    from pytia.wrapper.documents.part_documents import PyPartDocument  # noqa: F401


def test_bodies_get_main_body():
    """
    Creates a new document.
    Tests if the main body has a name.
    This test only passes when CATIA is running.
    """
    from pytia.wrapper.documents.part_documents import PyPartDocument

    with PyPartDocument() as part_document:
        part_document.new(name=test_name)
        main_body = part_document.bodies.main_body
    assert main_body.name


def test_bodies_create():
    """
    Creates a new document and a new body.
    Tests if that name is set correct.
    This test only passes when CATIA is running.
    """
    from pytia.wrapper.documents.part_documents import PyPartDocument

    with PyPartDocument() as part_document:
        part_document.new(name=test_name)
        body_1 = part_document.bodies.create(test_body_name)
        body_1_name = body_1.name
        part_document.save_as(folder=test_folder)
    assert body_1_name == test_body_name


def test_bodies_create_same_name():
    """
    Creates a new document and a new body.
    Tests if creating identical names raises an exception.
    This test only passes when CATIA is running.
    """
    from pytia.wrapper.documents.part_documents import PyPartDocument

    with PyPartDocument() as part_document:
        part_document.new(name=test_name)
        with pytest.raises(Exception):
            part_document.bodies.create(test_body_name)
            part_document.bodies.create(test_body_name)


def test_bodies_get_by_name():
    """
    Loads an existing document and test if the funcion return a body by its name.
    This test only passes when CATIA is running.
    """
    from pytia.wrapper.documents.part_documents import PyPartDocument

    with PyPartDocument() as part_document:
        part_document.open(test_path)
        body_1 = part_document.bodies.get_by_name(test_body_name)
        body_1_name = body_1.name
    assert body_1_name == test_body_name


def test_bodies_get_all_names():
    """
    Loads an existing document and test if all bodies have correct names.
    This test only passes when CATIA is running.
    """
    from pytia.wrapper.documents.part_documents import PyPartDocument

    with PyPartDocument() as part_document:
        part_document.open(test_path)
        bodies_names = part_document.bodies.names
    assert test_body_name in bodies_names


def test_bodies_get_all():
    """
    Loads an existing document and test if all bodies have correct names.
    This test only passes when CATIA is running.
    """
    from pytia.wrapper.documents.part_documents import PyPartDocument

    with PyPartDocument() as part_document:
        part_document.open(test_path)
        bodies = part_document.bodies.bodies
        bodies_names = [body.name for body in bodies]
    assert test_body_name in bodies_names
    os.remove(test_path)


if __name__ == "__main__":
    from pytia.log import log

    log.set_level_debug()
    log.add_stream_handler()

    test_import()
    test_bodies_get_main_body()
    test_bodies_create()
    test_bodies_create_same_name()
    test_bodies_get_by_name()
    test_bodies_get_all_names()
    test_bodies_get_all()
