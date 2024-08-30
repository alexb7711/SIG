"""!@file mock.py"""

from dataclasses import dataclass
from typing import TextIO, Self


@dataclass
class Mock:
    """!
    Defines the allowed parameters for a mock object.

    @param name String defining the name of the mock
    @param data Defines the set of data types and data structures in the mock
    @param description Description of the mock
    """

    # ==========================================================================
    # Data
    name: str
    data: dict
    desc: str

    # ==========================================================================
    # Helper methods
    def format_data(yml: TextIO) -> Self:
        """!
        Extracts the data from a YAML file and formats it in a data class.

        @param: yml File handle to the mock YAML file.

        @return
        Data class containing the allowed parameters for mocks.
        """

        # Extract the data
        Mock.name = yml["name"]
        Mock.data = yml["data"]
        Mock.desc = yml["desc"]

        return Mock
