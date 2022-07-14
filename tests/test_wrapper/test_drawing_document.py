import os
from tempfile import gettempdir

from pytia.const import BACKGROUND_VIEW, FOREGROUND_VIEW

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


def test_text():
    """
    Tests if text can be added to views.
    """
    from pytia.wrapper.documents.drawing_documents import PyDrawingDocument

    drawing_document = PyDrawingDocument()
    drawing_document.new(name=test_name)

    sheet = drawing_document.drawing_document.sheets.active_sheet
    foreground_view = sheet.views.item(FOREGROUND_VIEW)
    background_view = sheet.views.item(BACKGROUND_VIEW)

    foreground_texts = foreground_view.texts
    background_texts = background_view.texts

    foreground_text = foreground_texts.add("Text.Foreground", 10, 20)
    foreground_text.text = "Foreground text"
    foreground_text.name = "Text.Foreground"

    background_text = background_texts.add("Text.Background", 10, 40)
    background_text.text = "Background text"
    background_text.name = "Text.Background"


if __name__ == "__main__":
    from pytia.log import log

    log.set_level_debug()
    log.add_stream_handler()

    test_import()
    test_new()
    test_new_save()
    test_new_save_wrong_sep()
    test_open()
