"""!
@file sig.py
@package SIG
@brief This file defines the core for the Socket Interface Generator (SIG)

The SIG object requires:

- 'base_d': Base path of project to recursively search (Default: pwd)
- 'out_d': Output path for the documentation (Default: pwd)

At this point, the program shall execute, recursively searching directories for
appropriately named YAML files. The appropriate boilerplate code shall generate
with the specified language at the location that the file was located.

The allowed languages are: Python, Rust, C/C++.

After all of the files have been generated, a documentation file of the API
generated will be created and placed in the `out_d/[language]` directory where `[language]`
is a subdirectory used to separate interfaces for each language.
"""

# =====================================================================================================================
# Imports
import os
import re

import src.SIG.yaml.yaml_reader as yaml_reader
from src.SIG.topic_generator.topic_generator import generate
import src.SIG.topic_generator.topic as topic


# =====================================================================================================================
#


class SIG:
    """!@brief Socket Interface Generation Class."""

    ####################################################################################################################
    # PUBLIC
    ####################################################################################################################

    ##==================================================================================================================
    #
    def __init__(self, base_d: str = ".", out_d: str = ".") -> None:
        """! Initializes and creates the interface files given `base_d` and outputs them code to `out_d`

        @param base_d Base path to begin searching (Default: "."):
        @param out_d Output directory for the documentation (Default: ".")

        @return
        - Generates source code for the associated YAML file in the directory
          that the YAML file was found
        - Generates the API documentation
        """

        # fmt: off
        ## @var base_d
        # Absolute path to the directory from which SIG begins searching
        self.base_d = os.path.abspath(base_d)

        ## @var out_d
        # Absolute path to the directory where the API files and documentation will be output
        self.out_d = os.path.abspath(out_d)

        ## @var _files
        # List of files topic YAML files found
        self._files = []

        ## @var _data
        # List of data within the topics
        self._data = []
        # fmt: on

        return

    # --------------------------------------------------------------------------
    #
    def run(self) -> None:
        """!Executes the SIG process."""

        # Search for YAML files
        self._search_for_yaml()

        # Generate the files
        self._generate_files()

        # Create documentation
        self._generate_doc()

        return

    # --------------------------------------------------------------------------
    #
    def get_files(self) -> list[str]:
        """!
        Returns a list of the stored YAML file location's

        @return Dictionary of file paths separated by type.
        Example: list[0] -> [path]
        """
        return self._files.copy()

    ############################################################################
    # PRIVATE
    ############################################################################

    # --------------------------------------------------------------------------
    #
    def _search_for_yaml(self) -> list[str]:
        """!
        The search for YAML function recursively searches `base_d` for
        appropriately named files and returns the found absolute file paths.

        @return Dictionary of YAML file locations
        """
        # Create empty list
        files = []

        # Recursively search `base_d` for `[name].[yml,yaml]`
        for path, _, f_names in os.walk(self.base_d):
            # For all the files in `f_names`
            for f in f_names:
                ## If a YAML file is found
                if re.match(".*yml$", f) or re.match(".*yaml$", f):
                    ### Append the file to the files list
                    files.append(path + "/" + f)

        # Sort the files for consistency in processing
        files.sort()

        return files

    # --------------------------------------------------------------------------
    #
    def _generate_files(self):
        """!Generate the publisher, subscriber, and mock files"""
        # Create a buffer of all the topics
        self._data = self._get_message_data("pub")

        # Call publisher generation function
        generate(self._files, self._data)

        return

    # --------------------------------------------------------------------------
    #
    def _get_message_data(self, message_type: str) -> list[dict]:
        # Create empty buffer
        message = []

        # Iterate through each message to be created
        for fp in self._files:
            # Read in the YAML file
            yml = yaml_reader.open_yaml(fp, "r")

            # Save the data
            message.append(topic.Topic.format_data(yml))

        return message

    # --------------------------------------------------------------------------
    #
    def _generate_doc(self):
        """!Generate the documentation"""
        return
