import os
from random import randint
from tempfile import gettempdir

test_name = "pytest_test_drawing_document"
test_folder = gettempdir()
test_folder_wrong_sep = test_folder.replace(os.sep, "/")
test_path = f"{test_folder}{os.sep}{test_name}.CATDrawing"
test_path_wrong_sep = test_path.replace(os.sep, "/")


def test_import():
    """ """

    from pytia.wrapper.documents.drawing_documents import (
        PyDrawingDocument,
    )  # noqa: F401


def test_new():
    """
    Tests if a new drawing document has been created.
    This test only passes when CATIA is running.
    """
    from pytia.wrapper.documents.drawing_documents import PyDrawingDocument

    with PyDrawingDocument() as drawing_document:
        drawing_document.new(name=test_name)
        name = drawing_document.name

    assert name == test_name


def test_new_save():
    """
    Tests if the new drawing document can be saved.
    This test only passes when CATIA is running.
    """
    from pytia.wrapper.documents.drawing_documents import PyDrawingDocument

    with PyDrawingDocument() as drawing_document:
        drawing_document.new(name=test_name)
        drawing_document.save_as(folder=test_folder)
        name = drawing_document.drawing_document.name.split(".CATDrawing")[0]

    assert os.path.exists(test_path)
    assert name == test_name
    os.remove(test_path)


def test_new_save_wrong_sep():
    """
    Tests if the new drawing document can be saved with the linux style folder sep.
    This test only passes when CATIA is running.
    """
    from pytia.wrapper.documents.drawing_documents import PyDrawingDocument

    with PyDrawingDocument() as drawing_document:
        drawing_document.new(name=test_name)
        drawing_document.save_as(folder=test_folder_wrong_sep)

    assert os.path.exists(test_path_wrong_sep)
    os.remove(test_path_wrong_sep)


def test_open():
    """
    Tests if the previously created file can be opened.
    This test only passes when CATIA is running.
    """
    from pytia.wrapper.documents.drawing_documents import PyDrawingDocument

    with PyDrawingDocument() as drawing_document:
        drawing_document.new(name=test_name)
        drawing_document.save_as(folder=test_folder)

    with PyDrawingDocument() as drawing_document:
        drawing_document.open(path=test_path)

    assert drawing_document
    os.remove(test_path)


if __name__ == "__main__":
    from pytia.log import log

    log.set_level_debug()
    log.add_stream_handler()

    test_import()
    test_new()
    test_new_save()
    test_new_save_wrong_sep()
    test_open()
