"""!
@file dpsmf.py
@package dpsmf
@brief This file defines the core for the Dynamic Publisher Subscriber Mock Framework.

The DPSMF object requires:

- 'base_d': Base path of project to recursively search (Default: pwd)
- 'out_d': Output path for the documentation (Default: pwd)
- 'sim': Flag indicating the project is being built for simulation
  (Default false)

At this point, the program shall execute, recursively searching directories for
appropriately named YAML files. The appropriate boilerplate code shall generate
with the specified language at the location that the file was located.

The allowed languages are: Python, Rust, C/C++.

After all of the files have been generated, a documentation file of the API
generated will be created and placed in the `out_d` directory.
"""

# ==============================================================================
# Imports
import os
import re
import yaml_reader

import src.generators.publisher_generator as pg
import src.generators.subscriber_generator as sg
import src.generators.mock_generator as mg

from src.types.publisher import Publisher
from src.types.sub import Subscriber
from src.types.mock import Mock


# ==============================================================================
#


class DPSMF:
    """!Dynamic Publisher Subscriber Mock Framework Classy"""

    ############################################################################
    # PUBLIC
    ############################################################################

    # --------------------------------------------------------------------------
    #
    def __init__(self, base_d: str = ".", out_d: str = ".", sim: bool = False) -> None:
        """! Constructor for DPSMF.

        @param base_d Base path to begin searching (Default: "."):
        @param out_d Output directory for the documentation (Default: ".")
        @param sim Enables/disables the generation of mock YAML files for
               simulation (Default: False)

        @return
        - Generates source code for the associated YAML file in the directory
          that the YAML file was found
        - Generates the API documentation
        """

        # fmt: off
        ## @var base_d
        # Absolute path to the directory from which DPSMF begins searching
        self.base_d = os.path.abspath(base_d)

        ## @var out_d
        # Absolute path to the directory where the API documentation
        self.out_d = os.path.abspath(out_d)

        ## @var sim
        # Enables/Disables generating API for mock
        self.sim = sim

        ## @var _files
        # List of files publisher, subscriber, and mock YAML files found
        self._files = {"pub": [], "sub": [], "mock": []}

        ## @var _data
        # List of objects for publisher, subscriber, and mock YAML files found
        self._data = {"pub": [], "sub": [], "mock": []}
        # fmt: on

        return

    # --------------------------------------------------------------------------
    #
    def run(self) -> None:
        """!Executes the DPSMF process."""

        # Search for YAML files
        self._search_for_yaml()

        # Generate the files
        self._generate_files()

        # Create documentation
        self._generate_doc()

        return

    # --------------------------------------------------------------------------
    #
    def get_files(self) -> dict:
        """!
        Returns a dictionary of the stored YAML file location's

        @return Dictionary of file paths separated by type.
        Example: dict["pub"][0] -> [path]
        """
        return self._files.copy()

    # --------------------------------------------------------------------------
    #
    def get_data(self) -> dict:
        """!
        Returns a dictionary of the data objects for each type.

        @return Dictionary of data objects separated by type.
        Example: dict["pub"][0] -> Publisher
        """
        return self._data.copy()

    ############################################################################
    # PRIVATE
    ############################################################################

    # --------------------------------------------------------------------------
    #
    def _search_for_yaml(self) -> None:
        """!
        The search for YAML function recursively searches `base_d` for
        appropriately named files and returns the found absolute file paths.

        @return Dictionary of YAML file locations
        """
        # Recursively search `base_d` for
        # - pub_[name].[yml,yaml]
        # - sub_[name].[yml,yaml]
        # - mock_[name][yml.yaml]
        #
        for path, _, f_names in os.walk(self.base_d):
            # For all the files in `f_names`
            for f in f_names:
                if re.match(".*yml$", f) or re.match(".*yaml$", f):
                    # If the file type is a publisher
                    if re.match("^pub.*", f):
                        self._files["pub"].append(path + "/" + f)
                    # If the file type is a publisher
                    elif re.match("^sub.*", f):
                        self._files["sub"].append(path + "/" + f)
                    # If the file type is a mock and `sim` is enabled
                    elif self.sim and re.match("^mock.*", f):
                        self._files["mock"].append(path + "/" + f)

        # Sort the files for consistency in processing
        self._files["pub"].sort()
        self._files["sub"].sort()
        self._files["mock"].sort()

        return

    # --------------------------------------------------------------------------
    #
    def _generate_files(self):
        """!Generate the publisher, subscriber, and mock files"""
        # Generate publisher and subscriber files
        self._generate_pub_files()
        self._generate_sub_files()

        # If `sim` is enabled
        if self.sim:
            # Generate mock files
            self._generate_mock_files()

        return

    # --------------------------------------------------------------------------
    #
    def _generate_pub_files(self):
        """!
        Generate publisher files

        @return
        Returns a list of publisher objects.
        """

        # Create a buffer of all the publisher
        self._data["pub"] = self._get_message_data("pub")

        # Call publisher generation function
        pg.generate(self._files["pub"], self._data["pub"])

        return

    # --------------------------------------------------------------------------
    #
    def _generate_sub_files(self):
        """!Generate subscriber files"""
        # Create a buffer of all the publisher
        self._data["sub"] = self._get_message_data("sub")

        # Call subscriber generation function
        sg.generate(self._files["pub"], self._data["sub"])
        return

    # --------------------------------------------------------------------------
    #
    def _generate_mock_files(self):
        """!Generate mock files"""
        self._data["mock"] = self._get_message_data("mock")

        # Call mock generation function
        mg.generate(self._files["pub"], self._data["mock"])
        return

    # --------------------------------------------------------------------------
    #
    def _get_message_data(self, message_type: str) -> list[dict]:
        # Create empty buffer
        message = []

        # Iterate through each message to be created
        for fp in self._files[message_type]:
            # Read in the YAML file
            yml = yaml_reader.open_yaml(fp, "r")

            # Save the data
            if message_type == "pub":
                message.append(Publisher.format_data(yml))
            elif message_type == "sub":
                message.append(Subscriber.format_data(yml))
            elif message_type == "mock":
                message.append(Mock.format_data(yml))

        return message

    # --------------------------------------------------------------------------
    #
    def _generate_doc(self):
        """!Generate the documentation"""
        return
