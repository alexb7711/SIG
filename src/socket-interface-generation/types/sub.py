"""!@file sub.py"""

from dataclasses import dataclass
from typing import TextIO, Self


@dataclass
class Subscriber:
    """!
    Defines the allowed parameters for a subscriber object.

    @param name String defining the name of the subscriber
    @param data Defines the set of data types and data structures in the
           subscriber
    @param description Description of the subscriber
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

        @param: yml File handle to the subscriber YAML file.

        @return
        Data class containing the allowed parameters for subscribers.
        """

        # Extract the data
        Subscriber.name = yml["name"]
        Subscriber.subscriptions = yml["subscriptions"]
        Subscriber.desc = yml["desc"]

        return Subscriber
