"""
    Utility module for applying text or views to a CATDrawing.
"""


from __future__ import annotations

import os
from dataclasses import dataclass, fields
from datetime import datetime
from pathlib import Path
from typing import List, Tuple

from pytia.const import BACKGROUND_VIEW, FOREGROUND_VIEW
from pytia.exceptions import PytiaFileNotFoundError, PytiaFileOperationError
from pytia.framework.drafting_interfaces.drawing_text import DrawingText
from pytia.helper.scaling import get_view_scale
from pytia.helper.verify import verify_folder
from pytia.log import log
from pytia.wrapper.documents.drawing_documents import PyDrawingDocument
from pytia.wrapper.documents.part_documents import PyPartDocument
from pytia.wrapper.documents.product_documents import PyProductDocument


@dataclass
class DocketConfigTexts:
    """Dataclass for docket texts."""

    name: str
    value: str
    view: str


@dataclass
class DocketConfigViews:
    """Dataclass for docket views."""

    name: str
    x: float
    y: float
    max_width: float
    max_height: float
    definition: Tuple[float, float, float, float, float, float]


@dataclass
class DocketConfig:
    """Dataclass for docket configuration."""

    texts: List[DocketConfigTexts]
    views: List[DocketConfigViews]

    def __post_init__(self) -> None:
        self.texts = [DocketConfigTexts(**dict(text)) for text in self.texts]  # type: ignore
        self.views = [DocketConfigViews(**dict(view)) for view in self.views]  # type: ignore

    @classmethod
    def from_dict(cls, data: dict) -> DocketConfig:
        """
        Creates a DocketConfig by the given dict. Keys that are not in the dataclass
        will be ignored.
        """
        return DocketConfig(
            **{k: v for k, v in data.items() if k in {f.name for f in fields(cls)}}
        )


def create_docket_from_template(
    template: str,
    document: PyPartDocument | PyProductDocument,
    config: DocketConfig,
    hide_unknown_properties: bool = False,
    **kwargs,
) -> PyDrawingDocument:
    """
    Creates a docket from a template.
    The docket (CATDrawing) will be left open as ActiveDocument, you have to close it manually.

    Args:
        template (str): The path (folder and filename) of the template.
        document (PyPartDocument | PyProductDocument): The part or product document from which \
            to create the docket
        config (DocketConfig): The docket configuration dataclass.
        hide_unknown_properties (bool): Use empty string for unknown properties.

        kwargs: Keyword arguments will be added to the docket for text elements which names are \
            prefixed with `arg.`. Example: To add the quantity to the docket text \
            element with the name 'arg.quantity' you have to supply the argument `quantity=1`.

    Raises:
        PytiaFileNotFoundError: Raised if the template file cannot be found.

    Returns:
        PyDrawingDocument: Returns the docket as PyDrawingDocument.
    """
    if not os.path.isfile(template):
        raise PytiaFileNotFoundError(
            f"Cannot open docket template {template!r}: Not a file."
        )

    log.info(f"Creating docket from template {template!r}.")
    docket = PyDrawingDocument()
    docket.new_from(path=template, name="docket")

    sheet = docket.drawing_document.sheets.active_sheet
    fg_views = sheet.views.item(FOREGROUND_VIEW)
    bg_views = sheet.views.item(BACKGROUND_VIEW)
    fg_texts = fg_views.texts
    bg_texts = bg_views.texts

    # Apply texts from config
    log.debug("Applying texts from config ...")
    for item in config.texts:
        texts = fg_texts if item.view == "fg" else bg_texts
        try:
            text = DrawingText(texts.get_item(item.name).com_object)
        except Exception as e:
            log.warning(
                f"Could not retrieve drawing text {item.name!r}: Does not exist in CATDrawing."
            )
            continue

        match (item_type := item.name.split(".")[0]):
            case "text":
                log.info(f"Applying TEXT ({item.name}: {item.value}) to docket.")
                text.text = item.value
            case "arg":
                log.info(f"Applying ARGUMENT ({item.name}: {item.value}) to docket.")
                if item.value in kwargs:
                    text.text = str(kwargs[item.value])
                else:
                    log.warning(f"No argument for {item.value}.")
            case "object":
                log.info(f"Applying OBJECT ({item.name}: {item.value}) to docket.")
                match (object_type := item.name.split(".")[-1]):
                    case "date":
                        text.text = datetime.now().strftime(item.value)
                    case _:
                        text.text = f"Unknown ({object_type})"
            case "property":
                log.info(f"Applying PROPERTY ({item.name}: {item.value}) to docket.")
                if item.value == "partnumber":
                    text.text = document.product.part_number
                elif item.value == "definition":
                    text.text = document.product.definition
                elif item.value == "revision":
                    text.text = document.product.revision
                elif item.value == "nomenclature":
                    text.text = document.product.nomenclature
                elif item.value == "source":
                    text.text = str(document.product.source)
                elif item.value == "description_reference":
                    text.text = document.product.description_reference
                elif document.properties.exists(name=item.value):
                    text.text = document.properties.get_by_name(name=item.value).value
                else:
                    text.text = (
                        "" if hide_unknown_properties else f"Unknown ({item.value})"
                    )
                    log.warning(f"Unknown property for drawing text: {item.value}")
            case _:
                log.warning(f"Unknown type for drawing text: {item_type}")

    # Create isometric view
    log.debug("Creating views from config ...")
    for item in config.views:
        view = sheet.views.add(item.name)
        generative_behavior = view.generative_behavior
        generative_behavior.document = document.product
        generative_behavior.define_isometric_view(
            *(element for element in item.definition)
        )
        generative_behavior.update()
        view.x = item.x
        view.y = item.y
        log.info(f"Added view: {view.name} to docket.")

        view.scale = get_view_scale(
            view=view, max_width=item.max_width, max_height=item.max_height
        )
    return docket


def export_docket_as_pdf(
    docket: PyDrawingDocument, name: str, folder: str, close: bool = True
) -> str:
    """
    Exports the docket as pdf.

    Args:
        docket (PyDrawingDocument): The docket to export.
        name (str): The name of the exported pdf file.
        folder (str): The folder where the exported pdf file should be stored.
        close (bool, optional): Closes the CATDrawing afterwards. Defaults to True.

    Raises:
        PytiaFileOperationError: Raised when an existing docket cannot be deleted.

    Returns:
        str: The path to the exported pdf file (folder, filename and extension).
    """
    export_path = Path(verify_folder(folder), name + ".pdf")

    if os.path.exists(export_path):
        try:
            os.remove(export_path)
            log.warning(f"Removed existing docket file at {str(export_path)!r}.")
        except Exception as e:
            raise PytiaFileOperationError(
                f"Failed to remove existing docket file at {str(export_path)!r}: {e}"
            ) from e

    docket.drawing_document.export_data(export_path, "pdf")
    log.info(f"Exported docket {name!r} to {str(export_path)!r}.")
    if close:
        docket.close()
    return str(export_path)
