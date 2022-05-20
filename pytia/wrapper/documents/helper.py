"""
    Helper module for CATIA documents.
"""

from pytia import __version__
from pytia.exceptions import PytiaWrongDocumentTypeError
from pytia.framework import framework
from pytia.log import log
from pytia.wrapper.documents.part_documents import PyPartDocument
from pytia.wrapper.documents.product_documents import PyProductDocument


def get_current_document() -> PyPartDocument | PyProductDocument:
    """
    Detects the document type of the current active document.

    Returns a PyProductDocument or a PyPartDocument with the active
    document set as current (strict naming).

    Raises an error when the current document is neither of them.

    Use this when your application requires to work for both,
    CATParts and CATProduct.
    """
    document = framework.catia.active_document
    if document.is_part:
        log.debug("Detected current document as PART")
        doc = PyPartDocument()
    elif document.is_product:
        log.debug("Detected current document as PRODUCT")
        doc = PyProductDocument()
    else:
        raise PytiaWrongDocumentTypeError(
            f"Current document is neither a part or a product: {document.name!r}"
        )
    doc.current()
    return doc
