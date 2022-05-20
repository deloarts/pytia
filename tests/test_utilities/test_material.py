"""
    Tests the material utility.
"""
import os
from pathlib import Path

import pytest

test_name = "pytest_test_material"
test_files = Path("tests/assets")
test_catalog_file = str(Path(os.getcwd(), test_files, "Catalog.CATMaterial"))


def test_import():
    """ """
    from pytia.utilities.material import apply_material_on_part  # noqa: F401
    from pytia.utilities.material import get_material_families  # noqa: F401
    from pytia.utilities.material import get_material_from_part  # noqa: F401
    from pytia.utilities.material import get_materials  # noqa: F401

    os.path.isfile(test_catalog_file)


def test_new_empty():
    from pytia.utilities.material import get_material_from_part
    from pytia.wrapper.documents.part_documents import PyPartDocument

    with PyPartDocument() as part_document:
        part_document.new(name=test_name)
        material = get_material_from_part()
        assert material == ""


def test_apply_to_part():
    import random

    from pytia.utilities.material import (
        apply_material_on_part,
        get_material_from_part,
        get_materials,
    )
    from pytia.wrapper.documents.part_documents import PyPartDocument

    materials = get_materials(catalog_path=test_catalog_file)
    random_family = random.choice(list(materials))
    random_material = random.choice(materials[random_family])

    with PyPartDocument() as part_document:
        part_document.new(name=test_name)
        apply_material_on_part(
            material=random_material,
            catalog_path=test_catalog_file,
            part_document=part_document,
        )
        assert get_material_from_part(part_document) == random_material


def test_apply_to_part_with_false_name():
    from pytia.utilities.material import apply_material_on_part
    from pytia.wrapper.documents.part_documents import PyPartDocument

    with pytest.raises(Exception):
        with PyPartDocument() as part_document:
            part_document.new(name=test_name)
            apply_material_on_part(
                material="non_existent_material",
                catalog_path=test_catalog_file,
                part_document=part_document,
            )


def test_apply_to_product():
    import random

    from pytia.utilities.material import (
        apply_material_on_product,
        get_material_from_product,
        get_materials,
    )
    from pytia.wrapper.documents.product_documents import PyProductDocument

    materials = get_materials(catalog_path=test_catalog_file)
    random_family = random.choice(list(materials))
    random_material = random.choice(materials[random_family])

    with PyProductDocument() as product_document:
        product_document.new(name=test_name)
        apply_material_on_product(
            material=random_material,
            catalog_path=test_catalog_file,
            product_document=product_document,
        )
        assert get_material_from_product(product_document) == random_material


def test_apply_to_product_with_false_name():
    from pytia.utilities.material import apply_material_on_product
    from pytia.wrapper.documents.product_documents import PyProductDocument

    with pytest.raises(Exception):
        with PyProductDocument() as product_document:
            product_document.new(name=test_name)
            apply_material_on_product(
                material="non_existent_material",
                catalog_path=test_catalog_file,
                product_document=product_document,
            )


if __name__ == "__main__":
    from pytia.log import log

    log.set_level_debug()
    log.add_stream_handler()

    test_import()
    test_new_empty()
    test_apply_to_part()
    test_apply_to_part_with_false_name()
    test_apply_to_product()
    test_apply_to_product_with_false_name()
