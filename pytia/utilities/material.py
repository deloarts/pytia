"""
    Utility module for handling CATMaterials.
"""

from pathlib import Path
from typing import Dict, List, Optional

from pytia.exceptions import PytiaMaterialError, PytiaMaterialNotFound
from pytia.framework import framework
from pytia.log import log
from pytia.wrapper.documents.material_documents import PyMaterialDocument
from pytia.wrapper.documents.part_documents import PyPartDocument
from pytia.wrapper.documents.product_documents import PyProductDocument


def get_material_families(catalog_path: Path) -> List[str]:
    """
    Returns a list of strings representing the available material families of a given catalog.

    Args:
        catalog_path (Path): The absolute path to the catalog file.

    Returns:
        List[str]: A list of all material families in the catalog.
    """
    file_alert = framework.catia.display_file_alerts
    framework.catia.display_file_alerts = False
    with PyMaterialDocument() as material_document:
        material_document.load(catalog_path)
        value = material_document.catalog.families_str
        log.info(
            f"Retrieved material families from {material_document.document.name!r}"
        )
    framework.catia.display_file_alerts = file_alert
    return value


def get_materials(catalog_path: Path) -> Dict[str, List[str]]:
    """
    Returns a dict of strings representing the family and its materials.

    Args:
        catalog_path (Path): The absolute path to the catalog file.

    Returns:
        Dict[str, List[str]]: A dictionary with all material families as keys, and a list of all \
            materials of each family as values.
    """
    file_alert = framework.catia.display_file_alerts
    framework.catia.display_file_alerts = False
    with PyMaterialDocument() as material_document:
        material_document.load(catalog_path)
        value = material_document.catalog.materials_str
        log.info(f"Retrieved materials from {material_document.document.name!r}")
    framework.catia.display_file_alerts = file_alert
    return value


def apply_material_on_part(
    material: str, catalog_path: Path, part_document: Optional[PyPartDocument] = None
) -> None:
    """
    Applies the material from given catalog to the part.
    Uses the current active document if no part_document is given.

    Args:
        material (str): The name of the material.
        catalog_path (str): The absolute path of the catalog file.
        part_document (Optional[PyPartDocument], optional): The part to which the material will be \
            applied. Defaults to None.

    Raises:
        PytiaMaterialNotFound: Raised when the material is not available in the catalog.
        PytiaMaterialError: General error with materials.
    """
    if part_document is None:
        part_document = PyPartDocument()
        part_document.current()

    file_alert = framework.catia.display_file_alerts
    framework.catia.display_file_alerts = False

    try:
        with PyMaterialDocument() as material_document:
            material_document.load(catalog_path)
            part_document.material = material_document.catalog.get_material(material)
            log.info(
                f"Applied material {material!r} from {material_document.document.name!r} to "
                f"{part_document.document.name!r}"
            )

    except PytiaMaterialNotFound as e:
        raise PytiaMaterialNotFound(
            f"Cannot apply {material!r} to {part_document.document.name!r}: "
            f"Material not found in catalog."
        ) from e

    except Exception as e:
        raise PytiaMaterialError(
            f"Failed applying material to {part_document.document.name!r}: {e}"
        ) from e

    finally:
        framework.catia.display_file_alerts = file_alert


def apply_material_on_product(
    material: str,
    catalog_path: Path,
    product_document: Optional[PyProductDocument] = None,
) -> None:
    """
    Applies the material from given catalog to the product.
    Uses the current active document if no product_document is given.

    Args:
        material (str): The name of the material.
        catalog_path (Path): The absolute path of the catalog file.
        product_document (Optional[PyProductDocument], optional): The product to which the \
            material will be applied. Defaults to None.

    Raises:
        PytiaMaterialNotFound: Raised when the material is not available in the catalog.
        PytiaMaterialError: General error with materials.
    """
    if product_document is None:
        product_document = PyProductDocument()
        product_document.current()

    file_alert = framework.catia.display_file_alerts
    framework.catia.display_file_alerts = False

    try:
        with PyMaterialDocument() as material_document:
            material_document.load(catalog_path)
            product_document.material = material_document.catalog.get_material(material)
            log.info(
                f"Applied material {material!r} from {material_document.document.name!r} to "
                f"{product_document.document.name!r}"
            )

    except PytiaMaterialNotFound as e:
        raise PytiaMaterialNotFound(
            f"Cannot apply {material!r} to {product_document.document.name!r}: "
            f"Material not found in catalog."
        ) from e

    except Exception as e:
        raise PytiaMaterialError(
            f"Failed applying material to {product_document.document.name!r}: {e}"
        ) from e

    finally:
        framework.catia.display_file_alerts = file_alert


def get_material_from_part(part_document: Optional[PyPartDocument] = None) -> str:
    """
    Returns a string representing the material applied to the part.
    Uses the current active document if no part_document is given.
    Returns an empty string if no material is applied.

    Args:
        part_document (Optional[PyPartDocument], optional): The part from which the material name \
            will be returned. Defaults to None.

    Raises:
        PytiaMaterialError: General error with materials.

    Returns:
        str: The name of the applied material. Returns an empty string if no material is applied.
    """
    if part_document is None:
        part_document = PyPartDocument()
        part_document.current()
    try:
        value = part_document.material.name
        log.info(f"Retrieved material from {part_document.document.name!r}: {value!r}")
        return value
    except AttributeError:
        log.info(f"There is no material applied to {part_document.document.name!r}")
        return ""
    except Exception as e:
        raise PytiaMaterialError(
            f"Failed retrieving material from {part_document.document.name!r}: {e}"
        ) from e


def get_material_from_product(
    product_document: Optional[PyProductDocument] = None,
) -> str:
    """
    Returns a string representing the material applied to the product.
    Uses the current active document if no product_document is given.
    Returns an empty string if no material is applied.

    Args:
        product_document (Optional[PyProductDocument], optional): The product from which the \
            material name will be returned. Defaults to None.

    Raises:
        PytiaMaterialError: General error with materials.

    Returns:
        str: The name of the applied material. Returns an empty string if no material is applied.
    """
    if product_document is None:
        product_document = PyProductDocument()
        product_document.current()
    try:
        value = product_document.material.name
        log.info(
            f"Retrieved material from {product_document.document.name!r}: {value!r}"
        )
        return value
    except AttributeError:
        log.info(f"There is no material applied to {product_document.document.name!r}")
        return ""
    except Exception as e:
        raise PytiaMaterialError(
            f"Failed retrieving material from {product_document.document.name!r}: {e}"
        ) from e
