"""
    Module that holds all custom pytia exceptions.
"""

import sys
import traceback
from typing import Optional

from pytia.log import log


class PytiaBaseError(Exception):
    """Base class for all pytia exceptions. Logs exceptions as error messages"""

    def __init__(self, msg: str) -> None:
        super().__init__(msg)
        if traceback.extract_tb(sys.exc_info()[2]):
            log.exception(msg)
        else:
            log.error(msg)


class PytiaNotImplementedError(PytiaBaseError):
    """Exception for not implemented functions"""

    def __init__(self, msg: Optional[str] = None) -> None:
        msg = "Function not implemented." if msg is None else msg
        super().__init__(msg)


class PytiaValueError(PytiaBaseError):
    """Exception for value errors."""

    def __init__(self, msg: Optional[str] = None) -> None:
        msg = "Value error." if msg is None else msg
        super().__init__(msg)


class PytiaApplicationError(PytiaBaseError):
    """Exception for the dispatch."""


class PytiaFailsafeError(PytiaBaseError):
    """Exception for the failsafe decorator."""


class PytiaNotAFolderError(PytiaBaseError):
    """Exception for strings that aren't folders."""


class PytiaFileNotFoundError(PytiaBaseError):
    """Exception for non existent files"""


class PytiaFileOperationError(PytiaBaseError):
    """Exception for non existent files"""


class PytiaFileExistsError(PytiaBaseError):
    """Exception for non existent files"""


class PytiaDocumentOperationError(PytiaBaseError):
    """Exception for non existent files"""


class PytiaNoDocumentOpenError(PytiaBaseError):
    """Exception for non existent files"""


class PytiaWrongDocumentTypeError(PytiaBaseError):
    """Exception for wrong document types"""


class PytiaDocumentExistsError(PytiaBaseError):
    """Exception for existing documents"""


class PytiaDocumentNotOpenError(PytiaBaseError):
    """Exception for existing documents"""


class PytiaDocumentNotSavedError(PytiaBaseError):
    """Exception for existing documents"""


class PytiaDocumentNameConventionError(PytiaBaseError):
    """Exception for parts or product with other filenames than the partnumber"""


class PytiaBodyExistsError(PytiaBaseError):
    """Exception for existing bodies"""


class PytiaBodyNotFoundError(PytiaBaseError):
    """Exception for non-existing bodies"""


class PytiaBodyEmptyError(PytiaBaseError):
    """Exception for empty bodies"""


class PytiaPropertyExistsError(PytiaBaseError):
    """Exception for existing properties"""


class PytiaPropertyNotFoundError(PytiaBaseError):
    """Exception for non-existing properties"""


class PytiaParameterExistsError(PytiaBaseError):
    """Exception for existing parameters"""


class PytiaParameterTypeError(PytiaBaseError):
    """Exception for parameter type errors"""


class PytiaParameterNotFoundError(PytiaBaseError):
    """Exception for non-existing parameters"""


class PytiaAxisSystemExistsError(PytiaBaseError):
    """Exception for existing axis systems"""


class PytiaAxisSystemNotFoundError(PytiaBaseError):
    """Exception for missing axis systems"""


class PytiaHelperError(PytiaBaseError):
    """Base class for helper functions error exceptions."""


class PytiaBOMError(PytiaBaseError):
    """Base class for BOM functions error exceptions."""


class PytiaMaterialError(PytiaBaseError):
    """Base class for material functions error exceptions."""


class PytiaMaterialNotFound(PytiaBaseError):
    """Base class for missing materials exceptions."""


class PytiaDifferentDocumentError(PytiaBaseError):
    """Base class for errors when a document has changed."""


class PytiaLanguageError(PytiaBaseError):
    """Exception for language errors."""


class PytiaDispatchError(PytiaBaseError):
    """Exception when the dispatch failed."""


class PytiaNotInstalledError(PytiaBaseError):
    """Exception for not installed dependencies or software."""


class PytiaAbortedByUserError(PytiaBaseError):
    """Exception for user abortions."""


class PytiaConvertError(PytiaBaseError):
    """Exception when converting fails."""
