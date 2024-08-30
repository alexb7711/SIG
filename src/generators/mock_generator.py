"""!@file mock_generator.py

This module calls the appropriate generators to create the mock file with
the correct language.
"""

from src.types.mock import Mock


# ==============================================================================
#
def generate(fp: list[str], p: list[Mock]):
    """!
    Call the correct generation module to create each of the provided mock
    YAML files in their respective locations.

    @param fp List of file paths to each of the mock YAML files
    @param p List of dictionaries containing the mock data

    @return
    None
    """
    return
