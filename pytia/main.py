#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    PYTIA - A wrapper for the CATIA V5 api.
"""

from pytia import __version__
from pytia.cli import cli


def main() -> None:
    """Application entry point."""
    cli()


if __name__ == "__main__":
    main()
