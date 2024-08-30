"""!@file subscriber_generator.py

This module calls the appropriate generators to create the subscriber file with
the correct language.
"""

from src.types.sub import Subscriber


# ==============================================================================
#
def generate(fp: list[str], p: list[Subscriber]):
    """!
    Call the correct generation module to create each of the provided subscriber
    YAML files in their respective locations.

    @param fp List of file paths to each of the subscriber YAML files
    @param p List of dictionaries containing the subscriber data

    @return
    None
    """
    return
