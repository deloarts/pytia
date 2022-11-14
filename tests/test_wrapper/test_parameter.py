import os
from pathlib import Path
from random import randint
from tempfile import gettempdir

import pytest

test_name = "pytest_test_parameter"
test_folder = Path(gettempdir())
test_path = Path(test_folder, test_name + ".CATPart")
test_parameter_name = "param" + str(randint(10000, 99999))
test_parameter_value = randint(10000, 99999)


def test_import():
    """ """
    from pytia.wrapper.documents.part_documents import PyPartDocument  # noqa: F401


def test_part_parameter_create():
    """
    Creates a new document and a new parameter. Tests if the parameters name
    and value are correct.
    This test only passes when CATIA is running.
    """
    from pytia.wrapper.documents.part_documents import PyPartDocument

    with PyPartDocument() as part_document:
        part_document.new(name=test_name)

        length_parameter = part_document.parameters.create_length(
            name=test_parameter_name, value=test_parameter_value
        )

        length_parameter_name = length_parameter.name
        length_parameter_value = length_parameter.value

        part_document.save_as(folder=test_folder)
    assert length_parameter_name == test_parameter_name
    assert length_parameter_value == test_parameter_value


def test_part_parameter_create_multi_same_name():
    """
    Creates a new document and a new parameter. Tests if multiple
    parameters with the same name can be handled.
    This test only passes when CATIA is running.
    """
    from pytia.wrapper.documents.part_documents import PyPartDocument

    with pytest.raises(Exception):
        with PyPartDocument() as part_document:
            part_document.new(name=test_name)
            part_document.parameters.create_length(name=test_parameter_name, value=0)
            # This one will raise an exception! Same local names are not allowed.
            part_document.parameters.create_length(name=test_parameter_name, value=0)


def test_part_parameter_create_and_save():
    """
    Tests if the file can be saved.
    This test only passes when CATIA is running.
    """
    from pytia.wrapper.documents.part_documents import PyPartDocument

    with PyPartDocument() as part_document:
        part_document.new(name=test_name)

        part_document.parameters.create_length(
            name=test_parameter_name, value=test_parameter_value
        )
        part_document.save_as(folder=test_folder)
    assert os.path.exists(test_path)


def test_part_parameter_get_all():
    """ """
    from pytia.wrapper.documents.part_documents import PyPartDocument

    with PyPartDocument() as part_document:
        part_document.open(path=test_path)
        parameter_list = part_document.parameters.parameters
    assert len(parameter_list) > 0


def test_parameter_exists():
    """ """
    from pytia.wrapper.documents.part_documents import PyPartDocument

    with PyPartDocument() as part_document:
        part_document.open(path=test_path)
        should_be_true = part_document.parameters.exists(test_parameter_name)
    assert should_be_true


def test_part_parameter_get_by_name():
    """
    Tests if the previously created file can be opened, and if the properties
    have been saved correct.
    This test only passes when CATIA is running.
    """
    from pytia.wrapper.documents.part_documents import PyPartDocument

    with PyPartDocument() as part_document:
        part_document.open(path=test_path)
        parameter = part_document.parameters.get(test_parameter_name)
        value = parameter.value
    assert value == test_parameter_value


def test_part_parameter_check_type_true():
    """ """
    from pytia.wrapper.documents.part_documents import PyPartDocument

    with PyPartDocument() as part_document:
        part_document.open(path=test_path)
        parameter = part_document.parameters.get(test_parameter_name)
        should_be_true = part_document.parameters.is_dimension(parameter)
    assert should_be_true


def test_part_parameter_check_type_false():
    """ """
    from pytia.wrapper.documents.part_documents import PyPartDocument

    with PyPartDocument() as part_document:
        part_document.open(path=test_path)
        parameter = part_document.parameters.get(test_parameter_name)
        should_be_false = part_document.parameters.is_real(parameter)
    assert should_be_false == False


def test_part_parameter_type_dimension():
    """"""
    from pytia.wrapper.documents.part_documents import PyPartDocument

    with PyPartDocument() as part_document:
        part_document.open(path=test_path)
        length_param = part_document.parameters.create_length(
            name=test_parameter_name + "_length", value=10
        )
        angle_param = part_document.parameters.create_angle(
            name=test_parameter_name + "_angle", value=20
        )

        assert part_document.parameters.is_dimension(length_param)
        assert length_param.value == 10

        assert part_document.parameters.is_dimension(angle_param)
        assert angle_param.value == 20


def test_part_parameter_type_bool():
    """"""
    from pytia.wrapper.documents.part_documents import PyPartDocument

    with PyPartDocument() as part_document:
        part_document.open(path=test_path)
        param = part_document.parameters.create_bool(
            name=test_parameter_name + "_bool", value=True
        )

        assert part_document.parameters.is_bool(param)
        assert param.value == True


def test_part_parameter_type_int():
    """"""
    from pytia.wrapper.documents.part_documents import PyPartDocument

    with PyPartDocument() as part_document:
        part_document.open(path=test_path)
        param = part_document.parameters.create_int(
            name=test_parameter_name + "_int", value=30
        )

        assert part_document.parameters.is_int(param)
        assert param.value == 30


def test_part_parameter_type_real():
    """"""
    from pytia.wrapper.documents.part_documents import PyPartDocument

    with PyPartDocument() as part_document:
        part_document.open(path=test_path)
        param = part_document.parameters.create_real(
            name=test_parameter_name + "_real", value=40.40
        )

        assert part_document.parameters.is_real(param)
        assert param.value == 40.40


def test_part_parameter_type_str():
    """"""
    from pytia.wrapper.documents.part_documents import PyPartDocument

    with PyPartDocument() as part_document:
        part_document.open(path=test_path)
        param = part_document.parameters.create_string(
            name=test_parameter_name + "_str", value="foo bar"
        )

        assert part_document.parameters.is_str(param)
        assert param.value == "foo bar"


def test_part_parameter_cleanup():
    """Not a test."""
    os.remove(test_path)
    assert True


if __name__ == "__main__":
    from pytia.log import log

    log.set_level_debug()
    log.add_stream_handler()

    test_part_parameter_create()
    test_part_parameter_create_multi_same_name()
    test_part_parameter_create_and_save()
    test_part_parameter_get_all()
    test_parameter_exists()
    test_part_parameter_get_by_name()
    test_part_parameter_check_type_true()
    test_part_parameter_check_type_false()
