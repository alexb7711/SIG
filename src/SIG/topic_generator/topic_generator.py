"""!@file topic_generator.py

This module calls the appropriate generators to create the topic file with
the correct language.
"""

from src.SIG.topic_generator.topic import Topic

# from src.SIG.topic_generator.generators.gen_python import pygen
# from src.SIG.topic_generator.generators.gen_rust import rsgen
# from src.SIG.topic_generator.generators.gen_c import cgen


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
    # for p in topic:
    #     if p.lang == "python":
    #         pygen(fp, p)
    #     elif p.lang == "rust":
    #         rsgen(fp, p)
    #     elif p.lang == "C++":
    #         cgen(fp, p)
    #     elif p.lang == "C":
    #         cgen(fp, p)

    return
