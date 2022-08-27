import os
from pathlib import Path
from random import randint
from tempfile import gettempdir

import pytest

test_name = "pytest_test_parameter"
test_folder = Path(gettempdir())
test_path = Path(test_folder, test_name + ".CATPart")
test_property_name = "test_" + str(randint(10000, 99999))
test_property_value = "test_" + str(randint(10000, 99999))


def test_import():
    """ """
    from pytia.wrapper.documents.part_documents import PyPartDocument  # noqa: F401


def test_properties_create():
    """
    Creates a new document and a new property. Tests if the name and value are correct.
    This test only passes when CATIA is running.
    """
    from pytia.wrapper.documents.part_documents import PyPartDocument

    with PyPartDocument() as part_document:
        part_document.new(name=test_name)

        property = part_document.properties.create(
            name=test_property_name, value=test_property_value
        )

        name = property.name
        value = property.value
    assert name == test_property_name
    assert value == test_property_value


def test_properties_create_multi_same_name():
    """
    Creates a new document and a new parameter. Tests if multiple
    parameters with the same name can be handled.
    This test only passes when CATIA is running.
    """
    from pytia.wrapper.documents.part_documents import PyPartDocument

    with pytest.raises(Exception):
        with PyPartDocument() as part_document:
            part_document.new(name=test_name)

            part_document.properties.create(
                name=test_property_name, value=test_property_value
            )

            # This one will raise an exception! Same local names are not allowed.
            part_document.properties.create(
                name=test_property_name, value=test_property_value
            )


def test_properties_create_and_save():
    """
    Tests if the file can be saved.
    This test only passes when CATIA is running.
    """
    from pytia.wrapper.documents.part_documents import PyPartDocument

    with PyPartDocument() as part_document:
        part_document.new(name=test_name)

        part_document.properties.create(
            name=test_property_name, value=test_property_value
        )
        part_document.save_as(folder=test_folder)
    assert os.path.exists(test_path)


def test_properties_get_all():
    """ """
    from pytia.wrapper.documents.part_documents import PyPartDocument

    with PyPartDocument() as part_document:
        part_document.open(path=test_path)
        property_list = part_document.properties.properties
        property_names = [p.name for p in property_list]
        property_values = [p.value for p in property_list]

    assert len(property_list) >= 1
    assert test_property_name in property_names
    assert test_property_value in property_values


def test_properties_get_all_names():
    """ """
    from pytia.wrapper.documents.part_documents import PyPartDocument

    with PyPartDocument() as part_document:
        part_document.open(path=test_path)
        property_names = part_document.properties.names
    assert len(property_names) >= 1
    assert test_property_name in property_names


def test_properties_exists():
    """ """
    from pytia.wrapper.documents.part_documents import PyPartDocument

    with PyPartDocument() as part_document:
        part_document.open(path=test_path)
        should_be_true = part_document.properties.exists(test_property_name)
    assert should_be_true


def test_properties_exists_error():
    """ """
    from pytia.wrapper.documents.part_documents import PyPartDocument

    with PyPartDocument() as part_document:
        part_document.open(path=test_path)
        should_be_false = part_document.properties.exists("non_existent_parameter")
    assert should_be_false == False


def test_properties_exists_list():
    """ """
    from pytia.wrapper.documents.part_documents import PyPartDocument

    with PyPartDocument() as part_document:
        part_document.open(path=test_path)
        should_be_true = part_document.properties.exists([test_property_name])
    assert should_be_true


def test_properties_exists_list_error():
    """ """
    from pytia.wrapper.documents.part_documents import PyPartDocument

    with PyPartDocument() as part_document:
        part_document.open(path=test_path)
        should_be_false = part_document.properties.exists(
            [test_property_name, "non_existent_parameter"]
        )
    assert should_be_false == False


def test_properties_get_by_name():
    """
    Tests if the previously created file can be opened, and if the properties have been saved correct.
    This test only passes when CATIA is running.
    """
    from pytia.wrapper.documents.part_documents import PyPartDocument

    with PyPartDocument() as part_document:
        part_document.open(path=test_path)
        property = part_document.properties.get_by_name(test_property_name)
        value = property.value
    assert value == test_property_value
    os.remove(test_path)


def test_properties_delete():
    """
    Creates a new document and a new property, then deletes it again.
    Tests if the property is not present anymore.
    This test only passes when CATIA is running.
    """
    from pytia.wrapper.documents.part_documents import PyPartDocument

    with PyPartDocument() as part_document:
        part_document.new(name=test_name)

        property = part_document.properties.create(
            name=test_property_name, value=test_property_value
        )
        assert part_document.properties.exists(name=test_property_name)

        part_document.properties.delete(name=property.name)
        assert part_document.properties.exists(name=test_property_name) == False


if __name__ == "__main__":
    from pytia.log import log

    log.set_level_debug()
    log.add_stream_handler()

    test_import()
    test_properties_create()
    test_properties_create_multi_same_name()
    test_properties_create_and_save()
    test_properties_get_all()
    test_properties_get_all_names()
    test_properties_exists()
    test_properties_exists_error()
    test_properties_exists_list()
    test_properties_exists_list_error()
    test_properties_get_by_name()
    test_properties_delete()
