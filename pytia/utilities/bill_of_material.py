"""
    Utility module for extracting the bill of material from a CATProduct.
"""

import os
import tempfile
from pathlib import Path
from typing import Optional

from pycatia.product_structure_interfaces.assembly_convertor import AssemblyConvertor
from pycatia.product_structure_interfaces.product import Product

from pytia.const import ENV_IGNORE_BOM_ERROR, GET_ITEM_BILL_OF_MATERIAL, KNOWN_ERRORS
from pytia.exceptions import PytiaBOMError, PytiaFileExistsError
from pytia.helper.verify import verify_folder
from pytia.log import log
from pytia.wrapper.documents.product_documents import PyProductDocument


def set_current_format(
    current_format: tuple, product: Optional[Product] = None
) -> None:
    """
    Sets the current format of the products bill of material.

    Args:
        current_format (tuple): The elements that shall be visible in the bom.
        product (Optional[Product], optional): The product to which the format will be applied. \
            Defaults to None. If None the currently open CATProduct will be used.

    Raises:
        PytiaBOMError: Raised when the format cannot be applied.
    """
    if not product:
        product_document = PyProductDocument()
        product_document.current()
        product = product_document.product

    try:
        bom = product.get_item(GET_ITEM_BILL_OF_MATERIAL)
        assembly_convertor = AssemblyConvertor(bom.com_object)
        assembly_convertor.set_current_format(current_format)
        log.info(f"Set current BOM format of {product.name!r} to {current_format!r}")
    except Exception as e:
        raise PytiaBOMError(
            f"Failed setting current bom format of {product.name!r}: {e}"
        ) from e


def set_secondary_format(
    secondary_format: tuple, product: Optional[Product] = None
) -> None:
    """
    Sets the secondary format of the products bill of material.

    Args:
        secondary_format (tuple): The elements that shall be visible in the bom.
        product (Optional[Product], optional): The product to which the format will be applied. \
            Defaults to None. If None the currently open CATProduct will be used.

    Raises:
        PytiaBOMError: Raised when the format cannot be applied.
    """
    if not product:
        product_document = PyProductDocument()
        product_document.current()
        product = product_document.product

    try:
        bom = product.get_item(GET_ITEM_BILL_OF_MATERIAL)
        assembly_convertor = AssemblyConvertor(bom.com_object)
        assembly_convertor.set_secondary_format(secondary_format)
        log.info(
            f"Set secondary BOM format of {product.name!r} to {secondary_format!r}"
        )
    except Exception as e:
        raise PytiaBOMError(
            f"Failed setting secondary bom format of {product.name!r}: {e}"
        ) from e


def export_bom(
    filename: Optional[str] = None,
    folder: Optional[Path] = None,
    overwrite: bool = False,
    product: Optional[Product] = None,
) -> Path:
    """
    Exports the bill of material of the current product as excel file to the specified path.
    Returns the path (folder and filename) of the bill of material.

    Args:
        filename (Optional[str], optional): The filename of the BOM. Defaults to None.
        folder (Optional[Path], optional): The folder to which the BOM will be saved. \
            Defaults to None.
        overwrite (bool, optional): Overwrites any existing files if True. Defaults to False.
        product (Optional[Product], optional): The product from which the BOM will be extracted. \
            Defaults to None. If None the currently open CATProduct will be used.

    Returns:
        Path: The full path of the exported BOM.
    """

    def fallback():
        """
        Fallback option: Use dispatch instead of the framework.
        """
        from pytia.framework import Framework

        framework = Framework()

        d_document = framework.dispatch.ActiveDocument
        d_product = d_document.Product

        try:
            d_bom = d_product.GetItem("BillOfMaterial")
            d_bom.Print("XLS", path, d_product)
            log.info(f"Exported BOM of {d_product.Name!r} as {path!r} (fallback)")
        except Exception as e:
            raise PytiaBOMError(f"Failed exporting BOM: {e}") from e

    if not product:
        product_document = PyProductDocument()
        product_document.current()
        product = product_document.product

    log.info(f"Exporting bill of material for {product.name!r}.")

    if filename is None:
        filename = product.name + ".xls"
    elif ".xls" not in filename:
        filename = filename + ".xls"

    if folder is None:
        folder = Path(tempfile.gettempdir())
    else:
        folder = verify_folder(folder)

    if not os.path.exists(folder):
        os.makedirs(folder)
        log.info(f"Created new folder: {folder!r}")

    path = Path(folder, filename)

    if os.path.isfile(path):
        if overwrite:
            os.remove(path)
            log.info("Removed existing bill of material from folder.")
        else:
            raise PytiaFileExistsError(
                f"Failed exporting BOM of {product.name!r}: File already exists at {path!r}"
            )

    try:
        bom = product.get_item(GET_ITEM_BILL_OF_MATERIAL)
        assembly_convertor = AssemblyConvertor(bom.com_object)
        assembly_convertor.print("XLS", path, product)
        log.info(f"Exported BOM of {product.name!r} as {path!r}")
    except Exception as e:  # pylint: disable=W0703
        if not ENV_IGNORE_BOM_ERROR:
            raise PytiaBOMError(f"Failed exporting BOM: {e}") from e

        if not any([known_error in str(e) for known_error in KNOWN_ERRORS]):
            log.warning(
                f"Failed exporting BOM of {product.name!r}. Trying fallback option. Error: {e}"
            )
            fallback()
        else:
            log.warning(
                f"Exported BOM of {product.name!r} with known error to {path!r}"
            )

    return path
