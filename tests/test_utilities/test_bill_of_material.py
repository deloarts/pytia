"""
    Tests the export bom utility.
"""

import os
from pathlib import Path
from tempfile import gettempdir

import pytest

test_name = "pytest_test_export_bom"
test_folder = Path(gettempdir())
test_path = Path(test_folder, test_name + ".xls")
test_format = (
    "Number",
    "Quantity",
    "Part Number",
    "Type",
    "Nomenclature",
    "Revision",
    "Definition",
)


def test_import():
    """ """
    from pytia.utilities.bill_of_material import export_bom  # noqa: F401
    from pytia.utilities.bill_of_material import set_current_format  # noqa: F401
    from pytia.utilities.bill_of_material import set_secondary_format  # noqa: F401


def test_current_format():
    """ """
    from pytia.utilities.bill_of_material import set_current_format
    from pytia.wrapper.documents.product_documents import PyProductDocument

    with PyProductDocument() as product_document:
        product_document.new(name=test_name)
        set_current_format(current_format=test_format)


def test_secondary_format():
    """ """
    from pytia.utilities.bill_of_material import set_secondary_format
    from pytia.wrapper.documents.product_documents import PyProductDocument

    with PyProductDocument() as product_document:
        product_document.new(name=test_name)
        set_secondary_format(secondary_format=test_format)


def test_current_format_with_product():
    """ """
    from pytia.utilities.bill_of_material import set_current_format
    from pytia.wrapper.documents.product_documents import PyProductDocument

    with PyProductDocument() as product_document:
        product_document.new(name=test_name)
        set_current_format(current_format=test_format, product=product_document.product)


def test_secondary_format_with_product():
    """ """
    from pytia.utilities.bill_of_material import set_secondary_format
    from pytia.wrapper.documents.product_documents import PyProductDocument

    with PyProductDocument() as product_document:
        product_document.new(name=test_name)
        set_secondary_format(
            secondary_format=test_format, product=product_document.product
        )


def test_exported_file_exists():
    """
    Tests if the export bom utility actually exports the file.
    This test only passes when CATIA is running.
    """
    from pytia.utilities.bill_of_material import export_bom
    from pytia.wrapper.documents.product_documents import PyProductDocument

    with PyProductDocument() as product_document:
        product_document.new(name=test_name)
        location = export_bom(filename=test_name, folder=test_folder, overwrite=True)

    assert str(location) == str(test_path)
    assert os.path.exists(test_path)
    os.remove(test_path)


def test_exported_file_exists_no_args():
    """
    Tests if the export bom utility actually exports the file to the temp folder when
    no arguments are passed.
    This test only passes when CATIA is running.
    """
    from pytia.utilities.bill_of_material import export_bom
    from pytia.wrapper.documents.product_documents import PyProductDocument

    with PyProductDocument() as product_document:
        product_document.new(name=test_name)
        location = export_bom(overwrite=True)

    assert str(location) == str(test_path)
    assert os.path.exists(test_path)
    os.remove(test_path)


if __name__ == "__main__":
    from pytia.log import log

    log.set_level_debug()
    log.add_stream_handler()

    test_import()
    test_current_format()
    test_secondary_format()
    test_current_format_with_product()
    test_secondary_format_with_product()
    test_exported_file_exists()
    test_exported_file_exists_no_args()
