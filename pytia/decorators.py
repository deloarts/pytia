"""
    Decorator module for pytia.
"""

import functools
import time

from pytia.exceptions import PytiaFailsafeError
from pytia.log import log


def failsafe(func):
    """
    Decorator for running functions failsafe.
    """

    @functools.wraps(func)
    def wrapper_failsafe(*args, **kwargs):
        try:
            log.debug(f"Calling function {func.__name__!r}")
            t_0 = time.perf_counter()
            value = func(*args, **kwargs)
            t_1 = time.perf_counter()
            log.debug(
                f"Function {func.__name__!r} returned {value!r} in {(t_1-t_0):.4f}s"
            )
        except Exception as e:
            raise PytiaFailsafeError(f"Function {func.__name__!r} failed: {e}") from e
        return value

    return wrapper_failsafe
