from pathlib import Path
from tempfile import gettempdir

import pytest
from pytia.framework import framework

test_name = "pytest_test_materials"
test_folder = Path(gettempdir())
test_files = Path("tests/assets")
test_catalog_file = Path(
    framework.catia.system_service.environ("CATStartupPath"),
    "materials",
    "Catalog.CATMaterial",
)


def test_import():
    """ """
    from pytia.wrapper.documents.material_documents import (
        PyMaterialDocument,
    )  # noqa: F401
    from pytia.wrapper.material_catalogs import PyMaterialCatalog  # noqa: F401


def test_families_properties():
    """Tests the PyMaterialCatalog family properties."""
    from pytia.wrapper.documents.material_documents import PyMaterialDocument

    with PyMaterialDocument() as material_document:
        material_document.load(test_catalog_file)
        material_catalog = material_document.catalog
        material_family = material_catalog.families[0]
        material_family_str = material_catalog.families_str[0]

        assert material_family.name == material_family_str


def test_materials_properties():
    """Tests the PyMaterialCatalog materials properties."""
    from pytia.wrapper.documents.material_documents import PyMaterialDocument

    with PyMaterialDocument() as material_document:
        material_document.load(test_catalog_file)
        material_catalog = material_document.catalog
        material_family = material_catalog.families[0]
        material_family_str = material_catalog.families_str[0]
        material = material_catalog.materials[material_family][0]
        material_str = material_catalog.materials_str[material_family_str][0]

        assert material.name == material_str


def test_material_exists():
    """Checks if a material exists."""
    from pytia.wrapper.documents.material_documents import PyMaterialDocument

    with PyMaterialDocument() as material_document:
        material_document.load(test_catalog_file)
        material_catalog = material_document.catalog
        material_family = material_catalog.families[0]
        material = material_catalog.materials[material_family][0]

        assert material_catalog.material_exists(query="non existing material") == False
        assert material_catalog.material_exists(query=material)
        assert material_catalog.material_exists(query=material.name)


def test_get_material():
    """Tests if an existing material can be retrieved."""
    from pytia.framework.cat_mat_interfaces.material import Material
    from pytia.wrapper.documents.material_documents import PyMaterialDocument

    with PyMaterialDocument() as material_document:
        material_document.load(test_catalog_file)
        material_catalog = material_document.catalog
        material_family = material_catalog.families[0]
        material = material_catalog.materials[material_family][0]

        assert isinstance(material_catalog.get_material(name=material.name), Material)


def test_get_material_non_existent():
    """Tests if the correct error is raised."""
    from pytia.exceptions import PytiaMaterialNotFound
    from pytia.framework.cat_mat_interfaces.material import Material
    from pytia.wrapper.documents.material_documents import PyMaterialDocument

    with pytest.raises(PytiaMaterialNotFound):
        with PyMaterialDocument() as material_document:
            material_document.load(test_catalog_file)
            material_catalog = material_document.catalog
            material_catalog.get_material(name="non existing material")


if __name__ == "__main__":
    from pytia.log import log

    log.set_level_debug()
    log.add_stream_handler()

    test_import()
    test_families_properties()
    test_materials_properties()
    test_material_exists()
    test_get_material()
    test_get_material_non_existent()
