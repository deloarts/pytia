"""
    Helper module for CATIA Measurable objects.
"""

from typing import Optional

from pycatia.in_interfaces.document import Document
from pycatia.in_interfaces.reference import Reference
from pycatia.mec_mod_interfaces.body import Body
from pycatia.mec_mod_interfaces.part import Part
from pycatia.space_analyses_interfaces.measurable import Measurable

from pytia.decorators import failsafe
from pytia.framework import framework
from pytia.log import log


@failsafe
def get_measurable_from_reference(
    *, reference: Reference, document: Optional[Document] = None
) -> Measurable:
    """
    Gets measurements from the given reference. Uses the current active document
    if no document is provided.

    Args:
        reference (Reference): The reference object from which the measurable will be returned.
        document (Optional[Document], optional): The document in which the reference is. \
            Defaults to None.

    Returns:
        Measurable: The measurable object.
    """
    doc = document if document else framework.catia.active_document
    spa_workbench = doc.spa_workbench()
    log.debug(f"Loaded SPA workbench from {doc.name!r}")
    measurable = spa_workbench.get_measurable(reference)
    return measurable


@failsafe
def get_measurable_from_body(part: Part, body: Body) -> Measurable:
    """
    Gets measurements from the given body.

    Args:
        part (Part): The part that holds the body.
        body (Body): The body from which the measurable will be returned.

    Returns:
        Measurable: The measurable object.
    """
    reference = part.create_reference_from_object(body)
    measurable = get_measurable_from_reference(reference=reference)
    return measurable
