"""!@file publisher.py"""

from dataclasses import dataclass
from typing import TextIO, Self


@dataclass
class Topic:
    """!
    Defines the allowed parameters for a publisher object.

    @param name String defining the name of the publisher
    @param lang String specifying the output language(s)
    @param data Defines the set of data types and data structures in the
           publisher
    @param queue_size Number of elements that may be buffered (Optional)
    @param rate Rate of published data. (Optional)
    @param description Description of the publisher (Optional)
    """

    # ==========================================================================
    # Data
    name: str
    lang: str
    publish: dict
    queue_size: int
    rate: float
    desc: str

    # ==========================================================================
    # Helper methods
    def format_data(yml: TextIO) -> Self:
        """!
        Extracts the data from a YAML file and formats it in a data class.

        @param: yml File handle to the publisher YAML file.

        @return
        Data class containing the allowed parameters for publishers.
        """

        # Extract the data

        # Default values
        Topic.queue_size = 1
        Topic.lang = "python"

        # Required fields
        Topic.name = yml["name"]

        # Optional field
        if yml.get("queue_size"):
            Topic.rate = yml["queue_size"]
        if yml.get("rate"):
            Topic.rate = yml["rate"]
        if yml.get("desc"):
            Topic.desc = yml["desc"]

        return Topic
