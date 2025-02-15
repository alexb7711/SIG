"""!@file topic_generator.py

This module calls the appropriate generators to create the topic file with
the correct language.
"""

from SIG.supported_languages import SUPPORTED_LANGUAGES

from .generators.gen_c import GenerateC
from .generators.gen_python import GeneratePython
from .generators.gen_rust import GenerateRust
from .topic import Topic

########################################################################################################################
# PRIVATE CONSTANTS
########################################################################################################################

_LANGUAGE_GENERATOR_MAP = {
    SUPPORTED_LANGUAGES[0]: GeneratePython.generate,
    SUPPORTED_LANGUAGES[1]: GenerateRust.generate,
    SUPPORTED_LANGUAGES[2]: GenerateC.generate,
    SUPPORTED_LANGUAGES[3]: GenerateC.generate,
}


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

    # For each language in the topic
    for f, t in zip(fp, topic):
        ## For each supported language
        for i, l in enumerate(t.lang):
            ### If the language listed is a part of the supported languages
            if t.lang == SUPPORTED_LANGUAGES[i]:
                #### Execute the generator associated with that language
                _LANGUAGE_GENERATOR_MAP[SUPPORTED_LANGUAGES[i]](f, t)

    return
