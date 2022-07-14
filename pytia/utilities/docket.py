"""
    Utility module for applying text or views to a CATDrawing.
"""


from __future__ import annotations

import os
from dataclasses import dataclass, fields
from pathlib import Path
from typing import List, Tuple

from pytia.const import BACKGROUND_VIEW, FOREGROUND_VIEW
from pytia.exceptions import PytiaFileNotFoundError
from pytia.framework.drafting_interfaces.drawing_text import DrawingText
from pytia.helper.scaling import get_view_scale
from pytia.helper.verify import verify_folder
from pytia.log import log
from pytia.wrapper.documents.drawing_documents import PyDrawingDocument
from pytia.wrapper.documents.part_documents import PyPartDocument
from pytia.wrapper.documents.product_documents import PyProductDocument


@dataclass
class DocketConfigTexts:
    name: str
    value: str
    view: str


@dataclass
class DocketConfigViews:
    name: str
    x: float
    y: float
    max_width: float
    max_height: float
    definition: Tuple[float, float, float, float, float, float]


@dataclass
class DocketConfig:

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
) -> PyDrawingDocument:
    """ """
    if not os.path.isfile(template):
        raise PytiaFileNotFoundError(
            f"Cannot open docket template {template!r}: Not a file."
        )

    docket = PyDrawingDocument()
    docket.new_from(path=template, name="docket")

    sheet = docket.drawing_document.sheets.active_sheet
    fg_views = sheet.views.item(FOREGROUND_VIEW)
    bg_views = sheet.views.item(BACKGROUND_VIEW)
    fg_texts = fg_views.texts
    bg_texts = bg_views.texts

    # Apply texts from config
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
                text.text = item.value
            case "property":
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
                    text.text = f"Unknown ({item.value})"
            case _:
                log.warning(f"Unknown type for drawing text: {item_type}")

    # Create isometric view
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

        view.scale = get_view_scale(
            view=view, max_width=item.max_width, max_height=item.max_height
        )
    return docket


def export_docket_as_pdf(docket: PyDrawingDocument, name: str, folder: str) -> str:
    """ """
    export_path = Path(verify_folder(folder), name + ".pdf")

    if os.path.exists(export_path):
        os.remove(export_path)
        log.warning(f"Removed existing docket file at {str(export_path)!r}.")

    docket.drawing_document.export_data(export_path, "pdf")
    log.info(f"Exported docket {name!r} to {str(export_path)!r}.")
    return str(export_path)