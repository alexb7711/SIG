"""!@file topic_generator.py

This module calls the appropriate generators to create the topic file with
the correct language.
"""

from src.SIG.topic_generator.types.topic import Topic
from src.SIG.types.python.python_topic import pygen
from src.SIG.types.rust.rust_topic import rsgen
from src.SIG.types.c.c_topic import cgen


# ==============================================================================
#
def generate(fp: list[str], topic: list[Topic]):
    """!
    Call the correct generation module to create each of the provided topic
    YAML files in their respective locations.

    @param fp List of file paths to each of the topic YAML files
    @param topic List of dictionaries containing the topic data

    @return
    None
    """
    for p in topic:
        if p.lang == "python":
            pygen(fp, p)
        elif p.lang == "rust":
            rsgen(fp, p)
        elif p.lang == "C++":
            cgen(fp, p)
        elif p.lang == "C":
            cgen(fp, p)

    return
