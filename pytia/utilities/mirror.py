"""
    Utility for mirroring a part.
"""
import os
from pathlib import Path
from typing import Optional

from pytia.exceptions import (
    PytiaBodyEmptyError,
    PytiaBodyNotFoundError,
    PytiaFileExistsError,
)
from pytia.helper.symmetries import create_symmetry_of_main_body_zx
from pytia.helper.verify import verify_folder
from pytia.log import log
from pytia.wrapper.documents.part_documents import PyPartDocument


def mirror_main_body(
    postfix: str = "_mirror",
    keep_open: bool = True,
    folder: Optional[Path] = None,
) -> Path:
    """
    Mirrors the current parts main body to a new part file. Returns the path of the saved file.

    Args:
        postfix (str, optional): The postfix of the filename and partnumber. Defaults to "_mirror".
        keep_open (bool, optional): Keeps the mirrored document opens. Defaults to True.
        folder (Optional[Path], optional): The target folder for the mirrored part. \
            Defaults to None. Uses the original parts folder when None.

    Raises:
        PytiaBodyEmptyError: Raised when the original body is empty.
        PytiaFileExistsError: Raised when the target filename already exists.
        PytiaBodyNotFoundError: Raised when the main body cannot be found in the mirrored part.

    Returns:
        Path: The full path of the mirrored part.
    """
    original_document = PyPartDocument()
    original_document.current()
    original_document.save()  # This fails if the part isn't saved yet

    original_part = original_document.part
    original_product = original_document.product
    original_main_body = original_document.bodies.main_body
    original_selection = original_document.document.selection
    original_name = original_part.name
    original_path = Path(original_document.document.full_name)
    original_folder = Path(original_path.parent)

    if original_document.bodies.is_empty(
        original_main_body, count_sketches=False, count_hybrid_bodies=False
    ):
        raise PytiaBodyEmptyError(
            f"Cannot mirror part {original_product.part_number}: Main body is empty."
        )

    new_name = original_product.part_number + postfix

    if not folder:
        folder = original_folder
    folder = verify_folder(folder)
    new_path = Path(folder, new_name + ".CATPart")

    if os.path.exists(new_path):
        raise PytiaFileExistsError(
            f"Cannot mirror body {original_main_body.name!r}: Destination part already exists."
        )

    log.info(f"Creating mirror of {original_part.name!r}.")
    new_document = PyPartDocument()
    new_document.new_from(path=original_path, name=new_name)
    new_part = new_document.part
    new_selection = new_document.document.selection

    new_document.bodies.main_body.name = "old_main_body"
    bodies_pre_paste = set(new_document.bodies.names)

    # Copy the original main body
    original_document.remove_selection(selection=original_selection)
    original_selection.add(original_main_body)
    original_selection.copy()
    log.info("Copied main body of source part.")

    # Paste it to the new document
    new_document.remove_selection(selection=new_selection)
    new_selection.add(new_part)
    new_selection.paste_special("CATPrtResult")
    log.info("Pasted body to destination part.")

    bodies_post_paste = set(new_document.bodies.names)

    original_document.remove_selection(selection=original_selection)
    new_document.remove_selection(selection=new_selection)

    # Get the newly inserted body name.
    # We need to do this, because if the original main body is named
    # 'main body' CATIA will insert this as a generic named body to
    # the new document. So we have to get the generic name first.
    try:
        generic_named_body = list(bodies_post_paste - bodies_pre_paste)[0]
        new_part.main_body = new_part.bodies.item(generic_named_body)
    except Exception as e:
        raise PytiaBodyNotFoundError(f"Cannot set main body: {e}") from e

    # Some main bodies do have some more information attached to their
    # name (revision number, material, etc). We don't want to loose that.
    # This assumes that the main body of the original part has the same
    # base name as the part, e.g.:
    #   Part filename = Some_Part.CATPart
    #   Main body name = Some_Part Rev1
    if original_name in original_main_body.name:
        fixes = original_main_body.name.split(original_name)
        new_part.main_body.name = f"{fixes[0]}{new_part.name}{fixes[-1]}"
    else:
        new_part.main_body.name = original_main_body.name + postfix
    log.info("Set pasted body as main body.")

    new_document.delete_objects([new_part.bodies.item("old_main_body")])
    create_symmetry_of_main_body_zx(part=new_part)
    new_document.save_as(folder=folder)

    if not keep_open:
        new_document.close()

    log.info(f"Exported mirrored part to {str(new_path)!r}")
    return new_path
