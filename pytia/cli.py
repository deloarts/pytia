"""
    Module for handling the cli feature of pytia.
"""

from pathlib import Path

import click

from pytia import __version__
from pytia.console import console
from pytia.log import log


@click.group()
# @click.version_option(version=__version__)
@click.option(
    "--verbose", is_flag=True, default=False, help="Show detailed logging info."
)
def cli(verbose: bool = False) -> None:
    """
    Command line tool for CATIA V5.

    \f
    Args:
        verbose (bool): Enables the log stream handler. Defaults to False.
    """
    if verbose:
        log.add_stream_handler()
        log.set_level_debug()


@cli.command()
def box() -> None:
    """
    \b
    Retrieves the bounding box from the current part.

    Example: `pytia box`
    """
    console.info("Retrieving bounding box from current part ...")
    try:
        from pytia.utilities import bounding_box

        x, y, z = bounding_box.get_bounding_box()
        console.info(
            f"Bounding box of the current part:\nX = {x}mm\nY = {y}mm\nZ = {z}mm",
            in_current_line=True,
        )
    except Exception as e:  # pylint: disable=W0703
        console.error(
            f"Failed retrieving bounding box from current part:\n{e}",
            in_current_line=True,
        )


@cli.command()
@click.option(
    "--overwrite", is_flag=True, default=False, help="Overwrite existing files."
)
@click.argument("folder", type=click.Path(), default=None, required=False)
def bom(folder: Path, overwrite: bool) -> None:
    """
    \b
    Exports the bill of material for the current product.

    Example: `pytia bom "C:\\users\\me\\desktop"`

    Note: If the folder argument is omitted, the BOM will be exported to the products' folder.

    \f
    Args:
        folder (Path): The path where the bom will be saved.
        overwrite (bool): Overwrites any existing files if set to True.
    """
    console.info("Exporting bill of material ...")
    try:
        from pytia.utilities import bill_of_material

        path = bill_of_material.export_bom(folder=folder, overwrite=overwrite)
        console.info(f"Exported bill of material to {path!r}", in_current_line=True)
    except Exception as e:  # pylint: disable=W0703
        console.error(
            f"Failed exporting bill of material:\n{e}",
            in_current_line=True,
        )


@cli.command()
@click.argument("postfix", type=click.STRING, default="_mirror", required=False)
def mirror(postfix: str) -> None:
    """
    \b
    Creates a mirrored version of the current CATPart.

    Example: `pytia mirror "_my_postfix"`

    Note: The postfix defaults to "_mirror".

    \f
    Args:
        postfix (str): A string value that will be appended to the partnumber and filename.
    """
    console.info("Creating mirrored version of the current part ...")
    try:
        from pytia.utilities import mirror as m

        path = m.mirror_main_body(postfix=postfix)
        console.info(f"Saved mirrored part to {path!r}", in_current_line=True)
    except Exception as e:  # pylint: disable=W0703
        console.error(
            f"Failed creating mirrored part:\n{e}",
            in_current_line=True,
        )


@cli.command()
@click.argument("doc_type", type=click.STRING, required=True)
@click.argument("name", type=click.STRING, required=True)
def new(doc_type: str, name: str) -> None:
    """
    \b
    Creates a new document (CATPart, CATProduct or CATDrawing).

    Example: `pytia new part "my part"`

    \f
    Args:
        doc_type (str): The document type (part, product or drawing).
        name (str): The name (partnumber, filename) of the new document.
    """
    console.info(f"Creating a new {doc_type} ...")
    try:
        if doc_type.lower() == "part":
            from pytia.wrapper.documents.part_documents import PyPartDocument

            part_document = PyPartDocument()
            part_document.new(name=name)
            console.info(f"Created new CATPart {name!r}.", in_current_line=True)
        elif doc_type.lower() == "product":
            from pytia.wrapper.documents.product_documents import PyProductDocument

            product_document = PyProductDocument()
            product_document.new(name=name)
            console.info(f"Created new CATProduct {name!r}.", in_current_line=True)
        elif doc_type.lower() == "drawing":
            from pytia.wrapper.documents.drawing_documents import PyDrawingDocument

            drawing_document = PyDrawingDocument()
            drawing_document.new(name=name)
            console.info(f"Created new CATDrawing {name!r}.", in_current_line=True)
        else:
            console.error(
                f"Failed creating new document:\n{doc_type!r} is no supported document type.",
                in_current_line=True,
            )
    except Exception as e:  # pylint: disable=W0703
        console.error(
            f"Failed creating new document:\n{e}",
            in_current_line=True,
        )
