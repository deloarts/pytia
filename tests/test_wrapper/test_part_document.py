import os
from random import randint
from tempfile import gettempdir

test_name = "pytest_test_part_document"
test_folder = gettempdir()
test_folder_wrong_sep = test_folder.replace(os.sep, "/")
test_path = f"{test_folder}{os.sep}{test_name}.CATPart"
test_path_wrong_sep = test_path.replace(os.sep, "/")
test_defintion = str(randint(10000, 99999))


def test_import():
    """ """

    from pytia.wrapper.documents.part_documents import PyPartDocument  # noqa: F401


def test_new():
    """
    Tests if a new part document has been created with the correct PartNumber.
    This test only passes when CATIA is running.
    """
    from pytia.wrapper.documents.part_documents import PyPartDocument

    with PyPartDocument() as part_document:
        part_document.new(name=test_name)
        part_number = part_document.product.part_number

    assert part_number == test_name


def test_new_save():
    """
    Tests if the new part document can be saved.
    This test only passes when CATIA is running.
    """
    from pytia.wrapper.documents.part_documents import PyPartDocument

    with PyPartDocument() as part_document:
        part_document.new(name=test_name)
        part_document.save_as(folder=test_folder)

    assert os.path.exists(test_path)
    os.remove(test_path)


def test_new_save_wrong_sep():
    """
    Tests if the new part document can be saved with the linux style folder sep.
    This test only passes when CATIA is running.
    """
    from pytia.wrapper.documents.part_documents import PyPartDocument

    with PyPartDocument() as part_document:
        part_document.new(name=test_name)
        part_document.save_as(folder=test_folder_wrong_sep)

    assert os.path.exists(test_path_wrong_sep)
    os.remove(test_path_wrong_sep)


def test_new_with_definition():
    """
    Tests if standard properties of a new part can be accessed.
    This test only passes when CATIA is running.
    """
    from pytia.framework import framework
    from pytia.wrapper.documents.part_documents import PyPartDocument

    with PyPartDocument() as part_document:
        part_document.new(name=test_name)
        part_document.product.definition = test_defintion

        definition = framework.catia.active_document.product.definition  # type: ignore

        part_document.save_as(folder=test_folder)

    assert definition == test_defintion


def test_open():
    """
    Tests if the previously created file can be opened.
    This test only passes when CATIA is running.
    """
    from pytia.wrapper.documents.part_documents import PyPartDocument

    with PyPartDocument() as part_document:
        part_document.open(path=test_path)

    assert part_document


def test_open_wrong_sep():
    """
    Tests if the previously created file can be opened with a linux style sep.
    This test only passes when CATIA is running.
    """
    from pytia.wrapper.documents.part_documents import PyPartDocument

    with PyPartDocument() as part_document:
        part_document.open(path=test_path_wrong_sep)

    assert part_document


def test_open_defintion():
    """
    Tests if the previously created file can be opened, and if the properties
    have been saved correct.
    This test only passes when CATIA is running.
    This test deletes the file afterwards.
    """
    from pytia.wrapper.documents.part_documents import PyPartDocument

    path = f"{test_folder}/{test_name}.CATPart"
    with PyPartDocument() as part_document:
        part_document.open(path=path)
        definition = part_document.product.definition

    assert definition == test_defintion
    os.remove(path)


def test_auto_detect():
    """
    Tests if the part can be auto-detected and used.
    This test only passes when CATIA is running.
    """
    from pytia.wrapper.documents.helper import get_current_document
    from pytia.wrapper.documents.part_documents import PyPartDocument

    with PyPartDocument() as part_document:
        part_document.new(name=test_name)
        detected_document = get_current_document()
        assert part_document.document.name == detected_document.document.name
        assert detected_document.document.is_part


if __name__ == "__main__":
    from pytia.log import log

    log.set_level_debug()
    log.add_stream_handler()

    test_import()
    test_new()
    test_new_save()
    test_new_save_wrong_sep()
    test_new_with_definition()
    test_open()
    test_open_wrong_sep()
    test_open_defintion()
